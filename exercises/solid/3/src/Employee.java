public class Employee {
    String name;
    String email;

    public Employee(String name, String email) {
        this.name = name;
        this.email = email;
    }

    public void work() {
        System.out.println(name + " is working (at a logistics company!)");
    }
}