# Motorcycle-Handbook-scrapping
Scrapping The Official MTO Motorcycle Handbook using Python, Selenium

## Description
I am preparing for my M1 exam, however could not find a pdf copy of the book so I scrapped it. 
The scraped version does not have images and styling of the original website, 
but is free and contains all the relevant text.
The code may be useful for people starting with Selenium and Web-Scrapping in general
  
The website I scraped : http://www.mto.gov.on.ca/english/handbook/motorcycles/index.shtml

## Files 
* **chrome** - contains ChromeDriver required to run Selenium. The ChromeDriver **must** match the version
of Chrome Browser you have installed on your computer. So if you have a mistake, and Chrome does not open
by itself and start doing stuff, then this is the first thing to check;
* **scrapped pages** - contains html pages from the Handbook Website: 
* **jupyter_notebook.ipynb** - I was orginally running code from the notebook so decided to attach it
* **scraper.py** - the file with code

## How to run
Clone the code, locate the terminal to the right directory:
```
python scraper.py
```
Or open jupyter notebook and run code from there.
