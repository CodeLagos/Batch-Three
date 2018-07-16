/**ADESHINA OLUWASEYE
 * CODELAGOS BATCH3.0
 * STUDENT GRADE IS FOR STUDENT ANALYSIS ON GRADING AND SUBJECT DISTRIBUTION
 * SY4EVER2003@YAHOO.COM
*/
package studentgrade;

import java.util.Scanner;

public class StudentGrade {

    public static void average(int[] array) {
        double sum = 0;
        int count = 0;
        double average = 0;

        for (int i = 0; i < array.length; i++) {
            sum += array[i];
            count++;
        }
        average = sum / count;
        System.out.print(average);
    }

    public static void main(String[] args) {
        System.out.print("Welcome to ");
        System.out.println("Code Lagos!");
        // create a Scanner to obtain input from the command window
        Scanner input = new Scanner(System.in);
        String nameOfCourse;

        System.out.print("Please enter the course name:");
        nameOfCourse = input.nextLine();

        System.out.print("Enter the number of students for the course: ");
        int numberOfStudent = input.nextInt();

        String[] names = new String[numberOfStudent];
        int[] array = new int[numberOfStudent];
        int i = 0;
        int Score;
        while (i < numberOfStudent) {
            System.out.print("Enter the Student Name: ");
            String name = input.next();

            System.out.print("Enter the test Score: ");

            Score = input.nextInt();
            if (Score < 0 || Score > 100) {
                System.out.print("incorrect score,"
                        + " Re-enter the score-"
                        + "(must be positive and between 0 to 100):");
                Score = input.nextInt();

            }

            array[i] = Score;

            names[i] = name;
            i++;

        }
        int h = array[0];
        int high = 0;
        int j = 0;
        while (j < array.length) {

            if (h >= array[j]) {
                high = h;
                j++;
            } else {
                h = array[j];
            }
        }
        int l = array[0];
        int low = 0;
        int k = 0;
        while (k < array.length) {

            if (l <= array[k]) {
                low = l;
                k++;
            } else {
                l = array[k];
            }
        }
        int ind = 0;
        int n = 0;
        int m = 0;
        while (ind < array.length) {
            if (array[ind] == high) {
                n = ind;

            }
            if (array[ind] == low) {
                m = ind;

            }
            ind++;

        }
        System.out.print("\n");
        System.out.println("Test Analysis");
        System.out.println("High score: " + names[n] + ": " + high);
        System.out.println("Low score: " + names[m] + ": " + low);
        System.out.print("Class average is" + " ");
        average(array);

        int grade = 0;
        int a = 0;
        int b = 0;
        int c = 0;
        int d = 0;
        int e = 0;
        int f = 0;

        while (grade < array.length) {
            if (array[grade] >= 70 && array[grade] < 100) {
                a += 1;
            }
            if (array[grade] >= 60 && array[grade] < 70) {
                b += 1;
            }
            if (array[grade] >= 50 && array[grade] < 60) {
                c += 1;
            }
            if (array[grade] >= 40 && array[grade] < 50) {
                d += 1;
            }
            if (array[grade] >= 30 && array[grade] < 40) {
                e += 1;
            }
            if (array[grade] >= 0 && array[grade] < 30) {
                f += 1;
            }
            grade++;
        }
        System.out.print("\n");
        System.out.println("Grade Analysis");
        System.out.println("70-100: " + a);
        System.out.println("60-69:  " + b);
        System.out.println("50-59:  " + c);
        System.out.println("40-49:  " + d);
        System.out.println("30-39:  " + e);
        System.out.println("0-29:  " + f);

    }

}
