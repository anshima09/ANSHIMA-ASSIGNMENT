abstract class Animal {
    abstract void makeSound();
}

interface Pet {
    void play();
}

class Dog extends Animal implements Pet {
    @Override
    void makeSound() {
        System.out.println("Dog barks");
    }

    @Override
    public void play() {
        System.out.println("Dog is playing");
    }
}

public class Program23 {
    public static void main(String[] args) {
       Dog d=new Dog();
       d.makeSound();
       d.play();
    }
}
