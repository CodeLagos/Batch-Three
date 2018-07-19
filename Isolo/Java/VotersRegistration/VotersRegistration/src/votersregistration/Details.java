
package votersregistration;
import java.util.Random;

public class Details {
    
    private int serialNumber;
    private  String name;
    private  String sex;
    private String paddress;
    
 public Details (String lname, String sex, String address){
        Random rand = new Random();
        int Sno = rand.nextInt(90000000) + 10000000;  
        this.name = lname;
        this.sex = sex;
        this.serialNumber = Sno; 
        this.paddress = address;
    }
 
 public int getSerialNumber(){
        return this.serialNumber;
 }
 
 public String getName(){
     return this.name;
 }
 
public  void Display(){    
   System.out.println("PLEASE FIND BELOW YOUR DETAILS OF REGISTRATION");
   System.out.println("----------------------------------");
   System.out.println("NAME: " + this.name.toUpperCase());
   System.out.println("SEX: "+ this.sex.toUpperCase());
   System.out.println("ADDRESS: "+ this.paddress.toUpperCase());
   System.out.println("SERIAL NUMBER: "+ this.serialNumber);
   System.out.println("----------------------------------");
   System.out.println("***\t***\t***\t***");
   }
}