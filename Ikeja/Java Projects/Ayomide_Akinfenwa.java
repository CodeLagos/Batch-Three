/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaproject;

import java.util.*;

/**
 *
 * @author Heywhy
 */
public class Ayomide_Akinfenwa {

    

    public static void main(String[] args) {
        int[] randArray = new int[3];
        Random rand = new Random();
        Scanner scanner = new Scanner(System.in);
        
        for(int a =0;a<3;a++){
            int no = rand.nextInt(10);
            
            while (contains(randArray, no)){
                no = rand.nextInt(10);
            }
            randArray[a] = no;
        }
     for(int lives = 0;lives<12;lives++){
         int[] guess = new int[3];
         for(int z=0;z<3;z++){
             System.out.println("Enter number : ");
             guess[z] = scanner.nextInt();
         
         }
         int killed = 0, injured = 0;
         
         for(int y=0;y<3;y++){
             if(randArray[y] == guess[y]){
                 killed++;
             }else if(contains(randArray, guess[y])){
                 injured++;
             }
         }
         
         if(killed == 3){
             System.out.println("Congratulations you won the game. correct numbers are "+guess[0]+", "+guess[1]+", "+guess[2]);
             System.out.println("Trails => "+(lives+1));
             break;
         }else{
             System.out.println(killed+"killed, "+injured+"injured.");
         }
         
     }
        
        
    }
    public static boolean contains(final int[] array, final int v){
        boolean found = false;
        
        for(int a : array){
            if(a == v){
                found = true;
                break;
            }
            
        }
        return found;
    }
}