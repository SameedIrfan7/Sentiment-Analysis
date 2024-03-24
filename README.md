# Flask Sentiment Analysis Project

This Flask project demonstrates a simple web application for performing sentiment analysis on text input. The application uses the TextBlob library for sentiment analysis and Flask for the web framework.

## Features

- **Sentiment Analysis**: Analyzes the sentiment (positive, negative, or neutral) of user-provided text input.
- **Twitter Integration**: Includes integration with the Twitter API using Tweepy for fetching tweets and performing sentiment analysis on them.
- **Caching**: Utilizes Flask-Caching extension to cache the sentiment analysis model for improved performance.

## Prerequisites

- Python 3.x
- Flask
- Tweepy
- TextBlob
- scikit-learn
- NLTK

## Installation

1. Clone the repository:

   ```bash
   git clone [https://github.com/](https://github.com/SameedIrfan7/Sentiment-Analysis/)https://github.com/SameedIrfan7/Sentiment-Analysis/
2. Install Dependencies:

```bash
pip install -r requirements.txt
```
3. Set up Twitter API Credentials

  Create a `config.py` file with the following content:

```bash
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
```
4. Run the Flask Application

```bash
python app.py
```

## Usage

Enter text in the provided input field and click the **"Analyze"** button to perform sentiment analysis.
The application will display the sentiment **(positive, negative, or neutral)** of the entered text.

## Contributing
Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or create a pull request.
