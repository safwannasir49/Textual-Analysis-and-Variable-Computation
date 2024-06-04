import pandas as pd
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
import requests
from bs4 import BeautifulSoup

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

# Function to extract article text
def extract_article_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example structure: modify according to the actual structure of the webpage
    title = soup.find('h1').get_text() if soup.find('h1') else ''
    paragraphs = soup.find_all('p')
    article_text = ' '.join([para.get_text() for para in paragraphs])
    
    return title + "\n" + article_text

# Load the input Excel file
input_df = pd.read_excel("Input.xlsx")

# Function to preprocess text
def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [token.lower() for token in tokens]
    words = [word for word in tokens if word.isalnum()]
    return words

# Function to compute variables
def compute_variables(text):
    words = preprocess_text(text)
    sentences = sent_tokenize(text)
    
    word_count = len(words)
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]
    cleaned_word_count = len(words)
    unique_words = len(set(words))
    
    fdist = FreqDist(words)
    most_common_word = fdist.most_common(1)[0][0] if fdist else None
    
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    positive_score = sentiment_scores['pos']
    negative_score = sentiment_scores['neg']
    polarity_score = sentiment_scores['compound']
    subjectivity_score = (positive_score + negative_score) / (cleaned_word_count + 0.000001)
    
    average_sentence_length = word_count / len(sentences)
    complex_words = [word for word in words if len(word) > 2]
    percentage_complex_words = len(complex_words) / cleaned_word_count
    fog_index = 0.4 * (average_sentence_length + percentage_complex_words)
    average_words_per_sentence = cleaned_word_count / len(sentences)
    complex_word_count = len(complex_words)
    
    syllable_count = sum([sum(map(lambda w: 1 if w in ['a', 'e', 'i', 'o', 'u', 'y'] else 0, word.lower())) 
                          for word in words])
    syllable_per_word = syllable_count / cleaned_word_count
    
    personal_pronouns = len(re.findall(r'\b(I|we|my|ours|us)\b', text, flags=re.IGNORECASE))
    average_word_length = sum(map(len, words)) / cleaned_word_count
    
    return (positive_score, negative_score, polarity_score, subjectivity_score, 
            average_sentence_length, percentage_complex_words, fog_index,
            average_words_per_sentence, complex_word_count, word_count, 
            syllable_per_word, personal_pronouns, average_word_length)

# List to store computed variables as dictionaries
output_data = []

# Iterate through each URL in the input DataFrame and compute variables
for index, row in input_df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    
    # Extract article text
    article_text = extract_article_text(url)
    
    # Verify the extracted text
    print(f"Extracted text for URL_ID {url_id}: {article_text[:500]}...")  # Print first 500 characters
    
    # Compute variables
    variables = compute_variables(article_text)
    
    # Store computed variables as dictionary
    output_data.append({
        'URL_ID': url_id,
        'Positive_Score': variables[0],
        'Negative_Score': variables[1],
        'Polarity_Score': variables[2],
        'Subjectivity_Score': variables[3],
        'Avg_Sentence_Length': variables[4],
        'Percentage_of_Complex_Words': variables[5],
        'Fog_Index': variables[6],
        'Avg_Number_of_Words_Per_Sentence': variables[7],
        'Complex_Word_Count': variables[8],
        'Word_Count': variables[9],
        'Syllable_Per_Word': variables[10],
        'Personal_Pronouns': variables[11],
        'Avg_Word_Length': variables[12]
    })

# Create DataFrame from list of dictionaries
output_df = pd.DataFrame(output_data)

# Save output DataFrame to Excel file
output_df.to_excel("Output.xlsx", index=False)

print("Textual analysis and variable computation completed. Output saved to Output.xlsx.")
