import json

def load_game_list(filename='remaining_games.json'):
    try:
        with open(filename, 'r') as file:
            games = json.load(file)
            return games
    except Exception as e:
        print(f"Error loading game list: {e}")
        return []

def split_game_list(games):
    middle_index = len(games) // 2
    first_half = games[:middle_index]
    second_half = games[middle_index:]
    return first_half, second_half

def save_game_list(games, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(games, file)
            print(f"Saved game list to {filename}")
    except Exception as e:
        print(f"Error saving game list: {e}")

# Load the full list of games
games = load_game_list()

# Split the list into two halves
first_half, second_half = split_game_list(games)

# Save each half to a separate file
save_game_list(first_half, 'first_half_games.json')
save_game_list(second_half, 'second_half_games.json')
