/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package finding.prime.factors;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 *
 * @author hp
 */
public class FindingPrimeFactors {
    public static List<Integer> primeFactors(int number){
        int n = number;
        List<Integer> factors = new ArrayList<Integer>();
        for (int i = 2; i <= n; i++) {
            while (n % i == 0) {
                factors.add(i);
                n /= i;
                       
            }
        }
        return factors;
    }    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner primefactors = new Scanner(System.in);
        System.out.println("What prime factors are you looking for");
        System.out.println("Please input a value");
        int n = primefactors.nextInt();
        for (Integer integer : primeFactors(n)){
            System.out.println(integer);
        }
        
       
        
            
        
        
        
        
       
        
        // TODO code application logic here
    }
    
}
