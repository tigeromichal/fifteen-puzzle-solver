class ResultData:
    def __init__(self, node, visitedStatesCount, exploredStatesCount, maxDepth, time, state):
        self.node = node
        self.visitedStatesCount = visitedStatesCount
        self.exploredStatesCount = exploredStatesCount
        self.maxDepth = maxDepth
        self.time = time
        self.state = state
