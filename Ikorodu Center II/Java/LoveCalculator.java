/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package love.calculator;


import java.util.Scanner;
/**
 *
 * @author olatunde
 */
/**
 * 
 * Name:Oladunjoye Sinat 
 */
/**
 * 
 * Course: Java Programming
 */
/**
 * 
 * Project name: Love Calculator 
 */
/**
 * 
 * Email address: taojoye@gmail.com 
 */
//      This application is a love calculator. It is used to calculate how compatible two lovers can be.
//      
public class LoveCalculator {
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        sinat();
        // TODO code application logic here
    }
        public static void sinat(){
        Scanner Love = new Scanner(System.in);
        
        System.out.println("What is your name: ");
        String your_name = Love.nextLine();
        int number = your_name.length();
        
        System.out.println("What is your partner's name: ");
        String partner_name = Love.nextLine();
        int number2 =partner_name.length();
        
        if((number>=3 && number<=6) && (number2>=17 && number2<=20)){
        System.out.println("Romantic");}
        
        else if((number>=7 && number<=10) && (number2>=13 && number2<=16) ){
        System.out.println("Compatible");}
        
        else if((number>=11 && number<=14) && (number2>=9 && number2<=12)){
        System.out.println("Incompatible");}
        
        else if((number>=15 && number<=20) && (number2>=3 && number2<=8)){
        System.out.println("Lovely");}
        else{
             System.out.println("Unhappy couples");
        
//          Create an object called Love inside a class called Scanner. 
//          Collect input from the user(you).
//          Ask the user to input his or her name.
//          Collect input from the user for length. 
//          Print the user's name(you).
//          Collect input from the other user(partner).
//          Collect input from the user for length2. 
//          Ask the partner to input his or her name.
//          Print the partner's name.
//          Create a variable to store the length of the name.
//          Print out the result of the value store.
    }
    }
    
}
