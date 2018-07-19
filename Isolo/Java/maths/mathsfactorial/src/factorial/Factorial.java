/**@author Abdulahi salaudeen CODE LAGOS BATCH3 ISOLO
 * mail=asalau83@gmail.com phone=09060672728
 */
package factorial;
import java.util.Scanner;
/**
 *
 * @author Bolaji
 */
public class Factorial {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
       while(true) { 
           Scanner input =new Scanner (System.in); //snanner object for input
        Factorial factor=new Factorial();
        System.out.println("These program solve for factorial of a number N!"); 
        System.out.print("if you wish to proceed press 'y' for yes or 'n' for no: ");
        String option=input.next();
        if(option.equals("y")|| option.equals("Y")){ // checking the input
         System.out.print("NB the number must not be greater than 55 else you will get a wrong value");
        System.out.print("enter the number you wish to check the factorial: ");
        long v=input.nextLong();// input for the value to check it facorial
        long l=factor.recursion(v); // assigning the value to a type long data type
        System.out.println("The factorial of "+v+" is "+ l);}
        else if(option.equals("n")|| option.equals("N")){
            break;
        }}
    } 
    public long recursion(long v){
        if (v==1)
            return 1;
        else
            return v*recursion(v-1);
    }
    
}
