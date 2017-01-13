import java.io.*;
import java.util.Scanner;
import comp102x.IO;

public class Students2DArray {
    public static final int maxN = 40;
    public String[][] studentNames = new String[maxN][2];
    public int nStudents;

    public void readStudentNamesToArray() throws IOException {
        // 1. Create a File and Scanner objects
        File inputFile = new File("studentnames.txt");
        Scanner input = new Scanner(inputFile); 
        Scanner line;
        // 2. read the content and then store in an array using a loop
        for (int i=0;  input.hasNextLine(); i++) {  
              String inputStudentName = input.nextLine();   
              line = new Scanner(inputStudentName);         
              if (i >= maxN) break;
              studentNames[i][0] = line.next();
              studentNames[i][1] = line.next();
              nStudents++;       
           }       
         // 3. close the file and print the result
        input.close();     
       }
    
    public int findLastName(int size) {
        int maxIndex = 0;
        if (size > studentNames.length) size = studentNames.length;
        for (int i = 0; i < size; i++) {
            if (studentNames[i][1].compareToIgnoreCase(studentNames[maxIndex][1]) > 0) maxIndex = i;
        }
        return maxIndex;
    }
    
    public void swapNames(int pos1, int pos2) {
        String temp[][] = new String [1][2];
        for (int i = 0; i < studentNames[1].length; i++) {
            temp[0][i] = studentNames[pos1][i];
            studentNames[pos1][i] = studentNames[pos2][i];
            studentNames[pos2][i] = temp[0][i];
        }
    }
    
    public void alphaSort() {
        for (int i = 0; i < nStudents; i++) {
            int maxIndex = findLastName(nStudents - i);
            swapNames(maxIndex, nStudents - i - 1);
        }
    }
    
    public void outputNamesInArray( ) throws IOException {
        // 1.1 Create a File and PrintWriter objects
        File outputFile = new File("outputa.txt");
        PrintWriter writer = new PrintWriter(outputFile);     
        // 2. read the content and then store in an array using a loop
        for (int i=0;  i < nStudents; i++) {  
              writer.println(studentNames[i][1] + ", " + studentNames[i][0]);           
        }       
        // 3. close the file and print the result
        writer.close();     
     }

}
