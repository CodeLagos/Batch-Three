/**
 * A SIMPLE VOTERD CARD REGISTRAION PLATFORM WHICH ENABLES A USER TO REGISTER
 * AND GET HIS/HER TEMPORARY VOTERS CARD
 * ABOGUNRIN ABAYOMI
 * PROPHETHUG2000@GMAIL.COM
 * CODE LAGOS BATCH 3
 * JAVA CLASS
 */
package votersregistration;

import java.util.*;
 
public class VotersRegistration {
    public static ArrayList<Details>regList = new ArrayList<>();
   
    
    public static void Instruction(){
        System.out.println("WELCOME TO THE OFFICAL INEC REGISTRATION PORTAL");
        System.out.println("-------------------------------------------------");
        System.out.println("1. NEW REGISTRATION");
        System.out.println("2. DISPLAY INFORMATIONS");
        System.out.println("0. EXIT");
        System.out.println("-------------------------------------------------");
        System.out.println("Please enter your choice to perform an action");
        
    }
 
    public static void main(String[] args) {
       Instruction();
       Scanner input = new Scanner(System.in);
       int choice = input.nextInt();
       while (true){
        switch (choice){
            case 1:
            Information();
            Instruction();
            choice = input.nextInt();
            break;
            
            case 2:
            System.out.println("Please input Last Name");
            String lname = input.next();
            System.out.println("");
            for (Details det : regList){
                 if(det.getName().equals(lname)){
                     det.Display();
                    }
            }
            Instruction();
            choice = input.nextInt();
            break;
            
            case 0:
                System.out.println("Exiting the portal....");
                System.out.println("WELLDONE DEAR ENROLLMENT OFICER");
                System.out.println("Good Job!!");
                input.close();
                System.exit(0);
                break;
                
            default:
                System.out.println("Please choose a valid option!");
                break;
       
       }
    }
  }
         
        public static void Information(){
          
        Random rand = new Random();
        int cd = rand.nextInt(90) + 10;
        int dd = rand.nextInt(90) + 10;
        int ed = rand.nextInt(90) + 10;
        int fd = rand.nextInt(900) + 100;
        Scanner input = new Scanner(System.in);
        System.out.println("Please input First Name");
        String fname = input.next();
        System.out.println("Please input Middle Name");
        String mname = input.next();
        System.out.println("Please input Last Name");
        String lname = input.next();
        System.out.println("Please input your Age");
        int age = input.nextInt();
        System.out.println("Please input Sex");
        String sex = input.next();
        System.out.println("Please input Address");
        String addr = input.next();
        System.out.println("Please input Occupation");
        String occp = input.next();
        System.out.println("Please input State Of registration");
        String state = input.next();
        System.out.println("Please input LGA");
        String lg = input.next();
        System.out.println("Please input LG WARD");
        String ward = input.next();
        Details newUser = new Details(lname, sex, addr);
        regList.add(newUser);
        if (age >= 18){
        System.out.println("");
        System.out.println("GENERATING THE VOTERS CARD");
        System.out.println("");
        System.out.println("*****************************************************************");
        System.out.println("*\t\tFEDERAL REPUBLIC OF NIGERIA\t\t\t*");
        System.out.println("*\tINDEPENDENT NATIONAL ELECTORAL COMMISSION\t\t*");
        System.out.println("*\t\t\tVOTER'S CARD\t\t\t\t*");
        System.out.println("*   CODE\t" + cd + "-"+ dd + "-" + ed + "-" + fd + "\t\t\t\t\t*");
        System.out.println("*\t\t\t\t\t\t\t\t*");
        System.out.println("*\t\t\t\t\tDELIM: " + state.toUpperCase() + "|" + lg.toUpperCase()+"");
        System.out.println("*\t\t\t\t\t" + ward.toUpperCase() +"\t\t\t*");
        System.out.println("*\t\t\t" + lname.toUpperCase()+ " " + fname.toUpperCase()+ " " + mname.toUpperCase()+"");
        System.out.println("*\t\t\t\t\t\t\t\t*");
        System.out.println("*   AGE:\t\t\t\t\t" + "GENDER: \t*");
        System.out.println("*   " + age + "\t\t\t\t\t\t" + sex.toUpperCase()+"\t\t*");
        System.out.println("*\t\t\t\t\t\t\t\t*");
        System.out.println("*   OCCUPATION");
        System.out.println("*   " + occp.toUpperCase()+"");
        System.out.println("*\t\t\t\t\t\t\t\t*");
        System.out.println("*   ADDRESS");
        System.out.println("*   " + addr.toUpperCase());
        System.out.println("*\t\t\t\t\t\t\t\t*");
        System.out.println("*\tBATCH:\t" + cd + "/"+ dd + "/" + ed + "/" + fd +"\t\t|" + "SERIAL NO: " + newUser.getSerialNumber()+"\t*");
        System.out.println("*ISSUED BY INEC PURSUANT TO SECTION 16 OF THE ELECTORAL ACT 2010*");
        System.out.println("*****************************************************************");
        System.out.println("");
        }
        else
            System.out.println("You are underaged and thus not qualified to regiser now\n Kindly wait till you are 18!");
    }
    
  }

