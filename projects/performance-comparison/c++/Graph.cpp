#include "Graph.h"

Graph::~Graph() {
    for (auto& pair : vertices) {
        delete pair.second;
    }
}

void Graph::addVertex(int id) {
    if (vertices.find(id) == vertices.end()) {
        vertices[id] = new Vertex(id);
    }
}

void Graph::addEdge(int id1, int id2, int weight) {
    Vertex* v1 = vertices[id1];
    Vertex* v2 = vertices[id2];
    if (v1 && v2) {
        v1->addEdge(v2, weight);
        v2->addEdge(v1, weight); // Because the graph is undirected
    }
}

const std::unordered_map<int, Vertex*>& Graph::getVertices() const {
    return vertices;
}

void Graph::readGraphFromFile(const std::string& filename) {
    std::ifstream file(filename);
    if (!file) {
        std::cerr << "File not found: " << filename << std::endl;
        return;
    }
    int id1, id2, weight;
    while (file >> id1 >> id2 >> weight) {
        addVertex(id1);
        addVertex(id2);
        addEdge(id1, id2, weight);
    }
}

long long Graph::dijkstra(int sourceId) {
    using namespace std::chrono;  // Use the namespace for easier access to chrono functions

    if (vertices.find(sourceId) == vertices.end()) {
        std::cerr << "Vertex not found" << std::endl;
        return -1;  // Return -1 to indicate an error if the vertex doesn't exist
    }

    Vertex* source = vertices[sourceId];
    source->distance = 0;

    std::priority_queue<Vertex*, std::vector<Vertex*>, CompareVertex> queue;
    queue.push(source);

    auto startTime = high_resolution_clock::now();  // Start timing

    while (!queue.empty()) {
        Vertex* current = queue.top();
        queue.pop();

        if (current->visited) continue;
        current->visited = true;

        for (Edge& edge : current->edges) {
            Vertex* v = edge.vertex;
            int distanceThroughCurrent = current->distance + edge.weight;
            if (distanceThroughCurrent < v->distance) {
                v->distance = distanceThroughCurrent;
                v->predecessor = current;
                queue.push(v);
            }
        }
    }

    auto endTime = high_resolution_clock::now();  // End timing
    auto duration = duration_cast<microseconds>(endTime - startTime).count();  // Calculate duration in microseconds

    return duration;
}

void Graph::printGraph() {
    for (const auto& pair : vertices) {
        std::cout << "Vertex " << pair.first << " connected to:";
        for (const Edge& edge : pair.second->edges) {
            std::cout << "\n  - Vertex " << edge.vertex->id << " with weight " << edge.weight;
        }
        std::cout << std::endl;
    }
}

void Graph::printPath(int targetId) {
    if (vertices.find(targetId) == vertices.end()) {
        std::cout << "Vertex not found" << std::endl;
        return;
    }
    std::vector<int> path;
    for (Vertex* v = vertices[targetId]; v != nullptr; v = v->predecessor) {
        path.push_back(v->id);
    }
    if (path.size() == 1) {
        std::cout << "Target vertex is the same as the source vertex!\nTotal Distance: 0" << std::endl;
        return;
    }
    std::reverse(path.begin(), path.end());
    std::cout << "\nShortest path to Vertex " << targetId << " is:\n";
    for (size_t i = 0; i < path.size(); ++i) {
        std::cout << "Vertex " << path[i];
        if (i != path.size() - 1) {
            std::cout << " -> ";
        }
    }
    std::cout << "\nTotal Distance: " << vertices[targetId]->distance << std::endl;
}

int main() {
    Graph graph;
    graph.readGraphFromFile("graph_data.txt");

    int sourceId, targetId;
    std::cout << "Enter the ID of the source vertex:\n";
    std::cin >> sourceId;
    std::cout << "Enter the ID of the target vertex:\n";
    std::cin >> targetId;

    const auto& vertices = graph.getVertices();
    if (vertices.find(sourceId) == vertices.end() || vertices.find(targetId) == vertices.end()) {
        std::cerr << "One or both vertices were not found in the graph." << std::endl;
        return 1;
    }

    long long duration = graph.dijkstra(sourceId);  // Get the duration of Dijkstra's algorithm
    graph.printPath(targetId);

    std::cout << "\nUsing C++, Dijkstra's algorithm took " << duration << " microseconds.\n";

    return 0;
}