package be.pxl.h1.opdracht5;

public class StripboekApp {

    public static void main(String[] args) {
        Stripboek boek = new Stripboek();
        Stripboek boek2 = new Stripboek();

        boek.setReeks("Jommeke");
        boek.setTitel("Jommeke schrijft Java programmas");
        boek.setAlbum(5);
        boek.setAuteur("Jef Nys");

        boek2.setReeks("Suske & Wiske");
        boek2.setTitel("hebben nog een beetje honger");
        boek2.setAlbum(15);
        boek2.setAuteur("Willy Vandersteen");

        boek.print();
        boek2.print();
    }
}
