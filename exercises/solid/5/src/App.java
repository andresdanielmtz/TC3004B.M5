public class App {
    public static void main(String[] args) throws Exception {
        
        TransportService myService = new TransportService();

        myService.choseVehicle(0);
        myService.print_max_capacity();
        myService.print_max_dist();
        myService.ask_packet();

        myService.choseVehicle(1);
        myService.print_max_capacity();
        myService.print_max_dist();
        myService.ask_packet();
    }
}
