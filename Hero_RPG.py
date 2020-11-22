#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def alive(self):
        if self.health > 0:
            return True

    def attack(self, enemy):

        if enemy.character_name != "zombie":
                enemy.health -= self.power

        if(self.character_name == "hero"):
            print(f"You do {self.power} damage to the {enemy.character_name}.")
        elif(self.character_name == "goblin" or self.character_name == "zombie"):
            print(f"The {self.character_name} does {self.power} damage to you.")

    def print_status(self):
        if self.character_name == "hero":
            print(f"You have {self.health} health and {self.power} power.")
        elif self.character_name == "goblin" or self.character_name == "zombie":
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")

class Hero(Character):
    def __init__(self, health, power):
        self.character_name = "hero"
        super(Hero, self).__init__(health, power)

class Goblin(Character):
    def __init__(self, health, power):
        self.character_name = "goblin"
        super(Goblin,self).__init__(health, power)

class Zombie(Character):
    def __init__(self, health, power):
        self.character.name = "zombie"
        super(Zombie,self).__init__(health, power)

hero = Hero(10, 5)
goblin = Goblin(6, 2)
zombie = Zombie (10,1)

def main(enemy):

    while enemy.alive() > 0 and hero.alive():

        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print("f1. fight {enemy.character_name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(enemy)

        if not enemy.alive():
            print(f"The {enemy.character_name} is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")

        if enemy.alive():
            enemy.attack(hero)

        if not hero.alive():
            print("You are dead.")

        if goblin.health > 0:
            # Goblin attacks hero
            enemy.attack(hero)


main(zombie)