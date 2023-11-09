import requests
import pandas as pd

base_url = "https://appsource.microsoft.com/en-us/api/web/search?source=partner-directory&pageSize=100"
partner_names = []
regions = []
short_descriptions = []
contact_me_hrefs = []
for page in range(1, 4):
    url = f"{base_url}&page={page}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for result in data.get("results", []):
            partner_name = result.get("organizationName", "").strip()
            region = result.get("locationName", "").strip()
            short_description = result.get("shortDescription", "").strip()
            contact_me_href = result.get("contactButtonTargetUrl", "N/A").strip()
            partner_names.append(partner_name)
            regions.append(region)
            short_descriptions.append(short_description)
            contact_me_hrefs.append(contact_me_href)
    else:
        print(f"Failed to retrieve data from page {page}")
data = {
    "Partner Name": partner_names,
    "Region": regions,
    "Short Description": short_descriptions,
    "Contact Me Button Href": contact_me_hrefs
}
df = pd.DataFrame(data)
df.to_csv("arun_Task3_Output.csv", index=False, encoding="utf-8")

print("Scraping completed. Data saved to 'arun_Task3_Output.csv'.")