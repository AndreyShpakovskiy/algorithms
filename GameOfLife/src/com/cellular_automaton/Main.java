package com.cellular_automaton;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Cells cells = new Cells(40, 40);
        Field field = new Field(cells);
        field.repaint();


        while(true) {
            Thread.sleep(300);

            cells.checkAllCells();
            field.repaint();
        }
    }
}
