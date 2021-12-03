package be.pxl.h2.opdracht1;

public class persoonApp {
    public static void main(String[] args) {
        persoon persoon = new persoon();
        persoon.setPersoon("bijnens", "joren", 1.89,64.5, 2003);
        System.out.print(persoon.toString());
        persoon.berekenBmi();
        System.out.printf("gezondheid : %s", persoon.geefOmschrijving());
    }
}
