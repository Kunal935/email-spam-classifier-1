import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import sklearn

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)





cv = pickle.load(open('vectroizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))


st.title("Email/Sms Spam classifier")


input_sms = st.text_input("Enter The msg")

if st.button('predict'):

  transformed_sms = transform_text(input_sms)

  vector_input = cv.transform([transformed_sms])

  result = model.predict(vector_input)[0]

  if result == 1:
     st.header("spam")
  else:
     st.header("not spam")