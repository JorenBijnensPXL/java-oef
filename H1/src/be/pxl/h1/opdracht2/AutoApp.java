package be.pxl.h1.opdracht2;

public class AutoApp {

    public static void main(String[] args) {
        System.out.println("Dit programma maakt een auto");
        Auto car = new Auto();
        Auto car2 = new Auto();

        car.setKleur("rood");
        car.setMerk("Renault");
        car.setAantalDeuren(7);
        car.setKilometerstand(50000);
        car.setAutomaat(false);

        System.out.println(car.getMerk() + " (" + car.getKleur() + ")");
        System.out.println("Aantal deuren: " + car.getAantalDeuren());
        System.out.println(car.getKilometerstand() + " km");
        System.out.println("Prijs van de wagen: " + car.getPrijs());
    }
}
