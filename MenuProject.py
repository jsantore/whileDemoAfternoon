import Project5Start

game_data = Project5Start.get_project5_data()

menu_text = """
[1]Find most money made by a 2d game
[2]Find oldest release
[3]Find newest release
[4]Find most expensive game
[5]Add a new Game
[6]Quit
"""
while True:
    print(menu_text)
    choice = input("Please enter the number of your choice:")
    if '1' in choice:
        largest_money_amount = 0
        for game in game_data:
            if game['total_sales']>largest_money_amount:
                largest_money_amount=game['total_sales']
        print(f"The most money made by a 2d game on steam was ${largest_money_amount}")
    elif '2' in choice:
        oldest_game = game_data[0]
        for game in game_data:
            if game['release']<oldest_game['release']:
                oldest_game = game
        print(f"{oldest_game['name']} is the oldest in the top 10, released in {oldest_game['release']}")
    elif '3' in choice:
        newest_game = game_data[0]
        for game in game_data:
            if game['release'] > newest_game['release']:
                newest_game = game
        print(f"""{newest_game['name']} is the newest in the top 10, released in {newest_game["release"]}""")
    elif '6' in choice:
        break
    else:
        print("That option is not yet implemented, please pick another")