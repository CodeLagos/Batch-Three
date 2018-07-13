/*@author SALAUDEEN ABDULAHI AND STEPHEN AKPOVINO CODE LAGOS BATCH 3 ISOLO PUBLIC LIBRARY 2018 
*  (abdulahi salaudeen mail=asalau83@gmail.com   phone=09060672728)(stephen akpovino mail= stephenakpovino06@gmail.com,07067065925
 *THIS PROGRAM SOLVE SIMULTANEOUS 2 VARIABLE X&Y , AREA AND PERIMETER OF A CIRCLE AND SUM OF AN AP PROVIDED THAT THE FIRST
 * TERM, SECOND TERM AND NUMBER OF TERMS ARE GIVEN 
*/
package mathequation;

import java.util.*;

/**
 *
 * @author SALAUDEEN ABDULAHI AND STEVE CODE LAGOS BATCH 3
 */
public class Mathequation {

   
    public static void main(String [] args) {
        // TODO code application logic here
        for(;;){
            System.out.println("These program solve for simultaneous 2 variable X and Y,");
        System.out.println("Area and Perimeter of a circle,");
        System.out.println("and Sum of Arithmathic Progression" );
        System.out.println ("select out the options");
        System.out.println("1:Simultanous\n2:Area and perimeter of a circle\n3:Sum of an Arithmetic Progression ");
        System.out.print("option: ");
        Scanner input =new Scanner(System.in);// to select input for option\\
        Mathequation math=new Mathequation();
        int option;//option input 
        try { //catching wrong input and Wrong arithmetic expression such as String and undefine value
             option=input.nextInt();//input for the option
           switch(option){//checking over option inputted
            case 1:math.simultaneous();
             break;
            case 2:math.area();
            break;
            case 3:math.sumOfAP();
             break;
            default:
                System.out.print("your input doesn't not match the option"); }}
     catch(InputMismatchException | ArithmeticException ar){//catching wrong input and catching undefined value
         System.out.println("your input is incorrect retry again"); 
     } 
        System.out.print("Enter 'N' to end the program: ");
        String arr = input.next();
        if(arr.equals("N")){
            break;
        }
        
        }
        
 }
    public void simultaneous() { 
        System.out.println("you choose to solve for simultaneous");
        Scanner input =new Scanner(System.in);
      float x[][] =new float[2][3]; 
      
      String var="xyc";//itterate over x , y and c input clarifying
      int row=1; 
      for(int i=0;i<2;i++){ 
          row +=i;
         for(int j=0;j<3;j++){  
            System.out.print("input co-efficient of  "+var.charAt(j)+ " in equation "+row+": "); 
           x[i][j]=input.nextFloat();}//accepting input for cols in rows
      }
      System.out.println("This are your input match it with your problem");
      System.out.println(Math.round(x[0][0])+"x   "+Math.round(x[0][1])+"y= "+Math.round(x[0][2]));//eqn 1 by indexing of row to col 1-3 dimensions
      System.out.println(Math.round(x[1][0])+"x   "+Math.round(x[1][1])+"y= "+Math.round(x[1][2]));//eqn 2 by indexing of row to col 1-3 dimensions 
      System.out.println("NB that blank space withtin the output represent 'Addition'");
     //2 rows and 3 col 2x3=6
     float a,b,c,d,e,f,g,h;//g and h denote x and y in mathematical calcultion representing
     a=x[0][0];b=x[0][1];c=x[0][2];d=x[1][0];e=x[1][1];f=x[1][2];//matching array indexes to variable of type of float
     //applying simultaneous algorithm of variable X
     g=((b*f)-(e*c))/((b*d)-(a*e));//formular for variable X
     g=Math.round(g);//rounding of to the nearest number
     h=(c-a*g)/b;//formular for y after gotting the result of g then substitute it to the formular
     System.out.println("variable x="+Math.round(g)+"   variable Y="+Math.round(h));
  }
    public void area(){
        System.out.println("you choose to solve for area or perimeter of a circle");
        Scanner input =new Scanner(System.in);//
        System.out.println("select option\n1:calculate for perimeter\n2:calculate for area");
        System.out.print("option: ");
        int option=input.nextInt();//1 option input
       if (option==1){//testing the option 
            System.out.print("input radius: ");
            float radius=input.nextFloat();//input for radius
            double ans=2*Math.PI*radius;// formular for perimeter of circle
            System.out.println("the perimetere of the circle is: "+Math.round(ans));}
       else if(option==2){//2 option of input
            System.out.print("input radius: ");
            int radius=input.nextInt();//input radius
            double ans=Math.PI*Math.pow(radius,2);//formular for area of circle 
            System.out.println("the area of the circle is ="+Math.round(ans)); //rounding of to the nearest numb
       }
       else {System.out.println("the input does'nt match the options");//to output if non the input match
    }
  }      
    public void sumOfAP(){
        System.out.println("you choose to solve for sum of AP");
        Scanner input =new Scanner(System.in);
        float first,second,sum;//input for the first,second and sum Sn
        System.out.print("input the first term: ");
        first=input.nextFloat();//getting the first term
        System.out.print("input the second term: ");
        second=input.nextFloat();//getting the second term
        System.out.print("input the sum: ");
        sum=input.nextFloat();//getting sum
        second=second-first;//getting the common difference
        sum=(sum/2)*((2*first)+(sum-1)*second);//formular of arithmethic progression
        System.out.println("The sum of the AP is: "+Math.round(sum)+"\n");//outputing the ans
    }
}
