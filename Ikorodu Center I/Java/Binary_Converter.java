//Name: ADEYEMI AYOMIDE
//Class: JAVA
//Project: BINARY CONVERTER
//DATE: 6TH OF JULY, 2018
package binary_converter;
import java.util.Scanner;
public class Binary_Converter {
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner in = new Scanner(System.in);
        int Decimalnum;
        String binarynum;
        //for(int i = -5; i < 33; i++){
        System.out.print("Enter te number you want to convert as a positive int, e.g., 10,: ");
        Decimalnum = in.nextInt();
        
        if (Decimalnum <= 0)
            System.out.println("ERROR: You ave entered the int as a negative int.");
        else {
            binarynum = " ";
            while (Decimalnum != 0 ){
                //tis will add spaces to it to seperate 4-digit groups
                if (binarynum.length() % 5 == 0)
                binarynum = "  " + binarynum; 
                /*this will extract the last digit in binary represention 
                * and add it to the binary number
                */
                binarynum = ( Decimalnum % 2 ) + binarynum;
                //this is t cut out the last digit in binary representation 
                Decimalnum /= 2;
            }
            System.out.println("Binary: " + binarynum);
        }
        }
    }