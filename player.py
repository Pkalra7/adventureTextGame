import random, time
import world, items

class Player():
    def __init__(self):
        self.inventory = [items.Gold(30),items.Rock()]
        self.hp = 100
        self.location_x,self.location_y = (0,0)
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).introText())


    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1,dy=0)

    def move_west(self):
        self.move(dx=-1,dy=0)

    def attack(self,enemy):
        weaponChosen=None
        max_dmg=0

        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    weaponChosen = i

        #print("You attack {0} with a {1}!".format(weaponChosen.name,enemy.name))
        enemy.hp-=weaponChosen.damage
        time.sleep(1)
        print("You use {0} against {1}!".format(weaponChosen.name, enemy.name))
        time.sleep(2)
        print("Your {0} does {1} damage to the {2}!".format(weaponChosen.name, weaponChosen.damage, enemy.name))
        time.sleep(1)
        if not enemy.isAlive():
            time.sleep(1)
            print("You killed {}!".format(enemy.name))
        else:
            time.sleep(1)
            print("{} HP is {}.".format(enemy.name,enemy.hp))

    def do_action(self,action,**kwargs):
        action_method=getattr(self,action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def flee(self,tile):
        available_moves=tile.adjacent_moves()
        r=random.randint(0,len(available_moves)-1)
        self.do_action(available_moves[r])




