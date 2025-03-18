

 class First extends Thread{
    public void run(){
        System.out.println("Priority of "+Thread.currentThread().getName()+" is: "+Thread.currentThread().getPriority());
    }
}

public class Program26 {
    public static void main(String[] args) {
        First t1=new First();
        First t2=new First();

        t1.start();
        t2.start();
    }
}


//implement using runnable interface

/*

class Second implements Runnable {
 public void run() {
        System.out.println("Priority of "+Thread.currentThread().getName()+" is: "+Thread.currentThread().getPriority());
 }
}

public class Program26 {
    public static void main(String[] args) {
    Thread t1 = new Thread(new MyRunnable());
    Thread t2 = new Thread(new MyRunnable());
    t1.start();
    t2.start();
    }
   }

 
   */