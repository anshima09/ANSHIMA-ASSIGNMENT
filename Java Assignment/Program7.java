import java.util.Scanner;

public class Program7 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter first number: ");
        int n1=sc.nextInt();
        System.out.println("Enter second number: ");
        int n2=sc.nextInt();

        //Arithmetic Operators
        System.out.println("--------------------Arithmetic Operators-------------------");
        System.out.println("Addition (n1+n2): " +(n1+n2));
        System.out.println("Subtraction (n1-n2): "+(n1-n2));
        System.out.println("Multiplication: (n1*n2): "+(n1*n2));
        System.out.println("Division (n1/n2): "+(n1/n2));
        System.out.println("Modulus (n1%n2): "+(n1%n2));

        //Relational Operators
        System.out.println("----------------Relational Operators-------------------");
        System.out.println("n1==n2: "+(n1==n2));
        System.out.println("n1!=n2: "+(n1!=n2));
        System.out.println("n1>n2: "+(n1>n2));
        System.out.println("n1<n2: "+(n1<n2));
        System.out.println("n1>=n2: "+(n1>=n2));
        System.out.println("n1<=n2: "+(n1<=n2));

        boolean val1= (n1>0);
        boolean val2= (n2>0);

        System.out.println("------------------Logical Operators--------------------");
        System.out.println("AND Condition (val1 && val2): "+(val1&&val2));
        System.out.println("OR Condition (val1 || val2): "+(val1||val2));
        System.out.println("NOT Condition (!val1): "+(!val1));
        sc.close();
    }
}
