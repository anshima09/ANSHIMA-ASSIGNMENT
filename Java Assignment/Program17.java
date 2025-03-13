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
        this.marks=marks;
    }

    public void display(){
        System.out.println("Student Name: "+name);
        System.out.println("Roll Number: "+rollNo);
        System.out.println("Marks: "+marks);
    }


 }

 class GraduateStudent extends Student{
    private String specialization;
    private String city;

    public GraduateStudent(String name,int rollNo,double marks,String specialization, String city){
        super(name,rollNo,marks);
        this.specialization=specialization;
        this.city=city;
    }
    public String getSpecialization() {
        return specialization;
    }

    public void setSpecialization(String specialization) {
        this.specialization = specialization;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    @Override
    public void display() {
        super.display(); // Call parent class method
        System.out.println("Specialization: " + specialization);
        System.out.println("City: " + city);
    }
 }


public class Program17 {

    public static void main(String[] args) {
        GraduateStudent g1 = new GraduateStudent("Anshima", 10, 89.5, "Computer Science", "Indore");
        g1.display();
        g1.setSpecialization("Information Technology");
        System.out.println("After updating: ");
        g1.display();
    }
}

