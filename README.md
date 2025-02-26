# Book Scraper Project

This is a **web scraping project** that extracts book information (title, author, and rating) from [BooksToScrape](http://books.toscrape.com/) using **BeautifulSoup** and **Pandas**. The scraped data is saved in both CSV and Excel formats.

## Features
✅ Scrapes book **titles**, **authors**, and **ratings** from multiple pages  
✅ Saves data to **CSV (`books.csv`) and Excel (`books.xlsx`)**  
✅ Uses **Pandas** for data handling  
✅ Handles pagination to scrape all books on the website

## Installation
### Clone the repository
```bash
git clone https://github.com/your-username/BookScraper.git
cd BookScraper
```

### Install dependencies (if not already installed)
```bash
pip install requests beautifulsoup4 pandas openpyxl
```

## Usage
Run the script to start scraping:
```bash
python scraper.py
```
The scraped data will be saved as:
- `books.csv` (Plain text, can be opened in VS Code)
- `books.xlsx` (Excel format, needs Microsoft Excel or LibreOffice)

## Project Structure
```
BookScraper/
│-- scraper.py      # Main script for scraping books
│-- books.csv       # CSV file with scraped data
│-- books.xlsx      # Excel file with scraped data
│-- README.md       # Project documentation
│-- .gitignore      # Ignore unnecessary files (Excel, temp files, etc.)
```

## Future Enhancements
- 🔹 Extract book prices 💰  
- 🔹 Scrape book descriptions 📖  
- 🔹 Store data in a database 🗄️  

## Contributions
Feel free to fork this project and contribute! 🚀

## License
This project is open-source under the **MIT License**.


