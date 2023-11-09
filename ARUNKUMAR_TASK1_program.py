import requests
from bs4 import BeautifulSoup
import csv
import re
companies = [
    ("Advanced Physical Therapy Specialists", "https://www.advancedpts.com/"),
    ("Aiken Chiropractic Wellness Center Inc", "https://www.aikenchiropractic.com/"),
    ("Alpha Medical Clinic and MedSpa", "https://www.alphamedical.com.au/"),
    ("Coastal Integrative Healthcare Inc", "https://coastalintegrativehealthcare.com/"),
    ("Dermatology & Cutaneous Surgery Institute Dcsi Pa", "https://www.mydcsi.com/"),
    ("East Orlando Medical Care Llc", "http://eastorlandohealth.com/"),
    ("Eyes of Winter Park Llc", "https://www.eawp.me/"),
    ("Florida Retina Specialists PA", "https://www.floridaretinaspecialists.com/"),
    ("Gulf Coast Holistic and Primary Care Inc", "https://www.hcafloridahealthcare.com/physicians/profile/Dr-Angel-F-Berio-MD"),
    ("M & M Medical Enterprises Inc", "https://www.mandmmed.com/"),
    ("Space Coast Psychiatry Inc", "https://spacecoastpsychiatry.org/"),
    ("Westchase Orthopaedics Inc", "http://horanmd.com/")
]
def extract_contact_info(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')
        emails = []
        phone_numbers = []
        for email in soup.find_all('a', href=True):
            if 'mailto:' in email['href']:
                emails.append(email['href'].replace('mailto:', ''))
        phone_number_regex = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'
        phone_numbers = re.findall(phone_number_regex, soup.get_text())

        return emails, phone_numbers
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return ["Can't Scrape"], ["Can't Scrape"]
with open('contact_information.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Company Name", "Emails", "Phone Numbers"])
    for company_name, company_url in companies:
        emails, phone_numbers = extract_contact_info(company_url)
        cleaned_emails = ", ".join(emails) if emails else "Can't Scrape"
        cleaned_phone_numbers = ", ".join(phone_numbers) if phone_numbers else "Can't Scrape"
        csv_writer.writerow([company_name, cleaned_emails, cleaned_phone_numbers])