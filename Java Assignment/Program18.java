class Student{
    private String name;
    private int rollNo;

    public Student(String name,int rollNo){
        this.name=name;
        this.rollNo=rollNo;
    }

    

    public void display(){
        System.out.println("Student Name: "+name);
        System.out.println("Roll Number: "+rollNo);
    }
    public void display(String course){
        System.out.println("Student Name: "+name);
        System.out.println("Roll Number: "+rollNo);
        System.out.println("Course: "+course);

    }


 }

 class GraduateStudent extends Student {
    private String specialization;

    // Constructor
    public GraduateStudent(String name, int rollNumber, String specialization) {
        super(name, rollNumber); // Calling parent constructor
        this.specialization = specialization;
    }

    // Method Overriding (Runtime Polymorphism)
    @Override
    public void display() {
        super.display(); // Calling parent method
        System.out.println("Specialization: " + specialization);
    }
}


public class Program18 {

    public static void main(String[] args) {
        Student s1=new Student("Anshima", 11);
        System.out.println("Student details:");
        s1.display();
        

        System.out.println("Student details with course:");
        s1.display("Java");

        GraduateStudent g1=new GraduateStudent("Abhishek", 10, "CS");
        g1.display();
    }
}

