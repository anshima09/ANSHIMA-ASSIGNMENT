import java.util.Scanner;

public interface Program4 {

    public static void fibonacci(int n){
        int a=0;
        int b=1;
        System.out.println("Fibonacci Series: ");

        for(int i=0;i<n;i++){
            System.out.println( a+ "");
            int c=a+b;
            a=b;
            b=c;
        }
        System.out.println();
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter a number: ");
        int num=sc.nextInt();

        fibonacci(num);
        sc.close();

    }
}
