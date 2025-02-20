public class TransportService {
    Vehicle chosenVehicle;

    public void choseVehicle(int type){
        if (type == 1) {
            chosenVehicle = new Car();
        } else {
            chosenVehicle = new Bicycle();
        }
    }

    public void print_max_dist(){
        System.out.println("The max distance this vehicle can move is " + chosenVehicle.max_distance() + " km");
    }

    public void print_max_capacity(){
        System.out.println("The max capacity this vehicle can carry is " + chosenVehicle.max_capacity() + " kg");
    }

    public void ask_packet(){
        chosenVehicle.move();
    }
}
