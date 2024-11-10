# Game of Inputs: A fun way to play with lists in Python!
# Description:
# This interactive console game allows players to modify a simple list by replacing elements based on their input. Players can continue 
# updating the list until they decide to stop. It’s a fun way to practice input handling and list manipulation in Python!


def display_list(game_list):
    """Display the current state of the game list."""
    print('Updated Game List: ')
    print(game_list)

def position_choice():
    """Prompt the player to select a position in the list to replace."""
    while True:
        choice = input("Enter a position to replace (0, 1, 2): ")
        if choice in ["0", "1", "2"]:
            return int(choice)  # Convert the valid input to an integer
        print("Sorry, you entered an invalid input, try again!")  # Invalid input message

def replacement_choice(position, game_list):
    """Replace the value at the selected position with the player's input."""
    game_list[position] = input("Enter a value to place at position {}: ".format(position))
    return game_list  # Return the updated list

def game_runner_logic():
    """Ask the player if they want to continue playing."""
    while True:
        choice = input("Do you want to continue playing the game? (Y/N): ").upper()
        if choice in ['Y', 'N']:
            return choice == 'Y'  # Return True for 'Y' and False for 'N'
        print("Sorry, that was an invalid input.")  # Invalid input message

# Main game loop
game_list = [0, 1, 2]  # Initial game list
game_on = True  # Control variable for the game loop

print("Welcome to the Game of Inputs!")  # Welcome message
print("You will replace numbers in a simple list with your own values!")  # Game objective

while game_on:
    display_list(game_list)  # Show the current list
    position = position_choice()  # Get player's position choice
    game_list = replacement_choice(position, game_list)  # Update the list
    display_list(game_list)  # Show the updated list
    game_on = game_runner_logic()  # Check if the player wants to continue

print("Thanks for playing the Game of Inputs! Goodbye!")  # Exit message
