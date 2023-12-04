# pubrio-technical-test
## Prerequisites:
- python 3.11.1
1. Install the required dependencies
`pip install -r requirements.txt`
2. Include a .env file as follows in the base directory to set the environment variables of the server:
    ```
    OPEN_API_KEY=your-own-openai-api-key
    ```
3. Include extracted html file called "output.txt" in the base directory to extract relevant information
4. Run command below for main function
`python main.py`

## Notes:
scrape_website.py is used to scrape a website and generate a txt file, not required to use if you have your own txt file