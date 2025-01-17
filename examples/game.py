from cdp import *
import os
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key_name = os.getenv("API_KEY_NAME")
api_key_pk = os.getenv("API_KEY")

# Configure the API with the loaded values
Cdp.configure(api_key_name, api_key_pk)

# Token Smart Contract address from CDP Portal
contract_address = os.getenv("CONTRACT_ADDRESS")

# Fetch player's wallet from locally persisted seed file
seed = os.getenv("SEED")
fetched_wallet = Wallet.fetch(seed)

# Load seed into wallet from file
fetched_wallet.load_seed_from_file("test_wallet_seed.json")
print("Seed loaded.")

# Get player's address as a string
player_address = fetched_wallet.default_address.address_id

print(f"Player address: {player_address}")

# Create a wallet with one address by default
shop_wallet = Wallet.create()
print(f"Wallet successfully created: {shop_wallet}")

# Item price in tokens (e.g., 50 GameCoins)
item_price = 50

def buy_item(player_wallet, contract_address, item_price, shop_address):

    # A correctly formatted player's wallet address is needed to interact with the smart contract 
    player_address = player_wallet.default_address.address_id
    
    # 1: Check player's token balance
    balance = player_wallet.invoke_contract(
        contract_address=contract_address,  
        method="balanceOf",                 
        args={"account": player_address}    
    )
    
    # Tokens are often in the smallest unit (like wei for Ethereum-based tokens).
    balance_in_tokens = balance / (10**18)  # Convert from wei to human-readable tokens

    if balance_in_tokens < item_price:
        print(f"Not enough tokens to buy this item! Current balance: {balance_in_tokens}, Item price: {item_price}")
        return False

    # 2: Approve the contract to spend the player's tokens 
    approval = player_wallet.invoke_contract(
        contract_address=contract_address,  # Address of the token contract
        method="approve",                   # Approve method for spending tokens
        args={"spender": shop_address, "value": item_price}  # Allow shop to spend item price
    )
    approval.wait()  # Wait for approval transaction confirmation

    # 3: Transfer tokens to the shop's wallet address
    transfer = player_wallet.invoke_contract(
        contract_address=contract_address,  # Token contract address
        method="transferFrom",              # Method to transfer tokens from player 
        args={
            "from": player_address,         # Player's address
            "to": shop_address,             # Shop's address
            "value": item_price             # Item price in tokens
        }
    )
    transfer.wait()  # Wait for the transfer transaction confirmation

    # 4: Confirm the purchase
    print("Item purchased successfully!")
    return True

def buy_item_with_transfer(player_wallet, contract_address, item_price):

    # The player's wallet address is needed to interact with the smart contract in the correct format. 
    player_address = player_wallet.default_address.address_id  

    # Create a gasless USDC transfer on Base Mainnet
    transfer = player_wallet.transfer(
    0.01,
    "usdc",
    shop_wallet,
    gasless=True,
    )

    # Gasless transfer 0.00001 Ether to the destination address.
    transfer = wallet.transfer(0.00001, "eth", another_wallet, gasless=True)

    # Wait for transfer to settle.
    transfer.wait()

# Example 
buy_item(fetched_wallet, contract_address, item_price, shop_address)
buy_item_with_transfer(fetched_wallet, contract_address, item_price)

