import time

import requests
from pydantic import ValidationError

from near_omni_client.networks import Network

from .fee_service_types import (
    Fee,
    GetFeeResponse,
    GetFeesBadRequestResponse,
    GetFeesNotFoundResponse,
)


class FeeService:
    """Service for retrieving attestations from Circle's attestation service."""

    MAINNET_BASE_URL = "https://iris-api.circle.com/v2/burn/USDC/fees"
    SANDBOX_BASE_URL = "https://iris-api-sandbox.circle.com/v2/burn/USDC/fees"
    network_urls = {
        Network.BASE_SEPOLIA: f"{SANDBOX_BASE_URL}/{Network.BASE_SEPOLIA.domain}/{{}}",
        Network.BASE_MAINNET: f"{MAINNET_BASE_URL}/{Network.BASE_MAINNET.domain}/{{}}",
        Network.ETHEREUM_SEPOLIA: f"{SANDBOX_BASE_URL}/{Network.ETHEREUM_SEPOLIA.domain}/{{}}",
        Network.ETHEREUM_MAINNET: f"{MAINNET_BASE_URL}/{Network.ETHEREUM_MAINNET.domain}/{{}}",
        Network.OPTIMISM_SEPOLIA: f"{SANDBOX_BASE_URL}/{Network.OPTIMISM_SEPOLIA.domain}/{{}}",
        Network.OPTIMISM_MAINNET: f"{MAINNET_BASE_URL}/{Network.OPTIMISM_MAINNET.domain}/{{}}",
        Network.ARBITRUM_SEPOLIA: f"{SANDBOX_BASE_URL}/{Network.ARBITRUM_SEPOLIA.domain}/{{}}",
        Network.ARBITRUM_MAINNET: f"{MAINNET_BASE_URL}/{Network.ARBITRUM_MAINNET.domain}/{{}}",
    }

    def __init__(self, network: Network):
        self.network = network
        self.url = self.network_urls.get(network)
        if not self.url:
            raise ValueError(f"Unsupported network: {network}")

    def get_fees(self, destination_domain_id: int, finality_threshold: int = 1000) -> Fee:
        """Retrieve fees for a given source and destination domain ID."""
        url = self.url.format(destination_domain_id)
        print(f"Retrieving fees from {url}")
        if not self.url:
            raise ValueError(f"Unsupported network: {self.network}")

        if not destination_domain_id:
            raise ValueError("Destination domain ID is required")

        # Allowed finalities according to Circle
        allowed_finalities = {1000, 2000}

        # Validate input
        if finality_threshold not in allowed_finalities:
            raise ValueError(
                f"Invalid finality_threshold={finality_threshold}. "
                f"Must be one of {allowed_finalities}"
            )

        while True:
            try:
                response = requests.get(url)

                if response.status_code == 200:
                    try:
                        print("Response received (200)")
                        print(f"Response: {response.text}")
                        parsed = GetFeeResponse.model_validate(response.json())
                        fees = parsed.root
                        for fee in fees:
                            if fee.finalityThreshold == finality_threshold:
                                print(f"Selected fee for finality {finality_threshold}: {fee}")
                                return fee
                    except ValidationError as e:
                        print("Invalid response format (200):", e)

                elif response.status_code == 400:
                    try:
                        err = GetFeesBadRequestResponse(**response.json())
                        print(f"Bad request: {err.message}")
                    except ValidationError as e:
                        print("Invalid error format (400):", e)

                elif response.status_code == 404:
                    try:
                        err = GetFeesNotFoundResponse(**response.json())
                        print(f"Not found ({err.code}): {err.message}")
                    except ValidationError as e:
                        print("Invalid error format (404):", e)

                else:
                    print(f"Unhandled error ({response.status_code}): {response.text}")

            except requests.exceptions.RequestException as e:
                print(f"Network error: {e}")

            time.sleep(5)
