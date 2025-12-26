import random 

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 1 < players <= 4:
            break
        else:
            print("Number of players must be between 2 and 4.")
    else:
        print("Invalid input. Please enter a number between 2 and 4.")
        

max_score = 50
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer", player_idx + 1, "'s turn.")
        print("Your total score is:", players_scores[player_idx], '\n')
        current_score = 0
    
    while True: 
        should_roll = input("Do you want to roll the dice? (yes/no): ").lower()
        if should_roll != 'yes':
            break
        value = roll()
        if value == 1:
            print("You rolled a 1! Turn done")
            current_score = 0
            break
        else:
            current_score += value
            print("You rolle a: ", value)
            
        print("Your score is: ", current_score)
    
    players_scores[player_idx] += current_score
    print("Your total score is:", players_scores[player_idx])