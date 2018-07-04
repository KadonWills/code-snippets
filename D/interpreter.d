import std.stdio;
import std.conv;

/** This is the host struct for the interpreter and core/built-in functions
Still need to add greater than, less than and drop to memory module */
struct interpreter {
	
	string[] stack;			///Stack where program memory goes
	string[] src;			/// Source code that gets executed do "x.src = [(code here)];" to set source code
	
	uint[] readLocRec;		///This Keeps track of where the readLocation was last requested to be recorded so can resume from there
	uint readLocation = 0;	///This is the pointer that keeps track of execution location
	
	/** Frees stack of unused data at top of stack */
	void MemRelease() {
		stack = stack[0..stack.length-1];
	};
	
	
	/** This is a memory module used by interpreter. This memory offers types and value by key, not index making it easier to use and more practical */
	string[3][] object;	//object type memory
	
	void MemRead() {
		string want = stack[stack.length-1];
		MemRelease();
		string key = stack[stack.length-1];
		MemRelease();
		
		foreach (ref slice; object) {
			if (key == slice[0]) {
				switch (want) {
					default:
						stack ~= "err";
						break;
						
					case "type":
						stack ~= slice[1];
						break;
						
					case "value":
						stack ~= slice[2];
						break;
				}
			}
			break;
		}
	};
		
	void MemWrite() {
		string value = stack[stack.length-1];
		MemRelease();
		string type = stack[stack.length-1];
		MemRelease();
		string key = stack[stack.length-1];
		MemRelease();
		
		object ~= [key, type, value];
	};
		
	//void Drop() {};
	
	//End of memory module
	
	
	/** Call this method to begin execution of code */
	void run() {
		while (readLocation != src.length) {
			//Our main loop won't terminate till it is equal to the length of src
			
			
			/* Add flag -version=bugtracker when compiling to watch interpreter
			memory for bugs in execution */
			version (bugtracker) {
				writeln(readLocation, ": ", src[readLocation], " -> ", stack);
			}
			
			
			OpCodeFunction(src[readLocation]);	//Gets a value from source code and processes it as data or instruction
			readLocation += 1;					//Next instruction
		}
	};
	
	/** This function takes one parameter and executes it if it is a function
	and pushes it to the stack if it is a value. */
	void OpCodeFunction(string opcode) {
		switch (opcode) {
			
			default:		//Anything other than an opcode gets pushed to the stack
				PushToStack();
				break;
				
			case "m_read":	//Performs read from object type memory and pushes to stack
				MemRead();
				break;
				
			case "m_write":	//Performs write to object type memory from the stack
				MemWrite();
				break;
				
			case "f_plus":	//Performs additon on the stack
				Addition();
				break;
			
			case "f_sub":	//Performs subtraction on the stack
				Subtraction();
				break;
				
			case "f_mul":	//Performs multiplcation on the stack
				Multiplcation();
				break;
				
			case "f_div":	//Performs divison on the stack
				Divison();
				break;
				
			case "f_write":	//Writes to location of the stack
				WriteStack();
				break;
			
			case "f_read":	//Reads location on the stack
				ReadStack();
				break;
			
			case "f_isEq":	//Performs is equal
				IsEqual();
				break;
				
			case "f_notEq":	//Performs is not equal
				NotEqual();
				break;
				
			case "f_addr":	//Returns current address of readLocation pointer
				Address();
				break;
				
			case "f_goto":	//Moves execution on src
				Goto();
				break;
				
			case "f_call":	//Cashes current readLocation to the readLocRec stack for resume later and changes current location of readLocation
				Call();
				break;
				
			case "f_resu":	//Gets location from top of the readLocRec stack and pushes readLocation to there
				Resume();
				break;
			
			case "f_log":	  //Prints value to screen without newline
				Show();
				break;
				
			case "f_drop":	//Drop value on top of stack
				MemRelease();
				break;
		}
	};
	
	/** Pushes data onto the stack
		
	Template:
		["(anything that doesn't match an opcode)"]
	*/
	void PushToStack() {
		stack ~= src[readLocation];
	};
	
	/** Performs addition on the stack
		
	Template:
		["(number)", "(number)", "f_plus"]
	*/
	void Addition() {
		long num1 = to!long(stack[stack.length-1]);
		MemRelease();
		long num2 = to!long(stack[stack.length-1]);
		MemRelease();
		
		stack ~= to!string(num1 + num2);//Returns result to the stack
	};
	
	/** Performs subtraction on the stack
		
	Template:
		["(number)", "(number)", "f_sub"]
	*/
	void Subtraction() {
		long num1 = to!long(stack[stack.length-1]);
		MemRelease();
		long num2 = to!long(stack[stack.length-1]);
		MemRelease();
		
		stack ~= to!string(num2 - num1);///Returns result to the stack
	};
	
	/** Performs multiplcation on the stack
		
	Template:
		["(number)", "(number)", "f_mul"]
	*/
	void Multiplcation() {
		long num1 = to!long(stack[stack.length-1]);
		MemRelease();
		long num2 = to!long(stack[stack.length-1]);
		MemRelease();
		
		stack ~= to!string(num1 * num2);///Returns result to the stack
	};
	
	/** Performs divison on the stack
		
	Template:
		["(number)", "(number)", "f_div"]
	*/
	void Divison() {
		long num1 = to!long(stack[stack.length-1]);
		MemRelease();
		long num2 = to!long(stack[stack.length-1]);
		MemRelease();
		
		stack ~= to!string(num2 / num1);///Returns result to the stack
	};
	
	/** Gets value and writes it to location on the stack
	
	Template:
		["(any type of data)", "(number)", "f_write"]
	*/
	void WriteStack() {
		uint pointer = to!uint(stack[stack.length-1]);
		MemRelease();
		string value = stack[stack.length-1];
		MemRelease();
		
		stack[pointer] = value;//Rewrites data on stack at pointer
	};
	
	/** Reads location on stack and returns it to top of stack
		
	Template:
		["(number)", "f_read"]
	*/
	void ReadStack() {
		uint stackPolonger = to!uint(stack[stack.length-1]);
		MemRelease();
		
		stack ~= stack[stackPolonger];
	};
	
	/** Gets two values and checks to see if they are equal and if so it will
		execute code at pointer location
		
	Template:
		["(number)", "(data to compare)", "(data to compare)", "f_isEq"]
	*/
	void IsEqual() {
		string value1 = stack[stack.length-1];
		MemRelease();
		string value2 = stack[stack.length-1];
		MemRelease();
		
		if (value1 == value2) {
			Goto();
		} else {
			MemRelease();//Removes unused readLocation number from stack
		}
	};
	
	/** Gets two values and checks to see if they are equal and if so it will
		execute code at pointer location
		
	Template:
		["(number)", "(data to compare)", "(data to compare)", "f_notEq"]
	*/
	void NotEqual() {
		string value1 = stack[stack.length-1];
		MemRelease();
		string value2 = stack[stack.length-1];
		MemRelease();
		
		if (value1 != value2) {
			Goto();
		} else {
			MemRelease();//Removes unused readLocation number from stack
		}
	};
	
	/**	Call this function and it will replace with readLocation pointer length. Great for when you need to perform a goto
	over a slice of code but you don't know the number of current location
	
	Template:
		["f_addr"]
	*/
	void Address() {
		stack ~= to!string(readLocation-1);
	};
	
	/** Moves readLocation on the source code
		
	Template:
		["(number)", "f_goto"]
	*/
	void Goto() {
		readLocation = (to!uint(stack[stack.length-1]))-1;
		MemRelease();
	};
	
	/** Reads location of readLocation and appends it to top of readLocRec stack
		and then performs goto
		
	Template:
		["(number)", "f_call"]
	*/
	void Call() {
		readLocRec ~= readLocation;
		Goto();
	};
	
	/** Gets location from top of readLocRec stack, pops it and moves readLocation to there
		
	Template:
		["f_resu"]
	*/
	void Resume() {
		readLocation = readLocRec[readLocRec.length-1];//Sets new location for readLocation
		readLocRec = readLocRec[0..readLocRec.length-1];//Removes resume pointer
	};
	
	/** Prints value to screen
		
	Template:
		["(any type of data)", "f_log"]
	*/
	void Show() {
		write(stack[stack.length-1]);
		MemRelease();
	};
}

void main() {	
	interpreter tmp;
	/*
	tmp.src = [
		"0","1",											//0-1)	Memoy (a & b)
		"30","f_addr","f_plus","f_goto",					//2-5)	Function declaration
		"\n","f_log","0","f_read","f_log",					//6-10)	print value of a to screen
		"1","f_read","0","f_write",							//11-14)do a = b
		"0","f_read","1","f_read","f_plus","1","f_write",	//15-21)do b = a + b
		"9","f_addr","f_plus","0","f_read","0","f_isEq",	//22-28)if a == 0 leave function
		"6","f_call",										//29-30)calls function
		"f_resu",											//31)	This sends readLocation back to where is was before it was called by function
		"6","f_call",										//32-33)calls function
		"\n\nDone fibonacci!","f_log",						//34-35)tells us code is done executing
		"m_read"
	];
	*/
	tmp.src = [
		"x", "string", "Hello World", "m_write",
		"x", "value", "m_read", "f_log",
		" -> ", "f_log",
		"x", "type", "m_read", "f_log"
	];
	tmp.run();
}
