import java.util.Scanner;

public class Program15{
    public static int linearSearch(int[] arr,int n,int target)
    {
        for(int i=0;i<n;i++)
        {
            if(arr[i]==target){
                return i;
            }
        }
        return -1;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);

        System.out.println("Enter size of an array: ");
         int n=sc.nextInt();

         int[] arr=new int[n];

         System.out.println("Enter "+n+" elements in an array: ");
         for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
         }

         System.out.println("Enter the element you want to search: ");
         int target=sc.nextInt();

         int ans=linearSearch(arr,n,target);
         if(ans!=-1){
            System.out.println("Element found at index "+ans);
         }
         else{
            System.out.println("Element not found in an array");
         }
         sc.close();
    }
}