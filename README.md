# near-omni-client

**near-omni-client** is minimal Python library to interact with the NEAR blockchain and [Chain Signatures].

## Features

- Lightweight
- Fully asynchronous

## Getting Started

Install the latest version of `near-omni-client` by running:

```bash
$ pip install near-omni-client

# or if using uv

$ uv add near-omni-client
```

Create a NEAR account and get your private key using the [NEAR CLI].

## Contributing

If you are thinking about contributing to the **near-omni-client**, first of all thanks a lot ! We would love your contribution ! 

To understand the process for contributing, see [CONTRIBUTING.md].

<!-- REFERENCES -->
[Chain Signatures]: https://docs.near.org/chain-abstraction/chain-signatures
[CONTRIBUTING.md]: ./contributing.md


<!-- TO Review -->

# 🔧 Deinfra — Modular SDK for Multi-chain DeFi Infra

**Deinfra** is a modular Python SDK designed to interact with DeFi protocols, JSON-RPC APIs, and custom external signers (like MPCs or cold wallets) across multiple blockchains like Ethereum and NEAR.

Built for builders who simulate, automate, or execute complex on-chain flows.

---

## ✨ Features

- ✅ Wallet abstraction for Ethereum and NEAR
- ✅ Plugable signer system (MPC-ready, local keys, remote APIs)
- ✅ Clean JSON-RPC clients (NEAR + ETH)
- ✅ Protocol adapters (e.g. Aave, USDC, Compound)
- ✅ Transaction builders (create → sign → send)
- ✅ Async-ready, testable, and production-grade structure

---

## 🧠 Designed for

- Simulators of staking/lending/liquidity systems
- Automated bots that sign via external MPC
- DeFi dashboards, analytics, and backtest tools
- Builders of infra, not just frontend consumers

---

## 📦 Modules

```text
wallet/      # Wallets per chain (EthereumWallet, NearWallet)
signer/      # Signers: local, MPC, chain-level
rpc/         # JSON-RPC wrappers (NearRPC, EthRPC)
contracts/   # Protocol adapters (USDC, Aave, Compound, etc.)
provider/    # RPC provider factories (Alchemy, Infura, custom)
transaction/ # TX builders, utils
```

<!-- TO REVIEW -->

# 🔗 near-omni-client

Modular NEAR SDK for bots, dApps, and automated agents.

**near-omni-client** gives you:

- Clean access to the NEAR JSON-RPC API
- Extensible wallet/signing system (MPC, local keys, remote APIs)
- Adapters for higher-level NEAR abstractions (accounts, permissions, etc.)
- Provider factory for mainnet/testnet/localnet switching
- Transaction crafting and pre-signing

Ideal for keepers, bots, simulators, indexers or power-user dApps.

## Modules
- `json_rpc` – low-level JSON-RPC interface
- `wallets` – chain-safe wallet abstraction
- `signers` – pluggable signer implementations (MPC, local, remote)
- `adapters` – opinionated high-level logic
