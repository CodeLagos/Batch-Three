/**@author Abdulahi salaudeen CODE LAGOS BATCH3 ISOLO
 * mail=asalau83@gmail.com phone=09060672728
 */
package determinantmatrix.pkg3by3;
import java.util.Scanner;
/**
 *
 * @author Bolaji
 */
public class DeterminantMatrix3by3 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) { 
      for(;;){  DeterminantMatrix3by3 dM=new DeterminantMatrix3by3();
       System.out.println("The program solve Determinant of 3 by 3 matrix");  
       Scanner input=new Scanner(System.in);//create scanner object for input
       System.out.println("if you wish to proceed press 'Y' for yes or 'N' for no "); 
       System.out.print("option: ");//
       String option=input.next();// option to enter
        if(option.equals("Y")|| option.equals("y")){//checking condition
            System.out.println("you wish to proceed");
            dM.matrix3by3();//calling the matrix method
        }
        else if (option.equals("N")||option.equals("n")){//else breaking out of the loop if N or n is entered
            break;
        }}
    }
    public void  matrix3by3(){ //defining the matrix method
        Scanner input=new Scanner(System.in); //creating scanner object for inputting row and column in the matrix
    try{  float  z[][]=new float[4][4]; //creating array for 3 row 3 column . i chose size of 4 bcus of matching the input data with the console to enter the index from row 1 col 1 not row 0 column 0
      for(int i=1;i<4;i++){    //itteration over row
          for(int j=1;j<4;j++){ // itteration over 1-3 rows and 1-3 columns for each rows
              System.out.print("input row "+i+" column "+j+": ");//input started from first row first column as per say in the array size 
             z[i][j]=input.nextInt(); //itteration over rows and columns
          }
      } 
      float a,b,c,d,e,f,g,h,i,sum;//variable to store the index value of the arrays
      a=z[1][1];b=z[1][2];c=z[1][3];d=z[2][1];e=z[2][2];f=z[2][3];g=z[3][1];h=z[3][2];i=z[3][3];  
      System.out.println("These are your inputs");//outputting the enter value in rows and columns matching
      System.out.println("      "+Math.round(a)+"    "+Math.round(b)+"    "+Math.round(c));
      System.out.println("      "+Math.round(d)+"    "+Math.round(e)+"    "+Math.round(f));
      System.out.println("      "+Math.round(g)+"    "+Math.round(h)+"    "+Math.round(i));
      // application of algorithm
     sum= (a*((e*i)-(f*h))-b*((d*i)-(f*g))+c*((d*h)-(e*g))); //
     System.out.println("The Determinant of 3 by 3 matrix is :"+Math.round(sum));//outputting the sum of the matrix 
    } catch(Exception exce){
        System.out.println("You input a wrong option retry");
    }  }
}
