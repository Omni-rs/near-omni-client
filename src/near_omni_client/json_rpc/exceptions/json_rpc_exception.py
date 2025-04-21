class JsonRpcError(Exception):
    """
    Exception class for handling JSON-RPC errors.
    This class is designed to parse and store error information from a JSON-RPC response.
    The error information is expected to be in the following format:
    {
        "name": <ERROR_TYPE>,
        "cause": { "name": <ERROR_CAUSE>, "info": {...} },
        "code": int,
        "data": str,
        "message": str
    }
    """
    def __init__(self, error_json: dict):
        self.error_type  = error_json.get("name")
        cause           = error_json.get("cause", {})
        self.cause_name = cause.get("name")
        self.cause_info = cause.get("info")
        self.code       = error_json.get("code")
        self.data       = error_json.get("data")
        self.message    = error_json.get("message")
        super().__init__(f"[{self.cause_name or self.error_type}] {self.message}")
