import java.util.Map;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Graph {
    private Map<Integer, Vertex> vertices;

    public Graph() {
        vertices = new HashMap<>();
    }

    public void addVertex(int id) {
        vertices.putIfAbsent(id, new Vertex(id));
    }

    public void addEdge(int id1, int id2, int weight) {
        Vertex v1 = vertices.get(id1);
        Vertex v2 = vertices.get(id2);
        if (v1 != null && v2 != null) {
            v1.addEdge(v2, weight);
            v2.addEdge(v1, weight); // If the graph is undirected
        }
    }

    public void readGraphFromFile(String filename) {
        File file = new File(filename);
        try (Scanner scanner = new Scanner(file)) {
            while (scanner.hasNextLine()) {
                int id1 = scanner.nextInt();
                int id2 = scanner.nextInt();
                int weight = scanner.nextInt();
                
                if (!vertices.containsKey(id1)) {
                    addVertex(id1);
                }
                if (!vertices.containsKey(id2)) {
                    addVertex(id2);
                }
                addEdge(id1, id2, weight);
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + filename);
        }
    }

    public Map<Integer, Vertex> getVertices() {
        return vertices;
    }    

    public long dijkstra(int sourceId) {
        if (!vertices.containsKey(sourceId)) {
            System.out.println("Vertex not found");
            return -1; // Return -1 or another indicator of failure
        }
        Vertex source = vertices.get(sourceId);
        source.setDistance(0);
    
        PriorityQueue<Vertex> queue = new PriorityQueue<>();
        queue.add(source);
    
        long startTime = System.nanoTime(); // Start timing
    
        while (!queue.isEmpty()) {
            Vertex current = queue.poll();
            if (current.isVisited()) continue;
    
            current.setVisited(true);
    
            for (Edge edge : current.getEdges()) {
                Vertex v = edge.getVertex();
                int distanceThroughCurrent = current.getDistance() + edge.getWeight();
                if (distanceThroughCurrent < v.getDistance()) {
                    v.setDistance(distanceThroughCurrent);
                    v.setPredecessor(current);
                    queue.add(v);
                }
            }
        }
    
        long endTime = System.nanoTime(); // End timing
        long duration = (endTime - startTime)/1000; // Calculate the duration in microseconds
        return duration;
    }    

    public void printGraph() {
        for (Vertex vertex : vertices.values()) {
            System.out.println(vertex);
        }
    }

    public void printPath(int targetId) {
        if (!vertices.containsKey(targetId)) {
            System.out.println("Vertex not found");
            return;
        }
        Vertex target = vertices.get(targetId);
        List<Integer> path = new ArrayList<>();
        for (Vertex vertex = target; vertex != null; vertex = vertex.getPredecessor()) {
            path.add(vertex.getId());
        }
        Collections.reverse(path);
        
        if (path.size() > 1) {

            System.out.println("\nShortest path to Vertex " + targetId + " is:");
            StringBuilder result = new StringBuilder();

            for (int i = 0; i < path.size(); i++) {
                result.append("Vertex ").append(path.get(i));
                if (i != path.size() - 1) {
                    result.append(" -> ");
                }
            }

            result.append("\nTotal Distance: ").append(target.getDistance() + "\n");
            System.out.println(result.toString());

        } else {
            System.out.println("Target vertex is the same as the source vertex!");
            System.out.println("Total Distance: 0");
        }
    }

    public static void main(String[] args) {
        Graph graph = new Graph();
    
        // Replace this with the path to your graph data file
        graph.readGraphFromFile("graph_data.txt"); 
        
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the ID of the source vertex:");
        int sourceId = scanner.nextInt();
        
        System.out.println("Enter the ID of the target vertex:");
        int targetId = scanner.nextInt();
        
        if (!graph.getVertices().containsKey(sourceId) || !graph.getVertices().containsKey(targetId)) {
            System.out.println("One or both vertices were not found in the graph.");
            scanner.close();
            return;
        }
        
        long duration = graph.dijkstra(sourceId);
        graph.printPath(targetId);
        
        if (duration != -1) {
            System.out.println("Using Java, Dijkstra's algorithm took " + duration + " microseconds.");
        }
        
        scanner.close();
    }    
}