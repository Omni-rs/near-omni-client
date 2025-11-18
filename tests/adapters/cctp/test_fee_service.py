from unittest.mock import MagicMock, patch

from near_omni_client.adapters.cctp.fee_service import FeeService
from near_omni_client.networks import Network


@patch("requests.get")
def test_get_fees_fast_finality(mock_get):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "data": [
            {"finalityThreshold": 1000, "minimumFee": 1},
            {"finalityThreshold": 2000, "minimumFee": 0},
        ]
    }

    mock_get.return_value = mock_resp

    service = FeeService(Network.BASE_SEPOLIA)
    fee = service.get_fees(1, 2, finality_threshold=1000)

    assert fee.finalityThreshold == 1000
    assert fee.minimumFee == 1
