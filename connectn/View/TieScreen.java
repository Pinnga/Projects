package edu.wm.cs.cs301.connectn.View;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 * Represents the tie screen displayed when the game ends in a tie.
 * It extends JFrame and provides options to play again or quit the game.
 */
public class TieScreen extends JFrame {
    private static final long serialVersionUID = 1L;
    private ConnectNFrame connectNFrame;

    /**
     * Constructs a TieScreen frame with the specified ConnectNFrame.
     * 
     * @param connectNFrame The ConnectNFrame instance
     */
    public TieScreen(ConnectNFrame connectNFrame) {
        this.connectNFrame = connectNFrame;
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setResizable(false);

        JPanel panel = new JPanel(new BorderLayout());
        JLabel messageLabel = new JLabel("YOU TIED!");
        messageLabel.setFont(new Font("Arial Rounded MT Bold", Font.PLAIN, 16));
        messageLabel.setHorizontalAlignment(JLabel.CENTER);
        panel.add(messageLabel, BorderLayout.NORTH);

        JLabel emojiLabel = new JLabel("\uD83D\uDE0E");
        emojiLabel.setFont(new Font(Font.SANS_SERIF, Font.PLAIN, 100));
        emojiLabel.setHorizontalAlignment(JLabel.CENTER);
        panel.add(emojiLabel, BorderLayout.CENTER);
        
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
}
