# This program is still in development.
# If there is any suggestions, please let me know

import time
import os
import json

# Player Dictionary
Players = {}

print("This is money manager app for monopoly board game(or any other game)")
time.sleep(2)
print("Make sure you have the board game setup")
time.sleep(2)
print("You should enter the starting ")

starting_money = int(input("Enter the Starting game money: "))

# No. of players
number_of_players = int(input("Enter the number of player: "))
for a in range(1, number_of_players + 1):
	name_of_players = input(f"Enter the name of player {a}: ")
	Players[name_of_players] = starting_money
	print("Player Added!")


os.system("cls")
print("""Help Menu!
1) add(player name or number) === adds new player (Currently Does not work)
2) remove(player name or number) === removes a player (Currently Does not work)
3) give(player name or number, money) === gives a player money (Currently Does not work)
4) take(player name or number, money) === takes money from a player (Currently Does not work)
5) exit === to exit the program
6) view === to view the current players
7) cls === to clear the screen (leaves to help menu)
""")
run = 1
while run:
	game = input(">>> ")
	if game.lower() != "exit":
		if game.lower() == "view":
			print(json.dumps(Players, indent = 2))
		elif game.lower() == "add":
			name_of_players = input(f"Enter the name of player: ")
			Players[name_of_players] = starting_money
			print("Player Added!")
		elif game.lower() == "remove":
			name_of_players = input(f"Enter the name of player: ")
			Players.pop(name_of_players, 'Player not found')
		elif game.lower() == "cls":
			os.system("cls")
			print("""Help Menu!
1) add(player name or number) === adds new player (Currently Does not work)
2) remove(player name or number) === removes a player (Currently Does not work)
3) give(player name or number, money) === gives a player money (Currently Does not work)
4) take(player name or number, money) === takes money from a player (Currently Does not work)
5) exit === to exit the program
6) view === to view the current players
7) cls === to clear the screen (leaves to help menu)
""")
		elif game.lower() == "give":
			money_to_give_player_name = input("Enter the name of the player to give money: ")
			money_to_give = int(input(f"Enter the amount to give to {money_to_give_player_name}: "))
			Players[money_to_give_player_name] += money_to_give
		elif game.lower() == "take":
			money_to_take_player_name = input("Enter the name of the player to give money: ")
			money_to_take = int(input(f"Enter the amount to give to {money_to_take_player_name}: "))
			Players[money_to_take_player_name] -= money_to_take
	else:
		break