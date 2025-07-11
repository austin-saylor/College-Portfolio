public class Edge {
    private Vertex vertex; // The vertex this edge connects to
    private int weight; // The weight of this edge

    public Edge(Vertex vertex, int weight) {
        this.vertex = vertex;
        this.weight = weight;
    }

    public Vertex getVertex() {
        return vertex;
    }

    public int getWeight() {
        return weight;
    }

    @Override
    public String toString() {
        return "" + (vertex.getId());
    }
}
