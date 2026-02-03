import random


class Environment:
    def __init__(self, name, damage_bonus):
        self.name = name
        self.damage_bonus = damage_bonus

    def show(self):
        print(f"Environment: {self.name} | Damage Bonus: {self.damage_bonus}")


class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100

    def attack(self, env):
        base_damage = random.randint(10, 20)
        total_damage = base_damage + env.damage_bonus
        print(f"{self.name} attacks for {total_damage} damage")
        return total_damage

    def heal(self):
        heal_amount = random.randint(10, 15)
        self.hp += heal_amount
        print(f"{self.name} heals {heal_amount} HP")


class Monster:
    def __init__(self, name):
        self.name = name
        self.hp = 80

    def attack(self):
        damage = random.randint(8, 18)
        print(f"{self.name} attacks for {damage} damage")
        return damage


class Game:
    def __init__(self, player, monster, environment):
        self.player = player
        self.monster = monster
        self.environment = environment

    def start(self):
        print("GAME STARTED")
        self.environment.show()

        while self.player.hp > 0 and self.monster.hp > 0:
            print("\n--- STATUS ---")
            print(self.player.name, "HP:", self.player.hp)
            print(self.monster.name, "HP:", self.monster.hp)

            choice = input("\n1. Attack\n2. Heal\nChoose: ")

            if choice == "1":
                damage = self.player.attack(self.environment)
                self.monster.hp -= damage
            elif choice == "2":
                self.player.heal()
            else:
                print("Invalid choice")

            if self.monster.hp > 0:
                damage = self.monster.attack()
                self.player.hp -= damage

        if self.player.hp > 0:
            print("\n YOU WIN!")
        else:
            print("\n YOU LOST!")



player = Player("Hero")
monster = Monster("Dragon")
environment = Environment("Volcano", damage_bonus=5)

game = Game(player, monster, environment)
game.start()
