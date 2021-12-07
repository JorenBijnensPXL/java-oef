package be.pxl.h2.opdracht1;

public class persoon {

    private String naam;
    private String voornaam;
    private double lengte;
    private double gewicht;
    private int geboorteJaar;
    private double bmi;
    private int gegroeid;

    /*
    public String naam;
    public String voornaam;
    public double lengte;
    public double gewicht;
    public int geboorteJaar;
    */

    public void setPersoon(String naam, String voornaam, double lengte,double gewicht, int geboorteJaar) {
        this.naam = naam;
        this.voornaam = voornaam;
        setLengte(lengte);
        this.gewicht = gewicht;
        this.geboorteJaar = geboorteJaar;
    }

    public void setLengte(double lengte){
        if (lengte > 2.4){
            this.lengte = 2.4;
        }else{
            this.lengte = lengte;
        }
    }

    public String toString(){
        return String.format("Deze persoon is %s%n%-20s : %.2f%n%-20s : %.2f%n%-20s : %d%n",voornaam + " " + naam, "gewicht", gewicht, "lengte", lengte, "geboortejaar", geboorteJaar);
    }

    public void berekenBmi(){
        bmi = gewicht / (lengte * lengte);
    }

    public String geefOmschrijving(){
        String gezondheid = "";
        if (bmi < 18){
            gezondheid = "ondergewicht";
        }
        if (bmi >= 18 && bmi < 25){
            gezondheid = "normaal";
        }
        if (bmi >= 25 && bmi < 30){
            gezondheid = "overgewicht";
        }
        if (bmi >= 30 && bmi < 40){
            gezondheid = "obesitas";
        }
        if (bmi >= 40){
            gezondheid = "morbide obesitas";
        }
        return gezondheid;
    }
/*
    public void groei(int lengtes){
        this(lengtes, 1);
    }

    public void groei(int lengtes, int groei){
        gegroeid = lengtes;
    }*/
}