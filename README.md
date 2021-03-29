# Hidden-markov-model
In this assignment Hidden Markov model is used to Generate new text from the text corpus and then text prediction is performed using given sequence of words.

___
## Generation


### Dataset: Shakespeare's Plays

##### Steps: Following steps are used to implement the model and complete the assignment

#### Dataset
* Dataset is loaded using pandas.
* Data is cleaned and all the unnecessary lines are cleaned and are converted to string.
#### Building Hidden Markov model
* Markov Model is built using helper function.
* Unnecesary spaces and punctuation are removed and  converted in list of token whose probability is determined then.
* First order and second order markov chains are built based on tokens.
* First order and second order chain are converted in probability value.
* The word with highest probability is selected from second order markov chain.
* Text is generated based on corpus.
* A play of given length is written by randomly selecting starting values.

___

## Prediction:
* First order and second order markov chains were built in text generations so in this last word of the text is used to look for next word in markov chains and if the word is found then keep on looking for the next word.
* First we check for word in second order then if not found check for word in first order.
* Just determine the number of words to be predicted and the starting word.
