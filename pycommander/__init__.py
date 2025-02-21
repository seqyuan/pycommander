import warnings

warnings.filterwarnings("ignore")

from pycommander import tl, pl, pa
from trackc.gs import make_spec, savefig, tenon

__all__ = ["tl", "pl", "pa", "make_spec", "tenon"]

"""
import sys
sys.modules.update({f'{__name__}.{m}': globals()[m] for m in ['tl', 'pl', 'pa']})
from ._utils import annotate_doc_types
annotate_doc_types(sys.modules[__name__], 'pycommander')
del sys, annotate_doc_types
"""

