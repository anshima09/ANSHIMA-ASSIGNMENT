import java.util.Scanner;

public class Program24 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        try{
            System.out.println("Enter a number:");
            int num=sc.nextInt();
            System.out.println("Enter divisor which divides the number:");
            int div=sc.nextInt();

            int ans=num/div;
            System.out.println("Result is: "+ans);
        }

        catch(ArithmeticException e){
            System.out.println("Number cannot divided by zero");
        }
        catch(Exception e){
            System.out.println("Error occurred");
        }
        finally{
            System.out.println("Execution Completed");
            sc.close();
        }
    }

}
