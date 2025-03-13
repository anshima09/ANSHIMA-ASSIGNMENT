import java.util.Scanner;

public class Program20 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter a string: ");
        String s=sc.nextLine();

        String rev=new StringBuilder(s).reverse().toString();

        System.out.println("Reversed string: "+rev);
        sc.close();
    }
}
