#!/usr/bin/env python3

'''
Copyright 2018, VDMS
Licensed under the terms of the BSD 2-clause license. See LICENSE file for terms.
'''

# Run through Analysis
import logging
import re

import pyjq
import packaging.version

from pfe import PFE


class Comparison():

    def __init__(self,
                 object,
                 mtype="is",
                 mvalue=None,
                 ccomplex=None,
                 exemptfail=False,
                 comparison_name="unnamed",
                 **kwargs):

        '''

        :param object: A Single Object or List of Objects that I want to Make My Comparison Against
        :param mtype: enum= is, ver(lt|le|gt|ge), match(|ne), (gt|ge|gt|lt)
        :param ctype: A single or list of types to pull out of the object
        :param csubtype: A single or list of subtypes to pull out of the object
        :param mvalue: A single or list of values to make the comparison against
        :param ccomplex: If not None, a single or list of "jq rules" to pull out of the object to make the comparison against
        :param exemptfail: False by default. if true, non matches (either no type/subtype or None returned on ccomplex) are failures instead of exempts
        :param comparison_name: An optional name to use in logging
        :return:

        Originally this would also pull the data for the comparison out of the database and it had a prety structured feel,
        hence the ctype/csubtype logic.
        '''

        self.logger = logging.getLogger("pfe.Comparison <{}>".format(comparison_name))
        self.kwargs = kwargs
        self.exemptfail = exemptfail

        if isinstance(mvalue, str) or mvalue is None:
            self.mvalue = [mvalue]
        elif isinstance(mvalue, list):
            self.mvalue = mvalue
        else:
            raise ValueError("mvalue of unknown type.")

        if isinstance(ccomplex, str):
            self.ccomplex = [ccomplex]
        elif isinstance(ccomplex, list):
            self.ccomplex = ccomplex
        else:
            raise ValueError("ccomplex of unknown type")

        if len(self.ccomplex) != len(mvalue):
            raise AttributeError("Mvalue and CComplex are of differing lenghts.")
        else:
            self.length = len(self.ccomplex)

        if isinstance(mtype, str):
            # Expand mtype to length of comparisons
            self.mtype = [mtype for x in range(self.length)]
        elif isinstance(mtype, list):
            if len(mtype) != self.length:
                raise ValueError("Custom list of mtypes doesn't match length fo values and complexes")
            self.mtype = mtype

        self.id_field = self.kwargs.get("id_field", None)
        self.data_field = self.kwargs.get("data_field", None)

        if self.kwargs.get("obj_multi", True) and hasattr(object, "__iter__"):
            self.object = object
        elif self.kwargs.get("obj_multi", True) and hasattr(object, "__iter__") is False:
            raise SyntaxError("Object is not Iterable but obj_multi has not been set to False")
        else:
            self.object = [object]

        if self.kwargs.get("run", True) is True:
            self.results = self.big_loop()
        else:
            self.results = None

    def big_loop(self):

        pass_list = list()
        fail_list = list()
        exempt_list = list()

        for xobj in self.object:

            if isinstance(xobj, dict) and self.data_field is None:
                x = xobj
            elif isinstance(xobj, dict) and self.data_field is not None:
                x = xobj[self.data_field]
            elif hasattr(xobj, self.data_field):
                x = getattr(xobj, self.data_field)
            else:
                # Put it all on black baby!
                x = xobj

            object_name = x

            if self.id_field is not None and isinstance(object_name, dict) and self.id_field in object_name.keys():
                object_name = object_name[self.id_field]
            elif self.id_field is not None and hasattr(object, self.id_field):
                object_name = getattr(object_name, self.id_field)

            results = list()

            for ti in range(0, self.length):

                this_pfe = None

                this_mtype = self.mtype[ti]

                this_mvalue = self.mvalue[ti]

                try:
                    this_cvalue = pyjq.one(self.ccomplex[ti], x)

                    if this_cvalue is None and self.kwargs.get("none_return_exempt", True) is True:
                        this_pfe = PFE.EXEMPT
                        self.logger.debug("Exempting Object {}, {} not found.".format(object_name, self.ccomplex[ti]))
                        break

                except Exception as error:
                    self.logger.error("Invalid ccomplex {}, with error {}".format(self.ccomplex[ti], error))
                    self.logger.debug("Invalid ccomplex{}: {}".format(self.ccomplex[ti], x))
                    this_pfe = PFE.EXEMPT
                else:

                    if this_mtype == "is":
                        this_pfe = self.is_check(this_mvalue, this_cvalue)
                    elif this_mtype in ("match", "matchne"):
                        match_args = {"ne": False}
                        if "ne" in this_mtype:
                            match_args["ne"] = True

                        this_pfe = self.match_check(this_mvalue, this_cvalue, **match_args)

                    elif this_mtype.startswith("ver") or this_mtype in ("gt", "ge", "lt", "le"):
                        ver_args = {"direction": "eq"}

                        if "gt" in this_mtype:
                            ver_args["direction"] = "gt"
                        elif "ge" in this_mtype:
                            ver_args["direction"] = "ge"
                        elif "lt" in this_mtype:
                            ver_args["direction"] = "lt"
                        elif "le" in this_mtype:
                            ver_args["direction"] = "le"
                        elif "eq" in this_mtype:
                            ver_args["direction"] = "eq"

                        this_pfe = self.ver_check(this_mvalue, this_cvalue, **ver_args)
                finally:

                    if this_pfe == PFE.EXEMPT or this_pfe is None:
                        if self.exemptfail is True:
                            results.append(PFE.FAIL)
                        else:
                            results.append(this_pfe)

                        break
                    elif this_pfe == PFE.FAIL:
                        results.append(this_pfe)
                        break
                    else:
                        results.append(this_pfe)

            if PFE.EXEMPT in results:
                exempt_list.append(object_name)
            elif PFE.FAIL in results:
                fail_list.append(object_name)
            else:
                # List is empty or all items passed
                pass_list.append(object_name)

        return {"pass": pass_list,
                "fail": fail_list,
                "exempt": exempt_list}

    def is_check(self, mvalue, cvalue, **chargs):

        """
        Does the logic for is matching
        :param mvalue: From the rule, to match with
        :param cvalue: From the data to check
        :param chargs: any extra args this type supports
        :return: pfe.PFE
        """

        pfe = None

        if isinstance(cvalue, (str, int)):
            if mvalue == cvalue:
                pfe = PFE.PASS
            else:
                pfe = PFE.FAIL
        elif isinstance(cvalue, (list, dict)):
            pfe = PFE.EXEMPT

        elif cvalue is None:
            if mvalue is None or mvalue == "none":
                pfe = PFE.PASS
            else:
                pfe = PFE.EXEMPT

        return pfe

    def match_check(self, mvalue, cvalue, **chargs):

        '''
        Check Matches

        :param mvalue: From the rule, to match with
        :param cvalue: From the data to check
        :param chargs: any extra args this type supports, speficially looking for a ne=False/True to tell me if I'm
                       a NE match
        :return: pfe.PFE
        '''

        pfe = PFE.EXEMPT

        if isinstance(mvalue, str):
            try:
                if re.search(mvalue, cvalue) == None:
                    if chargs.get("ne", False) is True:
                        # matchne I never wanted to match
                        pfe = PFE.PASS
                    else:
                        # I wanted to match but couldn't
                        pfe = PFE.FAIL
                else:
                    if chargs.get("ne", False) is False:
                        # I have a matcha and wanted it
                        pfe = PFE.PASS
                    else:
                        # I have a match but wanted to not match
                        pfe = PFE.FAIL
            except Exception as regex_error:
                self.logger.warning("Unable to Run Regex Check of : {}".format(mvalue))
                self.logger.debug(regex_error)

                pfe = PFE.EXEMPT
        else:
            # Badly Matched Data
            pfe = PFE.EXEMPT

        return pfe

    def ver_check(self, mvalue, cvalue, **chargs):

        '''
        :param mvalue: From the rule, to match with
        :param cvalue: From the data to check
        :param chargs: any extra args this type supports, speficially looking for `direction` to be (lt|gt|le|ge|eq) set
                       defautls to eq
        :return: pfe.PFE
        '''

        pfe = PFE.EXEMPT

        direction = chargs.get("direction", "eq")
        ver = chargs.get("ver", True)

        if ver is True:
            try:
                mvalue_ver = packaging.version.parse(mvalue)
                cvalue_ver = packaging.version.parse(cvalue)
            except Exception as versioning_error:
                self.logger.error("Unable to Read {} or {} as Versions.".format(mvalue, cvalue))
                pfe = PFE.EXEMPT

                return pfe
        else:
            if type(mvalue) != type(cvalue):
                self.logger.error("Generic Comparsion types between mvalue and cvalue don't match returning exmpetion.")
                pfe = PFE.EXEMPT
                return

            if isinstance(mvalue, (str, list, tuple)) and isinstance(cvalue, (str, list, tuple)):
                mvalue_ver = len(mvalue)
                cvalue_ver = len(cvalue)
            else:
                # I have a numeric type
                mvalue_ver = len(mvalue)
                cvalue_ver = len(cvalue)

            if direction == "eq":
                if cvalue_ver == mvalue_ver:
                    pfe = PFE.PASS
                else:
                    pfe = PFE.FAIL
            elif direction == "lt":
                if cvalue_ver < mvalue_ver:
                    pfe = PFE.PASS
                else:
                    pfe = PFE.FAIL
            elif direction == "le":
                if cvalue_ver <= mvalue_ver:
                    pfe = PFE.PASS
                else:
                    pfe = PFE.FAIL
            elif direction == "gt":
                if cvalue_ver > mvalue_ver:
                    pfe = PFE.PASS
                else:
                    pfe = PFE.FAIL
            elif direction == "ge":
                if cvalue_ver >= mvalue_ver:
                    pfe = PFE.PASS
                else:
                    pfe = PFE.FAIL
            else:
                self.logger.warning("Unknown version direction {}".format(direction))
                pfe = PFE.EXEMPT

        return pfe
