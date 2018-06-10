import tools
import time
from ResultData import ResultData
from Node import Node


class BFS:
    def solve(initialState, desiredState, rows, cols, order):
        frontierList = tools.collections.OrderedDict()
        exploredList = dict()

        nodeState = initialState
        node = Node(None, None, 0)
        frontierList[nodeState] = node

        maxDepth = 0
        timeStart = time.clock()

        if (tools.compareStates(nodeState, desiredState)):
            timeEnd = time.clock()
            return ResultData(node, len(frontierList) + len(exploredList), len(exploredList), 0, timeEnd - timeStart,
                              nodeState)

        while (1):
            zeroIndex = nodeState.index("0")
            neighbours = tools.getNeighbours(nodeState, rows, cols, zeroIndex, order)
            for key in neighbours:
                neighbour = neighbours[key]
                if (not (neighbour in frontierList or neighbour in exploredList)):
                    newNode = Node(node, key, node.cost + 1)
                    frontierList[neighbour] = newNode
                    if (tools.compareStates(neighbour, desiredState)):
                        timeEnd = time.clock()
                        return ResultData(newNode, len(frontierList) + len(exploredList), len(exploredList),
                                          maxDepth + 1, timeEnd - timeStart, neighbour)

            exploredList[nodeState] = frontierList.pop(nodeState)

            nodeState = next(iter(frontierList))
            node = frontierList[nodeState]

            maxDepth = max(node.cost, maxDepth)
