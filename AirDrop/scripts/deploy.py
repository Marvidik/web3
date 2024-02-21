from brownie import Airdrop,accounts,network


def deploy_bet():
    
    recipient_address = "0x5f67AC1cE46699026B8E07C8418F26b148d6f9B1"
    deployed_contract = Airdrop.deploy(recipient_address, {'from': accounts[2]})

    # Print contract address
    print("Contract deployed at:", deployed_contract.address)


def main():
    deploy_bet()
    