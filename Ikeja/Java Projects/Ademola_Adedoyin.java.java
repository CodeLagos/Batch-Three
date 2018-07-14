/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author BEAST
 */
import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;
import javax.swing.JOptionPane;

public class practical 

        
{
    public static void main(String[] args) 
    {
        
  JOptionPane.showMessageDialog(null, "Welcome to Dead and Injured");
      boolean tryAgain =true;
      while (tryAgain == true)
      {
     
    System.out.println("Welcome to Dead and Injured");
    int[] random=numberGenerator();
       int option;
        int maxTry=3;
        int z = maxTry;
        int indexMatch=0;
        int match=0;
        while(maxTry>0 && indexMatch!=4)
        {
            int[] guess=getGuess();
            indexMatch=0;
            match=0;
            for(int i=0;i<guess.length;i++)
            {
                if(guess[i]==random[i]){
                    indexMatch++;
                }
                else if(guess[i]==random[0] || guess[i]==random[1] || guess[i]==random[2] || guess[i]==random[3])
                {
                    match++;
                }
            }
            if(indexMatch==4){
                System.out.print("Well done! Your guess is Correct! The number is: ");
                for(int i=0;i<guess.length;i++)
                {
                    System.out.print(guess[i]);
                }
            }
            else{
                maxTry--;
                if(maxTry>1)
                {
                    System.out.println("You have  "+indexMatch+" DEAD,"+
                    " and "+match+" INJURED. \n"+maxTry+" attempt remaining.");
                }
                else if(maxTry==1)
                {
                    System.out.println("You have  "+indexMatch+" DEAD,"+
                    " and "+match+" INJURED. \nLast attempt!. Good luck");
                }
                else{
                    System.out.println("Sorry, you failed to guess the number in " + z +" attempts.");
                    System.out.print("The number is: ");
                    for(int i=0;i<random.length;i++)
                    {
                        System.out.print(random[i]);
                }
                    System.out.println(" ");
            }
        }
    }
          System.out.println(" ");
        System.out.println("press 1 to countinue 0 to end game");
        Scanner answer = new Scanner(System.in);
     int again = answer.nextInt();
     if(again!=1)
     {
         tryAgain = false;
    }
}
   
    }
            
  public static int[] getGuess()
 {
    Scanner keyboard = new Scanner(System.in);
    System.out.println("Please enter your guess: ");
    String input = keyboard.nextLine();
        if(input.length()!=4 || input.replaceAll("\\D","").length()!=4)
        {
            System.out.println("Invalid number. You must enter 4 digits between 0-9 only.");
            return getGuess();
    }
    int[] guess = new int[4];
    for (int i = 0; i < 4; i++)
    {
        guess[i] = Integer.parseInt(String.valueOf(input.charAt(i)));
    }
    return guess;
}

public static int[] numberGenerator() 
{
    Random randy = new Random();
    int[] randArray = {10,10,10,10};

    for(int i=0;i<randArray.length;i++){
        int temp = randy.nextInt(9);
        while(temp == randArray[0] || temp == randArray[1] || temp == randArray[2] || temp == randArray[3]){
            temp=randy.nextInt(9);
        }
        randArray[i]=temp;      
    }
    return randArray;

}

}
    

     
   
   
 

 
        
 