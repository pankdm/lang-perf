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

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

typedef long long int64;

typedef vector <int> vi;
typedef vector <vi> vvi;


typedef vector <string> vs;


constexpr int NOT_PROCESSED = -1;

struct Solver {
  vvi graph;
  vs mines;
  int num_cities;

  void init() {
    cin >> num_cities;
    graph.resize(num_cities);

    int num_mines;
    cin >> num_mines;
    for (int i = 0; i < num_mines; ++i) {
      string m;
      cin >> m;
      mines.push_back(m);
    }

    int n_edges;
    cin >> n_edges;
    for (int i = 0; i < n_edges; ++i) {
      int s;
      int t;
      cin >> s >> t;

      graph[s].push_back(t);
      graph[t].push_back(s);
    }
  }

  void compute_hash() {
    clock_t tbegin = clock();

    vvi distances(num_cities);
    for (int i = 0; i < num_cities; ++i) {
      vi scores;
      run_bfs(i, scores);
      distances[i] = std::move(scores);
    }

    int total_score = 0;
    for (int i = 0; i < num_cities; ++i) {
      int current_score = 0;
      for (const auto& d : distances[i]) {
        if (d == NOT_PROCESSED) {
          continue;
        }
        int d2 = d * d;
        current_score ^= d2;
      }
      total_score += current_score;
    }
    cout << "graph_hash=" << total_score << endl;

    clock_t tend = clock();
    double elapsed_msecs = double(tend - tbegin) / CLOCKS_PER_SEC * 1000;
    cout << "time=" << elapsed_msecs << endl;
    // cout << "name=cpp" << endl;

  }

  void run_bfs(int start, vi& scores) {
    scores.assign(num_cities, NOT_PROCESSED);
    scores[start] = 0;

    deque<int> queue;
    queue.push_back(start);

    while (!queue.empty()) {
      int now = queue.front();
      queue.pop_front();
      int value = scores[now];

      for (const auto& next : graph[now]) {
        if (scores[next] == NOT_PROCESSED) {
          scores[next] = value + 1;
          queue.push_back(next);
        }
      }
    }
  }
};



int main (int argc, char *argv[]) {
  if (argc < 2) {
    cout << "map name not specified" << endl;
    return 1;
  }
	freopen(argv[1], "rt", stdin);
	//freopen("", "wt", stdout);
	//std::ios::sync_with_stdio(false);
  Solver s;
  s.init();
  s.compute_hash();

  return 0;
}
