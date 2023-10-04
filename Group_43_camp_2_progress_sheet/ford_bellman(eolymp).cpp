#include <iostream>
#include <vector>
#include <climits>

using namespace std;

vector<vector<int>> edges;

int main() {
    
    int n, m;
    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        edges.push_back({u, v, w});
    }
    const int inf = INT_MAX;
    vector<int> dist(n + 1, inf);
    dist[1] = 0;

    for (int i = 0; i < n - 1; i++) {
        for (const auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            if (dist[u] != inf && dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
            }
        }
    }

    int no_path = 30000;
    for (int i = 1; i <= n; i++) {
        if (dist[i] == inf) {
            dist[i] = no_path;
        }
    }

    for (int i = 1; i <= n; i++) {
        cout << dist[i] << " ";
    }
    cout << endl;

    return 0;
}
