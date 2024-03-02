from brownie import MarviesBet,accounts




def bet():
    betting=MarviesBet[-1]
    
    count_of_participants=int(input("enter the number of people betting"))
    print("Note The Amount to be staked for each person is 0.1 ether")

    for i in range(count_of_participants):
        participant=input("Enter the participant wallet address")
        betting.bet({"from":participant,"value":100000000000000000})


def main():
    bet()