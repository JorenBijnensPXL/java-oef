package be.pxl.h3.opdracht2;
import java.util.Scanner;

public class volumePizza {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("straal van de pizza ");
        double a = 1;
        double z = scanner.nextDouble();
        double result = Math.pow(z, 2) * Math.PI * a;
        System.out.printf("het volume van de pizza is %.2f cm³", result);

    }
}
