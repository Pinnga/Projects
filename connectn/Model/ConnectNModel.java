package edu.wm.cs.cs301.connectn.Model;

import javax.swing.JPanel;
import javax.swing.JLabel;

/**
 * The ConnectNModel class represents the model of the ConnectN game.
 * It contains the game logic and state information.
 */
public class ConnectNModel {
    private int difficulty;
    private int columnCount;
    private int maximumRows;
    private int piecesToWin;
    private JPanel[][] cells;

    /**
     * Constructs a new ConnectNModel with the specified difficulty level.
     * @param difficulty The difficulty level of the game.
     */
    public ConnectNModel(int difficulty) {
        this.difficulty = difficulty;
        if (difficulty == 1) {
            this.columnCount = 5;
            this.maximumRows = 4;
            this.piecesToWin = 3;
        } else if (difficulty == 2) {
            this.columnCount = 6;
            this.maximumRows = 7;
            this.piecesToWin = 4;
        } else {
            this.columnCount = 8;
            this.maximumRows = 9;
            this.piecesToWin = 5;
        }

        initializeCells();
    }

    private void initializeCells() {
        this.cells = new JPanel[maximumRows][columnCount];
        for (int i = 0; i < maximumRows; i++) {
            for (int j = 0; j < columnCount; j++) {
                cells[i][j] = new JPanel();
            }
        }
    }

    public int getColumnCount() {
        return columnCount;
    }

    public int getMaximumRows() {
        return maximumRows;
    }

    public int getDifficulty() {
        return difficulty;
    }

    public void setCells(JPanel[][] cells) {
        this.cells = cells;
    }

    public JPanel[][] getCells() {
        return cells;
    }

    public int getRowCount() {
        return cells.length;
    }

    public int getColumnCountInRow(int row) {
        return cells[row].length;
    }

    /**
     * Checks if the game is over by determining if there is a winner or a tie.
     * @return true if the game is over, false otherwise.
     */
    public boolean isGameOver() {
        return checkForWin("X") || checkForWin("O") || checkForTie();
    }

    /**
     * Checks if the player with the specified symbol has won the game.
     * @param playerSymbol The symbol of the player to check for win.
     * @return true if the player has won, false otherwise.
     */
    public boolean checkForWin(String playerSymbol) {
        for (int row = 0; row < maximumRows; row++) {
            for (int col = 0; col <= columnCount - piecesToWin; col++) {
                if (checkTokensInARow(row, col, 0, 1, playerSymbol)) {
                    return true;
                }
            }
        }

        // Check for win vertically
        for (int col = 0; col < columnCount; col++) {
            for (int row = 0; row <= maximumRows - piecesToWin; row++) {
                if (checkTokensInARow(row, col, 1, 0, playerSymbol)) {
                    return true;
                }
            }
        }

        // Check for win diagonally (bottom-left to top-right)
        for (int row = 0; row <= maximumRows - piecesToWin; row++) {
            for (int col = 0; col <= columnCount - piecesToWin; col++) {
                if (checkTokensInARow(row, col, 1, 1, playerSymbol)) {
                    return true;
                }
            }
        }

        // Check for win diagonally (bottom-right to top-left)
        for (int row = 0; row <= maximumRows - piecesToWin; row++) {
            for (int col = piecesToWin - 1; col < columnCount; col++) {
                if (checkTokensInARow(row, col, 1, -1, playerSymbol)) {
                    return true;
                }
            }
        }

        return false;
    }

    public boolean isColumnFull(int column) {
        return cells[0][column].getComponentCount() > 0;
    }

    public boolean checkForTie() {
        for (int row = 0; row < maximumRows; row++) {
            for (int col = 0; col < columnCount; col++) {
                if (cells[row][col].getComponentCount() == 0) {
                    return false;
                }
            }
        }
        return true;
    }

    private boolean checkTokensInARow(int row, int col, int rowIncrement, int colIncrement, String playerSymbol) {
        String token = getCellToken(row, col);
        if (!token.equals(playerSymbol)) {
            return false;
        }
        for (int i = 1; i < piecesToWin; i++) {
            if (!getCellToken(row + i * rowIncrement, col + i * colIncrement).equals(token)) {
                return false;
            }
        }
        return true;
    }

    private String getCellToken(int row, int col) {
        if (row < 0 || row >= maximumRows || col < 0 || col >= columnCount) {
            return " ";
        }
        if (cells[row][col].getComponentCount() == 0) {
            return " ";
        }
        return ((JLabel) cells[row][col].getComponent(0)).getText();
    }
}
