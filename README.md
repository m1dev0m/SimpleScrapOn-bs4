# SimpleScrapOn-bs4
This is a simple web scraping project built using `BeautifulSoup4 (bs4)` in 3 minutes.

## Tools Used
- **BeautifulSoup4 (bs4)**
- **requests**
- **csv**
- **lxml**

## What Was Scraped
The script scrapes data from the official website of the **Senate of Kazakhstan**:  
[https://senate.parlam.kz/ru-RU/about/deputies](https://senate.parlam.kz/ru-RU/about/deputies).  
It extracts information about senators, including their names and positions.

## How to Run
1. Install the required libraries:
    ```bash
    pip install beautifulsoup4 requests lxml
    ```
2. Run the script:
    ```bash
    python scraper.py
    ```

## Output
The script will scrape data and save it in a CSV file called `deputies.csv`.
