/**
 * CALCULATOR APPLICATION FOR ADDITION, SUBTRACTION, MULTIPLICATION, DIVISION, AND MODULOS.
 * MUHAMMED-MUSTAPHA APETE
 * APETE.MUHDMUSTAPHA@GMAIL.COM
 * CODELAGOS BATCH 3.0
 * 
*/

package calculator;


import java.util.*;

public class Calculator {

    public static void Add(int no1, int no2){
    float answer = no1 + no2;
    System.out.println("The addittion of the numbers is:" + answer);
}
    public static void Sub(int no1, int no2){
    float answer = no1 - no2;
    System.out.println("The subtraction of the numbers is:" + answer);
}
    public static void Multiply(int no1, int no2){
    float answer = no1 * no2;
    System.out.println("The Multiplication of the numbers is:" + answer);
    }
    public static void Division(int no1, int no2){
    float answer = no1 / no2;
    System.out.println("The Division of the numbers is:" + answer);
    }
    public static void Mod(int no1, int no2){
    float answer = no1 % no2;
    System.out.println("The Modulus / integer division of the numbers is:" + answer);
    }
    public static void Recieve(){
        Scanner input = new Scanner (System.in);
        while (true){
        System.out.print("WELCOME TO MY CALCULATOR APPLICATION\n");
        System.out.print("--------------------------------------------\n");
        System.out.println("1. ADDITTION");
        System.out.println("2. SUBTRACTION");
        System.out.println("3. MULTIPLICATION");
        System.out.println("4. DIVISION");
        System.out.println("5. INTEGER/MODULUS");
//        System.out.println("6. EXIT");
        System.out.print("--------------------------------------------\n");
        System.out.print("Please choose the action you want to perform by entering the corresponding number:");
        int choice = input.nextInt();
        System.out.print("Please input the first number to compute:");
        int no1 = input.nextInt();
        System.out.print("Please input the second number to compute:");
        int no2 = input.nextInt();
        switch (choice){
            case 1:
                Add(no1,no2);
                break;
            case 2:
            
                Sub(no1,no2);
                break;
            case 3:
             
                 Multiply(no1,no2);
                break;
            case 4:
              
                  Division(no1,no2);
                  break;
            case 5:
                  Mod(no1, no2);
                  break;
         
                       
            default:
                System.exit(0);
                input.close();
//        
        }
    }
    }
        
    public static void main(String[] args) {
        
        Recieve();
        
        
               
        
       
    } 
}
