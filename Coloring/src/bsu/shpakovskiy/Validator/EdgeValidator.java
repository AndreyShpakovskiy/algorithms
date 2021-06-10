package bsu.shpakovskiy.Validator;


import bsu.shpakovskiy.Classes.Edge;
import bsu.shpakovskiy.Classes.Vertex;

public class EdgeValidator {
    public static boolean isEdgesSame(Edge firstEdge, Edge secondEdge) {
        if (firstEdge.getFromVertex().getName() == secondEdge.getFromVertex().getName() &&
                firstEdge.getToVertex().getName() == secondEdge.getToVertex().getName()) {
            return true;
        }
        if (firstEdge.getFromVertex().getName() == secondEdge.getToVertex().getName() &&
                firstEdge.getToVertex().getName() == secondEdge.getFromVertex().getName()) {
            return true;
        }

        return false;
    }

    public static boolean isVertexSame(Vertex vertexOne, Vertex vertexTwo) {
        return vertexOne.getName() == vertexTwo.getName();
    }
}