from .WCET import WCET
from .ACET import ACET
from .CacheModel import CacheModel
from .FixedPenalty import FixedPenalty
from .PWCET import PWCET

execution_time_models = {
    'wcet': WCET,
    'acet': ACET,
    'cache': CacheModel,
    'fixedpenalty': FixedPenalty,
    'pwcet': PWCET
}

execution_time_model_names = {
    'WCET': 'wcet',
    'ACET': 'acet',
    'Cache Model': 'cache',
    'Fixed Penalty': 'fixedpenalty',
    'PWCET': 'pwcet'
}
