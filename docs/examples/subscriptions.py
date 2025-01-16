from cdp import *

api_key_name = "organizations/bbb02305-e5c0-4db2-a2dc-0fe2cb56c5bf/apiKeys/5f40498e-a928-4488-80fb-dd209daa514d"

api_key_private_key = "-----BEGIN EC PRIVATE KEY-----\nMHcCAQEEIAi7g9SoAvOEcCGSIoUtebKFeJjNHEO7tPjkdKkCnt8GoAoGCCqGSM49\nAwEHoUQDQgAEEr1Fk3XW7GjdmPSAaCFNRBzCgk72zdhjXyTFMJD+E/Q7+X54F90e\nuOQd+LgPhiRAKjs/ccVdPQRax5jsvNyf8g==\n-----END EC PRIVATE KEY-----\n"

#api_key_name = os.getenv('COINBASE_API_KEY_NAME') 
#api_key_private_key = os.getenv('COINBASE_API_PRIVATE_KEY')

Cdp.configure(api_key_name, api_key_private_key)

print("Completed config.")


# Create a wallet with one address by default
wallet = Wallet.create()

# Access the wallet's default address
address = wallet.default_address

print(f"Wallet successfully created: {wallet}")
    
# Pick a file to which to save your wallet seed.
file_path = "wallet_seed.json"

# Set encrypt=True to encrypt the wallet seed with your CDP secret API key.
wallet.save_seed(file_path, encrypt=True)

print(f"Seed for wallet {wallet.id} successfully saved to {file_path}.")

# Fund the wallet with a faucet transaction.
faucet_tx = wallet.faucet()

# Wait for faucet transaction to land on-chain.
faucet_tx.wait()

print(f"Faucet transaction successfully completed: {faucet_tx}")

# Step 3: Deploy the ERC-20 Token
#deployed_token = wallet.deploy_token("SubscriptionToken", "SUB", 1000000)
#deployed_token.wait()

# Step 4: Get the Token Address
#token_address = deployed_token.contract_address
#print(f"Token contract deployed at: {token_address}")


