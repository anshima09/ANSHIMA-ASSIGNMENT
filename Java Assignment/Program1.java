import java.util.*;
public class Program1{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Choose a shape:");
        System.out.println("1. Circle");
        System.out.println("2. Rectangle");
        System.out.println("3. Triangle");
        System.out.println("Enter your choice from 1-3: ");
        int choice= sc.nextInt();

        switch(choice){
            case 1: //circle
               System.out.println("Enter the radius: ");
               double radius=sc.nextDouble();
               double cirArea=Math.PI*radius*radius;
               System.out.println("Area of the circle: " +cirArea);
               break;
            case 2: //rectangle
               System.out.println("Enter the length of rectangle: ");
               double length=sc.nextDouble();
               System.out.println("Enter the width of rectangle: ");
               double width=sc.nextDouble();
               double rectArea=length*width;
               System.out.println("Area of the rectangle: " +rectArea);
               break;
            case 3: //Triangle
               System.out.println("Enter the base of triangle: ");
               double base=sc.nextDouble();
               System.out.println("Enter the height of triangle: ");
               double height=sc.nextDouble();
               double triArea=0.5*base*height;
               System.out.println("Area of the triangle: " +triArea);
               break;
            default:
               System.out.println("Please enter valid choice!");

        }

        sc.close();

    }
}