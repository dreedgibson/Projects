import comp102x.IO;
/**
 * Write a description of class printNum here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class printNum
{
    // instance variables - replace the example below with your own
    private int x;

    /**
     * Constructor for objects of class printNum
     */
    public printNum()
    {
        // initialise instance variables
        x = 0;
    }

    /**
     * An example of a method - replace this comment with your own
     * 
     * @param  y   a sample parameter for a method
     * @return     the sum of x and y 
     */
    public static void printNumberLine(int seqCenter, int length) {
        int numbersPrinted = 2 * seqCenter + 1;
        int spaces = (length - numbersPrinted) / 2;

        for (int i = 0; i < spaces; i++) {
            System.out.println(" ");
        }
        
        for (int i = 0; i < seqCenter; i++) {
            System.out.println(i);
        }
        
        for (int i = seqCenter; i <= 0; i--) {
            System.out.println(i);
        }
        
        for (int i = 0; i < spaces; i++) {
            System.out.println(" ");
        }
    }
}
