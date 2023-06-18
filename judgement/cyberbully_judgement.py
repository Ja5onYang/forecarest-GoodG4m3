import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

# 加载训练数据
train_data = pd.read_csv('training_data.csv')

# 分割输入和标签
X_train = train_data['text']
y_train = train_data['label']

# 创建分类器的管道
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),  # 使用TF-IDF向量化文本
    ('clf', LinearSVC())  # 使用线性支持向量机分类器
])

# 训练模型
pipeline.fit(X_train, y_train)

# 读取用户输入
user_input = input("Please enter a text：")

# 在模型中进行预测
prediction = pipeline.predict([user_input])

# 打印预测结果
if prediction[0] == 0:
    print("This is a normal statement.")
else:
    print("This is an online violent statement or an insulting statement.")

