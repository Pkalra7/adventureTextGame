from re import match
_world={}
_max_x = 0
_max_y = 0

def load_tiles():
    global _max_x, _max_y
    with open('resources/map.txt', 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split())  # assumes all rows contain the same number of tabs
    _max_x = x_max  # added for map
    _max_y = len(rows)  # added for map
    for y in range(len(rows)):
        cols = rows[y].split()
        for x in range(x_max):
            tile_name = cols[x].rstrip()
            _world[(x, y)] = None if match(r'^x+$', tile_name) else getattr(__import__('tiles'), tile_name)(x, y)

def tile_exists(x,y):
    return _world.get((x,y))

