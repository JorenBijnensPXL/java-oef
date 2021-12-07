package be.pxl.h2.opdracht3;
/* niet af*/
public class character {
    public static final int MAX_TITELS = 3;
    public static int count = 0;

    private String firstName;
    private String lastName;
    private String nickName;
    private String house;
    private int firstSeizon;
    private int lastSeizon;
    private int episodes;
    private String potrayedBy;
    private int numberOfTitels;
    private String[] titels = new String[MAX_TITELS];

    public character(String firstName, String lastName, String house, String potrayedBy) {
        this(firstName, lastName, "", house, 0, 0, 0, potrayedBy, 0);
    }

    public character(String firstName, String lastName, String nickName, String house, int firstSeizon, int lastSeizon, int episodes, String potrayedBy, int numberOfTitels) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.nickName = nickName;
        this.house = house;
        this.firstSeizon = firstSeizon;
        this.lastSeizon = lastSeizon;
        this.episodes = episodes;
        this.potrayedBy = potrayedBy;
        this.numberOfTitels = numberOfTitels;

    }

    public String toString(){
        String output = "";
        if (nickName == null || nickName.equals("")){
            output += String.format("%s %s of house %s%n", firstName, lastName, house);
        }else{
            output += String.format("%s \"%s\" %s of the house %s%n", firstName, nickName, lastName, house);
        }

        for(String title:titels){
            if (title != null){
                output +=  String.format("*** \"%s\"%n");
            }
        }
        return output;
    }
}
