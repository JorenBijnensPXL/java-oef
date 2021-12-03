package be.pxl.h1.opdracht9;

import java.util.Scanner;

public class ThermoApp {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Thermometer thermo = new Thermometer();

        System.out.print("Geef de temperatuur: ");
        double temp = input.nextDouble();
        thermo.setTemperature(temp);

        System.out.println(thermo.getTemperature());
        System.out.println(thermo.getFahrenheit());

        System.out.printf("|%10s|%10s|%n", "Celsius", "Fahrenheit");
        for(int c=-10;c<=25;c+=5) {
            thermo.setTemperature(c);
            System.out.printf("|%10.2f|%10.2f|%n", thermo.getTemperature(), thermo.getFahrenheit());
        }
    }
}
