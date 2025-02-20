public class Bicycle extends Vehicle{
    public void move(){
        System.out.println("Pedalling to your location");
    }

    public int max_distance(){
        return 10;
    }

    public int max_capacity(){
        return 10;
    }
}
