
package project;
import java.sql.*;
import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JTextField;
import static project.project1.Signin;
//import static project.project1.Signup;

public class signin extends JFrame {
    Connection conn = null;
    //public static JButton Username;
    public static JButton Enter;
    private JTextField Username;
    private JPasswordField Password;
    
    
    public signin (){
        super("welcome");
      Container con = getContentPane();
        con.setLayout(new BorderLayout());
        
       JPanel pan1 = new JPanel();
         pan1.setLayout( new GridLayout(8,1,5,3));
        JLabel lab1= new JLabel("Username");
        JLabel lab2= new JLabel("Password:");
       Username= new JTextField (10);
       Password= new JPasswordField (10);
       pan1.add(lab1);
        pan1.add(Username);
        pan1.add(lab2);
          pan1.add(Password);
          
          JPanel pan2 = new JPanel ();
        pan2.setLayout( new FlowLayout ());
        Enter = new JButton ("ENTER");
        pan2.add(Enter);
        
        Enter.addActionListener ((ActionEvent e)  ->   {
            Statement stmt = null;
            dispose();
            
           try
            {
                Class.forName("com.mysql.jdbc.Driver");
                conn = DriverManager.getConnection("jdbc:mysql://localhost:3306"+"/project","root","");
                System.out.println("connection successful");
                
                String User=Username.getText();
                String Pass= Password.getText();
                
                
                String que;
                que= "insert into sign in (Username,Password)values('"+User+"','"+Pass+"')";
                Statement st = conn.createStatement();
                int y1=st.executeUpdate(que);
                if (y1 >1){
                    JOptionPane.showMessageDialog(null, "insertion successful");
                }
                System.out.println("the data has been added");
                }
            catch (ClassNotFoundException | SQLException es )
                
            {
                System.out.println(es.getMessage());
            }  
            });
        
        
           //Enter.addActionListener(new ActionListener ()
   // {
    
       // @Override
        //public void actionPerformed(ActionEvent e)
        {
            //Transaction frame= new Transaction ();
            //frame.setVisible(true);
           // frame.setLocation(250,100);
            //frame.setSize(600,350);
            
        }
    
   // }
    
    //);
        
          
          con.add(pan1,BorderLayout.WEST);
          con.add(pan2,BorderLayout.SOUTH);
          
        
        
    }
    
}
