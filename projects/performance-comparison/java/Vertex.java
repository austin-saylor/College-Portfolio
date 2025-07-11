import java.util.List;
import java.util.ArrayList;

public class Vertex implements Comparable<Vertex> {
    private int id;
    private List<Edge> edges;
    private int distance = Integer.MAX_VALUE;
    private Vertex predecessor;
    private boolean visited = false;

    public Vertex(int id) {
        this.id = id;
        edges = new ArrayList<>();
    }

    public void addEdge(Vertex vertex, int weight) {
        edges.add(new Edge(vertex, weight));
    }

    public List<Edge> getEdges() {
        return edges;
    }

    public int getId() {
        return id;
    }

    public int getDistance() {
        return distance;
    }

    public void setDistance(int distance) {
        this.distance = distance;
    }

    public Vertex getPredecessor() {
        return predecessor;
    }

    public void setPredecessor(Vertex predecessor) {
        this.predecessor = predecessor;
    }

    public boolean isVisited() {
        return visited;
    }

    public void setVisited(boolean visited) {
        this.visited = visited;
    }

    @Override
    public int compareTo(Vertex otherVertex) {
        return Integer.compare(this.distance, otherVertex.distance);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("\n Vertex " + id + " connected to:");
        for (Edge edge : edges) {
            sb.append("\n- " + edge + " with weight " + edge.getWeight());
        }
        return sb.toString();
    }
}
