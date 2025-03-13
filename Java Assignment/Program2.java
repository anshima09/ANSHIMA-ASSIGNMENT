import java.util.*;
public class Program2 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter a number: ");
        int num=sc.nextInt();

        //check if the number is even or odd
        if (num%2==0){
            System.out.println("Number is even");
        }
        else{
            System.out.println("Number is odd");
        }

        sc.close();
    }
}
