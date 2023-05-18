# English

### This code snippet demonstrates how to use the Transformers library to perform text summarization on a blog post. The code uses the pip install transformers command to install the required library and imports the necessary modules: pipeline from Transformers, and BeautifulSoup and requests for web scraping.
### Load Summarization Pipeline: The code initializes a summarization pipeline using the pipeline("summarization") function from Transformers.

### Get Blog Post from Medium: The code fetches the content of a blog post from a Medium or Hacker Noon URL. The URL can be modified to retrieve content from different sources. It uses the requests library to make an HTTP  ### request to the URL and BeautifulSoup to parse the HTML response. It extracts the text from the <h1> and <p> tags and concatenates them into a single string.

### Preprocess Text: The code performs some preprocessing on the article text to split it into chunks of a maximum length (500 words in this case) to fit the summarization model's input requirements. It splits the text  ###  into sentences by adding "<eos>" at the end of each sentence and then divides the sentences into chunks of suitable size.

### Summarize Text: The code iterates over the chunks and uses the summarization pipeline to generate summaries for each chunk. It sets the maximum summary length to 120 words and the minimum length to 30 words. The ### ### do_sample parameter is set to False to generate deterministic outputs.

### Output to Text File: The code joins the generated summaries into a single text string and writes it to a file named "blogsummary.txt".

### Note: Make sure to install the required libraries (transformers, beautifulsoup4) before running the code.
