To implement the cyberbully judgement functionality, here is a step-by-step breakdown:

1. When a user enters text, we need to determine whether its utterance is related to cyber violence or not.
A database containing normal and insulting language is generated and used to train the model. When our product is made mature, it will store the user input data into the database to improve the training accuracy.

2. The python file determines if the statement is cyber violence related by calculating the value of the 0-1 interval.

limitations:
1. current program cannot recognize "'", such as the user input text containing That's or I'm, these cannot judge. This may need more training or adopt more advanced model or algorithm.
2. insufficient data in the dataset, resulting in low accuracy. We consider storing the data input by the user and automatically adding it to the training database to improve the accuracy
