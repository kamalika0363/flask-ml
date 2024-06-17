# Startup Screening Application - README

## Overview
This project automates the screening process for startups by leveraging a fine-tuned AI model. The application evaluates startups based on existing criteria and determines their eligibility for funding. The only input required is a CSV file containing the startup details with specific required columns.

## Model
https://huggingface.co/k011/startup-score

## Dataset 
https://huggingface.co/datasets/k011/startup_eligibility_scores

## Features
- **Automated Screening:** Streamlines the evaluation process for startups using AI.
- **Fine-Tuned Model:** Utilizes a custom-trained AI model to assess eligibility for funding.
- **CSV Input:** Accepts a CSV file with necessary startup details for evaluation.
- **Eligibility Output:** Provides a clear decision on whether a startup is eligible for funding.

## Prerequisites
- Python 3.x
- Required Python libraries (install via `requirements.txt`)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## CSV File Requirements
The CSV file should contain the following columns:
- **Startup Name:** Name of the startup
- **Founder:** Name(s) of the founder(s)
- **Industry:** Industry sector of the startup
- **Stage:** Current stage of the startup (e.g., Seed, Series A)
- **Funding Needed:** Amount of funding required
- **Revenue:** Current revenue of the startup
- **Employee Count:** Number of employees

### Example CSV Format
```csv
Startup Name,Founder,Industry,Stage,Funding Needed,Revenue,Employee Count
Startup A,Founder A,Tech,Seed,500000,100000,10
Startup B,Founder B,Health,Series A,1000000,200000,20
```

## Usage
1. Ensure your CSV file is formatted correctly as per the requirements.
2. Run the application:
   ```bash
   python screen_startups.py --input <path-to-csv-file>
   ```
3. The application will process the CSV file and output the eligibility results.

### Command Line Arguments
- `--input`: Path to the input CSV file.

### Example Command
```bash
python screen_startups.py --input startups.csv
```

## Output
The application will generate an output file `company_paragraphs.txt` with the following columns:
- **Startup Name:** Name of the startup
- **Eligibility:** "Eligible" or "Not Eligible" based on the evaluation

### Example Output
![alt text](image-1.png)
## Demo 
<http://cwb-kammo.centralindia.cloudapp.azure.com/>

## Screenshots
![Example of Output](image.png)