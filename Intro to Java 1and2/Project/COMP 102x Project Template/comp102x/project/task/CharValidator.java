package comp102x.project.task;

public class CharValidator {
	
	public boolean validateChar(char c) {
		
		// Please write your code after this line
		if (Character.isLetterOrDigit(c)) return true;
		return false; // This line should be modified or removed after finising the implementation of this method.
	}

}
