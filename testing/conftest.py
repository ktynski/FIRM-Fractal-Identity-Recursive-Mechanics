import os
import sys
import pytest

# Ensure project root is on sys.path for absolute imports during pytest collection
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

def pytest_configure(config):
    # Register markers used in the suite
    config.addinivalue_line("markers", "benchmark: performance benchmark suite")
    config.addinivalue_line("markers", "slow: marks tests as slow")


@pytest.fixture(scope="session")
def validation_phase():
    """Enable validation phase for tests that intentionally compare with sealed data.

    Usage:
        def test_something(validation_phase):
            ...
    """
    from validation.experimental_firewall import EXPERIMENTAL_FIREWALL
    # Ensure clean state
    EXPERIMENTAL_FIREWALL.enable_theory_phase()
    EXPERIMENTAL_FIREWALL.enable_validation_phase()
    yield EXPERIMENTAL_FIREWALL
    # Restore to theory phase to protect other tests
    EXPERIMENTAL_FIREWALL.enable_theory_phase()


@pytest.fixture(autouse=True)
def firewall_clean_state():
    """Ensure firewall is reset to a deterministic state before each test.

    Prevents cross-test contamination where a prior critical alert could leave
    the singleton in BREACHED/DISABLED, causing unrelated tests to fail.
    """
    from validation.experimental_firewall import EXPERIMENTAL_FIREWALL
    EXPERIMENTAL_FIREWALL.reset()
    yield
