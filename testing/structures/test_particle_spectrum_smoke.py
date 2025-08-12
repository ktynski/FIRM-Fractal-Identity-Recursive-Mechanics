def test_particle_spectrum_basic_apis():
    from structures.particle_spectrum import PARTICLE_SPECTRUM, Generation
    # Access some particles by name and check report shape
    e = PARTICLE_SPECTRUM.get_particle_by_name("electron")
    assert e is not None and e.particle_type.name in ("FERMION", "GAUGE_BOSON", "SCALAR_BOSON", "COMPOSITE")
    gen1 = PARTICLE_SPECTRUM.get_particles_by_generation(Generation.FIRST)
    assert isinstance(gen1, list) and len(gen1) >= 1
    verify = PARTICLE_SPECTRUM.verify_three_generation_structure()
    assert isinstance(verify, dict) and "exactly_three_generations" in verify
    text = PARTICLE_SPECTRUM.generate_particle_spectrum_report()
    assert isinstance(text, str) and "FIRM Particle Spectrum Report" in text

