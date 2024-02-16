from solcx import compile_standard
import json
from web3 import Web3

# Read the Solidity source code
with open("MarviesBet.sol", "r") as solfile:
    source_code = solfile.read()

# Compile the Solidity source code
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"MarviesBet.sol": {"content": source_code}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
                }
            }
        }
    },
    solc_version="0.8.0"
)

# Write the compiled output to a JSON file
with open("compiled_sol.json", "w") as compiled_sol_json:
    json.dump(compiled_sol, compiled_sol_json)

# Extract bytecode and ABI
bytecode = compiled_sol["contracts"]["MarviesBet.sol"]["MarviesBet"]["evm"]["bytecode"]["object"]
abi = compiled_sol["contracts"]["MarviesBet.sol"]["MarviesBet"]["abi"]

# Connect to the Ethereum node
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

# Define account information
chain_id =1337
my_address = "0xFa7Fe886e2C66F2f7854be41229F9E4f12b3D64C"
private_key = "0xa858661394d31bb3fc51e95ce48104e676476b56f84585cbbd59898230db3db0"

# Set the default account
w3.eth.default_account = my_address

# Create a contract instance
MarviesBet = w3.eth.contract(abi=abi, bytecode=bytecode)

nonce=w3.eth.get_transaction_count(my_address)


# # Deploy the contract
transaction = MarviesBet.constructor().build_transaction({"chainId":chain_id,"from":my_address,"nonce":nonce})

signed_txn=w3.eth.account.sign_transaction(transaction,private_key=private_key)
tx_hash=w3.eth.send_raw_transaction(signed_txn.rawTransaction)

tx_receipt=w3.eth.wait_for_transaction_receipt(tx_hash)



#Working with the contract
marvies_bet=w3.eth.contract(address=tx_receipt.contractAddress,abi=abi)

betting=marvies_bet.functions.bet().build_transaction({
    "chainId":chain_id,"from":my_address,"nonce":nonce+1
})

signed_bet=w3.eth.account.sign_transaction(betting,private_key=private_key)
bet_tnx=w3.eth.send_raw_transaction(signed_bet)
tx_receipt=w3.eth.wait_for_transaction_receipt(bet_tnx)
