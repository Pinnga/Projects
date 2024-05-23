package edu.wm.cs.cs301.connectn.Controller;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import edu.wm.cs.cs301.connectn.Model.Computer;
import edu.wm.cs.cs301.connectn.Model.ConnectNModel;
import edu.wm.cs.cs301.connectn.View.ConnectNFrame;
import edu.wm.cs.cs301.connectn.View.ConnectPanel;
import edu.wm.cs.cs301.connectn.View.FullColumn;
import edu.wm.cs.cs301.connectn.View.LossScreen;
import edu.wm.cs.cs301.connectn.View.TieScreen;
import edu.wm.cs.cs301.connectn.View.WinScreen;

/**
 * The ConnectNController class implements the controller for the ConnectN game.
 * It manages user interactions, updates the game model, and controls the game flow.
 */
public class ConnectNController {
    private ConnectNModel model;
    private ConnectNFrame frame;
    private ConnectPanel panel;
    private int turnCount;
    private Computer computer;
    private String playerSymbol;
    private boolean gameEnded;

    /**
     * Constructs a new ConnectNController with the specified frame, panel, and model.
     * @param frame The main frame of the game.
     * @param panel The panel containing the game board.
     * @param model The model representing the game logic.
     */
    public ConnectNController(ConnectNFrame frame, ConnectPanel panel, ConnectNModel model) {
        this.frame = frame;
        this.panel = panel;
        this.model = model;
        this.turnCount = 0;
        this.computer = new Computer(panel);
        this.playerSymbol = "X";
        this.gameEnded = false;

        JButton[] buttons = panel.getButtons();
        for (int i = 0; i < buttons.length; i++) {
            buttons[i].addActionListener(new ButtonListener(i));
        }
    }

    /**
     * ActionListener for the buttons on the game board.
     */
    private class ButtonListener implements ActionListener {
        private int column;

        /**
         * Constructs a ButtonListener with the specified column.
         * @param column The column index associated with the button.
         */
        public ButtonListener(int column) {
            this.column = column;
        }

        /**
         * Handles button click events.
         * @param e The ActionEvent representing the button click event.
         */
        @Override
        public void actionPerformed(ActionEvent e) {
            if (!gameEnded) {
                if (dropDisc(column)) {
                    model.setCells(panel.getCells());
                    if (model.isGameOver()) {
                        showWinScreen();
                        gameEnded = true;
                        removeButtonListeners();
                    } else {
                        computer.makeMove();
                        model.setCells(panel.getCells());
                        if (model.isGameOver()) {
                            showLossScreen();
                            gameEnded = true;
                            removeButtonListeners();
                        } else if (model.checkForWin(playerSymbol)) {
                            showTieScreen();
                            gameEnded = true;
                            removeButtonListeners();
                        }
                    }
                }
            }
        }

        /**
         * Drops a disc into the specified column if it's not full.
         * @param column The column index where the disc should be dropped.
         * @return True if the disc was successfully dropped, false otherwise.
         */
        private boolean dropDisc(int column) {
            JPanel[][] cells = panel.getCells();
            if (isColumnFull(column)) {
                FullColumn fullColumnFrame = new FullColumn();
                fullColumnFrame.setVisible(true);
                return false;
            }

            for (int row = model.getMaximumRows() - 1; row >= 0; row--) {
                if (cells[row][column].getComponentCount() == 0) {
                    JLabel label = new JLabel(playerSymbol);
                    label.setFont(new Font("Arial Rounded MT Bold", Font.BOLD, 30));
                    cells[row][column].add(label);
                    cells[row][column].revalidate();
                    cells[row][column].repaint();
                    turnCount++;
                    frame.updateTurnLabel(turnCount);
                    return true;
                }
            }
            return false;
        }

        /**
         * Checks if the specified column is full.
         * @param column The column index to check.
         * @return True if the column is full, false otherwise.
         */
        private boolean isColumnFull(int column) {
            JPanel[][] cells = panel.getCells();
            return cells[0][column].getComponentCount() > 0;
        }

        /**
         * Displays the win screen.
         */
        private void showWinScreen() {
            WinScreen winScreen = new WinScreen(frame, turnCount, model);
            winScreen.setVisible(true);
        }

        /**
         * Displays the loss screen.
         */
        private void showLossScreen() {
            LossScreen lossScreen = new LossScreen(frame);
            lossScreen.setVisible(true);
        }

        /**
         * Displays the tie screen.
         */
        private void showTieScreen() {
            TieScreen tieScreen = new TieScreen(frame);
            tieScreen.setVisible(true);
        }

        /**
         * Removes action listeners from all buttons.
         */
        private void removeButtonListeners() {
            JButton[] buttons = panel.getButtons();
            for (JButton button : buttons) {
                for (ActionListener listener : button.getActionListeners()) {
                    button.removeActionListener(listener);
                }
            }
        }
    }
}
