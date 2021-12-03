package be.pxl.h1.opdracht10;

import java.util.Scanner;

public class BankApp {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        BankAccount account = new BankAccount();
        account.setName("Sam Vanderstraeten");
        account.setCode("BE");
        account.setControlDigits(3);
        account.setNumber(539007547034L);

        System.out.println(account.getAccount());
        System.out.println("Geldig? " + account.isValid());

        // Opdracht 11
        System.out.print("Geef een startbedrag? ");
        double startbedrag = input.nextDouble();
        input.nextLine();
        account.setAmount(startbedrag);

        System.out.print("Wil je geld afhalen? ");
        String afhalen = input.nextLine();

        while(afhalen.equals("J") && account.getAmount() > 0) {
            System.out.printf("Hoeveel geld? (max. %.2f euro) ", account.getAmount());
            double bedrag = input.nextDouble();
            input.nextLine();
            account.withdraw(bedrag);

            if(account.getAmount() > 0) {
                System.out.print("Wil je geld afhalen? ");
                afhalen = input.nextLine();
            }
        }

        System.out.println("Doei");
        input.close();
    }
}
