class enemy():
    def __init__(self,name,hp,damage):
        self.name=name
        self.hp=hp
        self.damage=damage

    def isAlive(self):
        return self.hp > 0


class GiantSpider(enemy):
    def __init__(self):
        super(GiantSpider,self).__init__(name="Giant Spider", hp=10, damage=2)

class Ogre(enemy):
    def __init__(self):
        super(Ogre,self).__init__(name="Ogre", hp=20, damage=5)
