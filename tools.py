import collections


def compareStates(state1, state2):
    return state1 == state2


def getNeighbours(state, rows, cols, zeroIndex, order):
    neighbours = collections.OrderedDict()
    row = int(zeroIndex / cols)
    col = (zeroIndex % cols)

    for dir in order:
        if dir == "L":
            if col != 0:
                newState = list(state)
                newIndex = zeroIndex - 1
                newState[zeroIndex] = newState[newIndex]
                newState[newIndex] = "0"
                neighbours["L"] = tuple(newState)
        elif dir == "R":
            if col != cols - 1:
                newState = list(state)
                newIndex = zeroIndex + 1
                newState[zeroIndex] = newState[newIndex]
                newState[newIndex] = "0"
                neighbours["R"] = tuple(newState)
        elif dir == "U":
            if row != 0:
                newState = list(state)
                newIndex = zeroIndex - cols
                newState[zeroIndex] = newState[newIndex]
                newState[newIndex] = "0"
                neighbours["U"] = tuple(newState)
        elif dir == "D":
            if row != rows - 1:
                newState = list(state)
                newIndex = zeroIndex + cols
                newState[zeroIndex] = newState[newIndex]
                newState[newIndex] = "0"
                neighbours["D"] = tuple(newState)

    return neighbours
