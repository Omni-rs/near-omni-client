from .interfaces.signer import ISigner


class LocalEthSigner(ISigner):
    def __init__(self, private_key: str):
        self.private_key = private_key

    def sign(self, data: bytes) -> bytes:
        return self.private_key.sign(data)
