# Approach:

please make sure all required dependencies are installed.
load the input Excel file containing URLs and text.
Preprocess the text by tokenizing, converting to lowercase, and removing punctuation and stop words.
Compute variables such as sentiment scores, average sentence length, and percentage of complex words.
Store the computed variables and create a DataFrame.
Save the DataFrame to an Excel file.
Running the .py File:

Install dependencies: pip3 install pandas nltk.
download NLTK resources: nltk.download('punkt'), nltk.download('stopwords'), nltk.download('vader_lexicon').
place Input.xlsx in the same directory.
run the Python script.
output will be saved as Output.xlsx in the same directory.

Dependencies:

pandas
nltk