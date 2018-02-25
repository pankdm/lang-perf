#pragma once

#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <bitset>
#include <set>
#include <sstream>
#include <stdlib.h>
#include <map>
#include <queue>
#include <assert.h>
#include <deque>
#include <string.h>
#include <unordered_map>

#include <ctime>

using namespace std;

typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <string> vs;


struct CppSolver {
  CppSolver(vvi* _graph);

  void run_bfs(int start, vi* scores);
  void compute_hash();
private:
  vvi* graph;
};
