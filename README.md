# HedgeX — Delta-Neutral Hedging DApp

A web-based frontend for interacting with the HedgeX perpetual swap hedging protocol deployed on the Ethereum Sepolia testnet.

## Prerequisites

- **Python 3** (any version 3.6+)
- **MetaMask** browser extension installed
- **Sepolia test ETH** in your wallet (for gas fees)

## Quick Start

1. Place `HedgeX_DApp.html` and `run.py` in the same folder.

2. Open a terminal in that folder and run:

   ```
   python run.py
   ```

3. The browser will open automatically to `http://localhost:8000/HedgeX_DApp.html`.

4. Click **Connect Wallet** — MetaMask will prompt you to connect and switch to Sepolia if needed.

5. Click **Claim 100 HDGT** to get free test tokens, then start trading.

## Getting HDGT Tokens

HDGT is the custom ERC-20 collateral token for this protocol. The `mint()` function is open to everyone — no owner restriction.

**Option 1 — Use the DApp (recommended):**
Click the **Claim 100 HDGT** button at the top of the page. Each click mints 100 HDGT to your wallet.

**Option 2 — Use Etherscan directly:**
Call `mint(yourAddress, amount)` on the [HedgeToken Write Contract](https://sepolia.etherscan.io/address/0x2acdc6ce20e8b2274a6ea9ae12463d5f413cac9b#writeContract) page.

## Features

| Feature | Description |
|---------|-------------|
| **HDGT Faucet** | One-click mint of free HDGT test tokens — no restrictions |
| **Live Price Feed** | Reads BTC/USD price from Chainlink oracle via OracleAdapter |
| **Collateral Management** | Approve, deposit, and withdraw HDGT tokens to/from MarginBank |
| **Open Hedge** | Open a delta-neutral short perpetual position with configurable hedge ratio |
| **Close Hedge** | Close your active hedge and settle P&L |
| **Position Health** | View real-time equity, unrealized P&L, and maintenance margin status |
| **Simulate Hedge** | Run on-chain pure simulation with custom entry/exit prices |

## Deployed Contracts (Sepolia Testnet)

| Contract | Address | Etherscan |
|----------|---------|-----------|
| HedgeToken (HDGT) | `0x2acdc6ce20e8b2274a6ea9ae12463d5f413cac9b` | [View](https://sepolia.etherscan.io/address/0x2acdc6ce20e8b2274a6ea9ae12463d5f413cac9b#code) |
| HedgingVault | `0xe1de74229b02503282d247a568288860d0dca407` | [View](https://sepolia.etherscan.io/address/0xe1de74229b02503282d247a568288860d0dca407#code) |
| PerpetualEngine | `0xf4d282a0d4ea06bdae9e98480790bd5904e037cc` | [View](https://sepolia.etherscan.io/address/0xf4d282a0d4ea06bdae9e98480790bd5904e037cc#code) |
| MarginBank | `0xe8e7a72ff1803b22f4ee5d72406ada7ad4890bd5` | [View](https://sepolia.etherscan.io/address/0xe8e7a72ff1803b22f4ee5d72406ada7ad4890bd5#code) |
| OracleAdapter | `0x2f15b664afe72740ec4d98222f389a90f7c6c8a4` | [View](https://sepolia.etherscan.io/address/0x2f15b664afe72740ec4d98222f389a90f7c6c8a4#code) |
| RiskManager | `0x0eb59afb6e9e12df69e30db3d634c5e725e2b5c7` | [View](https://sepolia.etherscan.io/address/0x0eb59afb6e9e12df69e30db3d634c5e725e2b5c7#code) |
| Chainlink BTC/USD Feed | `0x1b44F3514812d835EB1BDB0acB33d3fA3351Ee43` | [View](https://sepolia.etherscan.io/address/0x1b44F3514812d835EB1BDB0acB33d3fA3351Ee43) |

## Usage Guide

### Step 0 — Get HDGT Tokens

Click **Claim 100 HDGT** at the top of the DApp. Repeat as needed.

### Step 1 — Approve & Deposit Collateral

Enter a HDGT amount (e.g. `1`), click **Approve**, then click **Deposit**.

### Step 2 — Open a Hedge

- **Spot Value (USD, 8 decimals):** The USD value of your spot exposure. For $100, enter `10000000000`.
- **Hedge Ratio (BPS):** `10000` = 100% hedge, `5000` = 50% hedge.
- **Collateral (18 decimals):** Amount of HDGT for margin. For 1 HDGT, enter `1000000000000000000`.

Click **Open Hedge Position**.

### Step 3 — Monitor & Close

Use the **Position Health** panel to monitor your hedge. Click **Close Hedge** when ready to settle.

### Withdraw

Enter the amount in the Collateral Management panel and click **Withdraw**. You can only withdraw your free (unreserved) balance. Close any active hedge first to free up reserved collateral.

### Simulation

Use the **Simulate Hedge** panel to test scenarios without spending gas. This calls a `pure` function on-chain.

## Architecture

```
User ──▶ HedgingVault ──▶ PerpetualEngine ──▶ OracleAdapter (Chainlink BTC/USD)
              │                   │
              ▼                   ▼
          MarginBank         RiskManager
           (HDGT)         (leverage/margin)
```

## Tech Stack

- **Frontend:** Vanilla HTML/CSS/JS with ethers.js v6
- **Smart Contracts:** Solidity 0.8.20–0.8.24, OpenZeppelin v5, Chainlink
- **Network:** Ethereum Sepolia Testnet
- **Server:** Python `http.server` (local development only)

## Troubleshooting

| Problem | Solution |
|---------|----------|
| MetaMask not connecting | Make sure MetaMask extension is installed and unlocked |
| Wrong network | Click Connect — the DApp will auto-prompt to switch to Sepolia |
| Price shows "Stale" | Chainlink Sepolia feed updates infrequently; the DApp will show the last known price with a warning |
| Claim HDGT failed | Make sure your wallet is connected and you have Sepolia ETH for gas |
| Withdraw failed | Make sure you are withdrawing ≤ your Free balance (not Reserved) |
| Transaction reverted | Check the Activity Log at the bottom for the error message |
| Port 8000 in use | Stop other servers, or edit `PORT` in `run.py` |
