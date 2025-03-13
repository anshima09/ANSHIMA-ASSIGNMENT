import java.util.Scanner;

public class Program13 {
    public static void main(String[] args) {
         Scanner sc=new Scanner(System.in);
         System.out.println("Enter size of array: ");
         int n=sc.nextInt();

         int[] arr=new int[n];
         int sum=0;

         System.out.println("Enter "+n+" elements in array: ");
         for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
            sum+=arr[i];
         }

         double avg=(double)sum/n;

         System.out.println("Average of array elements: "+avg);
         sc.close();
    }
}
