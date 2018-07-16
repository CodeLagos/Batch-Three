import java.util.Scanner ;
import java.util.ArrayList; // import array list
public class store{
	public static void main (String[] args){
		// saving my product in an array
		String product[] = { "" , "Chicken" , "Rice" , "Fruit" ,"Bread" , "Soda" , "Fish", "Wine" ,"Flour" , "Candy" ,"Cake" } ;
		// saving the product price in an array
		int price[] = {0 , 2500,570, 720 ,300 , 100 , 650, 1500,800,570,200};
		boolean domorep = true ;
		int shop = 0 ;
		
		
		ArrayList <String> cartproduct = new ArrayList <String>  ();
		ArrayList <Integer> cartamount = new ArrayList <>  ();
		ArrayList <Integer> cartquantity = new ArrayList <>  ();
		ArrayList <Integer> carttotal = new ArrayList <>  ();
		System.out.println("Welcome to Jay Store");
		// creating a loop to iterate over a condition
		do{
			System.out.println("code" + "\t" + "Product" + "\t\t" + "Amount") ;
			System.out.println("1" + "\t" + "Chicken" + "\t\t" + "N2500") ;
			System.out.println("2" + "\t" + "Rice" +  "\t\t" + "N570") ;
			System.out.println("3" + "\t" + "Fruit" +  "\t\t" + "N720") ;
			System.out.println("4" + "\t" + "Bread" +  "\t\t" + "N300") ;
			System.out.println("5" + "\t" + "Soda" +   "\t\t" + "N100") ;
			System.out.println("6" + "\t" + "Fish" + "\t\t" + "N650") ;
			System.out.println("7" + "\t" + "Wine" + "\t\t" + "N1500") ;
			System.out.println("8" + "\t" + "Flour" + "\t\t" + "N800") ;
			System.out.println("9" + "\t" + "Candy" + "\t\t" + "N570") ;
			System.out.println("10" + "\t" + "Cake" +  "\t\t" + "N200") ;
			System.out.println("Please Select product to buy") ;
			Scanner pinput = new Scanner(System.in) ;
			int pproduct = pinput.nextInt() ;
			while(pproduct == 0 || pproduct > product.length){
				System.out.println("Invalid Transaction Code") ;
				System.out.println("Please Select product to buy") ;
				pproduct = pinput.nextInt() ;	
				
			}
			System.out.println("product" + "\t" + "Amount") ;
			System.out.println( product[pproduct] + "\t" +"N" + price[pproduct] ) ;
			System.out.println("") ;
			System.out.println("Please Select number of " + product[pproduct] + " You want to add to your cart ") ;
			System.out.println(product[pproduct] + "\t" + "* " + " ?" ) ;
			int pproductnum = pinput.nextInt() ;
			int pproductnumprice = pproductnum * price[pproduct] ;
			System.out.println(product[pproduct] + " Added Successfully to cart") ; 
			System.out.println("Do you want to buy more goods " ) ;
			System.out.println("1" + "\t" + "YES") ;
			System.out.println("2" + "\t" + "Checkout") ;
			System.out.println("3" + "\t" + "View Cart") ;
			int domore = pinput.nextInt() ;
			while(domore != 1 && domore != 2 && domore != 3){
				System.out.println("Invalid Selection, Please selection either 1 or 2 " ) ;
				System.out.println("Do you want to buy more goods " ) ;
				System.out.println("1" + "\t" + "YES") ;
				System.out.println("2" + "\t" + "Checkout") ;
				System.out.println("3" + "\t" + "View Cart") ;
				domore = pinput.nextInt() ;
			}
			while(domore == 1){
				domorep = true ;
			    cartproduct.add(product[pproduct] ) ; 
				cartamount.add(price[pproduct]) ;
				cartquantity.add(pproductnum) ;
				carttotal.add(pproductnumprice) ;
				break ;
			}
			if(domore == 2 ){
				cartproduct.add(product[pproduct] ) ; 
				cartamount.add(price[pproduct]) ;
				cartquantity.add(pproductnum) ;
				carttotal.add(pproductnumprice) ;
				
				System.out.println("Your Purchase History ") ;
				System.out.println("Product" + "\t" + "Price" + "\t" + "Quantity" + "\t" + "Amount" ) ;
				int sum = 0 ;
				for (int i = 0 ; i < cartproduct.size() ; i++){
								 sum = sum + carttotal.get(i) ;
	
								
								System.out.println(cartproduct.get(i) +  "\t" + cartamount.get(i) + "\t\t" + cartquantity.get(i) + "\t" +carttotal.get(i)) ;
								
							}
							System.out.println("\t\t\t\t" + "______") ;
							System.out.println("Total " + "\t\t\t\t " + sum) ;
							System.out.println("\t\t\t\t" + "______") ;
							if (sum < 20000){
							System.out.println("Please pay a total of " + sum + " to the account details below, your order would be delivered between 24hrs of payment ") ;
								
							}
							
							if (sum >= 20000){
									 double per = 0.2 * sum ;
									 double sum2 = sum ;
									 sum2 = sum2 - per ;
									 System.out.println("Discount" + "\t\t\t" + per) ;
									 System.out.println("\t\t\t\t" + "______") ;
									 System.out.println("") ;
									 
									System.out.println("Due Payment " + "\t\t\t" + "N" + sum2) ;
									System.out.println("\t\t\t\t" + "______") ;
									System.out.println("Please pay a total of " + sum2 + 0 + " to the account details below, your order would be delivered between 24hrs of payment ") ;
							}
									System.out.println("ACCOUNT NAME" + "\t\t\t" + "Jatto Joshua") ;
									System.out.println("BANK" + "\t\t\t\t" + "Zenith Bank") ;
									System.out.println("ACCOUNT NUMBER" + "\t\t\t" + "1234567890") ;
									System.out.println("Thanks For Your Patronage") ;
									System.out.println("JAY STORE ") ;
									System.out.println("WE ARE COMMITTED TO SEARVE YOU BETTER") ;
							
							break ;
				
			}
			//while()
			if( domore == 3){
				cartproduct.add(product[pproduct] ) ; 
				cartamount.add(price[pproduct]) ;
				cartquantity.add(pproductnum) ;
				carttotal.add(pproductnumprice) ;
				
				System.out.println("Your cart History ") ;
				System.out.println("Product" + "\t" + "Price" + "\t" + "Quantity" + "\t" + "Amount" ) ;
				int sum = 0 ;
				for (int i = 0 ; i < cartproduct.size() ; i++){
								 sum = sum + carttotal.get(i) ;
	
								
								System.out.println(cartproduct.get(i) +  "\t" + cartamount.get(i) + "\t\t" + cartquantity.get(i) + "\t" +carttotal.get(i)) ;
								
							}
							System.out.println("\t\t\t\t" + "______") ;
							System.out.println("\t\t\t\t" + sum) ;
							System.out.println("\t\t\t\t" + "______") ;
							System.out.println("1" + "->" + " Cancel Transaction" ) ;
							System.out.println("2" + "->" + " Continue Shopping" ) ;
							shop = pinput.nextInt() ;
							if (shop == 1){
								System.out.println("Thanks For Your Patronage") ;
								System.out.println("JAY STORE ") ;
								System.out.println("WE ARE COMMITTED TO SEARVE YOU BETTER") ;
								break ;
							}
							
			}
				
			
		}
		while(domorep || shop == 1) ;
		
	}

	
}