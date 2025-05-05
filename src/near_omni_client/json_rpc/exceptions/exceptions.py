class UnknownBlockError(Exception):
    pass

class InvalidAccountError(Exception):
    pass

class UnknownAccountError(Exception):
    pass

class UnknownAccessKeyError(Exception):
    pass

class UnavailableShardError(Exception):
    pass

class NoSyncedBlocksError(Exception):
    pass


ERRORS = {
    "UNKNOWN_BLOCK": UnknownBlockError,
    "INVALID_ACCOUNT": InvalidAccountError,
    "UNKNOWN_ACCOUNT": UnknownAccountError,
    "UNKNOWN_ACCESS_KEY": UnknownAccessKeyError,
    "UNAVAILABLE_SHARD": UnavailableShardError,
    "NO_SYNCED_BLOCKS": NoSyncedBlocksError,
}

ERROR_MESSAGES = {
    "UNKNOWN_BLOCK": "The block has not been produced or has been garbage-collected.",
    "INVALID_ACCOUNT": "The account ID format is invalid.",
    "UNKNOWN_ACCOUNT": "The account doesn't exist or has been deleted.",
    "UNKNOWN_ACCESS_KEY": "The public key is not associated with the account.",
    "UNAVAILABLE_SHARD": "The shard is not tracked by this RPC node.",
    "NO_SYNCED_BLOCKS": "The node is still syncing and has no blocks.",
    "INTERNAL_ERROR": "Something went wrong with the node. Try again later.", # TODO
    "PARSE_ERROR": "Invalid JSON-RPC request parameters.", # TODO
}
