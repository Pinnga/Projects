package edu.wm.cs.cs301.connectn.View;

import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.Font;
import javax.swing.BorderFactory;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JPanel;
import javax.swing.JOptionPane;
import edu.wm.cs.cs301.connectn.Controller.ConnectNController;
import edu.wm.cs.cs301.connectn.Model.ConnectNModel;

/**
 * The ConnectNFrame class represents the main frame of the ConnectN game.
 * It contains the graphical user interface components and handles user input.
 */
public class ConnectNFrame {
    private JFrame frame;
    private JLabel turnLabel;
    private LeaderBoardStart leaderBoardStart;

    /**
     * Constructs a new ConnectNFrame object and initializes the game.
     */
    public ConnectNFrame() {
        this.frame = createAndShowGUI(new ConnectNModel(2));
        displayLeaderBoardStart();
    }

    /**
     * Creates and shows the main GUI of the game.
     * @param model The ConnectNModel object representing the game model.
     * @return The JFrame object representing the main frame of the game.
     */
    public JFrame createAndShowGUI(ConnectNModel model) {
        frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
        frame.setJMenuBar(createMenuBar());
        frame.setResizable(false);
        frame.addWindowListener(new java.awt.event.WindowAdapter() {
            @Override
            public void windowClosing(java.awt.event.WindowEvent windowEvent) {
                shutdown();
            }
        });

        frame.add(createTitlePanel(), BorderLayout.NORTH);

        JPanel gridPanel = new JPanel(new FlowLayout(FlowLayout.CENTER));
        ConnectPanel connectPanel = new ConnectPanel(model,this);
        gridPanel.add(connectPanel);
        frame.add(gridPanel, BorderLayout.CENTER);

        turnLabel = new JLabel("Turn: 0");
        turnLabel.setFont(new Font("Arial Rounded MT Bold", Font.PLAIN, 15));
        frame.add(turnLabel, BorderLayout.SOUTH);
        ConnectNController controller = new ConnectNController(this, connectPanel, model);

        frame.setSize(new Dimension(450, 630));
        frame.setLocationByPlatform(true);
        frame.setVisible(true);
        frame.setLocationRelativeTo(null);
        return frame;
    }

    /**
     * Creates the menu bar for the game.
     * @return The JMenuBar object representing the menu bar.
     */
    private JMenuBar createMenuBar() {
        JMenuBar menuBar = new JMenuBar();
        JMenu diffMenu = new JMenu("Difficulty");

        JMenuItem easyMode = new JMenuItem("Easy");
        easyMode.addActionListener(event -> changeDifficulty(1));
        diffMenu.add(easyMode);

        JMenuItem medMode = new JMenuItem("Medium");
        medMode.addActionListener(event -> changeDifficulty(2));
        diffMenu.add(medMode);

        JMenuItem hardMode = new JMenuItem("Hard");
        hardMode.addActionListener(event -> changeDifficulty(3));
        diffMenu.add(hardMode);
        
        JMenuItem quitItem = new JMenuItem("Quit");
        quitItem.addActionListener(event -> shutdown());
        
        JMenuItem separator = new JMenuItem();
        JMenuItem separator1 = new JMenuItem();
        JMenuItem separator2 = new JMenuItem();
        JMenuItem separator3 = new JMenuItem();
        JMenuItem separator4 = new JMenuItem();
        JMenuItem separator5 = new JMenuItem();
        JMenuItem separator6 = new JMenuItem();
        
        menuBar.add(diffMenu);
        menuBar.add(quitItem);
        menuBar.add(separator);
        menuBar.add(separator1);
        menuBar.add(separator2);
        menuBar.add(separator3);
        menuBar.add(separator4);
        menuBar.add(separator5);
        menuBar.add(separator6);

        return menuBar;
    }

    /**
     * Changes the difficulty level of the game.
     * @param difficulty The new difficulty level (1 = Easy, 2 = Medium, 3 = Hard).
     */
    public void changeDifficulty(int difficulty) {
        frame.dispose();
        if (leaderBoardStart != null) {
            leaderBoardStart.dispose();
        }
        ConnectNModel model = new ConnectNModel(difficulty);
        createAndShowGUI(model);
        displayLeaderBoardStart();
    }

    /**
     * Prompts the user to confirm quitting the game and exits if confirmed.
     */
    public void shutdown() {
        int option = JOptionPane.showConfirmDialog(frame, "Are you sure you want to quit?", "Quit Game", JOptionPane.YES_NO_OPTION);
        if (option == JOptionPane.YES_OPTION) {
            System.exit(0);
        }
    }

    /**
     * Creates the title panel for the game.
     * @return The JPanel object representing the title panel.
     */
    private JPanel createTitlePanel() {
        JPanel panel = new JPanel(new FlowLayout());
        panel.setBorder(BorderFactory.createEmptyBorder(0, 5, 5, 5));
        JLabel label = new JLabel("Connect N");
        label.setFont(new Font("Arial Rounded MT BOLD", Font.BOLD, 24));
        panel.add(label);
        return panel;
    }
    
    /**
     * Displays the leader board start screen.
     */
    private void displayLeaderBoardStart() {
        leaderBoardStart = new LeaderBoardStart();
        leaderBoardStart.setVisible(true);
    }

    /**
     * Updates the turn label with the current turn count.
     * @param turnCount The current turn count.
     */
    public void updateTurnLabel(int turnCount) {
        turnLabel.setText("Turn: " + turnCount);
    }
}
