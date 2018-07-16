public class mulArray{
	public static void main(String[] args){
		int[][] multArray = {
			{1,2,3,4,5,6},
			{2,3,4,5,6,7}
		};
		
		for(int i = 0; i < multArray[1].length; i++){
			System.out.print(multArray[0][i] + " ");
			System.out.println();
		}
		System.out.println(" ");
		for(int i = 0; i < multArray[1].length; i++){
			System.out.print(multArray[1][i] + " ");
			System.out.print(" ");
		}
	}
}