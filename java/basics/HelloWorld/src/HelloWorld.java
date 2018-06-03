import java.util.Scanner;

public class HelloWorld {

	public static void main(String[] args) {
		String greeting = "";
		
		
		System.out.println("Hello world!");
		
		System.out.println("Please enter a welcome message:");
		//A new Scanner Object must be created before we can proceed
		Scanner kb = new Scanner(System.in);
		greeting = kb.nextLine();
		
		//java does not auto add spaces like python does
		System.out.println("Your new greeting is: "+ greeting);
		
	}

}


// Author: Claudiu Moise
// Hello world comparison between Java and Python
// One with a static message and one where the input is user defined