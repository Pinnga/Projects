package edu.wm.cs.cs301.connectn.View;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;

/**
 * Represents a leaderboard panel displaying the best scores for each game mode.
 * It extends JFrame and contains methods to update and display the leaderboard.
 */
public class LeaderBoardPanel extends JFrame {
    private static final long serialVersionUID = 1L;
    private ConnectNFrame connectNFrame;
    private int turnCount;
    private String playerName;
    private int difficultyLevel;

    /**
     * Constructs a LeaderBoardPanel with the specified ConnectNFrame, turn count, player name, and difficulty level.
     * 
     * @param connectNFrame The ConnectNFrame instance
     * @param turnCount The number of turns taken
     * @param playerName The player's name
     * @param difficultyLevel The difficulty level
     */
    public LeaderBoardPanel(ConnectNFrame connectNFrame, int turnCount, String playerName, int difficultyLevel) {
        this.connectNFrame = connectNFrame;
        this.turnCount = turnCount;
        this.playerName = playerName;
        this.difficultyLevel = difficultyLevel;

        setSize(400, 300);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setResizable(false);

        JPanel panel = new JPanel(new BorderLayout());
        JLabel messageLabel = new JLabel("LEADERBOARD");
        messageLabel.setFont(new Font("Arial Rounded MT Bold", Font.PLAIN, 16));
        messageLabel.setHorizontalAlignment(JLabel.CENTER);
        panel.add(messageLabel, BorderLayout.NORTH);

        JPanel leaderboardPanel = new JPanel(new GridLayout(0, 1));

        updateLeaderboard();
        displayLeaderboard(leaderboardPanel);

        panel.add(leaderboardPanel, BorderLayout.CENTER);

        JPanel buttonPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
        JButton playAgainButton = new JButton("Play Again");
        playAgainButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dispose();
                connectNFrame.changeDifficulty(2);
            }
        });
        buttonPanel.add(playAgainButton);

        JButton quitButton = new JButton("Quit");
        quitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }
        });
        buttonPanel.add(quitButton);

        panel.add(buttonPanel, BorderLayout.SOUTH);

        add(panel);
        centerFrameOnScreen();
    }

    private void centerFrameOnScreen() {
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        Dimension frameSize = getSize();
        int x = (screenSize.width - frameSize.width) / 2;
        int y = (screenSize.height - frameSize.height) / 2;
        setLocation(x, y);
    }

    private void updateLeaderboard() {
        try (BufferedReader reader = new BufferedReader(new FileReader("LeaderBoard.txt"))) {
            StringBuilder updatedLeaderboard = new StringBuilder();
            String line;
            boolean updated = false;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(" ");
                if (parts.length >= 3) {
                    String name = parts[0];
                    String mode = parts[1];
                    int turns = Integer.parseInt(parts[2]);
                    int currentDifficultyLevel = getDifficultyLevel(mode);
                    if (turnCount < turns && difficultyLevel == currentDifficultyLevel) {
                        name = playerName;
                        turns = turnCount;
                        updated = true;
                    }
                    updatedLeaderboard.append(name).append(" ").append(mode).append(" ").append(turns).append("\n");
                }
            }
            if (!updated && difficultyLevel == 2 && turnCount < 6) {
                updatedLeaderboard.append(playerName).append(" Medium ").append(turnCount).append("\n");
            }
            try (BufferedWriter writer = new BufferedWriter(new FileWriter("LeaderBoard.txt"))) {
                writer.write(updatedLeaderboard.toString());
            } catch (IOException e) {
                e.printStackTrace();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private int getDifficultyLevel(String difficulty) {
        switch (difficulty.toLowerCase()) {
            case "easy":
                return 1;
            case "medium":
                return 2;
            case "hard":
                return 3;
            default:
                return 0;
        }
    }

    private void displayLeaderboard(JPanel leaderboardPanel) {
        try (BufferedReader reader = new BufferedReader(new FileReader("LeaderBoard.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(" ");
                if (parts.length >= 3) {
                    StringBuilder entryText = new StringBuilder(parts[0] + ": ");
                    for (int i = 1; i < parts.length - 1; i++) {
                        entryText.append(parts[i]).append(" ");
                    }
                    entryText.append(parts[parts.length - 1]);
                    JLabel entryLabel = new JLabel(entryText.toString());
                    leaderboardPanel.add(entryLabel);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
