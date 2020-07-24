# Text-Complexity-Analysis
The task was to analyse how the complexity of language changes across levels of the story,
using language processing techniques. The task of reading level classification is taken as a
proxy task to analyse the text complexity. A classifier is made to classify the stories into different
reading levels with various text related features which would probably help to decide the reading
complexity level. The absence and presence of such features make in the classification
accuracy is taken as the base for text complexity analysis.


# Install Required Packages
* All the codes are written in python 3.
* System tested in Ubuntu 16.04 LTS
```
$ cd Text-Complexity-Analysis
$ pip3 -r install requirements.txt
```

# How to run
```
$ cd Text-Complexity-Analysis 
$ python3 TextComplexityClassifier.py --language <LANGUAGE>
```
Supported Languages are english, hindi & telugu


