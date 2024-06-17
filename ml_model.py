from flask import Flask, jsonify, render_template, request
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

# Access the HF_TOKEN environment variable
KEY = os.getenv('HF_TOKEN')

API_URL = "https://api-inference.huggingface.co/models/k011/startup-score"
headers = {
    "Authorization": f"Bearer {KEY}"
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    file_path = "./uploads/company_data.txt"
    results = process_startup_descriptions(file_path)
    return render_template('data.html', results=results)

@app.route('/data', methods=['POST'])
def process_data():
    file_path = "./uploads/company_data.txt"
    results = process_startup_descriptions(file_path)
    return jsonify(results)

def process_startup_descriptions(file_path):
    results = []
    with open(file_path, 'r', encoding='utf-8') as file:
        startup_data = file.read().strip().split('\n\n')

    for startup_info in startup_data:
        lines = startup_info.strip().split('\n')

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

        payload = {
            "inputs": f"Team Size: {team_size}\n"
                      f"Market Opportunity / Problem to be solved: {market_opportunity}\n"
                      f"Innovation: {innovation}\n"
                      f"Business Model: {business_model_desc}\n"
                      f"Scalability: {scalability}\n"
                      f"Traction: {traction}\n"
        }

        output = query(payload)
        
        highest_score = max(output[0], key=lambda x: x['score'])
        eligibility = f"{highest_score['label']} (Score: {highest_score['score']:.2f})"
        
        result = {
                "Company Name": company_name,
                "Founder": gender,
                "Company Description": company_description,
                "Company Website": company_website,
                "Job Titles": job_titles,
                "Business Model": business_model,
                "Revenue": revenue,
                "Profit": profit,
                "Total External Funding": total_external_funding,
                "Notable Investors": notable_investors,
                "Competition Region": competition_region,
                "Eligibility": eligibility,
        }

        results.append(result)
        
    return results

if __name__ == "__main__":
    app.run(debug=True)
