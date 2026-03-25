# HedgeX — Delta-Neutral Hedging DApp

A web-based frontend for interacting with the HedgeX perpetual swap hedging protocol deployed on the Ethereum Sepolia testnet.

## Prerequisites

- **Python 3** (any version 3.6+)
- **MetaMask** browser extension installed
- **Sepolia test ETH** in your wallet (for gas fees)
- **HDGT tokens** (custom ERC-20 collateral — minted by the contract owner)

## Quick Start

1. Place `HedgeX_DApp.html` and `run.py` in the same folder.

2. Open a terminal in that folder and run:

   ```
   python run.py
   ```

3. The browser will open automatically to `http://localhost:8000/HedgeX_DApp.html`.

4. Click **Connect Wallet** — MetaMask will prompt you to connect and switch to Sepolia if needed.

## Getting HDGT Tokens

HDGT is the custom ERC-20 collateral token for this protocol. To get test HDGT:

1. Ask the contract owner to call `mint(yourAddress, amount)` on the HedgeToken contract.
2. Or, if you are the owner, call `mint()` directly via [Etherscan Write Contract](https://sepolia.etherscan.io/address/0x8eb6392ebb2c09413f3e9bd3976da199f6d253cc#writeContract).

## Features

| Feature | Description |
|---------|-------------|
| **Live Price Feed** | Reads ETH/USD price from Chainlink oracle via OracleAdapter |
| **Collateral Management** | Approve, deposit, and withdraw HDGT tokens to/from MarginBank |
| **Open Hedge** | Open a delta-neutral short perpetual position with configurable hedge ratio |
| **Close Hedge** | Close your active hedge and settle P&L |
| **Position Health** | View real-time equity, unrealized P&L, and maintenance margin status |
| **Simulate Hedge** | Run on-chain pure simulation with custom entry/exit prices |

## Deployed Contracts (Sepolia Testnet)

| Contract | Address | Etherscan |
|----------|---------|-----------|
| HedgeToken (HDGT) | `0x8eb6392ebb2c09413f3e9bd3976da199f6d253cc` | [View](https://sepolia.etherscan.io/address/0x8eb6392ebb2c09413f3e9bd3976da199f6d253cc#code) |
| HedgingVault | `0x9cdff898604459e52f4893d394b567d8b220fe9d` | [View](https://sepolia.etherscan.io/address/0x9cdff898604459e52f4893d394b567d8b220fe9d#code) |
| PerpetualEngine | `0x67d6336e7815a93d6558864112838037b5f5f42b` | [View](https://sepolia.etherscan.io/address/0x67d6336e7815a93d6558864112838037b5f5f42b#code) |
| MarginBank | `0xeb641df51fad8bf6945c7f64491023427241d12b` | [View](https://sepolia.etherscan.io/address/0xeb641df51fad8bf6945c7f64491023427241d12b#code) |
| OracleAdapter | `0xb3d728c5e17191b4c85f8b6e10acb9f6c2d33b08` | [View](https://sepolia.etherscan.io/address/0xb3d728c5e17191b4c85f8b6e10acb9f6c2d33b08#code) |
| RiskManager | `0xe1f0f15ebd6aa0672e21ab966b4778c15280884f` | [View](https://sepolia.etherscan.io/address/0xe1f0f15ebd6aa0672e21ab966b4778c15280884f#code) |
| Chainlink ETH/USD Feed | `0x1b44F3514812d835EB1BDB0acB33d3fA3351Ee43` | [View](https://sepolia.etherscan.io/address/0x1b44F3514812d835EB1BDB0acB33d3fA3351Ee43) |

## Usage Guide

### Step 1 — Approve & Deposit Collateral

Enter a HDGT amount (e.g. `0.1`), click **Approve**, then click **Deposit**.

### Step 2 — Open a Hedge

- **Spot Value (USD, 8 decimals):** The USD value of your spot exposure. For $2000, enter `200000000000`.
- **Hedge Ratio (BPS):** `10000` = 100% hedge, `5000` = 50% hedge.
- **Collateral (18 decimals):** Amount of HDGT for margin. For 0.1 HDGT, enter `100000000000000000`.

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
           (HDGT)         (leverage/margin)
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
