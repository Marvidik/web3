from brownie import MarviesBet,accounts




def bet():
    betting=MarviesBet[-1]
    

    betting.bet({"from":"0x2B246C091Fc2D52E274B758dC9938441AE53b7B0","value":50})


def main():
    bet()