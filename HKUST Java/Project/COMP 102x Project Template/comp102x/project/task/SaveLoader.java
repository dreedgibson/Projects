package comp102x.project.task;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;

import comp102x.project.model.GameRecord;

public class SaveLoader {
	
	public void saveGameRecords(GameRecord[] records, String filename) throws FileNotFoundException {
		
		PrintWriter fileWriter = new PrintWriter(new File(filename));
        
        for (int i = 0; i < records.length; i++) {
            fileWriter.println(records[i].getName() + '\t' + records[i].getLevel() +'\t' + records[i].getScore());
        }
        fileWriter.close();
	}
	
	public GameRecord[] loadGameRecords(String filename) throws FileNotFoundException {
		
		// write your code after this line
        // maximum amount of game records:
        int MAXSIZE = 30;
        
        Scanner input = new Scanner(new File(filename));
        int size = 0;
        
        // create the GameRecord return variable
        GameRecord[] recordsMax = new GameRecord[MAXSIZE];
        
        for (int i = 0; input.hasNextLine(); i++) {
            String inputGameRecord = input.nextLine();
            Scanner line = new Scanner(inputGameRecord);
            recordsMax[i] = new GameRecord(line.next(),line.nextInt(),line.nextInt());
            size++;
        }
        // create the GameRecord return variable
        GameRecord[] records = new GameRecord[size];
        
        for (int i = 0; i < size; i++) {
            records[i] = recordsMax[i];
        }
        
        return records; // This line should be modified or removed after finising the implementation of this method.
	}

}
