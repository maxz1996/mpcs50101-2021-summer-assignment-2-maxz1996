# Problem 8
# Max Zinski

import random

def prompt_for_selection():
    print("Select a weapon")
    user_input = input()
    if user_input not in {"rock", "paper", "scissors"}:
        print("You must choose paper, rock, or scissors")
        if prompt_to_play_again():
            return prompt_for_selection()
        # False indicates the game is over. i.e. the user does not want to play again
        else:
            return False
    else:
        return user_input

def prompt_to_play_again():
    print("Would you like to play again?")
    user_input = input()
    if user_input == 'yes' or user_input == 'y':
        return True
    else:
        return False

# reminds me of a state machine where the transitions between states are dictated by:
# --> the user's response to being asked to play again
# --> the cpu's weapon selection relative to the player. i.e. ties lead to different state transitions than decisive results
def play():
    # key: user weapon, val: the cpu weapon that the user's weapon beats
    victor_map = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    # prompt_for_selection will either return False or a valid weapon (rock, paper, scissors)
    selection = prompt_for_selection()
    if selection:
        cpu_weapon = random.choice(["paper", "rock", "scissors"])
        if selection == cpu_weapon:
            print(f"The computer choose {cpu_weapon}. Let's settle this.")
            play()
        else:
            if victor_map[selection] == cpu_weapon:
                print(f"The computer chose {cpu_weapon}. You win!")
            else:
                print(f"The computer chose {cpu_weapon}. You lose :'(")
            
            if prompt_to_play_again():
                play()

play()