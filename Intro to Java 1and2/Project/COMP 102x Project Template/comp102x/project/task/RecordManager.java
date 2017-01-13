package comp102x.project.task;

import comp102x.project.model.GameRecord;

public class RecordManager {

    public GameRecord[] updateGameRecords(GameRecord[] oldRecords, GameRecord newRecord) {
        
        int count = 0;
        int minIndex = 0;
        boolean existingRecord = false;
        int indexExistingRecord = 0;
        GameRecord[] newRecords;
        newRecords = new GameRecord[oldRecords.length + 1]; 
        for (int i = 0; i < oldRecords.length; i++) {
           
            if (oldRecords[i].getLevel() == newRecord.getLevel()) {
                count++;
                if (oldRecords[i].getName().equals(newRecord.getName())) {
                    existingRecord = true;
                    indexExistingRecord = i;
                }
                if (oldRecords[i].getScore() <= oldRecords[minIndex].getScore()) minIndex = i;
            }
            newRecords[i] = oldRecords[i];
        }
        if (existingRecord) {
            if (newRecord.getScore() > oldRecords[indexExistingRecord].getScore()) {
                oldRecords[indexExistingRecord] = newRecord;
                Util.sort(oldRecords);
                return oldRecords;
            } else return oldRecords;
        } else if (count == 10) {
            if (newRecord.getScore() > oldRecords[minIndex].getScore()) {
                oldRecords[minIndex] = newRecord;
                Util.sort(oldRecords);
                return oldRecords;
            } else return oldRecords;
        } else {
            newRecords[oldRecords.length] = newRecord;
            Util.sort(newRecords);
            return newRecords;
        } // This line should be modified or removed upon finishing the implementation of this method.
    }
}
