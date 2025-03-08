# Sentimental_analysis
Project Report: Financial News Sentiment Analysis using Gemini AI
1. Project Overview
The Financial News Sentiment Analysis project is designed to help users analyze the sentiment of the latest financial news articles using Google Gemini AI. It fetches news articles from NewsAPI and processes them using Google's Gemini AI to determine whether the sentiment is Positive, Neutral, or Negative. The tool provides insights into market sentiment based on recent news, helping investors and financial analysts make informed decisions.

2. Technologies and APIs Used
Streamlit: A Python framework for creating interactive web applications.
NewsAPI: Fetches the latest news articles based on a given query.
Google Gemini AI: Performs sentiment analysis on news headlines and descriptions.
Requests: Handles API calls to fetch data from NewsAPI.
Python: The core programming language for implementing this project.
3. Models Used
Google Gemini-1.5-Flash: A lightweight and fast generative AI model from Google, used for analyzing sentiment.
Sentiment Classification Model: Implemented within Gemini, which classifies news articles into Positive, Neutral, or Negative categories.
4. Problems the Project Solves
Market Sentiment Analysis: Helps users gauge the overall sentiment of financial news articles.
Automated Sentiment Classification: Eliminates the need for manual analysis by leveraging AI to classify news articles.
User-Friendly Insights: Provides clear and structured insights using emojis and color-coded labels.
Real-Time News Analysis: Fetches and analyzes the latest financial news in seconds.
5. Key Features
Real-Time News Fetching: Retrieves financial news articles using NewsAPI.
AI-Powered Sentiment Analysis: Uses Gemini AI to classify news into Positive, Neutral, or Negative sentiment.
User-Friendly Interface: Streamlit-based web app for easy interaction.
Security Measures: API keys are entered as password fields to protect user data.
Performance Optimization: Limits the number of articles analyzed per request for efficiency.
6. Limitations & Future Improvements
API Limitations: NewsAPI requires an API key and has request limits.
Limited Sentiment Categories: The classification is restricted to three sentiment types (Positive, Neutral, Negative).
Handling Long Articles: Currently analyzes only headlines and short descriptions.
Future Enhancements:
Implementing historical sentiment trends.
Expanding to more financial news sources.
Improving accuracy using fine-tuned sentiment models.
7. Conclusion
This Financial News Sentiment Analysis tool is a powerful, AI-driven application that provides users with real-time sentiment insights into financial news. It can be useful for investors, traders, and analysts who rely on news sentiment to make data-driven financial decisions. Future updates could enhance its accuracy, data sources, and analysis depth.
