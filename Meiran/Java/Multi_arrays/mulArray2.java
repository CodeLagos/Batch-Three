public class mulArray2{
	public static void main(String[] args){
		char[][] TwoD = new char[4][5];
		int i, j;
		char c = 'A';
		
		for(i = 0; i < 4; i++)
			for(j = 0; j < 5; j++){
				TwoD[i][j] = c;
				c++;
			}
			
		for(i = 0; i < 4; i++){
			for(j = 0; j < 4; j++)
				System.out.print(TwoD[i][j] + " ");
				System.out.println();
			
		}
	}
}