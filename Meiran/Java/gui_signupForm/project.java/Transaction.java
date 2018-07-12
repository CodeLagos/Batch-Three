
 
package project;
import javax.swing.ButtonGroup; //to help import Buttons
import java.awt.BorderLayout; //to help with the borderlayout
import java.awt.Container; //to help create container for the App.
import java.awt.FlowLayout;
import java.awt.GridLayout;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JTextField;

//class transaction extending the JfrAME CLASS
public class Transaction  extends JFrame{
    private JTextField Deposit;
    private JTextField Withdrawal;
    private JTextField FastCash;
    private JTextField Ministatement;
    private JTextField PinChange;
    private JTextField BalanceEnquiry;
   
    
    
    public Transaction (){
        super("Welcome");
        Container con= getContentPane ();
        con.setLayout( new BorderLayout());
        
        JPanel pan = new JPanel();
        JLabel lab1 = new JLabel ("Deposit");
        JLabel lab2= new JLabel ("Withdrawal");
        
      pan.setLayout( new FlowLayout ());
        Deposit= new JTextField (10);
        Withdrawal = new JTextField (10);
        
        pan.add(lab1);
        pan.add(Deposit);
        pan.add(lab2);
        pan.add(Withdrawal);
       
       JPanel pan1 = new JPanel();
        JLabel lab3 = new JLabel ("Fast Cash");
        JLabel lab4 = new JLabel ("Mini statement");
        pan.setLayout( new FlowLayout ());
        FastCash= new JTextField (10);
        Ministatement = new JTextField (10);
       pan1.add(lab3);
        pan1.add(FastCash);
        pan1.add(lab4);
        pan1.add(Ministatement);
        
         JPanel pan2 = new JPanel();
        JLabel lab5= new JLabel ("Pin Change");
        JLabel lab6 = new JLabel ("Balance Enquiry");
        pan.setLayout( new FlowLayout ());
        PinChange = new JTextField (10);
        BalanceEnquiry = new JTextField (10);
        pan2.add(lab5);
        pan2.add(PinChange);
        pan2.add(lab6);
        pan2.add(BalanceEnquiry);
        
        JPanel pan3 = new JPanel ();
        JLabel lab7 = new JLabel ("Please Select Your Transaction");
        pan3.add(lab7);
        
        
        con.add(pan,BorderLayout.WEST);
        con.add(pan1,BorderLayout.WEST);
        con.add(pan2,BorderLayout.SOUTH);
        con.add(pan3,BorderLayout.NORTH);
        
        
        
        
        
    }
            
    
    
}
