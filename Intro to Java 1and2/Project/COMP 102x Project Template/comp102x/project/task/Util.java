package comp102x.project.task;

import comp102x.project.model.GameRecord;

public class Util {
    
    public static void sort(GameRecord[] records) {
    
        int minIndex;
        int remaining = records.length;

        while (remaining > 1) {

            minIndex = minPos(records, remaining);
            swap(records, minIndex, --remaining);
        }
    }

    private static int minPos(GameRecord[] records, int size) {

       int minIndex = 0;
       int minLevel = 3;
       if (size > records.length) size = records.length;
       for (int i = 0; i < size; i++) {
            if (records[i].getLevel() > records[minIndex].getLevel()) continue;
            else if (records[i].getLevel() == records[minIndex].getLevel()) {
                if (records[i].getScore() <= records[minIndex].getScore()) minIndex = i;
            }
            else minIndex = i;
       }
       return minIndex; // This line should be modified or removed after finising the implementation of this method.
    }

    private static void swap(GameRecord[] array, int index1, int index2) {

        GameRecord temp = array[index1];
        array[index1] = array[index2];
        array[index2] = temp;
    }
}
