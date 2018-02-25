import sys
from collections import deque
from libcpp.vector cimport vector
import time

NOT_PROCESSED = -1

cdef extern from "cpp_solver.h":
    cdef cppclass CppSolver:
        #Methods
        CppSolver(vector[vector[int]]*) except +
        void run_bfs(int, vector[int]*)
        void compute_hash()


cdef class Solver:
    cdef vector[vector[int]] graph
    cdef int num_cities
    cdef CppSolver* cpp_solver

    def init(self, file_name):
        f = open(file_name)

        self.num_cities = int(f.readline())
        num_mines = f.readline()
        mines = f.readline().strip('\n').split(' ')

        num_rivers = int(f.readline().strip('\n'))
        cdef vector[vector[int]] graph
        graph.resize(self.num_cities)
        for _i in range(num_rivers):
            s, t = f.readline().strip('\n').split(' ')
            s = int(s)
            t = int(t)

            graph[s].push_back(t)
            graph[t].push_back(s)

        self.graph = graph
        self.cpp_solver = new CppSolver(&self.graph)

    def compute_hash(self):
        begin = time.clock()
        cdef vector[vector[int]] distances
        distances.resize(self.num_cities)
        cdef vector[int] local_dist
        for v in range(self.num_cities):
            local_dist.clear()
            self.cpp_solver.run_bfs(v, &distances[v])

        total_score = 0
        for v in range(self.num_cities):
            current_score = 0
            for d in distances[v]:
                if d == NOT_PROCESSED: continue
                d2 = d * d
                current_score ^= d2
            total_score += current_score

        end = time.clock()
        print ("graph_hash={}".format(total_score))
        print ("time={}".format(1000 * (end - begin)))

    def compute_hash_full(self):
        self.cpp_solver.compute_hash()
