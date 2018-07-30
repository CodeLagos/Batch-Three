/*
 * This project is a Quiz App.
 * It is a question and answer on current affairs.
 * It allows the user to test its knowledge about .
 */
package quizappnew;

import java.util.Scanner;

/**
 *
 * @author User
 */
public class QuizAppnew {

        
        
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       
    
        Scanner input =new Scanner(System.in);
       System.out.println("Enter Your Name");
       String user = input.nextLine();
       System.out.println("Welcome " +user);
       
       int score = 0;
       
       System.out.println("Who is the President of Nigeria?");
       String userAnswer = input.nextLine();
       String correctAnswer = "Muhammodu Buhari";
       System.out.println("Answer is: " +correctAnswer);
       
       if (userAnswer.equalsIgnoreCase(correctAnswer)){
           System.out.println("Correct");
       
           score = score +1;}
    
       else{
           System.out.println("You are wrong");}
       
       
       
       System.out.println("Who is the Governor of Lagos State?");
       String userAnswer2 = input.nextLine();
       String correctAnswer2 = "Akinwunmi Ambode";
       System.out.println("Answer is: " +correctAnswer2);
       
       if (userAnswer2.equalsIgnoreCase(correctAnswer2)){
           System.out.println("Correct");
      
           score = score +1;} 
       
       else{
           System.out.println("You are wrong");}
       
      
       
       System.out.println("20/4");
       String userAnswer3 = input.nextLine();
       String correctAnswer3 = "5";
       System.out.println("Answer is: " +correctAnswer3);
       
       if (correctAnswer3 == userAnswer3){
           System.out.println("Correct");
       
           score = score +1;}
       
       else{
           System.out.println("You are wrong");}
       
       
       System.out.println("What is the Capital of Lagos?");
       String userAnswer4 = input.nextLine();
       String correctAnswer4 = "Ikeja";
//       System.out.println("Answer is: " +correctAnswer4);
       
       if (userAnswer4.equalsIgnoreCase(correctAnswer4)){
           System.out.println("Correct");
       
       score = score +1;}
       
       else{
           System.out.println("You are wrong");}
       
       
       
       System.out.println("Which Country Host the 2018 Fifa World Cup?");
       String userAnswer5 = input.nextLine();
       String correctAnswer5 = "Russia";
       System.out.println("Answer is: " +correctAnswer5);
       
       if (userAnswer5.equalsIgnoreCase(correctAnswer5)){
           System.out.println("Correct");
       
           score = score +1;}
       
       else{
           System.out.println("You are wrong");}
       
       
       
       System.out.println("Ghana is in what part of Africa?");
       String userAnswer6 = input.nextLine();
       String correctAnswer6 = "West Africa";
       System.out.println("Answer is: " +correctAnswer6);
       
       if (userAnswer6.equalsIgnoreCase(correctAnswer6)){
           System.out.println("Correct");
       
       score = score +1;}
       else{
           System.out.println("You are wrong");}
      
              
       System.out.println("Gorge Weah is the President of which Country?");
       String userAnswer7 = input.nextLine();
       String correctAnswer7 = "Liberia";
       System.out.println("Answer is: " +correctAnswer7);
       
       if (userAnswer7.equalsIgnoreCase(correctAnswer7)){
           System.out.println("Correct");
       
      score = score +1;}
       
       else{
           System.out.println("You are wrong");}
      
       
       System.out.println("Which Nigerian former player also known as Jay Jay?");
       String userAnswer8 = input.nextLine();
       String correctAnswer8 = "Austin Okocha";
       System.out.println("Answer is: " +correctAnswer8);
       
       if (userAnswer8.equalsIgnoreCase(correctAnswer8)){
           System.out.println("Correct");
       
           score = score +1;}
       
       else{
           System.out.println("You are wrong");}
       
       
       System.out.println("What is Nigeria Official language");
       String userAnswer9 = input.nextLine();
       String correctAnswer9 = "English";
       System.out.println("Answer is: " +correctAnswer9);
       
       if (userAnswer9.equalsIgnoreCase(correctAnswer9)){
           System.out.println("Correct");
       
           score = score +1;}
       
       else{
           System.out.println("You are wrong");}
       
       
       System.out.println("Nigeria National Team is Known As?");
       String userAnswer10 = input.nextLine();
       String correctAnswer10 = "Super Eagle";
       System.out.println("Answer is: " +correctAnswer10);
       
       if (userAnswer10.equalsIgnoreCase(correctAnswer10)){
           System.out.println("Correct");
       
       score = score +1;}
       
       else {
           System.out.println("You are wrong");}
       
System.out.println("totalscore is: " +score +"/10");

       int totalpercentage = score*100/10;
 
       System.out.println("totalpercentage is: " +totalpercentage);
       
    if (totalpercentage >= 80 && totalpercentage <=100){
         System.out.println("Excellent");}
       
   else if (totalpercentage >= 60 && totalpercentage <=70){
         System.out.println("V.Good");}
    
   else if (totalpercentage >= 50 && totalpercentage <=60){
         System.out.println("Good");}
    
   else if (totalpercentage <= 30 && totalpercentage >=40){
         System.out.println("Fair");}
    
   else if (totalpercentage <= 30)
        System.out.println("Fail");
   
    }
    }
    
    
              
    
    

 