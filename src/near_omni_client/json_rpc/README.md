## NEAR JSON-RPC – Supported Methods

### 🔑 Access Keys

- [✅] `view_access_key`: Returns information about a single access key for given account.
- [✅] `view_access_key_list`: List of all access keys for a given account.
- [❌] `single_access_key_changes` (EXPERIMENTAL): Returns individual access key changes in a specific block.
- [❌] `all_access_key_changes` (EXPERIMENTAL): Returns changes to all access keys of a specific block. 

### 👤 Accounts / Contracts

- [✅] `view_account`: Returns basic account information.
- [❌] `account_changes` (EXPERIMENTAL): Returns account changes from transactions in a given account.
- [✅] `view_code`: Returns the contract code (Wasm binary) deployed to the account.
- [✅] `view_state`: Returns the state (key value pairs) of a contract based on the key prefix (base64 encoded).
- [❌] `data_changes` (EXPERIMENTAL): Returns the state change details of a contract based on the key prefix (encoded to base64).
- [❌] `contract_code_changes` (EXPERIMENTAL): Returns code changes made when deploying a contract.
- [✅] `call_function`: Allows you to call a contract method as a view function.

### 📦 Block / Chunk

- [✅] `block`: Queries network and returns block for given height or hash. You can also use finality param to return latest block details.
- [✅] `chunk`: Returns details of a specific chunk. 
- [❌] `EXPERIMENTAL_changes_in_block`: Returns changes in block for given block height or hash. You can also use finality param to return latest block details.

### ⛽ Gas

- [ ] `gas_price`: Returns gas price for a specific block_height or block_hash.

### ⚙️ Protocol

- [❌] `EXPERIMENTAL_genesis_config` (EXPERIMENTAL): Returns current genesis configuration.
- [❌] `EXPERIMENTAL_protocol_config` (EXPERIMENTAL): Returns most recent protocol configuration or a specific queried block.

### 🌐 Network

- [✅] `status`: Returns general status of a given node (sync status, nearcore node version, protocol version, etc.), and the current set of validators.
- [✅] `network_info`: Returns the current state of node network connections (active peers, transmitted data, etc.)
- [✅] `validators`: Queries active validators on the network returning details and the state of validation on the blockchain.

### 🔄 Transactions

- [✅] `send_tx`: Send a signed transaction.
- [✅] `tx`: Get transaction status by hash and signer.
- [❌] `EXPERIMENTAL_tx_status` (EXPERIMENTAL): Get status of a transaction.
- [❌] `EXPERIMENTAL_receipt`: Broadcast and wait for execution.