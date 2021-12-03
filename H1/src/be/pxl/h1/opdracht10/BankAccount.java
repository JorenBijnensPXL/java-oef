package be.pxl.h1.opdracht10;

public class BankAccount {
    private String name;
    private String code;
    private int controlDigits;
    private long number;
    private double amount;

    public double getAmount() {
        return amount;
    }

    public void setAmount(double amount) {
        this.amount = amount;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setControlDigits(int controlDigits) {
        this.controlDigits = controlDigits;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public void setNumber(long number) {
        this.number = number;
    }

    public String getAccount() {
        return String.format("%s%02d%d",code,controlDigits,number);
    }

    public boolean isValid() {
        long stap1 = number * 1000000 + 111400;
        int stap2 = (int) (stap1 % 97);
        int controle = 98 - stap2;

        return controle == controlDigits;
    }

    public void withdraw(double amount) {
        if(this.amount >= amount) {
            this.amount -= amount;
        } else {
            System.out.println("Ontoereikend saldo");
        }
    }
}
