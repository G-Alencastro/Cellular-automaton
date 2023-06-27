from random import choice

def random_fill_grid(grid, len=10):
    for _ in range(len):
        grid.append(choice([0, 1]))
    return grid
def default_fill_grid(grid, len=601):
    grid = [0 for _ in range(len)]
    grid[(len-1)//2] = 1
    return grid

def logical_rule(neighbor):
    if neighbor[0] ^ neighbor[1] ^ neighbor[2]:
        return 1
    else:
        return 0

def joao_rule(neighbor):
    if neighbor[0] or neighbor[1] and neighbor[2]:
        return 1
    else:
        return 0

def rule(ng, rule='00010110'):
    if ng[0] and ng[1] and ng[2]:
        return int(rule[0])
    if ng[0] and ng[1] and not ng[2]:
        return int(rule[1])
    if ng[0] and not ng[1] and ng[2]:
        return int(rule[2])
    if ng[0] and not ng[1] and not ng[2]:
        return int(rule[3])
    if not ng[0] and ng[1] and ng[2]:
        return int(rule[4])
    if not ng[0] and ng[1] and not ng[2]:
        return int(rule[5])
    if not ng[0] and not ng[1] and ng[2]:
        return int(rule[6])
    if not ng[0] and not ng[1] and not ng[2]:
        return int(rule[7])


def new_gen(grid, rule):
    new_grid = [0]
    for c in range(1,len(grid)-1):
        neighbor = (grid[c-1], grid[c], grid[c+1])
        new_grid.append(rule(neighbor))
    new_grid.append(0)
    return new_grid

if __name__ == "__main__":
    grid = []
    random_fill_grid(grid)
    for c in range(50):
        print(grid)
        grid = new_gen(grid, rule)
