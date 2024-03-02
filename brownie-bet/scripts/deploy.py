from brownie import MarviesBet,accounts,network


def deploy_bet():
    
    deployed_contract = MarviesBet.deploy(accounts[0],{'from': accounts[5]})

    # Print contract address
    print("Contract deployed at:", deployed_contract.address)



def main():
    deploy_bet()