
package project;

import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.GridLayout;
import javax.swing.ButtonGroup;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JRadioButton;
import javax.swing.JTextField;

public class project3 extends JFrame{
    
    private JTextField CardNumber;
    private JPasswordField Pin;
     private ButtonGroup Abiola;//the buttongrp see all the buttons as one
    private JRadioButton SavingsAccount;//PB stands for Plain RadioButton
    private JRadioButton FixedDepositAccount;//BB stands for Bold RadioButton
    private JRadioButton CurrentAccount;// IB stands for Italics RadioButton
    private JRadioButton ExistingAccount;
    private JRadioButton AtmCard;
    private JRadioButton InternetBanking;
    private JRadioButton Email;
    private JRadioButton sms;
    
    
    
    public project3 (){
        
         Container con= getContentPane ();
        con.setLayout( new BorderLayout());
        
        JPanel pan = new JPanel();
        JLabel lab = new JLabel ("Account Type");
         pan.setLayout(new GridLayout(8,1,1,4));
        
        JRadioButton button1 = new JRadioButton("SavingsAccount");
        JRadioButton button2= new JRadioButton("FIxedDepositAccount");
        JRadioButton button3 = new JRadioButton("CurrentAccount");
        JRadioButton button4 = new JRadioButton("ExistingAccount");
        pan.add(lab);
        pan.add(button1);
        pan.add(button2);
        pan.add(button3);
        pan.add(button4);
        
        JPanel pan1= new JPanel ();
        pan1.setLayout( new GridLayout(8,1,5,3));
        JLabel lab1 = new JLabel ("Card Number");
        CardNumber = new JTextField (10);
        JLabel lab2 = new JLabel ("Pin");
       Pin = new JPasswordField(10);
        pan1.add(lab1);
        pan1.add(CardNumber);
        pan1.add(lab2);
        pan1.add(Pin);
        
        
        JPanel pan3= new JPanel ();
         pan3.setLayout(new GridLayout(8,1,1,4));
        JLabel lab4 = new JLabel ("Services Required");
        JRadioButton button5= new JRadioButton("AtmCard");
        JRadioButton button6 = new JRadioButton("InternetBanking");
        JRadioButton button7 = new JRadioButton("Email");
        JRadioButton button8 = new JRadioButton ("sms");
        pan3.add(lab4);
        pan3.add(button5);
        pan3.add(button6);
        pan3.add(button7);
        pan3.add(button8);
        
      con.add(pan,BorderLayout.NORTH);
      con.add(pan1,BorderLayout.WEST);
      con.add(pan3,BorderLayout.SOUTH);
        
        
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
          
    
        
        
        
        
        
        
    }
    
    
    
}
