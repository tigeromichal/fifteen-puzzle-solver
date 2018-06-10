import tools
import time
from ResultData import ResultData
from Node import Node


class DFS:
    def solve(initialState, desiredState, rows, cols, order, depthLimit):
        frontierList = tools.collections.OrderedDict()
        exploredList = dict()

        nodeState = initialState
        node = Node(None, None, 0)
        frontierList[nodeState] = node

        maxDepth = 0
        visitedCount = 1
        exploredCount = 0
        timeStart = time.clock()

        if tools.compareStates(nodeState, desiredState):
            timeEnd = time.clock()
            return ResultData(node, visitedCount, exploredCount, 0, timeEnd - timeStart, nodeState)

        while 1:
            zeroIndex = nodeState.index("0")
            neighbours = tools.getNeighbours(nodeState, rows, cols, zeroIndex, order)
            for key, neighbour in reversed(neighbours.items()):
                isInFrontier = neighbour in frontierList
                isInExplored = neighbour in exploredList
                newNode = Node(node, key, node.cost + 1)
                if not (isInFrontier or isInExplored):
                    visitedCount += 1
                    if tools.compareStates(neighbour, desiredState):
                        timeEnd = time.clock()
                        return ResultData(newNode, visitedCount, exploredCount, maxDepth + 1, timeEnd - timeStart,
                                          neighbour)
                    if newNode.cost < depthLimit:
                        frontierList[neighbour] = newNode
                        frontierList.move_to_end(neighbour, last=False)
                else:
                    if isInFrontier and frontierList[neighbour].cost > newNode.cost:
                        frontierList[neighbour] = newNode
                        frontierList.move_to_end(neighbour, last=False)
                    elif isInExplored and exploredList[neighbour].cost > newNode.cost:
                        frontierList[neighbour] = newNode
                        frontierList.move_to_end(neighbour, last=False)
                        exploredList[neighbour] = newNode

            if not (nodeState in exploredList):
                exploredCount += 1
            exploredList[nodeState] = frontierList.pop(nodeState)

            if len(frontierList) == 0:
                timeEnd = time.clock()
                return ResultData(node, visitedCount, exploredCount, maxDepth, timeEnd - timeStart, nodeState)

            nodeState = next(iter(frontierList))
            node = frontierList[nodeState]

            if node.cost < depthLimit:
                maxDepth = max(node.cost, maxDepth)
