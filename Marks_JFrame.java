import javax.swing.*;
import java.awt.*;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class MarksApp {
    public static void main(String[] args) {
        // Create and set up the window (JFrame)
        JFrame frame = new JFrame("Student Marks Application");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 600);
        frame.setLayout(new GridLayout(9, 2, 10, 10));

        // Create components (labels, text fields, buttons)
        JLabel nameLabel = new JLabel("Enter Student Name:");
        JTextField nameField = new JTextField();
        
        JLabel rollNoLabel = new JLabel("Enter Roll No.:");
        JTextField rollNoField = new JTextField();

        JLabel englishLabel = new JLabel("Enter Marks for English:");
        JTextField englishField = new JTextField();

        JLabel hindiLabel = new JLabel("Enter Marks for Hindi:");
        JTextField hindiField = new JTextField();

        JLabel mathLabel = new JLabel("Enter Marks for Math:");
        JTextField mathField = new JTextField();

        JLabel physicsLabel = new JLabel("Enter Marks for Physics:");
        JTextField physicsField = new JTextField();

        JButton submitButton = new JButton("Submit");

        // Text area to display results
        JTextArea resultArea = new JTextArea(5, 20);
        resultArea.setEditable(false);

        // Add components to the frame
        frame.add(nameLabel);
        frame.add(nameField);

        frame.add(rollNoLabel);
        frame.add(rollNoField);

        frame.add(englishLabel);
        frame.add(englishField);

        frame.add(hindiLabel);
        frame.add(hindiField);

        frame.add(mathLabel);
        frame.add(mathField);

        frame.add(physicsLabel);
        frame.add(physicsField);

        frame.add(submitButton);
        
        frame.add(new JLabel("Results:"));
        frame.add(new JScrollPane(resultArea));

        // Action to be taken when the user clicks "Submit"
        submitButton.addActionListener(e -> {
            try {
                // Get data from input fields
                String name = nameField.getText();
                int rollNo = Integer.parseInt(rollNoField.getText());
                float englishMarks = Float.parseFloat(englishField.getText());
                float hindiMarks = Float.parseFloat(hindiField.getText());
                float mathMarks = Float.parseFloat(mathField.getText());
                float physicsMarks = Float.parseFloat(physicsField.getText());

                // Calculate total marks and percentage
                float totalMarks = englishMarks + hindiMarks + mathMarks + physicsMarks;
                float percentage = (totalMarks / 400) * 100;

                // Display the results in the JTextArea
                resultArea.setText("Total Marks: " + totalMarks + "\n" +
                        "Percentage: " + percentage + "%\n");

                // Append the results to a file
                appendToFile(name, rollNo, englishMarks, hindiMarks, mathMarks, physicsMarks, totalMarks, percentage);

            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(frame, "Please enter valid numeric values.");
            }
        });

        // Show the frame
        frame.setVisible(true);
    }

    private static void appendToFile(String name, int rollNo, float englishMarks, float hindiMarks, 
                                     float mathMarks, float physicsMarks, float totalMarks, float percentage) {
        try {
            // Specify the file path (make sure the directory exists)
            FileWriter writer = new FileWriter(new File("D:/Java/student_marks.txt"), true);

            // Write student details and results to the file
            writer.write("Student Name: " + name + "\n");
            writer.write("Roll No: " + rollNo + "\n");
            writer.write("Marks in English: " + englishMarks + "\n");
            writer.write("Marks in Hindi: " + hindiMarks + "\n");
            writer.write("Marks in Math: " + mathMarks + "\n");
            writer.write("Marks in Physics: " + physicsMarks + "\n");
            writer.write("Total Marks: " + totalMarks + "\n");
            writer.write("Total Percentage: " + percentage + "%\n");
            writer.write("--------------------------------------\n");

            // Close the writer
            writer.close();

        } catch (IOException ex) {
            JOptionPane.showMessageDialog(null, "Error occurred while writing to file.");
            ex.printStackTrace();
        }
    }
}
