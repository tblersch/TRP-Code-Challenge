# TRP-Code-Challenge
Code Challenge for T-Rowe Price

Instructions I was given below:

T Rowe Price SDET Screening

Expected Completion time of 30-60 minutes depending on experience

Write a method or function in the major programming language of your choice that returns the longest word in a sentence and its length. For example, “The cow jumped over the moon.” should return “jumped” and 6.
Write unit tests, reworking code as needed
Add a method that returns the shortest word and length with unit tests
Create a README documenting any assumptions you made and including instructions on how to build and execute your tests.
Share your code using GitHub or similar.



First, my choice of programming language: I chose to write this in Python (version 3.8, but I believe it will run with any version 3.0 and above).  I chose this over Java, for two reasons:
1) I prefer Python's regex support to Java's.  Java regular expressions alway strike me as awkward, and this particular problem lent itself to regular expressions, so I felt Python was the better choice.
2) I'm not as strong in Python as in Java.  So I took this opportunity to sharpen and broaden my skills.  I rarely pursue any activity to only a single purpose.  
I also considered C++, but that was overkill for this task.  And considered node.js and C#, but it's been a little while since I used either, so I'm rusty with both

Assumptions:
1) I assumed that "word" in this case was meant to be alphabetic, without punctuation.  The exceptions being compound words - possesives with an apostrophe and hyphenated words were treated as one word.  This lends itself to splitting on a regular expression that captures "all combinations of word characters, and instances of ' and - that are bounded by word characters. ((\w[\w'-]*\w)"  
2) I assumed that the function should return the first instance of the longest and shortest word.  E.g. "Hello there" has two 5-character length words, the longest and shortest functions should both return "Hello".

Design decisions: I wrote two separate functions, FindLongestWord(sentence) and FindShortestWord(sentence) that are distinct from each other.  Normally, I would write one function "FindWord(sentence, size)" where size is either "LONGEST" or "SHORTEST," because the functions are very similar otherwise.  I chose two distinct functions because 1) that's what the instructions said, and 2) it made the code and tests slightly more readable and testable, which I considered important for a coding challenge.  Were this production code, or a shared library, I would prioritize a proper function decomposition over human readability.

To run, 
 - make sure you have Python installed: https://www.python.org/downloads/release/python-383/  Make sure the installation path in in your    PATH variable
 - download the files CodeChallenge.py and CodeChallenge_test.py to the same folder.
 - From that folder, execute "python.exe CodeChallenge_test.py"
 Will run all seven unit tests.  Purposes of the unit tests are:
  - A simple test to find longest word 
  - A simple test to find shortest word
  - Entering an empty string returns an empty string
  - Punctuation is properly removed, and not counted in any word length
  - When a sentence has words of the same length, the first word found is the one returned
  - Hyphenated compound words are treated as a single word
  - Possesive words and compound words (ending with apostrophe and a suffix) are counted as a single word
  
Additionally, included is a short application, CodeChallenge_app.py.  Execute this as above, and you can enter sentences at the prompt, and it will return the first and last word of each.  More demonstrative than the unit tests returning "7 passed".
 

