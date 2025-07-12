import javax.swing.*;
import java.awt.event.*;

public class JTextFieldExample {
    public static void main(String[] args) {
        JFrame f = new JFrame("JTextField Example");

        JLabel label = new JLabel("Enter name:");
        label.setBounds(30, 30, 100, 30);

        JTextField textField = new JTextField();
        textField.setBounds(130, 30, 100, 30);

        JButton button = new JButton("Submit");
        button.setBounds(130, 70, 100, 30);

        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String name = textField.getText();
                JOptionPane.showMessageDialog(f, "Hello " + name);
            }
        });

        f.add(label);
        f.add(textField);
        f.add(button);

        f.setSize(300, 200);
        f.setLayout(null);
        f.setVisible(true);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
