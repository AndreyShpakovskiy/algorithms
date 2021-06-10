package bsu.shpakovskiy;

import bsu.shpakovskiy.Algorithms;

public class Main {
    public static void main(String[] args) {
        Integer[][] matrix = {
                {Integer.MAX_VALUE, 2, 6, 12, 3, 16},
                {2, Integer.MAX_VALUE, 5, 9, 12, 3},
                {6, 5, Integer.MAX_VALUE, 4, 2, 11},
                {12, 9, 4, Integer.MAX_VALUE, Integer.MAX_VALUE, 4},
                {3, 12, 2, Integer.MAX_VALUE, Integer.MAX_VALUE, 10},
                {16, Integer.MAX_VALUE, 11, 4, 10, Integer.MAX_VALUE}};

        Algorithms.floydAlgorithm(matrix);
        System.out.println("Little's algorithm:");
        Algorithms.littleAlgorithm(matrix);
    }
}
