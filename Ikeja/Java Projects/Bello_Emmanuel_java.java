/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaclass;
import java.util.Scanner;
import java.util.Random;
        /** mobile applications Android Studio, Spring for Web apps, JavaFX for mobile applications, ReactNative for javaScript to replace Android Studio, works for  Android and IOS
 *
 * @author Funmilola
 */
public class GAme {
    public static void main(String[] args) {
        System.out.println("Welcome to dead and injured.\n"+"You have 12 attempts to try to guess the three numbers coreectly\n"+"Good luck");

int tries = 12; 
int Dead = 0;
int Injured = 0;
int input [] = new int[3];
int[] randy = numberGenerator();
while(tries>0&& Dead!=3){
    int [] Prob = guess();
    Dead = 0;
    Injured = 0;
    for(int x = 0; x<Prob.length; x++){
        if(Prob[x]==randy[x]){
            Dead++;
        }
            else if(Prob[x]==randy[0]||Prob[x]==randy[1]||Prob[x]==randy[2]){
                Injured++;
        }
    }
    if(Dead==3){
        System.out.println("Congratulations. You have guessed the number correctly\n"+"The number is:"+" ");
        for(int x=0;x<Prob.length;x++){
            System.out.print(Prob[x]);
        }
    }
    else {
        tries--;
    }
    if(tries>1){
        System.out.println( "\n"+Dead+ "dead and "+ Injured +" injured\n" + tries + "attempts remaining");
    }
    else if(tries==1){
        System.out.println(Dead + "dead" + Injured + "injured\n Last attempt");
    }
    else{
        System.out.println("Game over\n"+"You have failed to guess the three digit word in 12 attempts");
        System.out.println("The numbers are:");
        for(int x=0;x<randy.length;x++)
            System.out.println(randy[x]);
    }
}
    }
    public static int[] guess(){
        Scanner scan = new Scanner(System.in);
        System.out.println("What is your guess");
        String input = scan.nextLine();
        if(input.length()!=3){
            System.out.println("Invalid guess. You can only enter 3 digits between 0 & 9");
            return guess();                        
            
        }
        int [] Try = new int [3];
        for(int x = 0; x<3; x++){
            Try [x] = Integer.parseInt(String.valueOf(input.charAt(x)));
        }
        return Try;
    }
    
    public static int [] numberGenerator(){
        Random rand = new Random();
        int [] randArray = {10, 10, 10};
        for(int x = 0; x<randArray.length; x++){
            int temp = rand.nextInt(9);
            while(temp==randArray[0]||temp==randArray[1]||temp==randArray[2]){
                temp=rand.nextInt(9);
                
            }
            randArray[x]=temp;
            
        }
        return randArray;
    }
}
//PinCom; nextDouble, nextLine, nextInt all accept input