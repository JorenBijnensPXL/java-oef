package be.pxl.h3.opdracht1;

import java.util.Scanner;

public class tot3de {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("getal tot de 3de macht? ");
        double getal = scanner.nextDouble();
        Double result = Math.pow(getal, 3);
        System.out.printf("het resultaat is : %f", result);

    }
}