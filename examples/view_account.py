import asyncio
import os

from dotenv import load_dotenv

from near_omni_client.json_rpc.client import NearClient


async def main():
    load_dotenv()

    # 1) Load account id
    account_id = os.getenv("NEAR_ACCOUNT_ID")

    # 2) Create client
    near_client = NearClient(provider_url="https://rpc.testnet.near.org")

    # 3) View account
    account = await near_client.view_account(account_id)
    print("account", account)


if __name__ == "__main__":
    asyncio.run(main())
