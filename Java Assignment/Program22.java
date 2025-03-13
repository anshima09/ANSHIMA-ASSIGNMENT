import java.util.Arrays;
import java.util.Scanner;

public class Program22 {

    public static boolean anagram(String str1,String str2){
        str1 = str1.replaceAll("\\s", "").toLowerCase();
        str2 = str2.replaceAll("\\s", "").toLowerCase();

        // If lengths are different, they can't be anagrams
        if (str1.length() != str2.length()) {
            return false;
        }

        
        char[] arr1 = str1.toCharArray();
        char[] arr2 = str2.toCharArray();
        Arrays.sort(arr1);
        Arrays.sort(arr2);

        
        return Arrays.equals(arr1, arr2);
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter first string: ");
        String s1=sc.nextLine();
        System.out.println("Enter second string: ");
        String s2=sc.nextLine();

        if(anagram(s1,s2)){
            System.out.println("Two strings are anagrams");
        }
        else{
            System.out.println("Two strings are not anagrams");
        }
        sc.close();
    }
}
