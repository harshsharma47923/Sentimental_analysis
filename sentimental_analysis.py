
import streamlit as st
import requests
import google.generativeai as genai  # Import Google AI API

# Configure Google AI API
def configure_gemini(api_key):
    genai.configure(api_key=api_key)

# Function to fetch news articles from NewsAPI
def fetch_news(api_key, query='finance'):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        articles = data.get('articles', [])

        news_texts = [
            article['title'] + " - " + article['description']
            for article in articles if article.get('title') and article.get('description')
        ]
        return news_texts
    except requests.RequestException as e:
        st.error(f"❌ Failed to fetch news: {e}")
        return []

# Function to analyze sentiment using Google Gemini
def analyze_sentiment(texts, gemini_api_key):
    configure_gemini(gemini_api_key)
    sentiment_results = []
    
    try:
        # ✅ Use the correct free model
        model = genai.GenerativeModel("gemini-1.5-flash")  

        prompt = (
            "Analyze the sentiment of the following news articles as Positive, Neutral, or Negative:\n\n"
            + "\n\n".join(texts[:5])  # Limit to 5 articles per request
        )

        response = model.generate_content(prompt)

        if hasattr(response, 'text'):
            sentiments = response.text.strip().split("\n")  # Parse the output
            sentiment_results = [{'text': text, 'sentiment': sentiment} for text, sentiment in zip(texts[:5], sentiments)]
        else:
            st.error("⚠ Gemini API response is invalid.")

    except Exception as e:
        st.error(f"⚠ Gemini API error: {e}")

    return sentiment_results

# Streamlit UI
def main():
    st.image("https://cdn-icons-png.flaticon.com/512/2332/2332324.png", width=150)  # ✅ Reduced image size
    
    st.title("📊 Financial News Sentiment Analysis (Gemini AI)")

    # Input for news topic
    query = st.text_input("🔍 Enter a news topic:", "finance")

    # Input for API Keys
    newsapi_key = st.text_input("🔑 Enter your NewsAPI key:", type="password")
    gemini_api_key = st.text_input("🔑 Enter your Gemini API key:", type="password")

    if st.button("🚀 Analyze Sentiment"):
        if newsapi_key and gemini_api_key:
            with st.spinner('🔄 Fetching news articles...'):
                news_data = fetch_news(newsapi_key, query)
            
            if news_data:
                with st.spinner('🤖 Analyzing sentiment using Gemini AI...'):
                    sentiment_data = analyze_sentiment(news_data, gemini_api_key)
                
                # Display results
                st.subheader("📈 Sentiment Analysis Results:")
                for result in sentiment_data:
                    sentiment_color = "🟢" if "Positive" in result['sentiment'] else "🟡" if "Neutral" in result['sentiment'] else "🔴"
                    st.write(f"{sentiment_color} *{result['text']}*")
                    st.write(f"📝 *Sentiment:* {result['sentiment']}")
                    st.markdown("---")
                
                st.info("Note: Analysis is limited to the first 5 articles for optimal performance.")
            else:
                st.warning("⚠ No news articles found for the given topic.")
        else:
            st.warning("⚠ Please enter both API keys.")

if __name__ == "__main__":
    main()
