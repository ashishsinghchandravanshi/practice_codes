import java.awt.*;
import java.awt.event.*;

class Mycanvas extends Canvas {
    public Mycanvas() {
        setBackground(Color.white);
        setSize(400, 300);
        setVisible(true);
    }

    public void paint(Graphics g) {
        g.setColor(Color.RED);                   // red circle
        g.fillOval(50,50, 120, 120);

        g.setColor(Color.BLUE);                  // blue rectangle
        g.drawRect(50, 50, 120, 120);
    }
}

public class FrameEx {
    public static void main(String[] args) {
        Frame f = new Frame("hello");
        f.setSize(600, 700);
        f.setLayout(new FlowLayout());

        Mycanvas c = new Mycanvas();
        f.add(c);

        f.add(new Label("this is frame"));
        f.setVisible(true);

        Dialog d = new Dialog(f, "Dialog Box", true);
        d.setSize(400, 400);
        d.setLayout(new FlowLayout());
        d.setBackground(Color.RED);
        d.add(new Label("this is dialog box"));
        d.setVisible(true);
    
   
    }
}