# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 12:40:12 2025

@author: dell
"""

import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

# Load the dataset
vc_data = pd.read_csv(R"C:\Users\dell\OneDrive\Documents\LEya\Ops Specialist Case Task -_ VC Qualification -_ Good luck!  - VCs Data from Crunchbase.csv")

# Function to scrape VC website data
def scrape_vc_data(url):
    driver = webdriver.Chrome()  # Use your browser driver
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # Extract relevant details (industry, stage, funding range, etc.)
    # Example logic:
    industry = soup.find('div', class_='industry-section').text if soup.find('div', class_='industry-section') else "N/A"
    funding = soup.find('div', class_='funding-section').text if soup.find('div', class_='funding-section') else "N/A"
    driver.quit()
    return industry, funding

# Apply scraping to each VC
vc_data['Industry'], vc_data['Funding'] = zip(*vc_data['VC Website'].apply(scrape_vc_data))

# Define Fit/Not Fit criteria
vc_data['Fit/Not Fit'] = vc_data.apply(lambda row: "Fit" if "AI" in row['Industry'] and "Seed" in row['Funding'] else "Not Fit", axis=1)

# Save results
vc_data.to_csv('vc_qualified.csv', index=False)

print(vc_data.to_csv)


if os.path.exists('vc_qualified.csv'):
    print("File successfully saved!")
else:
    print("File not found.")