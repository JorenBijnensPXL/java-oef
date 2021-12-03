package be.pxl.h1.opdracht13;

public class SalesApp {
    public static void main(String[] args) {
        SalesPerson person = new SalesPerson();
        person.setMonthlySale(0, 17000);
        person.setMonthlySale(1, 13000);
        person.setMonthlySale(2, 6000);

        System.out.println(person.getTotalSale());
        System.out.println(person.getAverageSale());
    }
}
