package edu.wm.cs.cs301.connectn.View;

import javax.swing.*;
import java.awt.*;

/**
 * Represents a dialog window displaying game instructions.
 */
public class InstructionsDialog extends JDialog {
    private static final long serialVersionUID = 1L;

    /**
     * Constructs an InstructionsDialog with the specified parent JFrame.
     * 
     * @param parent The parent JFrame
     */
    public InstructionsDialog(JFrame parent) {
        super(parent, "Instructions", true);
        setDefaultCloseOperation(DISPOSE_ON_CLOSE);
        setSize(600, 360);

        JTextArea instructionsText = createInstructionsTextArea();
        JPanel instructionsPanel = createInstructionsPanel(instructionsText);

        add(instructionsPanel);
        setLocationRelativeTo(parent);
    }

    private JTextArea createInstructionsTextArea() {
        JTextArea instructionsText = new JTextArea(
                        "1. ConnectN is a two-player game where the objective is to connect N of your own characters in a row, column, or diagonal.\n" +
                        "2. Players take turns placing their characters into any of the available slots in the game board.\n" +
                        "3. The game board has different modes: Small, Medium, and Large, each with varying dimensions.\n" +
                        "   - Small: 4 rows, 5 columns, and the first player to connect 3 characters wins.\n" +
                        "   - Medium: 6 rows, 7 columns, and the first player to connect 4 characters wins.\n" +
                        "   - Large: 8 rows, 9 columns, and the first player to connect 5 characters wins.\n" +
                        "4. The leaderboard displays the best scores for each game mode.\n" +
                        "   - The format is: Mode: Player - Turns\n" +
                        "   - The lower the number of turns, the better the score.\n" +
                        "   - If you match or beat the existing score, your entry will replace it.\n" +
                        "   - If you quit the game, your score will not be recorded.\n\n" +
                        "GOOD LUCK THE COMPUTER IS VERY SMART !");
        instructionsText.setEditable(false);
        instructionsText.setFocusable(false);
        instructionsText.setFont(new Font("Arial Rounded MT Bold", Font.PLAIN, 14));
        instructionsText.setLineWrap(true);
        instructionsText.setWrapStyleWord(true);
        instructionsText.setMargin(new Insets(10, 10, 10, 10));
        return instructionsText;
    }

    private JPanel createInstructionsPanel(JTextArea instructionsText) {
        JPanel instructionsPanel = new JPanel(new BorderLayout());
        instructionsPanel.add(createTitlePanel(), BorderLayout.NORTH);
        instructionsPanel.add(instructionsText, BorderLayout.CENTER);
        return instructionsPanel;
    }

    private JPanel createTitlePanel() {
        JPanel panel = new JPanel(new FlowLayout());
        panel.setBorder(BorderFactory.createEmptyBorder(0, 5, 5, 5));
        JLabel label = new JLabel("Instructions");
        label.setFont(new Font("Arial Rounded MT Bold", Font.BOLD, 20));
        panel.add(label);
        return panel;
    }
}
