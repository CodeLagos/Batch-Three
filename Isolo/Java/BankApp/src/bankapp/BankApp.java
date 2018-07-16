
/**
 * A SIMPLE BANKING APPLICATION THAT ALLOWS USER TO REGISTER, MAKE DEPOSIT, 
 * WITHDRAW FROM THE ACCOUNT AND CHECK ACCOUNT BALANCE
 * A PROGRAM WRITTEN BY ABOGUNRIN ABAYOMI O
 * E-MAIL:PROPHETHUG2000@GMAIL.COM
 * CODE LAGOS BATCH 3
 * JAVA CLASS
 */
package bankapp;

import java.util.*;


public class BankApp {
    private static double amount;
    public static ArrayList<Account>accountList = new ArrayList<>();
    private static boolean flag = false;
          
    public static void Instruction(){
         System.out.println("WELCOME TO OUR ONLINE BANKING APPLICATION");
        System.out.println("--------------------------------");
        System.out.println("1. CASH WITHDRAWAL");
        System.out.println("2. CASH DEPOSIT");
        System.out.println("3. ACCOUNT BALANCE");
        System.out.println("0. EXIT");
        System.out.println("---------------------------------");
        System.out.println("Please make a choice for the operation you want to perform:");
            
    }
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Scanner scan = new Scanner(System.in);
        System.out.println("WELCOME!!");
        System.out.println("New user, press 1");
        System.out.println("Existing user, press 2");
        int val = input.nextInt();
        if (val == 1){
        //int bal = 0;
        //Account account = null;
            System.out.println("Please enter your name");
            String name = input.next();
            System.out.println("Please enter your age");
            int age = input.nextInt();
            System.out.println("Please enter initial Deposit");
            double balance = input.nextDouble();
            Account newUser = new Account(name,age,balance);
            System.out.printf("Welcome %s %s %d: " , name,"Your Accoun Number: ", newUser.getAccountNumber());
            accountList.add(newUser);
            System.out.println("Please press 7 to continue..");
                int v = input.nextInt();
                if (v == 7){
                    Instruction();
           }
                else 
                    System.out.println("Invalid entry! Please choose 7 to continue");
                }
            else {
                      Instruction();
                }  
        System.out.println("Your choice:");
        int choice = input.nextInt();
        
        
    while (true){
            
        switch (choice) {
            
            case 1:
                //withdraw amount
                System.out.println("Please enter you account number");
                int accountToWithdraw = input.nextInt();
                System.out.print("Please enter the amount to withdraw: ");
                amount = scan.nextDouble();
                for (Account acc : accountList){
                    if(acc.getAccountNumber() == accountToWithdraw){
                        
                        System.out.println("Amount: #" + "" + acc.withdrawal(amount) );
                    }
                    Instruction();
                    choice = input.nextInt();
                }
                break;         
            case 2:
                //deposit module
                 //withdraw amount
                System.out.println("Please enter you account number");
                int accountToDeposit = input.nextInt();
                System.out.print("Please enter the amount to withdraw: ");
                amount = scan.nextDouble();
                for (Account acc : accountList){
                    if(acc.getAccountNumber() == accountToDeposit){
                        acc.credit(amount);
                         System.out.println("You current balance is #" + acc.credit(amount));
                    }
                    Instruction();
                    choice = input.nextInt();
                }
                break;
            case 3:
                 //Get Balance
                System.out.println("Please enter you account number");
                int accountToEnquire = input.nextInt();
                for (Account acc : accountList){
                    if(acc.getAccountNumber() == accountToEnquire){
                       System.out.println("BALANCE :"+acc.getBalance());
                       break;
                    }
                    Instruction();
                    choice = input.nextInt();
                }
                break;      
            case 0:               
                System.out.println("--------------------------------------");
                System.out.println("THANK YOU FOR BANKING WITH US\nDo have a nice day and Please Call again");
                System.out.println("If you have any complaints or comments, please call our helpdesk on +2348131061431 or email us at prophethug2000@gmail.com");
                System.out.println("---------------------------------------");
                input.close();
                System.exit(0);
                break;
            default:
                System.out.println("INVALID!!!");
                }
             }
        }
}

        
        
    

      
    
        

            


