
package project;
import java.sql.*;
import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
//import static java.lang.ProcessBuilder.Redirect.to;
import javax.swing.Icon;
import javax.swing.ImageIcon;
import javax.swing.JButton;
//import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JTextField;
//import static project.project2.Save;

class project1 extends JFrame {
    Connection conn = null;
    
     public static JButton Signup;
    public static JButton Signin;
    public static JButton Clear;
    public JLabel Desert;
    
    private JTextField CardNumber;
    private JPasswordField Pin;
    
    
    public project1 (){
        //super("welcome");
      Container con = getContentPane();
        con.setLayout(new BorderLayout());
        
        JPanel pan= new JPanel ();
        JLabel lab = new JLabel ("Welcome to ATM");
        pan.add(lab);
        
        JPanel pan1 = new JPanel();
         pan1.setLayout( new GridLayout(8,1,5,3));
        JLabel lab1= new JLabel("Card Number");
        JLabel lab2= new JLabel("Pin:");
       CardNumber= new JTextField (10);
       Pin = new JPasswordField (10);
       pan1.add(lab1);
        pan1.add(CardNumber);
        pan1.add(lab2);
          pan1.add(Pin);
        
       
       
         JPanel pan2= new JPanel ();
        Icon picture= new ImageIcon(getClass().getResource("Desert.jpg"));
      JLabel Desert = new JLabel(picture);
       pan2.add(Desert);
       
       JPanel pan3 = new JPanel ();
        pan3.setLayout( new FlowLayout ());
       Signup = new JButton ("Signup");
        Signin = new JButton ("Signin");
        Clear= new JButton("Clear");
        pan3.add(Signin);
        pan3.add(Signup);
        pan3.add(Clear);
        
        
        
        
           Signup.addActionListener(new ActionListener ()
    {
    
        @Override
        public void actionPerformed(ActionEvent e)
        {
            project2 frame= new project2 ();
            frame.setVisible(true);
            frame.setLocation(250,100);
            frame.setSize(600,350);
            
        }
    
    }
    
    );
           
                   Signin.addActionListener(new ActionListener ()
    {
    
        @Override
        public void actionPerformed(ActionEvent e)
        {
            signin frame= new signin ();
            frame.setVisible(true);
            frame.setLocation(480,0);
            frame.setSize(300,350);
             
            
        }
    
    }
    
    );
        
        
        
        
        
        con.add(pan,BorderLayout.NORTH);
        con.add(pan1,BorderLayout.WEST);
       con.add(pan2,BorderLayout.CENTER);
        con.add(pan3,BorderLayout.SOUTH);
        
        
        
        
        
        
        
        
    
}
}
