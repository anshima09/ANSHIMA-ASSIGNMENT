import java.util.Scanner;

public class Program21 {
    public static int vowelCount(String s){
        int count=0;
        String vowels="aeiouAEIOU";
        for(char ch:s.toCharArray()){
            if(vowels.indexOf(ch)!=-1){
                count++;
            }
        }
       return count;
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter s string: ");
        String s=sc.nextLine();
        int count=vowelCount(s);
        System.out.println("Number of vowels: "+count);
        sc.close();
    }
}
