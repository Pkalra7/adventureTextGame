import world,time
from player import Player
import sys

def isValid(actions,input):
    for action in actions:
        if input==action.hotkey:
            return True

    return False


def play():
    world.load_tiles()
    player = Player()
    room=world.tile_exists(player.location_x,player.location_y)
    player.move(2, 5)
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modifyPlayer(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            time.sleep(1)
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            while True:
                action_input = input('Action: ')
                if not isValid(available_actions,action_input):
                    print()
                    print("Sorry, '{}' is not a valid action in your current state. Try Again!\n".format(action_input))
                    for action in available_actions:
                        print(action)
                    continue
                else:
                    break
            for action in available_actions:
                if action_input==action.hotkey:
                    player.do_action(action, **action.kwargs)



