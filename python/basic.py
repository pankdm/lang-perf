import sys
from collections import deque
import time

NOT_PROCESSED = -1


class Solver:
    def init(self, file_name):
        f = open(file_name)

        self.num_cities = int(f.readline())
        num_mines = f.readline()
        mines = f.readline().strip('\n').split(' ')

        num_rivers = int(f.readline().strip('\n'))
        graph = [[] for x in range(self.num_cities)]
        for _i in range(num_rivers):
            s, t = f.readline().strip('\n').split(' ')
            s = int(s)
            t = int(t)
            graph[s].append(t)
            graph[t].append(s)

        self.graph = graph

    def compute_hash(self):
        begin = time.clock()
        distances = [None for x in range(self.num_cities)]
        for v in range(self.num_cities):
            local_dist = self.run_bfs(v)
            distances[v] = local_dist

        total_score = 0
        for v in range(self.num_cities):
            current_score = 0
            for d in distances[v]:
                if d == NOT_PROCESSED:
                    continue
                d2 = d * d
                current_score ^= d2
            total_score += current_score

        end = time.clock()
        print("graph_hash={}".format(total_score))
        print("time={}".format(1000 * (end - begin)))
        # print("name=python")

    def run_bfs(self, start):
        result = [NOT_PROCESSED for x in range(self.num_cities)]
        result[start] = 0

        q = deque()
        q.append(start)
        while q:
            now = q.popleft()
            value = result[now]

            for next in self.graph[now]:
                if result[next] == NOT_PROCESSED:
                    result[next] = value + 1
                    q.append(next)
        return result


s = Solver()
s.init(sys.argv[1])
s.compute_hash()
