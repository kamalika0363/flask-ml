import pandas as pd
import random
import os  # Import the 'os' module for file operations

def transform_csv_to_txt(csv_file):
    data = pd.read_csv(csv_file)

    selected_columns = [
        "Company Name",
        "Gender",
        "Company Description",
        "Company Website",
        "Job titles",
        "Business Model",
        "If generating revenue, what is your revenue by year?",
        "If generating profit, what is your profit by year?",
        "What is the total amount of external funding you have raised so far (USD)?",
        "Notable Investors to Date",
        "Competition Region"
    ]

    additional_sentences = [
        "The company has shown tremendous growth in the past year.",
        "It is known for its innovative solutions in the industry.",
        "The team consists of experienced professionals from diverse backgrounds.",
        "The company has received numerous awards for its outstanding performance.",
        "Its customer base has been expanding rapidly across different regions."
    ]

    paragraphs = []
    for index, row in data[selected_columns].iterrows():
        paragraph = (
            f"Company Name: {row['Company Name']}\n"
            f"Gender: {row['Gender']}\n"
            f"Company Description: {row['Company Description']}\n"
            f"Company Website: {row['Company Website']}\n"
            f"Job Titles: {row['Job titles']}\n"
            f"Business Model: {row['Business Model']}\n"
            f"Revenue: {row['If generating revenue, what is your revenue by year?']}\n"
            f"Profit: {row['If generating profit, what is your profit by year?']}\n"
            f"Total External Funding: {row['What is the total amount of external funding you have raised so far (USD)?']}\n"
            f"Notable Investors: {row['Notable Investors to Date']}\n"
            f"Competition Region: {row['Competition Region']}\n"
            f"{random.choice(additional_sentences)}\n"
        )
        paragraphs.append(paragraph)

    txt_file = os.path.join('uploads', 'company_paragraphs.txt')
    with open(txt_file, 'w') as f:
        f.write('\n\n'.join(paragraphs))

    return txt_file
