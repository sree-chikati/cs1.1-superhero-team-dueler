import random
class Hero: 
    # We want our hero to have a default "starting_health",
     def __init__(self, name, starting_health=100):
         self.name = name
         self.starting_health = starting_health
         # when a hero is created, their current health is always the same as their starting health (no damage taken yet!)
         self.current_health = starting_health

     def fight(self, opponent):
         ''' Current Hero will take turns fighting the opponent hero passed in.'''
         # TODO: Fight each hero until a victor emerges.
         fight_winner = random.choice([self.name, opponent.name])
         print(f'{fight_winner} won!')



if __name__ == "__main__":
    # If you run this file from the terminal this block is executed.
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    hero1.fight(hero2)