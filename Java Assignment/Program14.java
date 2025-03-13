import java.util.Scanner;

public class Program14 {

    public static void bubbleSort(int[] arr,int n){
        for(int i=0;i<n-1;i++){
            int minIndex=i;
            for(int j=i+1;j<n;j++){
                if(arr[j]<arr[minIndex]){
                    minIndex=j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }

        //displaying array
        for(int i=0;i<n;i++){
            System.err.print(arr[i]+" ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
         Scanner sc=new Scanner(System.in);

         System.out.println("Enter size of array: ");
         int n=sc.nextInt();

         int[] arr=new int[n];

         System.out.println("Enter "+n+" elements in an array: ");
         for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
         }
        System.out.println("Sorted elements in an array:");
         bubbleSort(arr,n);
         sc.close();
    }
}
