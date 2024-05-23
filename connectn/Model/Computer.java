package edu.wm.cs.cs301.connectn.Model;

import javax.swing.JLabel;
import java.awt.Font;
import java.util.Random;
import edu.wm.cs.cs301.connectn.View.ConnectPanel;

/**
 * The Computer class represents the computer player in the ConnectN game.
 * It is responsible for making moves and interacting with the game panel.
 */
public class Computer {
    private ConnectPanel panel;
    private String playerSymbol;

    /**
     * Constructs a new Computer player with the specified game panel.
     * @param panel The game panel where the computer makes moves.
     */
    public Computer(ConnectPanel panel) {
        this.panel = panel;
        this.playerSymbol = "O";
    }

    /**
     * Makes a move for the computer player.
     * The computer first tries to win the game, then tries to block the opponent,
     * and if neither, makes a random move.
     */
    public void makeMove() {
        String opponentSymbol = playerSymbol.equals("X") ? "O" : "X";

        // Try to win the game
        for (int col = 0; col < panel.getButtons().length; col++) {
            if (isColumnEmpty(col)) {
                int row = findEmptyRow(col);
                placeSymbol(row, col, playerSymbol);
                if (panel.getConnectNModel().checkForWin(playerSymbol)) {
                    return;
                } else {
                    removeSymbol(row, col);
                }
            }
        }

        // Try to block the opponent
        for (int col = 0; col < panel.getButtons().length; col++) {
            if (isColumnEmpty(col)) {
                int row = findEmptyRow(col);
                placeSymbol(row, col, opponentSymbol);
                if (panel.getConnectNModel().checkForWin(opponentSymbol)) {
                    removeSymbol(row, col);
                    placeSymbol(row, col, playerSymbol);
                    return;
                } else {
                    removeSymbol(row, col);
                }
            }
        }

        // If no winning move or blocking move, make a random move
        makeRandomMove();
    }

    private void placeSymbol(int row, int col, String symbol) {
        JLabel label = new JLabel(symbol);
        label.setFont(new Font("Arial Rounded MT Bold", Font.BOLD, 30));
        panel.getCells()[row][col].add(label);
        panel.getCells()[row][col].revalidate();
        panel.getCells()[row][col].repaint();
    }

    private void removeSymbol(int row, int col) {
        panel.getCells()[row][col].removeAll();
    }

    private boolean isColumnEmpty(int column) {
        for (int row = 0; row < panel.getCells().length; row++) {
            if (panel.getCells()[row][column].getComponentCount() == 0) {
                return true;
            }
        }
        return false;
    }

    private int findEmptyRow(int column) {
        for (int row = panel.getCells().length - 1; row >= 0; row--) {
            if (panel.getCells()[row][column].getComponentCount() == 0) {
                return row;
            }
        }
        return -1;
    }

    private void makeRandomMove() {
        Random random = new Random();
        int column;
        do {
            column = random.nextInt(panel.getButtons().length);
        } while (!isColumnEmpty(column));

        int row = findEmptyRow(column);
        placeSymbol(row, column, playerSymbol);
    }

    /**
     * Gets the player symbol.
     * @return The player symbol.
     */
    public String getPlayerSymbol() {
        return playerSymbol;
    }
}
