# coding: utf-8

from __version__ import __version_info__, __version__

from fold import seq_fold, seq_pf_fold, seq_subopt, seq_eval,\
    get_T, set_T, str_inverse, str_pf_inverse

# from util import str_base_pairs, seq_str_compatible
from util import *

# previous line also place fold and util inside viennaRNA
del fold

__all__ = ['seq_fold', 'seq_pf_fold', 'seq_subopt', 'seq_eval',
           'get_T', 'set_T', 'str_inverse', 'str_pf_inverse',
           'str_base_pairs', 'seq_str_compatible']
