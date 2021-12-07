package be.pxl.h3.opdracht6;

import java.util.Locale;

public class tekst {
    public static void main(String[] args) {
        String tekst = new String("hoi");
        System.out.println(tekst);

        tekst = tekst.replace("o","a");
        System.out.println(tekst);

        int count = 0;
        for(char c:tekst.toCharArray()){
            if(c == 'e'){
                count++;
            }
        }
        System.out.println(count);

        String andere = "andere";
        System.out.println("zelfde? " + tekst.equals(andere));

        String woord = "pizza";
        int capFrom = woord.length()/2;
        int capTo = capFrom + 1;
        if(woord.length()%2 == 0){
            capFrom = (woord.length()/2)+1;
            capTo = capFrom + 2;
        }
        String output = woord.substring(0,capFrom);
        output += woord.substring(capFrom, capTo).toUpperCase();
        output += woord.substring(capTo);
        System.out.println(output);
    }
}
