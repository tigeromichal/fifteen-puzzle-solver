import queue
import tools
import time
from ResultData import ResultData
from Node import Node


class ASTR:
    def solve(initialState, desiredState, rows, cols, heuristics):
        order = "LRUD"

        frontierList = queue.PriorityQueue()
        frontierListDict = dict()
        exploredList = dict()
        nodes = dict()

        nodeState = initialState
        node = Node(None, None, 0)
        nodes[nodeState] = node

        maxDepth = 0
        timeStart = time.clock()

        if (tools.compareStates(nodeState, desiredState)):
            timeEnd = time.clock()
            return ResultData(node, len(frontierListDict) + len(exploredList), len(exploredList), 0,
                              timeEnd - timeStart, nodeState)

        while (1):
            zeroIndex = nodeState.index("0")
            neighbours = tools.getNeighbours(nodeState, rows, cols, zeroIndex, order)
            for key in neighbours:
                neighbour = neighbours[key]
                if (not (neighbour in frontierListDict or neighbour in exploredList)):
                    priority = node.cost + 1 + heuristics(neighbour, desiredState, rows, cols)
                    frontierListDict[neighbour] = 1
                    frontierList.put((priority, neighbour))
                    nodes[neighbour] = Node(node, key, node.cost + 1)
                    if (tools.compareStates(neighbour, desiredState)):
                        timeEnd = time.clock()
                        return ResultData(nodes[neighbour], len(frontierListDict) + len(exploredList),
                                          len(exploredList), maxDepth + 1, timeEnd - timeStart, neighbour)

            exploredList[nodeState] = 1
            nodeState = frontierList.get()[1]
            frontierListDict.pop(nodeState)
            node = nodes[nodeState]

            maxDepth = max(node.cost, maxDepth)
