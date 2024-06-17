import requests

API_URL = "https://api-inference.huggingface.co/models/k011/startup-score"
headers = {
    "Authorization": "Bearer ${HF_TOKEN}"
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def process_startup_descriptions(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        startup_data = file.read().strip().split('\n\n')

    for startup_info in startup_data:
        lines = startup_info.strip().split('\n')

        if len(lines) < 12:
            print(f"Error: Insufficient lines in paragraph: {lines}")
            continue

        try:
            company_name = lines[0].split(':')[1].strip()
            gender = lines[1].split(':')[1].strip()
            company_description = lines[2].split(':')[1].strip()
            company_website = lines[3].split(':')[1].strip()
            job_titles = lines[4].split(':')[1].strip()
            business_model = lines[5].split(':')[1].strip()
            revenue = lines[6].split(':')[1].strip()
            profit = lines[7].split(':')[1].strip()
            total_external_funding = lines[8].split(':')[1].strip()
            notable_investors = lines[9].split(':')[1].strip()
            competition_region = lines[10].split(':')[1].strip()
            team_size = lines[11].split(':')[1].strip()
            market_opportunity = lines[12].split(':')[1].strip()
            innovation = lines[13].split(':')[1].strip()
            business_model_desc = lines[14].split(':')[1].strip()
            scalability = lines[15].split(':')[1].strip()
            traction = lines[16].split(':')[1].strip()

            # Construct payload for Hugging Face API
            payload = {
                "inputs": f"Team Size: {team_size}\n"
                          f"Market Opportunity / Problem to be solved: {market_opportunity}\n"
                          f"Innovation: {innovation}\n"
                          f"Business Model: {business_model_desc}\n"
                          f"Scalability: {scalability}\n"
                          f"Traction: {traction}\n"
            }

            # Query Hugging Face API
            output = query(payload)

            # Print or do further processing as needed
            print(f"Company Name: {company_name}")
            print(f"Gender: {gender}")
            print(f"Company Description: {company_description}")
            print(f"Company Website: {company_website}")
            print(f"Job Titles: {job_titles}")
            print(f"Business Model: {business_model}")
            print(f"Revenue: {revenue}")
            print(f"Profit: {profit}")
            print(f"Total External Funding: {total_external_funding}")
            print(f"Notable Investors: {notable_investors}")
            print(f"Competition Region: {competition_region}")
            print(f"Team Size: {team_size}")
            print(f"Market Opportunity / Problem to be solved: {market_opportunity}")
            print(f"Innovation: {innovation}")
            print(f"Business Model: {business_model_desc}")
            print(f"Scalability: {scalability}")
            print(f"Traction: {traction}")
            print(f"Output: {output}\n")

        except IndexError as e:
            print(f"IndexError: {e}. Lines: {lines}")

if __name__ == "__main__":
    file_path = "./uploads/company_data.txt"
    process_startup_descriptions(file_path)
