/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* @Author: HUNSU MICHAEL O
*  Class: JAVA PROGRAMMING
*  Centre: CODE LAGOS, IKORODU CENTRE 2 - IGBOGBO
*  Sex: MALE
*/

/* Project Mini Accountant is an offline Application 
*  that allows the user to perform several banking activities from wherever they are. 
*  There are several features available on the application such as Account Opening, Deposit and Withdrawal,
*  checking of account balance, and account details.
*  The First option is Opening an Account, here the user is presented with a form,
*  where the user enters all the Bio data and it is automatically stored in a reserved location.
*  The application generates an account number which will serve as the user password to access
*  all other informations on the application.
*  To deposit, the user is asked to enter his account number, after which the dashboard is opened, then, 
*  he enters the amount of money to be deposited, and it will automatically reflect in the account.
*  To withdraw, the user is asked to enter his account number, after which the dashboard is opened, then, 
*  he enters the amount of money to be withdrawn, and it will automatically reflect in the account.
*  Also, f the user wants to check his account balance, He enters his account number and the account 
*  balance is displayed on the screen.
*  Lastly, if the user wants to view his account details, he enters account details option, 
*  then view the account details by entering his account number.
*  In Conclusion, it is a temporary alternative way of banking from home or anywhere in the world. 
*  It is still a work in progress.................................. 
*/

package miniaccountant;

import java.util.InputMismatchException;
import java.util.Date;
import java.util.Scanner;

// Create a Class named Account
class Account{
    String account_name, account_type;
    int account_number, account_balance;
    long verification_number;
    
    // Create a Method named Account
    Account(String acc_name, String acc_type, int acc_num, long ver_number, int acc_bal ){ 
// Store the Variables in the Method Account
        account_name=acc_name;
        account_type=acc_type;
        account_number=acc_num;
        verification_number=ver_number;
        account_balance=acc_bal; 
    }
    
    void account_details() { //Create a Method for Account Details
        System.out.println("Account Name :" + account_name);
        System.out.println("Account Type :" + account_type);
        System.out.println("Account Number :" + account_number);
        System.out.println("Verification Number: :" + verification_number);
        System.out.println("Account Balance :" + account_balance);
    }
    
    void insert(String acc_name, String acc_type, int acc_num, long ver_number, int acc_bal) { 
// Create a Method that Inserts Account Details
        account_name=acc_name;
        account_type=acc_type;
        account_number=acc_num;
        verification_number=ver_number;
        account_balance=acc_bal;
    }
}
public class MiniAccountant  {
    static void throwOne() throws InputMismatchException {
    System.out.println("");
    throw new InputMismatchException("");
}

    public static void main(String[] args) throws InputMismatchException {
        
        try{
        Scanner inputIntg = new Scanner(System.in); //Create Scanner for Integer Variables
        Scanner inputStr = new Scanner(System.in); //Create Scanner for String Variables
        
        Date today = new Date();
        // Declare all the Variables to be Used
        
        String acc_name, acc_type;
        String state, sex, address;
        String phone_number, marital;
        int acc_bal=0;
        int amount;
        int tempacc;
        int withdraw;
        int loan;
        int accountOption;
        
        
        int acc_num = (int) ((Math.random()*9999)); // Generate a Random Account Number
        long ver_number = (long) ((Math.random()*9999999990L));// Generate a Random Verification Number
        boolean quit = false; //Expression to Quit the Application
        
        Account user = new Account("user_name" ,"current", 0, 0, 0); // Create an Object 'user' in the Class 'Account'
        
        System.out.println("Welcome To CodeLagos Int'l Bank, Plc \n If You Would Like\n");
        
        do { //Using do a Conditional Statement to Display the Account Options
            System.out.println("1. To Open an Account, Press 1");
            System.out.println("2. To Deposit, Press 2");
            System.out.println("3. To Withdraw, Press 3");
            System.out.println("4. To Take A Loan, Press 4");
            System.out.println("5. To Check Balance, Press 5");
            System.out.println("6. To Display Account Details, Press 6");
            System.out.println("0. To Quit, Press 0 \n");
            
            System.out.print("Enter An Account Option : ");
            accountOption = inputIntg.nextInt();
             
            switch(accountOption) { 
                //Using a Switch Statement to Operate each Account Option
            case 1: //To Create an Account
                    System.out.print("Full Name : ");
                    acc_name = inputStr.nextLine();
                    
                    System.out.print("Type of Account : ");
                    acc_type = inputStr.nextLine();
                    
                    System.out.print("Marital Status : ");
                    marital = inputStr.nextLine();
                    
                    System.out.print("Sex : ");
                    sex = inputStr.nextLine();
                    
                    System.out.print("State of Origin : ");
                    state = inputStr.nextLine();
                    
                    System.out.print("Phone Number : ");
                    phone_number = inputStr.nextLine();
                    
                    System.out.print("Residential Address : ");
                    address = inputStr.nextLine();
                    
                    user.insert(acc_name, acc_type, acc_num, ver_number, acc_bal);
                    System.out.println("\n YOUR ACCOUNT DETAILS");
                    
                    user.account_details();
                    System.out.println("\n**Don't Forget Your Account Number**"); break;
            
            case 2: //To Deposit Any Amount of Money
                    System.out.print("Enter your Account Number : ");
                    tempacc = inputIntg.nextInt();
     
                    if (tempacc==user.account_number) {
                        System.out.print("To Deposit, Enter Amount : ");
                        amount = inputIntg.nextInt();
                        
                        user.account_balance = user.account_balance+amount;
                        System.out.println("\n Cash Deposited Successfully . Your Current Balance is : " + (user.account_balance));
                    }
                    else
                        System.out.println("Wrong Account Number, Try Again!"); break;
                        
            case 3: // To Withdraw Any Amount of Money
                    System.out.print("Enter your Account Number : ");
                    tempacc = inputIntg.nextInt();
                    
                    if (tempacc==user.account_number) {
                        if(user.account_balance==0)
                            System.out.print("Your Account is Empty.");
                        else{
                            System.out.print("To Withdraw, Enter Amount : ");
                            withdraw = inputIntg.nextInt();
                            
                            if(withdraw>user.account_balance) {
                                System.out.print("Enter Valid Amount of Money : ");
                                withdraw = inputIntg.nextInt();
                            }
                            else{
                            user.account_balance = user.account_balance - withdraw;
                            System.out.println("\n Cash Withdrawal Successful. Your Current Balance is : " + user.account_balance);
                                }
                            }
                        }
                    else 
                        System.out.println("Wrong Account Number, Try Again!"); break;
                        
            case 4: // To Take A Loan
                    System.out.print("Enter your Account Number : ");
                    tempacc = inputIntg.nextInt();
                    
                    if (tempacc==user.account_number) {
                        System.out.print("To Take A Loan, Enter Amount : ");
                        loan = inputIntg.nextInt();
                        
                        user.account_balance = user.account_balance - loan;
                        System.out.println("\n Loan Successful . Your Current Balance is : " + (user.account_balance));
                    }
                    else
                        System.out.println("Wrong Account Number, Try Again!"); break;
            
            case 5: //To Check Current Balance
                    System.out.print("Enter your Account Number : ");
                    tempacc = inputIntg.nextInt();
                    
                    if(tempacc==user.account_number) {
                        System.out.println("\n Your Current Balance is : "+ user.account_balance);
                    }
                    else
                        System.out.println("Wrong Account Number, Try Again!"); break;
            
            case 6: //To Display Account Details
                    System.out.print("Enter your Account Number : ");
                    tempacc = inputIntg.nextInt();
                    
                    if(tempacc==user.account_number) {
                        System.out.println("\n YOUR ACCOUNT DETAILS");
                        user.account_details();
                    }
                    else
                        System.out.println("Wrong Account Number, Try Again!"); break;
            
            case 0: //To Quit the Application
                    quit = true; break;
            default:
                    System.out.println("Wrong Option."); break;
            }
            System.out.print("\n");
           
        }
        while(!quit);
     
        System.out.println("Thank You for Banking With Us"); //End of Program
        System.out.println(today); // To Display Current Date and Time
        
    }catch(InputMismatchException e) { // Handle InputMismatchExceptions
                System.out.println("Your Input Should be A Digit e.g. 1,2,...");
                }
        
    } 
}