import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd


def extract_technographic_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')

        
        detected_technologies = {
            'jQuery': 'jquery.min.js',
            'WordPress': 'wp-content/themes/',
            'Joomla': 'joomla.min.js',
            'Drupal': 'drupal.min.css',
            'Magento': 'magento.min.css',
            'Shopify': 'shopify.min.js',
            'React': 'react.min.js',
            'Vue.js': 'vue.min.js',
            'Angular': 'angular.min.js',
            'Ruby on Rails': 'rubyonrails.min.css',
            'ASP.NET': 'aspnet.min.js',
            'Django': 'django.min.css',
            'Node.js': 'nodejs.min.js',
        }

        # Detect the presence of technologies
        detected_data = []
        for tech, signature in detected_technologies.items():
            if signature in str(soup):
                detected_data.append(tech)

        return ', '.join(detected_data)
    except requests.exceptions.RequestException as e:
        return f'Error: RequestException - {str(e)}'
    except Exception as e:
        return f'Error: {str(e)}'


input_file = 'order.csv'
output_file = 'arun_Task2_Output.csv'

data = []

with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  
    for row in reader:
        website = row[0]
        technographic_data = extract_technographic_data(website)
        data.append([website, technographic_data])


output_df = pd.DataFrame(data, columns=['Website', 'Technographic Data'])
output_df.to_csv(output_file, index=False)

print("Scraping and data extraction completed. Output saved to 'arun_Task2_Output.csv'")