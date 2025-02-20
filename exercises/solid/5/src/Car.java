public class Car extends Vehicle{
    public void move(){
        System.out.println("Driving to your location");
    }

    public int max_distance(){
        return 50;
    }

    public int max_capacity(){
        return 50;
    }
}
