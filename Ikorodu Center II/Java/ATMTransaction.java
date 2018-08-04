/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package atmtransaction;

import java.util.Scanner;

/**
 *
 * @author HP
 */
public class ATMTransaction {

    public static void main(String args[]){ 

        int balance = 0; 
        int withdraw = 0;
        int borrow = 0;
        int deposit = 0;

        Scanner s = new Scanner(System.in);

        while (true) {
            System.out.println("Automated Teller Machine");
            System.out.println("Choose 1 for Withdraw");
            System.out.println("Choose 2 for Deposit");
            System.out.println("Choose 3 for Check Balance");
            System.out.println("Choose 4 for Borrow ");
            System.out.println("Choose 5 for EXIT");
            System.out.print("Choose the operation you want to perform:");
            int n = s.nextInt();
            switch (n){
                case 1:
                    System.out.print("Enter money to be withdrawn: ");
                    withdraw = s.nextInt();
                    if (balance >= withdraw) {
                        balance = balance - withdraw;
                        System.out.println("Please collect your money");
                    }else{
                        System.out.println("Insufficient Balance");
                    }
                    System.out.println("");
                    break;
                case 2:
                    System.out.print("Enter money to be deposited: ");
                    deposit = s.nextInt();
                    balance = balance + deposit;
                    System.out.println("Your Money has been successfully depsited");
                    System.out.println("");
                    break;
                case 3:
                    System.out.println("Balance : " + balance);
                    System.out.println("");
                    break;
                case 4:
                    System.out.print("Enter the amount you want to borrow: ");
                    borrow = s.nextInt();
                    if(balance <=20000)
                     {
                        System.out.println("Your loan has been granted");
                    }else{
                        System.out.println("Your loan cannot be granted");
                            }
                    break;
                case 5:
                    System.exit(0);
            }
        }
    }
}
