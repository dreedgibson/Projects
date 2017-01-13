import comp102x.IO;

/**
 * Demostrate the use of array for storing and manipulating a set of scores
 */
public class Scores
{
   //private double[][] scores; // declare a reference variable to an array
   
   private double[][] scores = {
     {99.0, 89.0, 85.0, 92.0}, 
     {90.0, 74.0, 75.0, 82.0},
     {85.0, 100.0, 64.0, 91.0},
     {72.0, 82.0, 81.0, 94.0}
    };

   /**
    * SetScore asks user to enter score for each array element
    */
   public void initializeAllScores() {       
      scores = new double[4][4];  
      scores[0][0] = 99.0; scores[0][1] = 89.0;
      scores[0][2] = 85.0; scores[0][3] = 92.0;
      
      scores[1][0] = 90.0; scores[1][1] = 74.0;
      scores[1][2] = 75.0; scores[1][3] = 82.0;  
      
      scores[2][0] = 85.0; scores[2][1] = 100.0;    
      scores[2][2] = 64.0; scores[2][3] = 91.0;

      scores[3][0] = 72.0; scores[3][1] = 82.0;
      scores[3][2] = 81.0; scores[3][3] = 94.0;

    }
    
   public double getScoreByIndices(int rowIndex, int colIndex, int numOfCols) {    
        int numOfRows = scores.length;                        

        if ( rowIndex < 0 || rowIndex >= numOfRows )
            return -1.0;        
        if ( colIndex < 0 || colIndex >= numOfCols )
            return -1.0;            

        return scores[rowIndex][colIndex]; 
    }
    
   public void printAllScores() {
       int numOfRows = scores.length;                        
       
       for ( int r=0; r<numOfRows; r++) {
           int numOfCols = scores[r].length; 
           IO.output("Row " + r + " : ");
           for (int c=0; c<numOfCols; c++) {
                IO.output(getScoreByIndices(r,c,numOfCols) + " " );
            } // for loop c
            IO.outputln(""); // next line
        } // for loop r
    } 
   
   public double aveByRow(int row) {
       double sum = 0; // for storing sum
       int numOfCols = scores[row].length;
   
       for (int i = 0; i < numOfCols; i++) {
           sum += scores[row][i];
       }
       return sum / numOfCols;
   }
   
   public double aveByCol(int col) {
       double sum = 0; // for storing sum
       int numOfRows = scores.length;
   
       for (int i = 0; i < numOfRows; i++) {
           sum += scores[i][col];
       }
       return sum / numOfRows;
   }
   
   public double aveTwoDArr() {
       double sum = 0; // for storing sum
       int count = 0; // count of total values in array
       int numOfRows = scores.length;
   
       for (int i = 0; i < numOfRows; i++) {
           int numOfCols = scores[i].length;
           for (int j = 0; j < numOfCols; j++) {
               sum += scores[i][j];
               count++;
           }
       }
       return sum / count;
   }
   
   public int maxColIndex(int row) {
       int mIndex = 0; // index for current maximum
       int numOfCols = scores[row].length;
   
       for (int i = 0; i < numOfCols; i++) {
           if (scores[row][i] > scores[row][mIndex]) mIndex = i;
       }
       return mIndex;
   }
   
   public int maxRowIndex(int col) {
       int mIndex = 0; // index for current maximum
       int numOfRows = scores.length;
   
       for (int i = 0; i < numOfRows; i++) {
           if (scores[i][col] > scores[mIndex][col]) mIndex = i;
       }
       return mIndex;
   }
   
   public int[] maxTwoDArrIndex() {
       int[] answerArray = new int[2];
       answerArray[0] = 0; //row 
       answerArray[1] = 0; //col
       int numOfRows = scores.length;
   
       for (int i = 0; i < numOfRows; i++) {
           int numOfCols = scores[i].length;
           for (int j = 0; j < numOfCols; j++) {
               if (scores[i][j] > scores[answerArray[0]][answerArray[1]]) {
                    answerArray[0] = i;
                    answerArray[1] = j;
               }
               
           }
       }
       return answerArray;
   }
}