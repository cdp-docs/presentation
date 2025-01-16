# Create your first wallet and transact funds

<!-- For the sake of brevity, I'm only covering the CDP Python setup here -->
## Introduction

The CDP SDK allows you to create wallets and send funds onchain within minutes. 

In this quickstart, you will learn:

- How to create a Developer-Managed wallet
- Fund the wallet with testnet ETH (for experimentation using a simulated ETH network)
- Transfer funds between wallets
- Trade assets  

## Prerequisites

You must meet the following requirements before continuing:

- Completed installation and setup of [`cdp-sdk`](getting-started.md)
- Python 3.10 or higher
  
It is assumed that you already have an API key as a part of installing and setting up the SDK.

## Step 1 -- Initialize the CDP SDK
  
Create a Python script and paste the following:  

```python title="wallet.py"
from cdp import *

# Paste in your API key name and private key
api_key_name = ""
api_key_private_key = ""

Cdp.configure(api_key_name, api_key_private_key)

# Alternatively, you can source the API key directly from a file downloaded from the CDP portal:
# Cdp.configure_from_json("~/Downloads/cdp_api_key.json")

print("CDP SDK has been successfully configured.")
```

Here, we have the option to pass the API key name and private key or pass in the API key file directly.

## Step 2 -- Create a wallet

Now that the SDK has been initialized, we can create a wallet. Add the following to your script.

```title="wallet.py"
# Create a wallet with one address by default
wallet = Wallet.create()

# Access the wallet's default address
address = wallet.default_address

print(f"Wallet successfully created: {wallet}")
```

!!! warning
    To prevent losing access to your wallet, make sure you [persist the wallet](). Wallets are not persisted by default.

## Step 3 -- Fund the wallet

The wallet you created is empty by default. Let's add some funds. 

For Base Sepolia testnet, we provide a faucet method to fund your wallet with testnet ETH. Add the following to your script:

```title="wallet.py"
# Fund the wallet with a faucet transaction.
faucet_tx = wallet1.faucet()

# Wait for faucet transaction to land on-chain.
faucet_tx.wait()

print(f"Faucet transaction successfully completed: {faucet_tx}")
```

## Step 4 -- Transfer funds

Now that your [faucet transaction](https://www.coinbase.com/learn/crypto-glossary/what-is-a-crypto-faucet) has funded your wallet, you can transfer funds to another wallet. 

Add the code below to your script.

```python title="wallet.py"
# Create a new wallet to which we will transfer funds.
another_wallet = Wallet.create()

print(f"Wallet successfully created: {another_wallet}")

# Tranfer ETH from our original wallet and into the new wallet
transfer = wallet.transfer(0.00001, "eth", another_wallet).wait()

print(f"Transfer successfully completed: {transfer}")
```

## Step 5 -- Test

At this point, your script should contain the following:

```python title="wallet.py"
from cdp import *

# Paste in your API key name and private key
api_key_name = ""
api_key_private_key = ""

Cdp.configure(api_key_name, api_key_private_key)

# Alternatively, you can source the API key directly from a file downloaded from the CDP portal:
# Cdp.configure_from_json("~/Downloads/cdp_api_key.json")

print("CDP SDK has been successfully configured.")

# Create a wallet with one address by default
wallet = Wallet.create()

# Access the wallet's default address
address = wallet.default_address

print(f"Wallet successfully created: {wallet}")

# Fund the wallet with a faucet transaction.
faucet_tx = wallet.faucet()

# Wait for faucet transaction to land on-chain.
faucet_tx.wait()

print(f"Faucet transaction successfully completed: {faucet_tx}")

# Create a new wallet to which we will transfer funds.
another_wallet = Wallet.create()

print(f"Wallet successfully created: {another_wallet}")

# Tranfer ETH from our original wallet and into the new wallet
transfer = wallet.transfer(0.00001, "eth", another_wallet).wait()

print(f"Transfer successfully completed: {transfer}")
```

Run your script and observe its output. You should see similar output:

```console
CDP SDK has been successfully configured.
Wallet successfully created: Wallet: (id: 72126803-5d32-4742-b2fa-8b827f0a52e2, network_id: base-sepolia, server_signer_status: None)
Faucet transaction successfully completed: FaucetTransaction: (transaction_hash: 0x2c5ea6c2b0a8a49579155058831c45da0e0640cb16f532b832c7bca744146832, transaction_link: https://sepolia.basescan.org/tx/0x2c5ea6c2b0a8a49579155058831c45da0e0640cb16f532b832c7bca744146832, status: complete, network_id: base-sepolia)
Wallet successfully created: Wallet: (id: 081a99f6-7b87-455a-a533-f9c971561e83, network_id: base-sepolia, server_signer_status: None)
Transfer successfully completed: Transfer: (transfer_id: ce6c6135-1b9e-4588-97ee-c953281b3c08, network_id: base-sepolia, from_address_id: 0x9E0E8d7eA52478790F1ec2145Db747fE858926dd, destination_address_id: 0x236447789d2622bf403026227Ad356D74ba62239, asset_id: eth, amount: 0.00001, transaction_link: https://sepolia.basescan.org/tx/0xeae6dcc43b6fda764638a49887d28007562534b49b674021a91ebfb53ba7eed1, status: complete)
```

We can see that our first wallet was created and funded using a faucet transaction.

Our secondary wallet, `081a99f6-...` was also successfully created, with a completed transaction.

## Step 6 -- Trade assets

On `base-mainnet` you can trade between different assets from your wallet. 

Since trading is only supported on mainnet wallets, wallet should be funded with real assets before trading. The code below creates a wallet and trades some ETH to USDC and then all of the USDC to WETH:

```
# Create a wallet on `base-mainnet` to trade assets with.
wallet = Wallet.create(network_id="base-mainnet")

print("Wallet successfully created: {wallet}")

# Fund wallet's default address with ETH from an external source.

# Trade 0.00001 ETH to USDC
trade = wallet.trade(0.00001, "eth", "usdc").wait()

if trade.status is Transaction.Status.COMPLETE:
  print(f"Trade successfully completed: {trade}")
else:
  print(f"Trade failed on-chain: {trade}")

# Trade the wallet's full balance of USDC to WETH
trade2 = wallet.trade(wallet.balance("usdc"), "usdc", "weth").wait()

if trade2.status is Transaction.Status.COMPLETE:
  print(f"Second trade successfully completed: {trade2}")
else:
  print(f"Second trade failed on-chain: {trade}")
```

## What to read next

- **[Trades](https://docs.cdp.coinbase.com/mpc-wallet/docs/trades):** Convert one asset into a different asset
- **[Transfers](https://docs.cdp.coinbase.com/mpc-wallet/docs/transfers):** Send an asset from wallet or address to another
- **[Persisting a Wallet](https://docs.cdp.coinbase.com/mpc-wallet/docs/NodeJS/quickstart/persist_wallet):** A new wallet is not persisted by default. Learn more on how to persist a wallet.