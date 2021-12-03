package be.pxl.h1.opdracht2;

public class Auto {
    private String kleur;
    private String merk;
    private int kilometerstand;
    private int aantalDeuren;
    private boolean automaat;

    public void setKleur(String kleur) {
        this.kleur = kleur;
    }

    public String getKleur() {
        return this.kleur;
    }

    public void setMerk(String merk) {
        this.merk = merk;
    }

    public String getMerk() {
        return merk;
    }

    public void setKilometerstand(int kilometerstand) {
        this.kilometerstand = kilometerstand;
    }

    public int getKilometerstand() {
        return kilometerstand;
    }

    public void setAantalDeuren(int aantalDeuren) {
        this.aantalDeuren = aantalDeuren;
    }

    public int getAantalDeuren() {
        return aantalDeuren;
    }

    public void setAutomaat(boolean automaat) {
        this.automaat = automaat;
    }

    public boolean getAutomaat() {
        return automaat;
    }

    public int getPrijs() {
        int prijs = 20000;

        if(aantalDeuren == 5) {
            prijs += 2000;
        } else if(aantalDeuren == 3) {
            prijs -= 500;
        }

        if(automaat) {
            prijs += 2000;
        } else {
            prijs = (int) (prijs * 0.98);
        }

        return prijs;
    }

}
