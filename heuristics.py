def hamming(state, desiredState, rows, cols):
    notInPlaceCount = 0
    for i in range(len(state)):
        if state[i] != desiredState[i]:
            notInPlaceCount += 1
    return notInPlaceCount


def manhattan(state, desiredState, rows, cols):
    distancesSum = 0
    for i in range(len(state)):
        desiredIndex = desiredState.index(state[i])
        distancesSum += abs(i % cols - desiredIndex % cols) + abs(int(i / cols) - int(desiredIndex / cols))
    return distancesSum
