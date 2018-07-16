// A java Program to Calculate your Age
import java.time.*;
import java.util.*;

public class age{
	public static void main (String [] Args){
		
		// Date of birth
		LocalDate bDate = LocalDate.of(1987, 12, 07);
		//Scanner LocalDate = new Scanner(System.in);
		//System.out.println(" Enter the year, month and day");
		//bdate = LocalDate.nextInt()
		
		// Current Date
		
		LocalDate now = LocalDate.of(2018,07,12);
		//Scanner LocalDate = new Scanner(System.in);
		//System.out.println(" Enter the year, month and day");
		//now = LocalDate.nextInt()
		
		Period diff = Period.between(bDate, now);
		System.out.printf("\n I am %d years, %d months, and %d days old.\n\n", diff.getYears(), diff.getMonths(),diff.getDays());
	}
}