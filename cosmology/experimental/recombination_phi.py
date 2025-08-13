import warnings as _warnings
from . import experimental_notice as _exp

_warnings.warn(
    "cosmology.experimental.recombination_phi is deprecated; use cosmology.recombination_saha_phi",
    DeprecationWarning,
    stacklevel=2,
)
_exp("recombination_phi")

