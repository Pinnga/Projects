package edu.wm.cs.cs301.connectn.View;

import javax.swing.*;
import java.awt.*;

/**
 * Represents a frame displayed when a column is full.
 * It extends JFrame and displays a message along with an emoji.
 */
public class FullColumn extends JFrame {
    private static final long serialVersionUID = 1L;

    /**
     * Constructs a FullColumn frame with a message indicating that the column is full
     * and an emoji to express the message.
     */
    public FullColumn() {
        setSize(400, 200);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

        JPanel panel = new JPanel(new BorderLayout());

        JLabel messageLabel = new JLabel("Column is full! Please choose another column");
        messageLabel.setFont(new Font("Arial Rounded MT Bold", Font.PLAIN, 16));
        messageLabel.setHorizontalAlignment(JLabel.CENTER);
        panel.add(messageLabel, BorderLayout.CENTER);

        JLabel emojiLabel = new JLabel("\uD83D\uDE41");
        emojiLabel.setFont(new Font(Font.SANS_SERIF, Font.PLAIN, 40));
        emojiLabel.setHorizontalAlignment(JLabel.CENTER);
        panel.add(emojiLabel, BorderLayout.SOUTH);

        add(panel);

        centerFrameOnScreen();
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
}
