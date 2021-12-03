package be.pxl.h1.opdracht7;

public class Planet {

    private String name;
    private long distanceToSun;
    private int diameter;

    public String getName() {
        return name;
    }

    public long getDistanceToSun() {
        return distanceToSun;
    }

    public int getDiameter() {
        return diameter;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setDistanceToSun(long distanceToSun) {
        this.distanceToSun = distanceToSun;
    }

    public void setDiameter(int diameter) {
        this.diameter = diameter;
    }

    public double getAE() {
        return (distanceToSun / 149600000.0);
    }
}
