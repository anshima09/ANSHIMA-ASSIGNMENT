import java.util.Scanner;

public class Program11 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter a number to print multiplication table: ");
        int n=sc.nextInt();

        System.out.println("Multiplication table of "+n+ " is: ");

        for(int i=1;i<=10;i++){
            System.out.println(n + " * " + i + " = " + (n * i));
        }
        sc.close();
    }
}
