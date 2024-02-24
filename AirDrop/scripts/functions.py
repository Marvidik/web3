from brownie import EtherCollector,accounts,network

def transfer():
    trans=EtherCollector[-1]

    trans.collectAndTransfer({"from":accounts[0],"value":100000000000000000})

   

def main():
    transfer()
    