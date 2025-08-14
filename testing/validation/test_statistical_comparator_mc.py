from validation.experimental_firewall import EXPERIMENTAL_FIREWALL
from validation.statistical_comparator import STATISTICAL_COMPARATOR


def test_statistical_comparator_multiple_comparisons_summary():
    # Ensure clean firewall state and enable validation phase (preconditions enforced internally)
    EXPERIMENTAL_FIREWALL.reset()
    EXPERIMENTAL_FIREWALL.enable_validation_phase()

    # Enable comparator
    STATISTICAL_COMPARATOR.enable_validation_mode()

    analysis = STATISTICAL_COMPARATOR.comprehensive_validation_analysis()
    assert isinstance(analysis, dict)

    results = analysis.get("individual_tests", [])
    global_info = analysis.get("global_analysis", {})

    # At least fine-structure chi-squared and Bayesian tests if firewall key is available
    assert len(results) >= 1
    assert "global_chi_squared" in global_info
    assert "bonferroni_alpha" in global_info

    # Bonferroni logic sanity: corrected significant count <= uncorrected
    sig_default = global_info.get("significant_individual", 0)
    sig_corrected = global_info.get("significant_corrected", 0)
    assert sig_corrected <= sig_default

    # Report includes multiple-comparisons summary string
    report = STATISTICAL_COMPARATOR.generate_statistical_report(results)
    assert "Bonferroni" in report
