from brownie import EtherCollector,accounts,network


def deploy_bet():
    
    recipient_address = accounts[1]
    deployed_contract = EtherCollector.deploy(recipient_address, {'from': accounts[0]})

    # Print contract address
    print("Contract deployed at:", deployed_contract.address)


def main():
    deploy_bet()
    