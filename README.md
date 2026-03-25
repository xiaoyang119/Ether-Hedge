# HedgeX — Delta-Neutral Hedging DApp

A web-based frontend for interacting with the HedgeX perpetual swap hedging protocol deployed on the Ethereum Sepolia testnet.

## Prerequisites

- **Python 3** (any version 3.6+)
- **MetaMask** browser extension installed
- **Sepolia test ETH** in your wallet (for gas fees)
- **Sepolia LINK tokens** (used as collateral)

## Quick Start

1. Place `HedgeX_DApp.html` and `run.py` in the same folder.

2. Open a terminal in that folder and run:

   ```
   python run.py
   ```

3. The browser will open automatically to `http://localhost:8000/HedgeX_DApp.html`.

4. Click **Connect Wallet** — MetaMask will prompt you to connect and switch to Sepolia if needed.

## Getting Sepolia LINK Tokens

LINK is used as collateral in this protocol. To get test LINK:

1. Go to Chainlink's faucet: https://faucets.chain.link/sepolia
2. Connect your wallet and request LINK tokens.

## Features

| Feature | Description |
|---------|-------------|
| **Live Price Feed** | Reads ETH/USD price from Chainlink oracle via OracleAdapter |
| **Collateral Management** | Approve, deposit, and withdraw LINK tokens to/from MarginBank |
| **Open Hedge** | Open a delta-neutral short perpetual position with configurable hedge ratio |
| **Close Hedge** | Close your active hedge and settle P&L |
| **Position Health** | View real-time equity, unrealized P&L, and maintenance margin status |
| **Simulate Hedge** | Run on-chain pure simulation with custom entry/exit prices |

## Deployed Contracts (Sepolia Testnet)

| Contract | Address | Etherscan |
|----------|---------|-----------|
| HedgingVault | `0x0f6230e89d3e4740b9bcf96822fc4697e60fcd23` | [View](https://sepolia.etherscan.io/address/0x0f6230e89d3e4740b9bcf96822fc4697e60fcd23#code) |
| PerpetualEngine | `0x13b8af01bc24679e46b0a4337309f6cc42700515` | [View](https://sepolia.etherscan.io/address/0x13b8af01bc24679e46b0a4337309f6cc42700515#code) |
| MarginBank | `0x572da6dae1d0fba4ad2fae2d59da68702e44c435` | [View](https://sepolia.etherscan.io/address/0x572da6dae1d0fba4ad2fae2d59da68702e44c435#code) |
| OracleAdapter | `0xb5064fe9407d646e425ac3c86e9c533bff046b1a` | [View](https://sepolia.etherscan.io/address/0xb5064fe9407d646e425ac3c86e9c533bff046b1a#code) |
| RiskManager | `0x779f77def6dd09ad3471fdae33eb2efd86c27ddb` | [View](https://sepolia.etherscan.io/address/0x779f77def6dd09ad3471fdae33eb2efd86c27ddb#code) |
| LINK Token | `0x779877A7B0D9E8603169DdbD7836e478b4624789` | [View](https://sepolia.etherscan.io/address/0x779877A7B0D9E8603169DdbD7836e478b4624789) |
| Chainlink ETH/USD Feed | `0x1b44F3514812d835EB1BDB0acB33d3fA3351Ee43` | [View](https://sepolia.etherscan.io/address/0x1b44F3514812d835EB1BDB0acB33d3fA3351Ee43) |

## Usage Guide

### Step 1 — Approve & Deposit Collateral

Enter a LINK amount (e.g. `0.1`), click **Approve**, then click **Deposit**.

### Step 2 — Open a Hedge

- **Spot Value (USD, 8 decimals):** The USD value of your spot exposure. For $2000, enter `200000000000`.
- **Hedge Ratio (BPS):** `10000` = 100% hedge, `5000` = 50% hedge.
- **Collateral (18 decimals):** Amount of LINK for margin. For 0.1 LINK, enter `100000000000000000`.

Click **Open Hedge Position**.

### Step 3 — Monitor & Close

Use the **Position Health** panel to monitor your hedge. Click **Close Hedge** when ready to settle.

### Simulation

Use the **Simulate Hedge** panel to test scenarios without spending gas. This calls a `pure` function on-chain.

## Architecture

```
User ──▶ HedgingVault ──▶ PerpetualEngine ──▶ OracleAdapter (Chainlink)
              │                   │
              ▼                   ▼
          MarginBank         RiskManager
           (LINK)         (leverage/margin)
```

## Tech Stack

- **Frontend:** Vanilla HTML/CSS/JS with ethers.js v6
- **Smart Contracts:** Solidity 0.8.24, OpenZeppelin v5, Chainlink
- **Network:** Ethereum Sepolia Testnet
- **Server:** Python `http.server` (local development only)

## Troubleshooting

| Problem | Solution |
|---------|----------|
| MetaMask not connecting | Make sure MetaMask extension is installed and unlocked |
| Wrong network | Click Connect — the DApp will auto-prompt to switch to Sepolia |
| Price shows "Error" | Chainlink price may be stale; try refreshing after a few minutes |
| Transaction reverted | Check the Activity Log at the bottom for the error message |
| Port 8000 in use | Stop other servers, or edit `PORT` in `run.py` |
