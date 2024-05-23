package edu.wm.cs.cs301.connectn.View;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import edu.wm.cs.cs301.connectn.Model.ConnectNModel;

/**
 * Represents the win screen displayed when the player wins the game.
 * It extends JFrame and provides options to enter the player's name and view the leaderboard.
 */
public class WinScreen extends JFrame {
    private static final long serialVersionUID = 1L;
    private ConnectNFrame connectNFrame;
    private JTextField nameTextField;
    private int turnCount;
    private ConnectNModel model;
    
    /**
     * Constructs a WinScreen frame with the specified ConnectNFrame, turn count, and ConnectNModel.
     * 
     * @param connectNFrame The ConnectNFrame instance
     * @param turnCount The number of turns taken to win
     * @param model The ConnectNModel instance
     */
    public WinScreen(ConnectNFrame connectNFrame, int turnCount, ConnectNModel model) {
        this.connectNFrame = connectNFrame;
        this.turnCount = turnCount;
        this.model = model;
        setSize(400, 400);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setResizable(false);

        JPanel panel = new JPanel(new BorderLayout());
        JLabel messageLabel = new JLabel("YOU WIN! CONGRATULATIONS!");
        messageLabel.setFont(new Font("Arial Rounded MT Bold", Font.PLAIN, 16));
        messageLabel.setHorizontalAlignment(JLabel.CENTER);
        panel.add(messageLabel, BorderLayout.NORTH);

        createSouthPanel(panel, turnCount, model.getDifficulty());

        add(panel);
        centerFrameOnScreen();
    }

    /**
     * Creates the south panel containing player name input, score display, and button options.
     * 
     * @param mainPanel The main panel to add the south panel to
     * @param turnCount The number of turns taken to win
     * @param difficulty The difficulty level of the game
     */
    private void createSouthPanel(JPanel mainPanel, int turnCount, int difficulty) {
        JPanel southPanel = new JPanel(new BorderLayout());
        southPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        JLabel emojiLabel = new JLabel("\uD83D\uDE0E");
        emojiLabel.setFont(new Font(Font.SANS_SERIF, Font.PLAIN, 100));
        emojiLabel.setHorizontalAlignment(JLabel.CENTER);
        southPanel.add(emojiLabel, BorderLayout.NORTH);

        JPanel centerPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));

        JLabel nameLabel = new JLabel("Enter your name:");
        nameLabel.setFont(new Font("Arial Rounded MT Bold", Font.PLAIN, 16));
        centerPanel.add(nameLabel);

        nameTextField = new JTextField(20);
        centerPanel.add(nameTextField);

        JLabel scoreLabel = new JLabel("Your Score is: " + turnCount);
        scoreLabel.setFont(new Font("Arial Rounded MT Bold", Font.PLAIN, 16));
        centerPanel.add(scoreLabel);

        JLabel difficultyLabel = new JLabel("Difficulty: " + getDifficultyString(difficulty));
        difficultyLabel.setFont(new Font("Arial Rounded MT Bold", Font.PLAIN, 16));
        centerPanel.add(difficultyLabel);

        southPanel.add(centerPanel, BorderLayout.CENTER);

        JPanel buttonPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
        JButton enterButton = new JButton("Enter");
        enterButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String playerName = nameTextField.getText().trim();
                if (!playerName.isEmpty()) {
                    if (playerName.contains(" ")) {
                        JOptionPane.showMessageDialog(WinScreen.this, "Player name cannot contain spaces!", "Error", JOptionPane.ERROR_MESSAGE);
                    } else {
                        Showlbp(playerName);
                        dispose();
                    }
                } else {
                    JOptionPane.showMessageDialog(WinScreen.this, "Please enter your name!", "Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        });

        buttonPanel.add(enterButton);

        JButton quitButton = new JButton("Cancel");
        quitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dispose();
            }
        });
        buttonPanel.add(quitButton);

        southPanel.add(buttonPanel, BorderLayout.SOUTH);

        mainPanel.add(southPanel, BorderLayout.CENTER);
    }

    /**
     * Displays the leaderboard panel with the entered player name.
     * 
     * @param playerName The name of the player
     */
    private void Showlbp(String playerName) {
        LeaderBoardPanel leaderboardPanel = new LeaderBoardPanel(connectNFrame, turnCount, playerName, model.getDifficulty());
        leaderboardPanel.setVisible(true);
    }

    /**
     * Centers the frame on the screen.
     */
    private void centerFrameOnScreen() {
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        Dimension frameSize = getSize();
        int x = (screenSize.width - frameSize.width) / 2;
        int y = (screenSize.height - frameSize.height) / 2;
        setLocation(x, y);
    }
    
    /**
     * Converts the difficulty level integer to its corresponding string representation.
     * 
     * @param difficulty The difficulty level integer
     * @return The string representation of the difficulty level
     */
    private String getDifficultyString(int difficulty) {
        switch (difficulty) {
            case 1:
                return "Easy";
            case 2:
                return "Medium";
            case 3:
                return "Hard";
            default:
                return "Unknown";
        }
    }
}
