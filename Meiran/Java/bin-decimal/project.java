// A Java Program that converts Binary to Decimal Number

import java.util.Scanner;

public class project{
	public static void main (String [] args){
		
		long binaryNumber, decimalNumber = 0, j = 1, remainder;
		Scanner number = new Scanner(System.in);
		System.out.print("Input a Binary number: ");
		binaryNumber = number.nextLong();
		
		while (binaryNumber > 0){
			
			remainder = binaryNumber % 10;
			decimalNumber = decimalNumber + remainder * j;
			j = j* 2;
			binaryNumber = binaryNumber / 10;
			
			
			}
		
		System.out.println( "Decimal Number: " + decimalNumber);
	}
}