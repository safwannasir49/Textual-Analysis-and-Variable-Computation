<h1 align="center">
    <img src="https://readme-typing-svg.herokuapp.com?font=Sedan+SC&pause=1000&color=73AEF7&center=true&random=false&width=435&lines=Hello+!;How+are+you%3F+%F0%9F%98%83;This+Project+is+Based+Upon+;Data+Extraction;Text+Analysis"/>
</h1>

 <h1>Textual Analysis and Variable Computation</h1>
    <p>This project extracts textual data from articles provided in a given Excel file of URLs, performs text analysis to compute various linguistic variables, and saves the results to an output Excel file.</p>
    <h2>Description</h2>
    <h3>Data Extraction</h3>
    <p>The project reads a list of URLs from an <code>Input.xlsx</code> file, extracts the article's title and main text from each URL using web scraping techniques, and saves the extracted text into separate <code>.txt</code> files named after their respective URL IDs. Only the article's title and main body text are extracted, excluding any headers, footers, or ads.</p>
    <h3>Text Analysis</h3>
    <p>After extracting the text, the project performs several text analysis tasks including:</p>
    <ul>
        <li><strong>Tokenization and Preprocessing:</strong> The text is tokenized into words and sentences, converted to lowercase, and stripped of punctuation and stop words.</li>
        <li><strong>Sentiment Analysis:</strong> Using the VADER sentiment analysis tool, the project computes sentiment scores including positive, negative, and polarity scores.</li>
        <li><strong>Linguistic Metrics:</strong> Various linguistic metrics are computed such as:
            <ul>
                <li>Positive Score</li>
                <li>Negative Score</li>
                <li>Polarity Score</li>
                <li>Subjectivity Score</li>
                <li>Average Sentence Length</li>
                <li>Percentage of Complex Words</li>
                <li>Fog Index</li>
                <li>Average Number of Words per Sentence</li>
                <li>Complex Word Count</li>
                <li>Word Count</li>
                <li>Syllable per Word</li>
                <li>Personal Pronouns Count</li>
                <li>Average Word Length</li>
            </ul>
        </li>
    </ul>
    <h3>Output</h3>
    <p>The computed variables are saved in an <code>Output.xlsx</code> file with the following columns:</p>
    <ul>
        <li>URL_ID</li>
        <li>Positive_Score</li>
        <li>Negative_Score</li>
        <li>Polarity_Score</li>
        <li>Subjectivity_Score</li>
        <li>Avg_Sentence_Length</li>
        <li>Percentage_of_Complex_Words</li>
        <li>Fog_Index</li>
        <li>Avg_Number_of_Words_Per_Sentence</li>
        <li>Complex_Word_Count</li>
        <li>Word_Count</li>
        <li>Syllable_Per_Word</li>
        <li>Personal_Pronouns</li>
        <li>Avg_Word_Length</li>
    </ul>
    <h3>Python Libraries and Packages Used</h3>
    <ul>
        <li><strong>pandas:</strong> For reading and writing Excel files, and handling data in DataFrame format.</li>
        <li><strong>nltk (Natural Language Toolkit):</strong> For text processing, including tokenization, stopwords removal, and sentiment analysis.</li>
        <li><strong>requests:</strong> For making HTTP requests to fetch web page content.</li>
        <li><strong>beautifulsoup4:</strong> For parsing HTML content and extracting article text.</li>
        <li><strong>openpyxl:</strong> For working with Excel files.</li>
    </ul>
    <h2>Installation</h2>
    <p>To install the required Python libraries, use the following pip command:</p>
    <pre class="code-block">
pip install pandas nltk requests beautifulsoup4 openpyxl
    </pre>
    <p>Additionally, download the necessary NLTK resources:</p>
    <pre class="code-block">
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
    </pre>
</body>
</html>
