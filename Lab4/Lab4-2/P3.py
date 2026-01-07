from videogame import VideoGame

player1 = VideoGame("Hero01", "Ninja")
player2 = VideoGame("Mage99", "Wizard")

player1.collect_coins(50)
player1.fight_monster("Slime", 2)
player1.fight_monster("Dragon", 5)

print()
print(player1.get_stats())

print()
party = VideoGame.create_party(["Tank01", "Healer02"], "Doctor")

print(VideoGame.get_leaderboard())
print(VideoGame.get_server_stats())
