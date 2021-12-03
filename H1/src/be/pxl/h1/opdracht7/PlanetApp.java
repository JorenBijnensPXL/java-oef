package be.pxl.h1.opdracht7;

public class PlanetApp {

    public static void main(String[] args) {
        Planet mars = new Planet();
        Planet neptunus = new Planet();

        mars.setName("Mars");
        neptunus.setName("Neptunus");

        mars.setDiameter(6792);
        mars.setDistanceToSun(227900000);

        neptunus.setDiameter(49528);
        neptunus.setDistanceToSun(4495100000L);

        if(mars.getDistanceToSun() < neptunus.getDistanceToSun()) {
            System.out.println(mars.getName());
        } else {
            System.out.println(neptunus.getName());
        }

        System.out.println("MARS: " + mars.getAE());
        System.out.println("NEPTUNUS: " + neptunus.getAE());
    }
}
