from random import choice

class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name and an empty list of heroes
        '''
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        """Remove Hero from heroes list. If Hero isn't found return 0."""
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0
    
    def view_all_heroes(self):
        """Print out all heroes to the console."""
        for hero in self.heroes:
            print(hero.name)
    
    def add_hero(self, hero):
        """Add Hero object to self.heroes."""
        self.heroes.append(hero)
    
    def stats(self):
        """Print team statistics."""
        for hero in self.heroes:
            if hero.deaths == 0:
                hero.deaths = 1
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths:{kd}")
    
    def revive_heroes(self, health=100):
        """Reset all heroes health to starting_health."""
        for hero in self.heroes:
            hero.current_health = hero.starting_health
            print(f"{hero.name} is revived.")
    
    def attack(self, other_team):
        ''' Battle each team against each other.'''

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            rand_hero = choice(living_heroes)
            rand_opponent = choice(living_opponents)
            rand_hero.fight(rand_opponent)
            if rand_hero.is_alive() == True:
                living_opponents.remove(rand_opponent)
            elif rand_opponent.is_alive() == True:
                living_heroes.remove(rand_hero)
            else:
                living_opponents.remove(rand_opponent)
                living_heroes.remove(rand_hero)