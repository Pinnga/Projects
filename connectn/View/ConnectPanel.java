package edu.wm.cs.cs301.connectn.View;

import javax.swing.*;
import edu.wm.cs.cs301.connectn.Model.ConnectNModel;
import java.awt.*;

/**
 * Represents the panel containing the game grid and column selection buttons.
 * It extends JPanel and contains methods to initialize the grid cells, buttons,
 * and set properties for the panel.
 */
public class ConnectPanel extends JPanel {
    private static final long serialVersionUID = 1L;
    private JPanel[][] cells;
    private JButton[] buttons;
    private int rows;
    private int columns;
    private ConnectNModel connectNModel;

    /**
     * Constructs a ConnectPanel with the specified ConnectNModel and ConnectNFrame.
     * Initializes the grid cells, buttons, and sets properties for the panel.
     * 
     * @param model The ConnectNModel instance
     * @param connectNFrame The ConnectNFrame instance
     */
    public ConnectPanel(ConnectNModel model, ConnectNFrame connectNFrame) {
        this.rows = model.getMaximumRows();
        this.columns = model.getColumnCount();
        this.connectNModel = model;
        setLayout(new GridLayout(rows + 1, columns));
        cells = new JPanel[rows][columns];
        buttons = new JButton[columns];
        addCells();
        addButtons();
        setPanelProperties();
    }

    /**
     * Adds cells to the grid panel based on the number of rows and columns.
     */
    private void addCells() {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                JPanel cell = createCell();
                cells[i][j] = cell;
                add(cell);
            }
        }
    }

    /**
     * Creates a cell panel with a white background and black border.
     * 
     * @return The created cell panel
     */
    private JPanel createCell() {
        JPanel cell = new JPanel();
        cell.setBackground(Color.WHITE);
        cell.setBorder(BorderFactory.createLineBorder(Color.BLACK));
        return cell;
    }

    /**
     * Sets properties for the grid panel, such as preferred size and background color.
     */
    private void setPanelProperties() {
        setPreferredSize(new Dimension(400, 400));
        setBackground(Color.BLACK);
        setBorder(BorderFactory.createLineBorder(Color.BLACK));
    }

    /**
     * Adds buttons to the grid panel for column selection.
     */
    private void addButtons() {
        Font buttonFont = new Font("Arial Rounded MT Bold", Font.BOLD, 12);
        for (int i = 0; i < columns; i++) {
            JButton button = new JButton(Integer.toString(i + 1));
            button.setBackground(Color.WHITE);
            button.setForeground(Color.BLACK);
            button.setFont(buttonFont);
            button.setBorder(BorderFactory.createLineBorder(Color.BLACK, 2));
            button.setFocusPainted(false);
            buttons[i] = button;
            add(button);
        }
    }

    /**
     * Retrieves the grid cells.
     * 
     * @return The grid cells
     */
    public JPanel[][] getCells() {
        return cells; // Return the grid cells
    }

    /**
     * Retrieves the column selection buttons.
     * 
     * @return The column selection buttons
     */
    public JButton[] getButtons() {
        return buttons; // Return the column selection buttons
    }

    /**
     * Retrieves the ConnectNModel instance associated with the panel.
     * 
     * @return The ConnectNModel instance
     */
    public ConnectNModel getConnectNModel() {
        return connectNModel; // Return the ConnectNModel instance
    }
}
