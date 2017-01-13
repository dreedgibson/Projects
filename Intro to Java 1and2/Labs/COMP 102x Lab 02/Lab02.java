import comp102x.IO;

public class Lab02
{
    
    public static void multiply()
    {
        // Please write your code after this line
        IO.output("Enter an integer, x: ");
        double x = IO.inputDouble();
        IO.output("Enter an integer, y: ");
        double y = IO.inputDouble();
        int answer = (int) x * (int) y;
        IO.output("Answer = " + answer);
        
        
        
    }
    
    public static void calculateTriangleArea()
    {
        // Please write your code after this line
        IO.output("Enter the width of the triangle: ");
        double w = IO.inputDouble();
        IO.output("Enter the height of the triangle: ");
        double h = IO.inputDouble();
        double answer = (h * w) / 2.0; 
        IO.output("The triangle area = " + answer); 
        
        
        
        
    }
    
    public static void solveQuadraticEquation()
    {
        // Please write your code after this line
        IO.output("Enter a: ");
        double a = IO.inputDouble();
        IO.output("Enter b: ");
        double b = IO.inputDouble();
        IO.output("Enter c: ");
        double c = IO.inputDouble();
        double answer1 = ((-1 * b) + Math.sqrt((b * b) - (4 * a * c))) / (2.0 * a);
        double answer2 = ((-1 * b) - Math.sqrt((b * b) - (4 * a * c))) / (2.0 * a);
        IO.output("First solution for x = " + answer1 + '\n');
        IO.output("Second solution for x = " + answer2);    
        
        
        
        
    }
}
