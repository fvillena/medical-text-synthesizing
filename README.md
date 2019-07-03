[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fvillena/medical-text-synthesizing/master?filepath=notebooks%2Fsynthesizer.ipynb)
# Diagnostic Generator

This model is trained over around 2 millions diagnostics to extract the probability distributions of word bigrams, which are groups of 2 words that appear one after the other. There are more frequent bigrams than others, for example the _bigram caries dentinaria_ is more frequent than _caries gingival_ and using these conditional probabilities we can synthesize new diagnostics that appears to be written by humans. The method used to model this process is a First Order Hidden Markov Model.

## TODO
Create a Second Order Hidden Markov Model extracting the probability distributions of trigrams to synthesize more realistic diagnostics.


## Test the Model by Yourself

Simply launch the [binder container](https://mybinder.org/v2/gh/fvillena/medical-text-synthesizing/master?filepath=notebooks%2Fsynthesizer.ipynb) and start playing with the model or clone this repository.

## Train Your Own Model

All the scripts used to train the model are published in the `src` folder.
