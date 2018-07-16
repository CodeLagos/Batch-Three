
package project;

import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JTextField;
import java.sql.*;
import static project.project1.Signup;


public class project2 extends JFrame {
    Connection conn= null;
    
    private JTextField Name;
    private JTextField Surname;
    private JTextField Dob;
    private JTextField Gender;
    private JTextField MailAddress;
    private JTextField MaritalStatus;
    private JTextField State;
    private JTextField City;
    
    public static JButton Next;
    public static JButton Previous;
    public static JButton Save;
    
    
    public project2 (){
        Container con= getContentPane ();
        con.setLayout( new BorderLayout());
        
        JPanel pan = new JPanel ();
        JLabel lab = new JLabel ("Application Form");
        pan.add(lab);
        
        JPanel pan1 = new JPanel ();
         JLabel lab1 = new JLabel ("Name");
        JLabel lab2= new JLabel ("Surname");
        JLabel lab3 = new JLabel ("Dob");
        JLabel lab4 = new JLabel ("Gender");
        JLabel lab5 = new JLabel ("MailAddress");
        JLabel lab6 = new JLabel ("MaritalStatus");
        JLabel lab7 = new JLabel ("State");
        JLabel lab8 = new JLabel ("City");
        pan1.setLayout( new GridLayout(8,1,5,3));
        
        Name= new JTextField (10);
        Surname = new JTextField (10);
        Dob = new JTextField(10);
        Gender= new JTextField(10);
        MailAddress= new JTextField (10);
        MaritalStatus = new JTextField (10);
        State = new JTextField(10);
       City = new JTextField(10);
        pan1.add(lab1);
        pan1.add(lab2);
        pan1.add(lab3);
        pan1.add(lab4);
        pan1.add(lab5);
        pan1.add(lab6);
        pan1.add(lab7);
        pan1.add(lab8);
        
        JPanel pan2 = new JPanel();
        pan2.setLayout(new GridLayout(8,1,1,4));
        pan2.add(Name);
        pan2.add(Surname);
        pan2.add(Dob);
        pan2.add(Gender);
        pan2.add(MailAddress);
        pan2.add(MaritalStatus);
        pan2.add(State);
        pan2.add(City);
        
        JPanel pan3 = new JPanel ();
      Save = new JButton("Save");
        Next = new JButton("Next");
        Previous = new JButton("previous");
        pan3.add(Save);
       pan3.add(Next);
        pan3.add(Previous);
        
          
         
    {
    Save.addActionListener ((ActionEvent e)  ->   {
            Statement stmt = null;
            dispose();
            
           try
            {
                Class.forName("com.mysql.jdbc.Driver");
                conn = DriverManager.getConnection("jdbc:mysql://localhost:3306"+"/project","root","");
                System.out.println("connection successful");
                
                String nam=Name.getText();
                String sur= Surname.getText();
                String db= Dob.getText();
                String gen= Gender.getText();
                String mail= MailAddress.getText();
                String mar=MaritalStatus.getText();
                String sta= State.getText();
                String cit= City.getText();
                
                String que;
                que= "insert into project2 (Name,Surname,Dob,Gender,MailAddress,MaritalStatus,State,City)values('"+nam+"','"+sur+"','"+db+"','"+gen+"','"+mail+"','"+mar+"','"+sta+"','"+cit+"')";
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
      
           Previous.addActionListener(new ActionListener ()
    {
    
        @Override
        public void actionPerformed(ActionEvent e)
        {
            project1 frame= new project1 ();
            frame.setVisible(true);
            frame.setLocation(250,100);
            frame.setSize(600,350);
            
        }
    
    }
    
    );
           
             Next.addActionListener(new ActionListener ()
    {
    
        @Override
        public void actionPerformed(ActionEvent e)
        {
            project3 frame= new project3 ();
            frame.setVisible(true);
            frame.setLocation(250,100);
            frame.setSize(600,350);
            
        }
    
    }
    
    );
    
    
    
    
        
        
            con.add(pan,BorderLayout.NORTH);
      con.add(pan1,BorderLayout.WEST);
      con.add(pan2,BorderLayout.CENTER);
      con.add(pan3,BorderLayout.SOUTH);
        }
    
    }
    
    
        
            
        
        
        
        
        
       
        
      
        
        
        
        
        
        
    
    
    
    
    
    
}

