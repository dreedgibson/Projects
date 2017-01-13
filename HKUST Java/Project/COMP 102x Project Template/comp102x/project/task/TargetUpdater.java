package comp102x.project.task;

import java.util.Random;

import comp102x.project.model.Target;

public class TargetUpdater {
    
    public void updateTarget(Target[] targets, int level) {
        
        // Please write your code after this line
        Random random = new Random();
        if (level == 2) {
            for(int i = 0; i < 4; i++) {
                
                int target1 = random.nextInt(targets.length);
                int target2 = random.nextInt(targets.length);
                while (target1 == target2) target2 = random.nextInt(targets.length);
                
                if (targets[target1].isHit() != targets[target2].isHit()) {
                    swapTarget(targets, target1, target2);
                }
            }
            
        } else if (level == 3) {
            for(int i = 0; i < 10; i++) {
                
                int target1 = random.nextInt(targets.length);
                int target2 = random.nextInt(targets.length);
                while (target1 == target2) target2 = random.nextInt(targets.length);
                
                if (targets[target1].isHit() != targets[target2].isHit()) {
                    swapTarget(targets, target1, target2);
                }
            }
        }
    }
    
    public void swapTarget(Target[] targets, int target1, int target2) {
        int tempX = targets[target1].getX();
        int tempY = targets[target1].getY();
        int tempZ = targets[target1].getZ();
        targets[target1].setX(targets[target2].getX());
        targets[target1].setY(targets[target2].getY());
        targets[target1].setZ(targets[target2].getZ());
        targets[target2].setX(tempX);
        targets[target2].setY(tempY);
        targets[target2].setZ(tempZ);
    }

}
