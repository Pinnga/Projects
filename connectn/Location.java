/**
 * REPLACE THIS COMMENT WITH YOUR OWN JAVA DOC COMMENT
 * THAT DESCRIBES THE PURPOSE OF YOUR CLASS
 * 
 * You may change this file as much as you like, including:
 * 	- adding constructor parameters
 *  - overloading the constructor
 *  - adding instance variables
 *  - adding methods (public or private)
 *  
 * HOWEVER:
 *  - You may not move the file to a different package
 * 	- You may not change the name of the file or the class
 *  - You must overload the Object class's equals method
 *  - You must provide isEmpty and getToken methods
 *  - You must represent the symbol as a Character
 *  - the symbol can be one of 'X', 'O', or ' '
 */
package edu.wm.cs.cs301.connectn;

public class Location {
	private Character symbol;
	
	public Location() {
		
	}
	
	public boolean isEmpty() {
		return false;	//placeholder, replace with correct code
	}
	
	public Character getToken() {
		return symbol;
	}
	
	@Override
	public boolean equals(Object other) {
		return false;	//placeholder, replace with correct code
	}
	
}
