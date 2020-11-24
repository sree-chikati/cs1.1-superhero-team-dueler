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