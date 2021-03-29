# hidden-markov-model
EECS-738: Hidden Mark.. M.. (Assignment-2)

In this assignment Hidden Markov model is used to Generate new text from the text corpus

________________________________________
Dataset: Shakespeare's Plays
Steps: Following steps are used to implement the model and complete the assignment:
*Dataset is loaded using pandas.
*Data is cleaned and all the unnecessary lines are cleaned and are converted to string.
*Markov Model is built using helper function.
*Unnecesary spaces and punctuation are removed and  converted in list of token whose probability is determined then.
*First order and second order markov chains are built based on tokens.
*First order and second order chain are converted in probability value.
*The word with nhighest probability is selected from second order markov chain.
*Text is generated based on corpus.
*A play of given length is written by randomly selecting starting values.

##Predicntion:
*First order and second order markov chains were built in text generations so in this last word of the text is used to look for next word in markov chains and if the word is found then keep on looking for the next word.
*First we check for word in second order then if not found check for word in first order.
*Just determine the number of words to be predicted and the starting word.


•	Dataset is loaded into pandas and cleaned; giving a list of all of the player-lines
•	Markov model is built
o	Each line is tokenized
o	First-order and second-order markov chains are built based on tokens
•	A function is written (write_line ()) which, given a word hint, generates a full sentence based on the pre-built markov chains
•	A play of given length is written; by randomly selecting starting words from Shakespeare's plays
In order to improve readability, the notebook is divided into sections based on the main task achieved in that section. Each of the section is described below:
Section-1: Dataset Manipulation
The following main goals are achieved in this section:
•	Dataset is loaded
•	Uninteresting lines are deleted from the dataset
•	Lines are converted into a list of string for further processing
Section-2: Hidden Markov Model
This section provides helper functions for building the hidden markov model on a text corpus. It is further divided into sub-section to increase modularity.
•	2.1: Declaration of Global Control Switches
•	2.2: Helper Functions for Text-Parsing
•	2.3: Main Function for Building the HMM Model
•	2.4: Helper Functions for Using the HMM Model for Text-Generation
•	2.5: User API for Predicting Text Given a Sequence of Words
Section-3: Demonstration
In this section, the hidden markov model is used for text-generation. For this purpose, a play of given length is written to demonstrate the correctness as well as extent and limitation of this model. Also the utility of user-API for text-generation given a word sequence is demonstrated.
ACKNOWLEDGEMENT: Following source has been used to understand the principles of text-generation using HMM:
•	Reference

