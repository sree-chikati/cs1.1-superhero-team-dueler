import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero: 
    # We want our hero to have a default "starting_health",
     def __init__(self, name, starting_health=100):
         ''' STEP 4: 
          Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        # abilities and armors don't have starting values, and are set to empty lists on initialization
         self.abilities = list()
         self.armors = list()
         self.name = name
         self.starting_health = starting_health
         self.current_health = starting_health
         self.deaths = 0
         self.kills = 0
    
     def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)
    
     def add_weapon(self, weapon):
        """Add weapon to abilities list.
        weapon: Weapon Object.
        """
        self.abilities.append(weapon)

     def add_armor(self, armor):
         '''Add armor to self.armors
            Armor: Armor Object
         '''
         self.armors.append(armor)
    
     def add_kill(self, num_kills=1):
        """Update self.kills by num_kills amount"""
        self.kills += num_kills
    
     def add_death(self, num_deaths=1):
        """Update deaths with num_deaths"""
        self.deaths += num_deaths

     def attack(self):
         '''Calculate the total damage from all ability attacks.
            return: total_damage:Int
         '''
         total_damage = 0
         for ability in self.abilities:
             damage = ability.attack() #have to do this to save random values to a variable or else  will keep changing
             total_damage += damage
         return total_damage

     def defend(self):
         '''Calculate the total block amount from all armor blocks.
            return: total_block:Int
         '''
         total_block = 0
         for armor in self.armors:
             total_block += armor.block()
         return total_block
     
     def take_damage(self, damage):
         '''Updates self.current_health to reflect the damage minus the defense.'''
         # TODO: Create a method that updates self.current_health to the current minus the the amount returned from calling self.defend(damage).
         self.current_health -= damage + self.defend()
         if self.current_health < 0:
             self.current_health = 0

     def is_alive(self):  
         '''Return True or False depending on whether the hero is alive or not.
         '''
         if self.current_health <= 0:
             return False
         else:
             return True

     def fight(self, opponent):  
         ''' Current Hero will take turns fighting the opponent hero passed in.
         '''
         if len(self.abilities) == 0 and len(opponent.abilities) == 0:
             print("Draw")
             return

         while self.is_alive() and opponent.is_alive():
             self.take_damage(opponent.attack())
             opponent.take_damage(self.attack())

             if self.is_alive():
                 opponent.take_damage(self.attack())
                 print(f'{self.name} won!')

             elif opponent.is_alive():
                 self.take_damage(opponent.attack())
                 print(f'{opponent.name} won!')
         
         if not self.is_alive():
             opponent.add_kill(1)
             self.add_death(1)
             return opponent.name

         elif not opponent.is_alive():
             self.add_kill(1)
             opponent.add_death(1)
             return self.name



if __name__ == "__main__":
    # If you run this file from the terminal this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())


   

    #hero1 = Hero("Wonder Woman")
    #hero2 = Hero("Dumbledore")
    #hero1.fight(hero2)
   