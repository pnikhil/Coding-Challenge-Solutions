import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc  = new Scanner(System.in);
        int num_test_cases = sc.nextInt();
        int[] a = new int[num_test_cases];
        int[] b = new int[num_test_cases];
        int[] n = new int[num_test_cases];
        int sum;
        for(int i = 0;i<num_test_cases;i++)
            {
            a[i] = sc.nextInt();
            b[i] = sc.nextInt();
            n[i] = sc.nextInt();
        }
        for(int i = 0 ; i < num_test_cases ; i++)
        {
        	
        	for(int  j=0 ; j < n[i]; j++)
        	{
        		sum = a[i];
        		 for (int k = 0; k <= j; k++){
        			 sum = (int) (sum + Math.pow(2,k) * b[i]);
        		 }
        		System.out.print(sum +" "); 
        	}
        	System.out.println();
        }
        sc.close();
    }
}