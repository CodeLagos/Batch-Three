/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package weather.app;

import java.util.Scanner;

/**
 *
 * @author HP
 */
public class WeatherApp {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner input = new Scanner(System.in);
        System.out.println("I am your weather app, pls tell me your name so that I can give you personalized weather forecasts");
        String name = input.nextLine();
        System.out.println("welcome "+name+" to the weather app");
        double currentWeather = Math.random()*50;
        System.out.printf("The weather forecast for this morning in celsius is %.1f %n",currentWeather);
        if(currentWeather>=0 && currentWeather<= 20) {
        System.out.println(name+" It is going to be freaky cold and would be madly windy and would rain the hell today, please try to stay at home and rest and enjoy your day also do the following:");
        System.out.println(name+" please wear a sweater");
        System.out.println(name+" please you are advised to take hot tea");
        System.out.println(name+" also try to wear a boot to keep you warm");
        System.out.println("and before I forget "+name+", sitch on your heater for keeping yourself warm during the cold :)");
        } else if(currentWeather>=21 && currentWeather<= 30) {
            System.out.println(name+" It is going to be cold and would likely rain today, please remember to take along the following to enjoy your day:");
        System.out.println(name+" please wear a jacket");
        System.out.println(name+" please also take hot tea to warm your body");
        System.out.println(name+" your rainy boot should also not be forgotten");
        System.out.println("and before I forget pls "+name+" do not switch off  your heater for keeping yourself warm during the cold :)");
        } else if(currentWeather>=31 && currentWeather<= 40) {
            System.out.println(name+" It is going to be warm and sunny today, please remember to take along the following to enjoy your day:");
        System.out.println(name+" take an umbrella along with you");
        System.out.println(""+name+" pls also take cold water");
        System.out.println(""+name+" your hand or rechargable fan should not be forgotten");
        System.out.println(""+name+" and remember to wear a light cloth so that you do not sweat to much :)");
        } else if(currentWeather>=41 && currentWeather<= 50) {
            System.out.println(""+name+" It is going to be so sunny and hot today that you may be melted by the sun, please remember to take along the following to enjoy your day:");
        System.out.println("I am actually serious about this "+name+" an umbrella to protect you from the freaky heat");
        System.out.println(""+name+" chilled water");
        System.out.println(""+name+"a very light bag so you don't get worked out");
        System.out.println(""+name+"and pls wear a very light cloth so that you don't have to regret your day :)");
        }
        System.out.println();
        System.out.println();
        System.out.println("Do you also need the forecast for the afternoon and evening yes or no");
        String question = input.nextLine();
        if(question.equalsIgnoreCase("yes")) {
        
        System.out.println();
        System.out.println();
        double currentWeather2 = Math.random()*50;
        System.out.printf("In the afternoon the weather forecast will be in celsius %.1f %n",currentWeather2);
        if(currentWeather2>=0 && currentWeather2<= 20) {
        System.out.println(name+" It is going to be freaky cold and would be madly windy and would rain the hell by then, please try to stay at home and rest and enjoy your day also do the following:");
        System.out.println(name+" please wear a sweater");
        System.out.println(name+" please you are advised to take hot tea");
        System.out.println(name+" also try to wear a boot to keep you warm");
        System.out.println("and before I forget "+name+", on your heater for keeping yourself warm during the cold :)");
        } else if(currentWeather2>=21 && currentWeather2<= 30) {
            System.out.println(name+" It is going to be cold and would likely rain by then, please remember to take along the following to enjoy your day:");
        System.out.println(name+" please wear a jacket");
        System.out.println(name+" please also take hot tea to warm your body");
        System.out.println(name+" your rainy boot should also not be forgotten");
        System.out.println("and before I forget pls "+name+" do not switch off  your heater for keeping yourself warm during the cold :)");
        } else if(currentWeather2>=31 && currentWeather2<= 40) {
            System.out.println(name+" It is going to be warm and sunny by then, please remember to take along the following to enjoy your day:");
        System.out.println(name+" take an umbrella along with you");
        System.out.println(""+name+" pls also take cold water");
        System.out.println(""+name+" your hand or rechargable fan should not be forgotten");
        System.out.println(""+name+" and remember to wear a light cloth so that you do not sweat to much :)");
        } else if(currentWeather2>=41 && currentWeather2<= 50) {
            System.out.println(""+name+" It is going to be so sunny and hot by then that you may be melted by the sun, please remember to take along the following to enjoy your day:");
        System.out.println("I am actually serious about this "+name+" an umbrella to protect you from the freaky heat");
        System.out.println(""+name+" chilled water");
        System.out.println(""+name+" a very light bag so you don't get worked out");
        System.out.println(""+name+" and pls wear a very light cloth so that you don't have to regret your day :)");
        
    }
        
    System.out.println();
        System.out.println();
        System.out.println();
        
        double currentWeather3 = Math.random()*50;
        System.out.printf("In the evening the weather forecast will be in celsius %.1f %n",currentWeather3);
        if(currentWeather3>=0 && currentWeather3<= 20) {
        System.out.println(name+" It is going to be freaky cold and would be madly windy and would rain the hell by then, please try to come back home early and enjoy your day also do the following:");
        System.out.println(name+" please wear a sweater");
        System.out.println(name+" please you are advised to take hot tea");
        System.out.println(name+"also try to wear a boot to keep you warm");
        System.out.println("and before I forget "+name+", do not switch off your heater for keeping yourself warm during the cold :)");
        } else if(currentWeather3>=21 && currentWeather3<= 30) {
            System.out.println(name+" It is going to be cold and would likely rain by then, please remember to come home early:");
        System.out.println(name+" please wear a jacket");
        System.out.println(name+" please also take hot tea to warm your body");
        System.out.println(name+" by then you can also take a nap");
        System.out.println("and before I forget pls "+name+" do not switch off  your heater for keeping yourself warm during the cold :)");
        } else if(currentWeather3>=31 && currentWeather3<= 40) {
            System.out.println(name+" It is going to be warm and kind of hot by then, please remember to come back as early has you can:");
        System.out.println(name+" make sure you take your hat with you this morning so that by then you will not be heated up");
        System.out.println(""+name+" pls also be with cold water");
        System.out.println(""+name+" your hand or rechargable fan should not be forgotten");
        System.out.println(""+name+" and remember to wear a light cloth so that you do not start sweating:)");
        } 
        }
        else if(question.equalsIgnoreCase("no")) {
            System.out.println("bye for now see you later");
        }
    }

         //To change body of generated methods, choose Tools | Templates.
    }
