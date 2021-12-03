package be.pxl.h1.opdracht5;

public class Stripboek {

    private String reeks;
    private String titel;
    private int album;
    private String auteur;

    public String getReeks() {
        return reeks;
    }

    public String getTitel() {
        return titel;
    }

    public String getAuteur() {
        return auteur;
    }

    public int getAlbum() {
        return album;
    }

    public void setReeks(String reeks) {
        this.reeks = reeks;
    }

    public void setTitel(String titel) {
        this.titel = titel;
    }

    public void setAuteur(String auteur) {
        this.auteur = auteur;
    }

    public void setAlbum(int album) {
        this.album = album;
    }

    public void print() {
        System.out.println(reeks + ": " + titel);
        System.out.println("Nummer " + album);
        System.out.println("Auteur: " + auteur);
    }
}
