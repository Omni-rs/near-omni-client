class JsonRpcError(Exception):
    """Excepción base for JSON-RPC errors."""
    def __init__(self, cause: str, message: str):
        self.cause = cause
        super().__init__(f"[{cause}] {message}")
