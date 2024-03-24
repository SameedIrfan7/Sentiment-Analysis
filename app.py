from flask import Flask, request, render_template
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from flask_caching import Cache
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# Twitter API credentials
consumer_key = "jXgE7yj8ngdDGGjTZYtFK8BCn"
consumer_secret = "jtxltGQvu07A2LYUyNdNC4f0kyo8LJcrNPLWvrScaPnt4EDWmi"
access_token = "1604667419242696704-0yUqKl20G9RaHrQ6wcM9ul8EuCrzoK"
access_token_secret = "CnsCz4obMXosQP9V1PwfiU7uWj3HKMRyw0I7xKiEPxCV4"

# Authenticate with Twitter API
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Load sentiment analysis model
# Assuming you have a pre-trained model saved as sentiment_analysis_model.pkl
@cache.cached(timeout=3600)  # Cache model for 1 hour
def load_model():
    with open('sentiment_analysis_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Load TfidfVectorizer
with open('vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

nltk.download('stopwords')
nltk.download('punkt')

# Text preprocessing function
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text.lower())
    filtered_sentence = [word for word in word_tokens if word.isalnum() and word not in stop_words]
    return ' '.join(filtered_sentence)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_sentiment', methods=['POST'])
def predict_sentiment():
    user_input = request.form['text']
    user_input = preprocess_text(user_input)

    # Perform sentiment analysis on user input
    model = load_model()  # Load model from cache
    user_input_vectorized = vectorizer.transform([user_input])
    prediction = model.predict(user_input_vectorized)[0]

    return f'The sentiment of the text is: {prediction}'

if __name__ == '__main__':
    app.run(debug=True)
