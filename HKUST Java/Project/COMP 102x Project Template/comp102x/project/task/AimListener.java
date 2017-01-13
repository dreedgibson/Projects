package comp102x.project.task;

import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionListener;

import comp102x.project.view.GameScreen;

public class AimListener implements MouseMotionListener {
    private double pan;
    private double tilt;
    
    public double getPan() {
        return this.pan;
    }
    
    public double getTilt() {
        return this.tilt;
    }
    
    public void setPan(double value) {
        this.pan = value;
    }

    public void setTilt(double value) {
        this.tilt = value;
    }
    
    @Override
    public void mouseMoved(MouseEvent e) {
        setPan(((double)e.getX() / GameScreen.WIDTH) * 180 - 90);
        setTilt(((double)e.getY() / GameScreen.HEIGHT) * 90);
    }
    
    public void mouseDragged(MouseEvent e) {}
}
