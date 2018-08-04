/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package text.summarizer.master;

/**
 *
 * @author HP
 */
class Sentence{
	int paragraphNumber;
	int number;
	int stringLength; //Dont need this 
	double score;
	int noOfWords;
	String value;

	Sentence(int number, String value, int stringLength, int paragraphNumber){
		this.number = number;
		this.value = new String(value);
		this.stringLength = stringLength;
		noOfWords = value.split("\\s+").length;
		score = 0.0;
		this.paragraphNumber=paragraphNumber;
	}
}
