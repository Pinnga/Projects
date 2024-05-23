package edu.wm.cs.cs301.connectn;

import edu.wm.cs.cs301.connectn.View.*;

/**
 * The main class for the ConnectN game.
 */
public class Main {

    /**
     * The main method that starts the game.
     * It displays the instructions and initializes the game frame.
     *
     * @param args Command-line arguments (not used)
     */
    public static void main(String[] args) {
        showInstructions();
        new ConnectNFrame();
    }

    /**
     * Displays the instructions dialog.
     */
    public static void showInstructions() {
        InstructionsDialog instructionsDialog = new InstructionsDialog(null);
        instructionsDialog.setVisible(true);
    }
}
