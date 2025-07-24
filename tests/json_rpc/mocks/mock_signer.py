from near_omni_client.signers.interfaces import ISigner


class MockSigner(ISigner):
    def sign_bytes(self, data: bytes) -> bytes:
        # return a dummy signature 64 bytes (64 zeros)
        return b"\x00" * 64
