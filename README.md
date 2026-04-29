# CMPSC132_Final_Project

# Project Description

A web scraper built in Python that extracts laptop name, price, and rating from a static e-commerce website. The program displays the data in the terminal and allows sorting and filtering by name, price, or rating.

# Requirements

Install the required libraries before running:

pip install requests beautifulsoup4

# How to Run

python3 -i Final_Project.py

# Usage

Note: The URL is hardcoded in the script as it only works with one specific website, so no changes are needed before running.

x = LaptopScraper(url)
x.scrape()

    # Display all laptops

        x.display()

    # Sort, filter, and display results

        x.filter("Laptop", None)  # sort alphabetically, show all
        x.filter("Price", 10)     # sort by price, show top 10
        x.filter("Rating", 5)     # sort by rating, show top 5
        x.display_filtered()

# Project Link

[Final Project Report](CMPSC132%20Report.pdf)