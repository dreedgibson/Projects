import java.util.Stack;

public class Questions {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] a = {{0, 1, 2, 3, 2},
					 {1, 2, 3, 2, 1},
					 {2, 3, 2, 1, 0}};
		System.out.println(histogram(a, 3));
		System.out.println(removeRepeatedWords("cat fat cat cat hat"));
		System.out.println(powerOfTen(454321));
		System.out.println(reverseDigits(454321));
	}
	
	public static int[] histogram(int[][] a, int high) {
		int[] h = new int[high + 1];
		for (int i = 0; i < a.length; i++) {
			for (int j = 0; j < a[i].length; j++) {
				h[a[i][j]]++;
			}
		}
		
		return h;		
	}
	
	public static String removeRepeatedWords(String inputString) {

        inputString = inputString.trim(); // Remove any leading and trailing blanks
        String result = "", currentWord = "", nextWord = "";
        int stringLength = inputString.length(); // Length of the input string
        int stringIndex = 0; // Index for input string
        
        while (stringIndex < stringLength) {
        
                // Get the next word in inputString
                while (stringLength > stringIndex && inputString.charAt(stringIndex) != ' ') {
                
                        nextWord = nextWord + inputString.charAt(stringIndex);
                        stringIndex++;
                }
                // Check if nextWord is the same as currentWord
                if (!nextWord.equals(currentWord)) {
                
                        result = result + nextWord + " ";
                }
                
                stringIndex++;
                currentWord = nextWord;
                nextWord = "";
        }
        
        return result.trim(); // Remove any leading and trailing blanks from result
        
	}
	
	public static int powerOfTen(int n) {

        // Please write your code after this line
		if (n / 10 == 0) return 1;
		else return 10 * powerOfTen(n / 10);
	}
	

	public static int reverseDigits(int n) {

        // Please write your code after this line
		if (n / 10 == 0) return n;
		else return (n % 10) * powerOfTen(n) + reverseDigits(n / 10);
	}
	
	public static void arrangeStack(Stack<Integer> original) {

        // Please write your code after this line
		Stack<Integer> even = new Stack();
		Stack<Integer> odd = new Stack();
		while (!original.empty()) {
			int x = original.pop();
			if (x % 2 == 0) even.push(x);
			else odd.push(x);
		}
		while (!odd.empty()) {
			original.push(odd.pop());
		}
		while (!even.empty()) {
			original.push(even.pop());
		}
	}
}
