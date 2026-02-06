#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import pandas as pd
import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


# In[6]:


df = pd.read_csv("zomato_reviews.csv")


# In[7]:


df.head()


# In[8]:


def rating_to_sentiment(rating):
    if rating >= 4:
        return "positive"
    elif rating == 3:
        return "neutral"
    else:
        return "negative"

df["sentiment"] = df["rating"].apply(rating_to_sentiment)
df.head()


# In[9]:


X = df["review_text"]   # input (text)
y = df["sentiment"]     # output (label)


# In[10]:


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# In[11]:


model = make_pipeline(
    CountVectorizer(),
    MultinomialNB()
)

model.fit(X_train, y_train)


# In[13]:


test_text = "worst food"
prediction = model.predict([test_text])

print(f"Text: {test_text}")
print(f"Predicted Sentiment: {prediction[0]}")


# In[14]:


with open("sentiment_model.pkl", "wb") as f:
    pickle.dump(model, f)

