<h1 align="center">
    <img src="https://readme-typing-svg.herokuapp.com?font=Sedan+SC&pause=1000&color=73AEF7&center=true&random=false&width=500&height=80&lines=Hello+!"/>
</h1>

# Textual Analysis and Variable Computation
This project extracts textual data from articles provided in a given Excel file of URLs, performs text analysis to compute various linguistic variables, and saves the results to an output Excel file.

Description
Data Extraction
The project reads a list of URLs from an Input.xlsx file, extracts the article's title and main text from each URL using web scraping techniques, and saves the extracted text into separate .txt files named after their respective URL IDs. Only the article's title and main body text are extracted, excluding any headers, footers, or ads.

Text Analysis
After extracting the text, the project performs several text analysis tasks including:

Tokenization and Preprocessing: The text is tokenized into words and sentences, converted to lowercase, and stripped of punctuation and stop words.
Sentiment Analysis: Using the VADER sentiment analysis tool, the project computes sentiment scores including positive, negative, and polarity scores.
Linguistic Metrics: Various linguistic metrics are computed such as:
Positive Score
Negative Score
Polarity Score
Subjectivity Score
Average Sentence Length
Percentage of Complex Words
Fog Index
Average Number of Words per Sentence
Complex Word Count
Word Count
Syllable per Word
Personal Pronouns Count
Average Word Length
Output
The computed variables are saved in an Output.xlsx file with the following columns:

URL_ID
Positive_Score
Negative_Score
Polarity_Score
Subjectivity_Score
Avg_Sentence_Length
Percentage_of_Complex_Words
Fog_Index
Avg_Number_of_Words_Per_Sentence
Complex_Word_Count
Word_Count
Syllable_Per_Word
Personal_Pronouns
Avg_Word_Length
Python Libraries and Packages Used
pandas: For reading and writing Excel files, and handling data in DataFrame format.
nltk (Natural Language Toolkit): For text processing, including tokenization, stopwords removal, and sentiment analysis.
requests: For making HTTP requests to fetch web page content.
beautifulsoup4: For parsing HTML content and extracting article text.
openpyxl: For working with Excel files.
Installation

To install the required Python libraries, use the following pip command:

pip install pandas nltk requests beautifulsoup4 openpyxl
