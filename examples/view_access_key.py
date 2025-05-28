import asyncio
import os

from near_omni_client.json_rpc.client import NearClient
from dotenv import load_dotenv


async def main():
    load_dotenv()

    # 1) Load account id
    account_id = os.getenv("NEAR_ACCOUNT_ID")
    public_key_str = os.getenv("NEAR_PUBLIC_KEY")

    # 2) Create client
    near_client = NearClient(provider_url="https://rpc.testnet.near.org")

    # 3) View access key
    access_key = await near_client.view_access_key(account_id, public_key_str)
    print("access_key", access_key)


if __name__ == "__main__":
    asyncio.run(main())
