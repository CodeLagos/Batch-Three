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
//## The Algorithm
//1. Take the full CONTENT and split it into PARAGRAPHS. 
//2. Split each paragraph into SENTENCES. 
//3. Compare every sentence with every other. This is done by Counting the number of common words and then Normalize this by dividing by average number of words per sentence
//
//4. These intermediate scores/values are stored in an INTERSECTION matrix
//
//5. Create the key-value dictionary
//	- Key : Sentence
//	- Value : Sum of intersection values with this sentence
//
//6. From every paragraph, extract the sentences  with the highest score.
//
//7. Sort the selected sentences in order of appearance in the original text to preserve content and meaning.
//
//And like that, you have generated a summary of the original text.
//
//
//

class improved_summary{
	public static void main(String[] args){
		SummaryTool summary = new SummaryTool();
		summary.init();
		summary.extractSentenceFromContext();
		summary.groupSentencesIntoParagraphs();
		//summary.printSentences();
		summary.createIntersectionMatrix();

		//System.out.println("INTERSECTION MATRIX");
		//summary.printIntersectionMatrix();

		summary.createDictionary();
		//summary.printDicationary();

		System.out.println("SUMMMARY");
		summary.createSummary();
		summary.printSummary();

		summary.printStats();
	}
}
