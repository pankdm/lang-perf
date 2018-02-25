#include "cpp_solver.h"

const int NOT_PROCESSED = -1;


CppSolver::CppSolver(vvi* _graph)
  : graph(_graph)
{

}

void CppSolver::run_bfs(int start, vi* _scores) {
  vi& scores = *_scores;
  auto num_cities = graph->size();
  scores.assign(num_cities, NOT_PROCESSED);
  scores[start] = 0;

  deque<int> queue;
  queue.push_back(start);

  while (!queue.empty()) {
    int now = queue.front();
    queue.pop_front();
    int value = scores[now];

    for (const auto& next : (*graph)[now]) {
      if (scores[next] == NOT_PROCESSED) {
        scores[next] = value + 1;
        queue.push_back(next);
      }
    }
  }
}

void CppSolver::compute_hash() {
  clock_t tbegin = clock();

  auto num_cities = graph->size();
  vvi distances(num_cities);
  for (int i = 0; i < num_cities; ++i) {
    vi scores;
    run_bfs(i, &scores);
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
}
