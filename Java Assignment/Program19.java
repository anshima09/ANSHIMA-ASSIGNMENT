class Student{
    private String name;
    private int rollNo;
    private double marks;

    public Student(String name,int rollNo, double marks){
        this.name=name;
        this.rollNo=rollNo;
        this.marks=marks;
    }

    public String getName(){
        return name;
    }

    public void setName(String name){
        this.name=name;
    }

    public int getRollNo(){
        return rollNo;
    }
    public void setRollNo(int rollNo){
        this.rollNo=rollNo;
    }
   
    public double getMarks(){
        return marks;

    }
    public void setMarks(double marks){
        if (marks >= 0 && marks <= 100) {
            this.marks = marks;
        } else {
            System.out.println("Invalid marks! Please enter between 0 and 100.");
        }
    }

    public void display(){
        System.out.println("Student Name: "+name);
        System.out.println("Roll Number: "+rollNo);
        System.out.println("Marks: "+marks);
    }


 }
 
public class Program19 {

    public static void main(String[] args) {
        Student s1=new Student("Anshima",11 , 98);
        s1.display();
        s1.setMarks(95.5);
        System.out.println("Updates details: ");
        s1.display();
        
    }
}

