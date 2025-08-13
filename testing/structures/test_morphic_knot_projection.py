from __future__ import annotations

import math

from structures.morphic_knot_projection import (
    derive_recursive_depth_and_form_factor,
    derive_spin_from_internal_symmetry,
    derive_charge_from_quantum_numbers,
)
from structures.particle_spectrum import PARTICLE_SPECTRUM


def test_mass_depth_basic_examples():
    for name in ("electron", "muon", "tau", "proton"):
        dec = derive_recursive_depth_and_form_factor(name)
        assert dec.mass_ratio_to_electron >= 0.0
        # C_n should be finite and positive for massive states
        if dec.mass_ratio_to_electron > 0:
            assert math.isfinite(dec.form_factor_Cn)
            assert dec.form_factor_Cn > 0


def test_spin_projection_matches_catalog():
    for key in ("electron", "muon", "tau", "photon", "W_boson_plus", "Z_boson"):
        spec = PARTICLE_SPECTRUM.get_particle_by_name(key)
        assert spec is not None
        s = derive_spin_from_internal_symmetry(spec)
        assert spec.quantum_numbers is not None
        assert abs(spec.quantum_numbers.spin - s) < 1e-12


def test_charge_from_T3Y_matches_catalog():
    for key in ("electron", "muon", "tau", "up", "down", "W_boson_plus", "Z_boson", "photon"):
        spec = PARTICLE_SPECTRUM.get_particle_by_name(key)
        assert spec is not None
        q = derive_charge_from_quantum_numbers(spec)
        if spec.quantum_numbers is None:
            continue
        assert abs((q or 0.0) - spec.quantum_numbers.electric_charge) < 1e-12


