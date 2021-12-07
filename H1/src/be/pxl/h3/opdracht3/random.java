package be.pxl.h3.opdracht3;

import java.util.Random;

public class random {
    public static void main(String[] args) {
        Random random = new Random();

        System.out.println(random.nextInt());

        for (int i=0;i<20;i++) {
            int getal = random.nextInt(10);
            System.out.println(getal);
        }

        for(int i=0; i<10; i++){
            int getal2 = random.nextInt(10,20);
            System.out.println(getal2);
        }
    }
}
