import heapq

GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

class Puzzle:
    def __init__(self, state, parent=None, move="", depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth         

    def display(self):
        for row in self.state:
            print(row)
        print()

    def is_goal(self):
        return self.state == GOAL_STATE

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def generate_successors(self):
        successors = []
        x, y = self.find_blank()

        moves = {
            "Up": (x - 1, y),
            "Down": (x + 1, y),
            "Left": (x, y - 1),
            "Right": (x, y + 1)
        }

        for move, (new_x, new_y) in moves.items():
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = [row[:] for row in self.state]
                # Swap blank with target tile
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                successors.append(Puzzle(new_state, self, move, self.depth + 1))

        return successors

    def manhattan_distance(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                value = self.state[i][j]
                if value != 0:
                    goal_x = (value - 1) // 3
                    goal_y = (value - 1) % 3
                    distance += abs(i - goal_x) + abs(j - goal_y)
        return distance

    def __lt__(self, other):
        return (self.depth + self.manhattan_distance()) < (other.depth + other.manhattan_distance())


def a_star(initial_state):
    start = Puzzle(initial_state)
    open_list = []
    closed_set = set()

    heapq.heappush(open_list, (start.depth + start.manhattan_distance(), start))

    while open_list:
        _, current = heapq.heappop(open_list)

        
        state_tuple = tuple(tuple(row) for row in current.state)

        if state_tuple in closed_set:
            continue

        closed_set.add(state_tuple)

        if current.is_goal():
            return current

        for successor in current.generate_successors():
            heapq.heappush(open_list, (successor.depth + successor.manhattan_distance(), successor))

    return None


def print_solution(solution):
    path = []
    while solution:
        path.append(solution)
        solution = solution.parent

    path.reverse()

    print("Solution Steps:\n")
    for i, step in enumerate(path):
        print(f"Step {i}: {step.move}")
        step.display()
 
initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

solution = a_star(initial_state)

if solution:
    print_solution(solution)
else:
    print("No solution found.")