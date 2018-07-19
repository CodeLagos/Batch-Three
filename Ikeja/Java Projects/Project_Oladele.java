/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaclass1;
import java.util.Random;
import java.util.Scanner;


/**
 *
 * @author Abdulsemihi
 */
public class RandomGame {
    public static void main(String[] args) {
        
        int [] randomList = new int [3];
        int [] inputArray = new int [3];
    
        
  
        
    Random rand = new Random();
    int i=0;
    int j=0;
    
    
      
    while(i<3) {
        // generate radom numbers
           int rn = rand.nextInt(9)+1;
              //method to test if number is unique
              
            if (randomList[0]!=rn && randomList[1]!=rn && randomList[0]!=rn   ){
            randomList[i] = rn;
            //System.out.println(randomList[i]);
                i++;
                
            }else{
            
            
            }
            
          
                

                }
    
    
   
    
    
    
    
    
   Scanner input = new Scanner (System.in);
   
   
   for (int check =1;check<13;check++){
       int injured,killed;
       
    while(j<3) {
        System.out.println("kindly input #" +(j+1)+" : " );
        int un = input.nextInt();
                  if (inputArray[0]!=un && inputArray[1]!=un && inputArray[0]!=un   ){
            inputArray[j] = un;
            //System.out.println(inputArray[j]);
                j++;
                
            }else{
            
                      System.out.println("input matched re-enter value");
            }
          

                } 
    
    injured=injured(randomList,inputArray);
    killed=killed(randomList,inputArray);
    if (killed ==3 ){ 
        System.out.println("Congrats you win ");
        break;
    
    }else {System.out.print("Try Again injured = ");
    for (int in =0; in<3;in++){inputArray[in]=0;}
        System.out.print(injured +" killed = "+killed +"\n");
    }
    
    if (check ==12 ){ System.out.println("Game over you have Exsuted your 12 chances ");
    
    break;}
    
    j=0;
    
   }

    //int [] randomList1={1,2,3};
    //int [] arraytest= {3,1,2};
    
        
       // System.out.println(injured(randomList1,arraytest));
    }
    
    // check killed
     public static int killed(int[] ar1,int [] ar2) {
         int killed =0;
         for (int n1 =0;n1<3;n1++){
         if ( ar1[n1]==ar2[n1] ){
         killed+=1;
         
         }
         
         }
         return killed;
        
    }
    
     public static int injured (int[] ar1,int [] ar2){
     int injured =0;
     for (int n1=0;n1<3;n1++){
         switch (n1){
              case 0:
                  if (ar1[n1]== ar2[1] || ar1[n1]== ar2[2] )
                      injured +=1;
           

            break;

        case 1:
            if (ar1[n1]== ar2[0] || ar1[n1]== ar2[2] )
                      injured +=1;
            break;

        case 2:

           if (ar1[n1]== ar2[0] || ar1[n1]== ar2[1] )
                      injured +=1;

            break;
         }

             }
   // check if number is unique
   return injured;

     }  
     
// returns integer
            
}