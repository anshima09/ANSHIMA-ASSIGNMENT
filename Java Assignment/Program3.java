import java.util.Scanner;

public class Program3 {

    public static long factorial(int num){
        if(num==0 || num==1){
            return 1;
        }
        return num*factorial(num-1);
    }
    public static void main(String[] args) {
        Scanner sc =new Scanner(System.in);
        System.out.println("Enter a number: ");
        int num=sc.nextInt();

        long ans=factorial(num);
        System.out.println("Factorial of "+num+" is: "+ans);
        sc.close();
    }
}
