#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <limits>
#include <algorithm>
#include <fstream>
#include <string>
#include <chrono>

struct Vertex;

struct Edge {
    Vertex* vertex;
    int weight;
    Edge(Vertex* v, int w) : vertex(v), weight(w) {}
};

struct Vertex {
    int id;
    std::vector<Edge> edges;
    int distance;
    Vertex* predecessor;
    bool visited;

    Vertex(int id) : id(id), distance(std::numeric_limits<int>::max()), predecessor(nullptr), visited(false) {}

    void addEdge(Vertex* vertex, int weight) {
        edges.emplace_back(vertex, weight);
    }
};

struct CompareVertex {
    bool operator()(const Vertex* v1, const Vertex* v2) {
        return v1->distance > v2->distance;
    }
};

class Graph {
    std::unordered_map<int, Vertex*> vertices;

public:
    Graph() = default;
    ~Graph();

    void addVertex(int id);
    void addEdge(int id1, int id2, int weight);
    void readGraphFromFile(const std::string& filename);
    long long dijkstra(int sourceId);
    void printGraph();
    void printPath(int targetId);
    const std::unordered_map<int, Vertex*>& getVertices() const; // Accessor for vertices
};
