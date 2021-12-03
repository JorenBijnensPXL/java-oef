package be.pxl.h1.opdracht13;

public class SalesPerson {
    private String naam;
    private double[] verkoopscijfers = new double[12];

    public void setMonthlySale(int maand, double bedrag) {
        verkoopscijfers[maand] = bedrag;
    }

    public double getTotalSale() {
        double total = 0;
        for(double s : verkoopscijfers) {
            total += s;
        }
        return total;
    }

    public double getAverageSale() {
        double total = getTotalSale();
        return total/verkoopscijfers.length;
    }

}
