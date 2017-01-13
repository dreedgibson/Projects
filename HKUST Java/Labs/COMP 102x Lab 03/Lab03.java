import comp102x.ColorImage;
import comp102x.Canvas;

public class Lab03
{  
    
    public void loadAnImage() 
    {
        // Please write your code after this line
        ColorImage image1 = new ColorImage();
        Canvas canvas = new Canvas(image1.getWidth(), image1.getHeight());
        canvas.add(image1);
        
    }
    
    public void loadTwoImagesOnTheSameCanvas()
    {
        // Please write your code after this line
        ColorImage image1 = new ColorImage();
        ColorImage image2 = new ColorImage();
        int height;
        if (image1.getHeight() > image2.getHeight()) {
            height = image1.getHeight();
        } else {
            height = image2.getHeight();
        }
        Canvas canvas = new Canvas(image1.getWidth() + image2.getWidth(), height);
        canvas.add(image1);
        canvas.add(image2, image1.getWidth(), 0);      
               
    }
    
    public void imageAddition() 
    {    
        // Please write your code after this line
        ColorImage image1 = new ColorImage();
        ColorImage image2 = new ColorImage();
        ColorImage image3 = image1.add(image2);
        int height;
        if (image1.getHeight() > image2.getHeight()) {
            height = image1.getHeight();
        } else {
            height = image2.getHeight();
        }
        Canvas canvas = new Canvas(3 * image1.getWidth() + 20, height);
        canvas.add(image1);
        canvas.add(image2, image1.getWidth() + 10, 0);
        canvas.add(image3, 2 * image1.getWidth() + 20, 0);
                     
        
    }
   
    public void imageMultiplication() 
    {
        // Please write your code after this line
        ColorImage image1 = new ColorImage();
        ColorImage image2 = new ColorImage();
        ColorImage image3 = image1.multiply(image2);
        int height;
        if (image1.getHeight() > image2.getHeight()) {
            height = image1.getHeight();
        } else {
            height = image2.getHeight();
        }
        Canvas canvas = new Canvas(3 * image1.getWidth() + 20, height);
        canvas.add(image1);
        canvas.add(image2, image1.getWidth() + 10, 0);
        canvas.add(image3, 2 * image1.getWidth() + 20, 0);               
        
    }
    
    public void changeColor()
    {
        ColorImage image = new ColorImage();
        image.increaseRed(40);
        Canvas canvas = new Canvas(image.getWidth(), image.getHeight());
        canvas.add(image);
        
        //image.save();
    }
}
