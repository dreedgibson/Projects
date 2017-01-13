 
import comp102x.ColorImage;

public class Lab03Task1 {
     
    /**
     * This recursive method draws stripe images from left to right, top to bottom, right to left and bottom to top repeatedly.
     * The drawing repeats until the remaining area is too small for drawing two horizontal stripes or two vertical stripes without overlapping.
     * All the remaining area that are too small for drawing should be covered by a single stripe drawn from left to right at the end.
     * 
     * @param image the ColorImage of which the stripes should be drawn on.
     * @param x the x position of the remaining area.
     * @param y the y position of the remaining area.
     * @param width the width of the remaining area.
     * @param height the height of the remaining area.
     * @param stripeSize the thickness of the stripe to be drawn.
     */
    public void changeScreen(ColorImage image, int x, int y, int width, int height, int stripeSize) {
    
        // Please write your code after this line 
        if (2 * stripeSize > height || 2 * stripeSize > width ) {
            animateStripe(image, x, y, width, height, "toRight");
        } else {
            animateStripe(image, x, y, width, stripeSize, "toRight");
            animateStripe(image, width - stripeSize + x, y + stripeSize , height - stripeSize, stripeSize, "toBottom");
            animateStripe(image, x, height - stripeSize + y, width - stripeSize, stripeSize, "toLeft");
            animateStripe(image, x, y + stripeSize, height - 2 * stripeSize, stripeSize, "toTop");
            changeScreen(image, x + stripeSize, y + stripeSize, width - 2 * stripeSize, height - 2 * stripeSize, stripeSize);
        }
    }
    
    private void animateStripe(ColorImage image, int left, int top, int length, int stripeSize, String direction) {

        long delay = (long) Math.pow(10, 5.5);
        
        switch (direction) {

            case "toRight":
                for (int i = 0; i < length; i++) {
                    image.drawRectangle(left + i, top, 1, stripeSize);
                    pauseByTicks(delay);
                }
                break;
    
            case "toBottom":
                for (int i = 0; i < length; i++) {
                    image.drawRectangle(left, top + i, stripeSize, 1);
                    pauseByTicks(delay);
                }
                break;
    
            case "toLeft":
                for (int i = length - 1; i >= 0; i--) {
                    image.drawRectangle(left + i, top, 1, stripeSize);
                    pauseByTicks(delay);
                }
                break;
    
            case "toTop":
                for (int i = length - 1; i >= 0; i--) {
                    image.drawRectangle(left, top + i, stripeSize, 1);
                    pauseByTicks(delay);
                }
                break;
    
            default:
                System.err.println("Invalid direction: " + direction);
                System.err.println("Only \"toRight\", \"toBottom\", \"toLeft\", \"toTop\" are allowed!");
        }
    }

    private void pauseByTicks(long ticks) {
        while (ticks != 0) {
            ticks--;
        }
    }

}
