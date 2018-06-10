import sys
import BFS
import DFS
import ASTR
import heuristics
import tools

initialState = ()
rows = 0
cols = 0


def main(argv):
    if len(argv) != 6:
        print("Error: No arguments given (expected 5)")
        return
    print("Arguments given: ", argv[1:])
    strategy = argv[1]
    strategyParam = argv[2]
    initialStateFilePath = argv[3]
    solutionFilePath = argv[4]
    statsFilePath = argv[5]

    loadInitialState(initialStateFilePath)

    desiredState = tuple([str(i) for i in range(1, rows * cols)] + ["0"])

    if strategy == "bfs":
        resultData = BFS.BFS.solve(tuple(initialState), desiredState, rows, cols, strategyParam)
    elif strategy == "dfs":
        resultData = DFS.DFS.solve(tuple(initialState), desiredState, rows, cols, strategyParam, 21)
    elif strategy == "astr":
        if strategyParam == "hamm":
            resultData = ASTR.ASTR.solve(tuple(initialState), desiredState, rows, cols, heuristics.hamming)
        elif strategyParam == "manh":
            resultData = ASTR.ASTR.solve(tuple(initialState), desiredState, rows, cols, heuristics.manhattan)
        else:
            print("Error: Bad argument: ", strategyParam)
            return
    else:
        print("Error: Bad argument: ", strategy)
        return

    saveResults(resultData, solutionFilePath, statsFilePath, desiredState)


def loadInitialState(path):
    global initialState, rows, cols

    fileObject = open(path)
    lines = fileObject.readlines()
    fileObject.close()

    rows = int(lines[0].split(" ")[0])
    cols = int(lines[0].split(" ")[1])

    for line in lines[1:]:
        initialState += tuple(line.replace("\n", "").split(" "))

        # print ("rows = ", rows)
        # print ("cols = ", cols)
        # print("initial state = ", initialState)


def saveResults(resultData, solutionFilePath, statsFilePath, desiredState):
    # print ("cost: ", resultData.node.cost)
    # print("visitedStatesCount: ", resultData.visitedStatesCount)
    # print("exploredStatesCount: ", resultData.exploredStatesCount)
    # print ("maxDepth: ", resultData.maxDepth)
    print("time: ", '{0:.3f}'.format(resultData.time * 1000.0))

    path = str()
    if tools.compareStates(resultData.state, desiredState):
        node = resultData.node
        while node.operator is not None:
            path = node.operator + path
            node = node.parentNode
    else:
        path = -1
        resultData.node.cost = -1
    # print ("path: ", path)

    fileObject = open(solutionFilePath, 'w+')
    if path == -1:
        fileObject.write("-1")
    else:
        fileObject.write(str(resultData.node.cost) + "\n" + path + "\n")
    fileObject.close()

    fileObject = open(statsFilePath, 'w+')
    fileObject.write(
        str(resultData.node.cost) + "\n"
        + str(resultData.visitedStatesCount) + "\n"
        + str(resultData.exploredStatesCount) + "\n"
        + str(resultData.maxDepth) + "\n"
        + str('{0:.3f}'.format(resultData.time * 1000.0)) + "\n"
    )
    fileObject.close()


main(sys.argv)
