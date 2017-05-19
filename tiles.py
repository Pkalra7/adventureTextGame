import items,enemies,actions,world
import time,random

class MapTile():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def introText(self):
        raise NotImplementedError()

    def modifyPlayer(self, the_player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        return moves


class StartingRoom(MapTile):
    def __init__(self, x, y):
        super(StartingRoom, self).__init__(x, y)

    def introText(self):
        return """
        You find yourself if a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """

    def modifyPlayer(self,the_player):
        #no action/modification in startingroom
        pass


class LootRoom(MapTile):
    def __init__(self,x,y,item):
        self.item=item
        super().__init__(x,y)

    def add_Loot(self,the_player):
        the_player.inventory.append(self.item)

    def modifyPlayer(self,the_player):
        self.add_Loot(the_player)


class EnemyRoom(MapTile):
    def __init__(self,x,y,enemy):
        self.enemy=enemy
        super().__init__(x,y)

    def modifyPlayer(self,the_player):
        if self.enemy.isAlive():
            damageTaken=random.randint(1,self.enemy.damage)
            the_player.hp=the_player.hp-damageTaken
            time.sleep(2)
            print("Enemy does {} damage. You have {} HP remaining.".format(damageTaken, the_player.hp))

    def available_actions(self):
        if self.enemy.isAlive():
            return[actions.Attack(enemy=self.enemy), actions.Flee(tile=self)]
        else:
            return self.adjacent_moves()

class EmptyCavePath(MapTile):
    def introText(self):
        return """
               Another unremarkable part of the cave. You must forge onwards
               """

    def modifyPlayer(self, the_player):
        # Room has no action on player
        pass

class GiantSpiderRoom(EnemyRoom):
    def __init__(self,x,y):
        super().__init__(x,y,enemies.GiantSpider())

    def introText(self):
        if self.enemy.isAlive():
            time.sleep(1)
            return """
            A giant spider jumps down from its web in front of you and attacks you!
            """
        else:
            return """
            Here lies the corps of dead spider rotting on the ground
            """

class OgreRoom(EnemyRoom):
    def __init__(self,x,y):
        super().__init__(x,y,enemies.Ogre())

    def introText(self):
        if self.enemy.isAlive():
            time.sleep(1)
            return """
            A hostile and incredibly hungry beast charges towards you and attacks you! It's an Ogre!
            """
        else:
            return """
            Here lies the corpse of the ogre that was defeated by you
            """
    


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def introText(self):
        time.sleep(1)
        return """
        Your notice something shiny in the corner.
        It's a dagger! You pick it up.
        """

class FindRockRoom(LootRoom):
    def __init__(self,x,y):
        super().__init__(x,y,items.Rock())

    def introText(self):
        return """
        As you're walking, you trip over something and land face first!
        You get up angrily, and investigate. It's a rock! Not as effective 
        as a dagger, but one could just about use anything to defend 
        themselves in desperature situations.
        """


class LeaveCaveRoom(MapTile):
    def introText(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!


        Victory is yours!
        """

    def modifyPlayer(self, player):
        player.victory = True
