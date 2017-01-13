import java.util.Scanner;

public class Greetings {
	static int step;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = {3, 5, 7, 9, 11, 22, 27, 35, 42, 55, 65, 75, 95};
        System.out.println(binSearch(arr, arr.length - 1, 0, 65));
        System.out.println(binSearchIter(arr, arr.length - 1, 0, 65));
        Scanner input = new Scanner(System.in);
        System.out.println("Input Value to compute factorial");
        long value = input.nextLong();
        System.out.println(fact(value));
        System.out.println("Hola, mundo!");
        towers(20,1,3);
        input.close();
	}
	public static long fact(long n) {
        if (n == 1) return 1;
        else return n * fact(n - 1);
    }
    
    public static int handshake(int n) {
        if (n <= 1) {
            System.out.println("There must be more than one person in room");
            return -1;
        } else if (n == 2) return 1;
        else return handshake(n-1) + (n-1);
    }
    
    public static int fibonacci(int n) {
        if (n == 0) return 0;
        else if (n == 1) return 1;
        else return fibonacci(n-2) + fibonacci(n-1);
    }
    
    public static int binSearch (int [] data, int upperIndex, int lowerIndex, int value) {
        int middle = (upperIndex + lowerIndex) / 2;
        if (upperIndex - lowerIndex < 0) return -1;
        if (data[middle] == value) return middle;
        else if (data[middle] < value) return binSearch(data, upperIndex, middle+1, value);
        else return binSearch(data, middle-1, lowerIndex, value);
    }
    
    public static int binSearchIter (int[] data, int upperIndex, int lowerIndex, int value) {
        while (upperIndex >= lowerIndex) {
            int middle = (upperIndex + lowerIndex) / 2;
            if (data[middle] == value) return middle;
            else if (data[middle] < value) lowerIndex = middle + 1;
            else upperIndex = middle - 1;
        }
        return -1;
    }
       
    public static void towers(int num, int from, int to) {
        int temp = 6 - from - to;
        if (num == 1){
            System.out.println(++step + ": move disk 1 from " + from + " to " + to);
        } else {
            towers(num-1, from, temp);
            System.out.println(++step + ": move disk " + num + " from " + from + " to " + to);
            towers(num-1, temp, to);
        }
    }
    
    void demo(int num) {
        step = 0;
        towers(num, 1, 3);
    }
}
