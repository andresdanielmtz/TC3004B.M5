/*
 * SOLID Principles: Interface Segregation Principle (ISP) - Team 35
 * Victor Javier Quintana Cisneros - A01643020
 * Jean Paul López Pandura - A01637266
 */


public class ISPExercise {
    public static void main(String[] args) {
        DeliveryDriver deliveryDriver = new DeliveryDriver("John Doe", "john.doe@example.com");
        deliveryDriver.work();
        deliveryDriver.deliver();
        deliveryDriver.receive();

        RouteAdmin routeAdmin = new RouteAdmin("Jane Doe", "jane.doe@example.com");
        routeAdmin.work();
        routeAdmin.track();
        routeAdmin.getRoute();
        routeAdmin.optimizeRoute();

        CustomerService customerService = new CustomerService("Alice Smith", "alice.smith@example.com");
        customerService.work();
        customerService.track();
    }
}

class DeliveryDriver extends Employee implements Deliverable {
    public DeliveryDriver(String name, String email) {
        super(name, email);
    }

    // La anotación @Override no es requerida para implementar métodos, pero es buena práctica por algunas razones:
    // 1. Indica claramente al desarrollador que se está sobrescribiendo un método de una interfaz o clase padre.
    // 2. Detecta errores de ortografía y errores de firma de método, lanzando error en lugar de crear un método nuevo sin Override.
    @Override
    public void work() {
        System.out.println("Picking up package...");
        receive();
        System.out.println("Delivering package...");
        deliver();
    }

    @Override
    public void deliver() {
        System.out.println("Marking package as delivered.");
    }

    @Override
    public void receive() {
        System.out.println("Receiving package.");
    }
}

class RouteAdmin extends Employee implements Trackable, Routable {
    public RouteAdmin(String name, String email) {
        super(name, email);
    }

    @Override
    public void work() {
        System.out.println("Route admin is working.");
        track();
        getRoute();
        optimizeRoute();
    }

    @Override
    public void track() {
        System.out.println("Route admin is tracking package.");
    }

    @Override
    public void getRoute() {
        System.out.println("Getting route.");
    }

    @Override
    public void optimizeRoute() {
        System.out.println("Optimizing route.");
    }
}

class CustomerService extends Employee implements Trackable {
    public CustomerService(String name, String email) {
        super(name, email);
    }

    public void work() {
        System.out.println("Customer service is working.");
        track();
    }

    @Override
    public void track() {
        System.out.println("Customer service is tracking package.");
    }
}
