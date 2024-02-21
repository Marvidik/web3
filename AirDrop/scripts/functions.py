from brownie import Airdrop,accounts,network

def displayAmount():
    betting=Airdrop[-1]

    amount=betting.displayAmount({"from":"0x5f67AC1cE46699026B8E07C8418F26b148d6f9B1","value":50})



def transfer():
    trans=Airdrop[-1]

    trans.transferEther({"from":"0x5f67AC1cE46699026B8E07C8418F26b148d6f9B1"})

   

def main():
    transfer()
    