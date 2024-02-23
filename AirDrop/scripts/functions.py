from brownie import Airdrop,accounts,network

def displayAmount():
    betting=Airdrop[-1]

    amount=betting.displayAmount({"from":accounts[1],"value":50})



def transfer():
    trans=Airdrop[-1]

    trans.transferEther({"from":accounts[1]})

   

def main():
    displayAmount()
    