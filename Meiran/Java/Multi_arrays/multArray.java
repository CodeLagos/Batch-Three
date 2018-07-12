import java.util.Scanner;

public class multArray{
    public static void main(String[] args){

        Scanner n = new Scanner(System.in);
        int arr = n.nextInt();

        for(int i = 0; i <= n; i++){
            
        }
        int[][] a = {{3,4,5}, {3,6,7}};
        int[][] b = {{5,3,6}, {8,9,3}};
        int[][] c = new int[2][3];

        for(int i = 0; i < 2; i++){
            for(int j = 0; j < 3; j++){
                c[i][j] = a[i][j] + b[i][j];
                System.out.print(c[i][j] + " ");
            }
            System.out.println();
        }

        n.close();
    }
}