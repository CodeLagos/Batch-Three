/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package converter;

import java.util.Scanner;

/**
 *
 * @author olatunde
 */
/**
 * 
 * Name:Oladunjoye Olasubomi
 */
/**
 * 
 * Email: Olasubomi24200201@gmail.com
 */
/**
 * 
 * Project name: Simple unit converter
 */
/**
 * 
 * This is a simple unit Converter that convert from one unit to another, i.e from metre to kilometre,kilobyte to byte and so on.
 */
public class Converter {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
       kilo();
        inch();
       tao();
       ali(); 
       sbo();
       ola();
       Kilo();
       mega();
       gram();
       mile();
       gallon();
       feet();
       yard();
       area();
       litre();
       inches();
       temp();
       carat();
       power();
       speed();
       time();
    }  
private static void kilo(){
    Scanner input = new Scanner(System.in);
    System.out.println("Enter your name:");
    String name=input.nextLine();
    System.out.println(" Welcome " + name);
     System.out.println("Kilobyte to Byte");
        System.out.print("kilobyte:");
        int kilobyte=input.nextInt();
        int Byte=1024;
        int value=kilobyte*Byte;
        System.out.print("Byte:");
        System.out.println(value+" B " );
}
private static void inch(){
    Scanner input= new Scanner (System.in);
    System.out.println("inches to meter");
    System.out.print("Inches:");
    double inches=input.nextDouble();
    double meter=(0.0254);
    double value=inches*meter;
    System.out.print("meter:");
    System.out.printf("%.2f",value);
}
private static void Kilo(){
        Scanner input=new Scanner (System.in);
System.out.print("Kilometer to Meter");
        System.out.print("Kilometer:");
        int kilometer=input.nextInt();
        int meter=1000;
        int value=kilometer*meter;
        System.out.print("Meter:");
        System.out.println(value+" M ");
}
private static void mega(){
 Scanner input=new Scanner (System.in);
   System.out.println("Megabyte to Kilobyte");
        System.out.print("Megabyte:");
        int mega=input.nextInt();
        int kilo=1024;
        int value=mega*kilo;
        System.out.print("Kilobyte:");
        System.out.println(value+" Kb ");
}
private static void mile(){
 Scanner input=new Scanner (System.in);
  System.out.println("Mile to Kilometer");
        System.out.print("Mile:");
        double mile=input.nextDouble();
        double kilo=(1.609);
        double value=mile*kilo;
        System.out.print("Kilometer:");
        System.out.println(value+" Km ");
}
private static void gram(){
 Scanner input=new Scanner (System.in);
  System.out.println("Kilogram to Gram");
        System.out.print("Kilogram:");
        int kgram=input.nextInt();
        int gram=1000;
        int value=kgram*gram;
        System.out.print("Gram:");
        System.out.println(value+ "g");
}
private static void gallon(){
 Scanner input=new Scanner (System.in);
 System.out.println("Gallon to litre");
 System.out.print("Gallon:");
 double gallon=input.nextDouble();
 double litre=(3.785);
 double result=gallon*litre;
 System.out.print("litre:");
 System.out.println(result+" L ");
 
}
private static void yard(){
 Scanner input=new Scanner (System.in);
  System.out.println("Yard to feet");
  System.out.print("Yard:");
  int yard=input.nextInt();
  int feet=3;
  int result=yard*feet;
  System.out.print("feet:");
  System.out.println(result+" Ft ");
}
private static void feet(){
 Scanner input=new Scanner (System.in);
  System.out.println("Miles to feet");
    System.out.print("mile:");
    int miles=input.nextInt();
    int feet=5280;
    int result=feet*miles;
    System.out.print("feet:");
    System.out.println(result);
}
private static void area(){
 Scanner input=new Scanner (System.in);
  System.out.println("Acres to hectares");
  System.out.print("Acres:");
  double Acres=input.nextDouble();
  double hectares=(0.4046);
  double result=Acres*hectares;
  System.out.print("hectares:");
  System.out.println(result);
}
private static void litre(){
 Scanner input=new Scanner (System.in);
  System.out.println("litre to millimeter");
  System.out.print("litre:");
  int litre=input.nextInt();
  int millimeter=1000;
  int result=litre*millimeter;
  System.out.print("millimeter:");
  System.out.println(result+" Ml ");
}
private static void inches(){
 Scanner input=new Scanner (System.in);
  System.out.println("inches to feet");
  System.out.print("inches:");
  double inches=input.nextDouble();
  double feet=(0.0833);
  double result=inches*feet;
  System.out.print("feet:");
  System.out.println(result);
}
private static void sbo(){
 Scanner input=new Scanner (System.in);
  System.out.println("yard to inch");
  System.out.print("yard:");
  int yard=input.nextInt();
  int inch=36;
  int result=yard*inch;
  System.out.print("inch:");
  System.out.println(result+" in ");
}
private static void ali(){
 Scanner input=new Scanner (System.in);
  System.out.println("feet to inch");
  System.out.print("feet:");
  int feet=input.nextInt();
  int inch=12;
  int result=feet*inch;
  System.out.print("inch:");
  System.out.println(result+" in ");
}
private static void ola(){
 Scanner input=new Scanner (System.in);
  System.out.println("kilogram to pound");
  System.out.print("kilogram:");
  double kilogram=input.nextDouble();
  double pound=(2.204);
  double result=kilogram*pound;
  System.out.print("pound:");
  System.out.println(result);
}
private static void tao(){
 Scanner input=new Scanner (System.in);
  System.out.println("kilogram to ounce");
  System.out.print("kilogram:");
  double kilogram=input.nextDouble();
  double ounce=(35.2);
  double result=kilogram*ounce;
  System.out.print("ounce:");
  System.out.println(result);
}
private static void carat(){
 Scanner input=new Scanner (System.in);
  System.out.println("kilogram to carat");
  System.out.print("kilogram:");
  int kilogram=input.nextInt();
  int carat=5000;
  int result=carat*kilogram;
  System.out.print("carat:");
  System.out.println(result);
}
private static void temp(){
 Scanner input=new Scanner (System.in);
  System.out.println("celsius to fahrenheit");
  System.out.print("celsius:");
  double litre=input.nextDouble();
  double millimeter=(33.8);
  double result=litre*millimeter;
  System.out.print("fahrenheit:");
  System.out.println(result);
}
private static void speed(){
 Scanner input=new Scanner (System.in);
  System.out.println("Mph to Kph");
  System.out.print("Mph:");
  double Mph=input.nextDouble();
  double Kph=(1.6092);
  double result=Kph*Mph;
  System.out.print("Kph:");
  System.out.println(result);
}
private static void time(){
 Scanner input=new Scanner (System.in);
  System.out.println("hours to seconds");
  System.out.print("hours:");
  int hours=input.nextInt();
  int seconds=3600;
  int result=hours*seconds;
  System.out.print("hours:");
  System.out.println(result+" S ");
}
private static void power(){
 Scanner input=new Scanner (System.in);
  System.out.println("kilowatts to horsepower");
  System.out.print("kilowatts:");
  double watts=input.nextDouble();
  double hps=(1.341);
  double result=watts*hps;
  System.out.print("hoursepower:");
  System.out.println(result);
}
}
// Create an object called input inside class scanner
// Create a class called Converter
// Create a method for each of the unit Conversion
// Collect the value of the first unit
// Store the S.I unit value in a datatype 
// 
//