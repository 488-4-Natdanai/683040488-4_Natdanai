from datetime import datetime, timedelta

class VideoGame:
    total_players = 0
    difficulty_levels = ["Easy", "Medium", "Hard"]
    max_level = 100
    server_start_time = datetime.now()
    active_players = []
    leaderboard = {}

    def __init__(self, player_name, character_type):
        if not VideoGame.is_valid_character_name(player_name):
            raise ValueError("Invalid character name")

        self.player_name = player_name
        self.character_type = character_type
        self.level = 1
        self.health = 100
        self.exp = 0
        self.coins = 0
        self.inventory = []
        self.is_alive = True

        VideoGame.total_players += 1
        VideoGame.active_players.append(player_name)
        VideoGame.leaderboard[player_name] = 0

    def level_up(self):
        if self.level < VideoGame.max_level:
            self.level += 1
            self.health = 100

        VideoGame.leaderboard[self.player_name] = self.level * 100 + self.coins

        print(f"{self.player_name} leveled up!")
        print(f"Level: {self.level}, Health: {self.health}, Score: {VideoGame.leaderboard[self.player_name]}")

    def collect_coins(self, amount):
        if amount <= 0:
            return

        self.coins += amount
        VideoGame.leaderboard[self.player_name] = self.level * 100 + self.coins

        print(f"{self.player_name} collected {amount} coins.")
        print(f"Coins: {self.coins}, Score: {VideoGame.leaderboard[self.player_name]}")

    def take_damage(self, damage):
        if not self.is_alive:
            print(f"{self.player_name} is already dead.")
            return

        self.health -= damage

        if self.health <= 0:
            self.health = 0
            self.is_alive = False
            if self.player_name in VideoGame.active_players:
                VideoGame.active_players.remove(self.player_name)
            print(f"{self.player_name} has died.")
        else:
            print(f"{self.player_name} took {damage} damage. Health: {self.health}")

    def fight_monster(self, monster_name, monster_level):
        print(f"{self.player_name} fights {monster_name} (Level {monster_level})")

        damage = VideoGame.calculate_damage(
            attack_power=10,
            defense=5,
            level=self.level
        )

        self.take_damage(monster_level * 5)

        if not self.is_alive:
            return

        gained_exp = 10 * monster_level
        self.exp += gained_exp
        print(f"Gained {gained_exp} EXP")

        self.collect_coins(3 * monster_level)

        while self.exp >= VideoGame.calculate_exp_needed(self.level):
            self.exp -= VideoGame.calculate_exp_needed(self.level)
            self.level_up()

    def get_stats(self):
        return (
            f"Player: {self.player_name}\n"
            f"Type: {self.character_type}\n"
            f"Level: {self.level}\n"
            f"Health: {self.health}\n"
            f"EXP: {self.exp}\n"
            f"Coins: {self.coins}\n"
            f"Alive: {self.is_alive}\n"
            f"Rank: {VideoGame.get_rank_title(self.level)}"
        )

    @classmethod
    def create_party(cls, player_names, character_type):
        party = []
        for name in player_names:
            party.append(cls(name, character_type))
        return party

    @classmethod
    def get_server_stats(cls):
        uptime = datetime.now() - cls.server_start_time
        return (
            f"Server Uptime: {uptime}\n"
            f"Total Players: {cls.total_players}\n"
            f"Active Players: {cls.active_players}\n"
            f"Leaderboard: {cls.leaderboard}"
        )

    @classmethod
    def get_leaderboard(cls):
        sorted_board = sorted(
            cls.leaderboard.items(),
            key=lambda item: item[1],
            reverse=True
        )

        result = "=== Leaderboard ===\n"
        for name, score in sorted_board:
            result += f"{name}: {score}\n"
        return result

    @classmethod
    def reset_server(cls):
        cls.total_players = 0
        cls.leaderboard = {}
        cls.active_players = []
        cls.server_start_time = datetime.now()

    @staticmethod
    def calculate_damage(attack_power, defense, level):
        damage = (attack_power * level) - defense
        return max(0, damage)

    @staticmethod
    def calculate_exp_needed(level):
        return 100 * level

    @staticmethod
    def is_valid_character_name(name):
        return 3 <= len(name) <= 20 and name.isalnum()

    @staticmethod
    def get_rank_title(level):
        if level < 10:
            return "Beginner"
        elif level < 30:
            return "Adventurer"
        elif level < 60:
            return "Elite"
        elif level < 90:
            return "Master"
        else:
            return "Legend"
