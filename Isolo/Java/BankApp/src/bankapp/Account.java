
package bankapp;
//import java.util.*;

import java.util.Random;


public class Account {
    
    private final int accNumber;
    private  double balance;
    private  String name;
    private  int Age;
    public Account(String name, int age,double initialBalance){
        Random rand = new Random();
        this.accNumber = rand.nextInt(9000) + 1000;
        
        this.name=name;
        this.Age = age;
        this.balance = initialBalance;
//     accNumber = accNo;   
     if (initialBalance > 0.0)
        balance = initialBalance; 
//     return balance;
    }
    public int getAccountNumber(){
        return this.accNumber;
    }
    
    public double credit(double depositAmount){
        balance = balance + depositAmount;
        return balance;
        
    }
    
    public double getBalance(){
        return balance;
    }
    
    public double withdrawal(double Amount){
        balance = balance - Amount;
        return balance;
    }
    
       
   public  void Display(){
                  
//        
   System.out.println("NAME :"+ this.name);
   System.out.println("AGE :"+ this.Age);
   System.out.println("BALANCE :"+ this.balance);
   System.out.println("ACCOUNT NUMBER :"+ this.accNumber);
   }
            
     }
        
          
        

