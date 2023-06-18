import pandas as pd

# Create training data
train_data = [
    {'text': 'This is a normal comment.', 'label': 0},
    {'text': 'Another normal comment.', 'label': 0},
    {'text': 'You are a fool!', 'label': 1},
    {'text': 'I hate you!', 'label': 1},
    {'text': 'Example of abusive comment.', 'label': 1},
    {'text': 'Great job!', 'label': 0},
    {'text': 'I disagree with your opinion.', 'label': 0},
    {'text': 'You are amazing!', 'label': 0},
    {'text': 'This is offensive.', 'label': 1},
    {'text': 'Nice work!', 'label': 0},
    {'text': 'You make me sick!', 'label': 1},
    {'text': 'I completely agree with you.', 'label': 0},
    {'text': 'You are so stupid!', 'label': 1},
    {'text': 'You are talented!', 'label': 0},
    {'text': 'You disgust me!', 'label': 1},
    {'text': 'Well said!', 'label': 0},
    {'text': 'I strongly dislike you!', 'label': 1},
    {'text': 'You are an inspiration.', 'label': 0},
    {'text': 'I love your work!', 'label': 0},
    {'text': 'You are the worst!', 'label': 1},
    {'text': 'What a fantastic achievement!', 'label': 0},
    {'text': 'You are a disgrace!', 'label': 1},
    {'text': 'Keep up the good work!', 'label': 0},
    {'text': 'You are pathetic!', 'label': 1},
    {'text': 'Your kindness is appreciated.', 'label': 0},
    {'text': 'I hope you fail!', 'label': 1},
    {'text': 'You are a bully!', 'label': 1},
]

# Create a DataFrame and save as CSV file
df = pd.DataFrame(train_data)
df.to_csv('training_data.csv', index=False)
