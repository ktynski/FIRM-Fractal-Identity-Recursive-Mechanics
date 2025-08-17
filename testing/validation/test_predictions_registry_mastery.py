#!/usr/bin/env python3
"""
Team 2 Validation Mastery: Predictions Registry
Target: validation/predictions_registry.py
"""

import sys
import json
from pathlib import Path
from unittest.mock import patch, MagicMock

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from validation.predictions_registry import PredictionsRegistry, PredictionRecord, register_cmb_phi_peaks

class TestPredictionsRegistryMastery:
    """
    Mastery tests for the predictions registry module.
    """

    def test_initialization(self, tmp_path):
        """Verify the registry initializes correctly."""
        test_registry_file = tmp_path / "test_registry.json"
        registry = PredictionsRegistry(registry_file=str(test_registry_file))
        assert registry.registry_file == test_registry_file

    def test_register_and_get_prediction(self, tmp_path):
        """Test the registration and retrieval of a prediction."""
        test_registry_file = tmp_path / "test_registry.json"
        registry = PredictionsRegistry(registry_file=str(test_registry_file))
        prediction_id = registry.register_prediction(
            prediction_type="test_type",
            target_observable="test_observable",
            predicted_values={"value": 1.0},
            mathematical_derivation="test derivation",
            provenance_chain=["test_provenance"]
        )
        
        retrieved = registry.get_prediction(prediction_id)
        assert retrieved is not None
        assert retrieved.prediction_id == prediction_id
        assert retrieved.predicted_values["value"] == 1.0
        assert retrieved.verify_integrity() is True

    def test_list_predictions(self, tmp_path):
        """Test listing predictions."""
        test_registry_file = tmp_path / "test_registry.json"
        registry = PredictionsRegistry(registry_file=str(test_registry_file))
        registry.register_prediction("type1", "obs1", {}, "", [])
        registry.register_prediction("type2", "obs2", {}, "", [])
        registry.register_prediction("type1", "obs3", {}, "", [])

        all_preds = registry.list_predictions()
        assert len(all_preds) == 3

        type1_preds = registry.list_predictions(prediction_type="type1")
        assert len(type1_preds) == 2

    def test_integrity_verification(self, tmp_path):
        """Test the integrity verification of the registry."""
        test_registry_file = tmp_path / "test_registry.json"
        registry = PredictionsRegistry(registry_file=str(test_registry_file))
        pred_id = registry.register_prediction("test", "test", {}, "", [])
        
        # Manually tamper with the file
        with open(test_registry_file, 'r+') as f:
            data = json.load(f)
            data[pred_id]['predicted_values']['hacked'] = True
            f.seek(0)
            json.dump(data, f)
            f.truncate()

        # Re-load the registry to see the tampered data
        tampered_registry = PredictionsRegistry(registry_file=str(test_registry_file))
        verification_results = tampered_registry.verify_all_integrity()
        
        assert verification_results[pred_id] is False

    def test_export(self, tmp_path):
        """Test exporting the registry for verification."""
        test_registry_file = tmp_path / "test_registry.json"
        registry = PredictionsRegistry(registry_file=str(test_registry_file))
        registry.register_prediction("test", "test", {}, "", [])
        export_file = tmp_path / "export.json"
        registry.export_for_verification(str(export_file))

        assert export_file.exists()
        with open(export_file, 'r') as f:
            data = json.load(f)
            assert data['registry_metadata']['total_predictions'] == 1
            assert len(data['predictions']) == 1

    @patch('validation.predictions_registry.get_cmb_phi_peaks')
    def test_register_cmb_phi_peaks(self, mock_get_peaks, tmp_path):
        """Test the helper function to register CMB phi peaks."""
        test_registry_file = tmp_path / "test_registry.json"
        registry = PredictionsRegistry(registry_file=str(test_registry_file))
        mock_peak_data = MagicMock()
        mock_peak_data.series_name = "test_series"
        mock_peak_data.l0 = 220.0
        mock_peak_data.peaks = [220, 356]
        mock_peak_data.k_decomposition = {'k': 12.6, 'phi_inv': 0.618, 'epsilon': -0.002}
        mock_peak_data.amplitudes = [1.0, 0.618]
        mock_peak_data.definition = "test definition"
        mock_get_peaks.return_value = mock_peak_data

        with patch('validation.predictions_registry.PREDICTIONS_REGISTRY', registry):
            prediction_id = register_cmb_phi_peaks()
            
        assert prediction_id is not None
        prediction = registry.get_prediction(prediction_id)
        assert prediction is not None
        assert prediction.prediction_type == 'cmb_phi_geometric_peaks'
