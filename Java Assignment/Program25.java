import java.io.FileInputStream;

import java.io.FileNotFoundException;

import java.io.IOException;
public class Program25 {
    public static void main(String[] args){
        try{
            FileInputStream fis=new FileInputStream("C:/Users/anshima/OneDrive/Desktop/Myjava/Test.txt");
            /*byte b[]=new byte[fis.available()];
            fis.read(b);
            String str=new String(b);
            System.out.println(str);*/

            // int x;
            // do{
            //     x=fis.read();
            //     System.out.print((char)x);    with do while it will print an extra character
            // }while(x!=-1);


            int x;
            while((x=fis.read())!=-1){
                System.out.print((char)x);
            }
            fis.close();
        }
        catch(FileNotFoundException e){
            System.out.println(e);
        }
        catch(IOException e){
            System.out.println(e);
        }
    }
}
