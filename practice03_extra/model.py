import matplotlib.pyplot as plt
import random


def random_coord(size):
    return random.randint(0, size - 1)


def choose_coords(agents, size):
    while 1:
        x = random_coord(size)
        y = random_coord(size)
        is_busy = False

        for agent in agents:
            if agent.x == x and agent.y == y:
                is_busy = True
                break

        if not is_busy:
            return [x, y]


class Agent:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    def distance(self, agent):
        return abs(self.x - agent.x) + abs(self.y - agent.y)

    def move(self, agents, size):
        coords = choose_coords(agents, size)
        self.x = coords[0]
        self.y = coords[1]

    def is_happy(self, agents, neighbor_num, neighbor_type_p):
        distances = []

        for agent in agents:
            if self != agent:
                distance = self.distance(agent)
                distances.append((distance, agent))

        distances.sort(key=lambda k: k[0])
        neighbors = [agent for d, agent in distances[:neighbor_num]]

        num_same_type = sum(self.type == agent.type for agent in neighbors)
        num_same_type_p = num_same_type / neighbor_num * 100

        return num_same_type_p >= neighbor_type_p

    def update(self, agents, neighbor_num, neighbor_type_p, size):
        if not self.is_happy(agents, neighbor_num, neighbor_type_p):
            self.move(agents, size)
            return 1
        return 0


def create_agents(size, num_type_1, num_type_2):
    agents = []

    for i in range(num_type_1):
        coords = choose_coords(agents, size)
        agents.append(Agent(coords[0], coords[1], 1))

    for i in range(num_type_2):
        coords = choose_coords(agents, size)
        agents.append(Agent(coords[0], coords[1], 2))

    return agents


def to_field(agents, size):
    field = [[0] * size for i in range(size)]

    for agent in agents:
        field[agent.y][agent.x] = agent.type

    return field


def main():
    size = 75  # размеры сетки
    num_type_1 = 1000
    num_type_2 = 500
    neighbor_num = 200
    neighbor_type_p = 75  # пороговое значение "толерантности" в процентах
    loop_num = 50  # количество шагов моделирования
    agents = create_agents(size, num_type_1, num_type_2)

    for i in range(loop_num):
        field = to_field(agents, size)
        plt.title(f"Шаг {i + 1}")
        plt.imshow(field, cmap='plasma')
        plt.show()
        for agent in agents:
            agent.update(agents, neighbor_num, neighbor_type_p, size)


if __name__ == '__main__':
    main()
