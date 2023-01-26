class WaterJug:
    def __init__(self, m, n):
        self.m = m # capacity of jug 1
        self.n = n # capacity of jug 2
        self.visited = set()

    def dfs(self, state):
        if state in self.visited: # check if the state has been visited before
            return
        print(state) # print the current state
        self.visited.add(state)
        x, y = state
        self.dfs((0, y)) # empty jug 1
        self.dfs((x, 0)) # empty jug 2
        self.dfs((self.m, y)) # fill jug 1
        self.dfs((x, self.n)) # fill jug 2
        self.dfs((x-(self.n-y), self.n) if x-(self.n-y) > 0 else (0, y+x)) # pour water from jug 1 to jug 2
        self.dfs((x+(y), 0) if x+y <= self.m else (self.m, y-(self.m-x))) # pour water from jug 2 to jug 1

w = WaterJug(1,7)
w.dfs((0,0)) # start from initial state (0,0)
