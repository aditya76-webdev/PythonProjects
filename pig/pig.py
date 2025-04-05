import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll



while True:
    players = input("Enter number of players(2-4) : ")
    if players.isdigit():
        players = int(players)
        if 2<=players <=4:
            break
        else:
            print('number of players must be between 2-4')
    else:
        print("Invalid input, try again")

max_score = 50
# player_scores = [0]*players this will cause error in cases where inside mutable object is present

player_scores = [0 for player in range(players)]
print(player_scores)

while max(player_scores)<max_score:
    
    for player_idx in range(len(player_scores)):
        print('\nplayer number ',player_idx+1,'turn has just started.\n')
        curr_score = 0
        while True:
            should_roll = input("would you like to roll?(y)").lower()
            if should_roll !='y':
                break
            value = roll()
            # print(value)
            if value==1:
                curr_score=0
                break
            else:
                curr_score+=value
            print('Player ',player_idx+1,'rolled a ',value ,'and','Player', player_idx+1 ,'current score is ',curr_score)
        player_scores[player_idx]=curr_score
        print('score of player number ',player_idx+1,'is ',player_scores[player_idx])

        
        
    