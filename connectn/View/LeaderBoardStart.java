package edu.wm.cs.cs301.connectn.View;

import javax.swing.*;
import java.awt.*;
import java.io.*;

/**
 * Represents the starting point for the leaderboard display.
 * It extends JFrame and contains methods to display the leaderboard.
 */
public class LeaderBoardStart extends JFrame {
    private static final long serialVersionUID = 1L;

    /**
     * Constructs a LeaderBoardStart frame to display the leaderboard.
     */
    public LeaderBoardStart() {
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setResizable(false);

        JPanel panel = new JPanel(new BorderLayout());
        JLabel messageLabel = new JLabel("LEADERBOARD");
        messageLabel.setFont(new Font("Arial Rounded MT Bold", Font.PLAIN, 16));
        messageLabel.setHorizontalAlignment(JLabel.CENTER);
        panel.add(messageLabel, BorderLayout.NORTH);

        JPanel leaderboardPanel = new JPanel(new GridLayout(0, 1));
        displayLeaderboard(leaderboardPanel);
        panel.add(leaderboardPanel, BorderLayout.CENTER);

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
