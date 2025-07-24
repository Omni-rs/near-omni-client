import asyncio
import os

from dotenv import load_dotenv

from near_omni_client.networks.network import Network


async def main():
    load_dotenv()

    # 1) Load account id
    private_key = os.getenv("PRIVATE_KEY")
    source_network = Network.parse(os.getenv("SOURCE_NETWORK"))
    destination_network = Network.parse(os.getenv("DESTINATION_NETWORK"))
    alchemy_api_key = os.getenv("ALCHEMY_API_KEY")
    print(f"PRIVATE_KEY: {private_key}")
    print(f"SOURCE_NETWORK: {source_network}")
    print(f"DESTINATION_NETWORK: {destination_network}")
    print(f"ALCHEMY_API_KEY: {alchemy_api_key}")

    # 2) Create client
    # alchemy_provider = AlchemyFactoryProvider(api_key=alchemy_api_key)

    # 3)
    #     wallet = Wallet(


#         private_key,
#         provider_factory=alchemy_provider,
#         supported_networks=[source_network, destination_network]
#     )

#     print(f"Wallet Address: {wallet.get_wallet_address()}")
#     print(f"Supported Networks: {wallet.supported_networks}")

#     # approve usdc
#     usdc_approve_tx = USDCContract(source_network, wallet).approve(
#         spender=Web3.to_checksum_address(MessengerContract.get_address_for_network(source_network)),
#         amount=to_usdc_units(10000000)) # 10 million USDC
#     print(f"USDC approved successfully!")
#     print(f"USDC approved Transaction Hash: 0x{usdc_approve_tx.hex()}")

#     # burn usdc
#     messenger_deposit_for_burn_tx_hash = MessengerContract(source_network, wallet).deposit_for_burn(
#         amount=to_usdc_units(1),
#         destination_domain=int(destination_network.domain),
#         destination_address=address_to_bytes32(wallet.get_wallet_address()),
#         token_address=Web3.to_checksum_address(USDCContract.get_address_for_network(source_network)),
#         destination_caller=address_to_bytes32(wallet.get_wallet_address()),
#         max_fee=to_usdc_units(0.99),
#         min_finality_threshold=1000, # check readme for more info about the finality threshold
#     )
#     print(f"USDC burned successfully!")
#     print(f"USDC burned Transaction Hash: 0x{messenger_deposit_for_burn_tx_hash.hex()}")

#     # retrieve attestation
#     attestation = AttestationService(source_network).retrieve_attestation(f"0x{messenger_deposit_for_burn_tx_hash.hex()}")
#     print(f"Attestation retrieved successfully!")
#     print(f"Attestation: {attestation}")

#     # mint usdc
#     usdc_mint_tx_hash = TransmitterContract(destination_network, wallet).mint_usdc(
#         attestation_message=attestation.message,
#         attestation=attestation.attestation
#     )
#     print(f"USDC transfer completed successfully!")
#     print(f"Transaction Hash: 0x{usdc_mint_tx_hash.hex()}")


if __name__ == "__main__":
    asyncio.run(main())
