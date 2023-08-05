from enum import StrEnum

class PFE(StrEnum):
    EXEMPT = "exempt"
    PASS = "pass"
    FAIL = "fail"



from .comparison import Comparison