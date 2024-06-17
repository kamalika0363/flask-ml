import pandas as pd
import random
from ml_model import process_startup_descriptions

def transform_csv_to_txt(file_path):
    data = pd.read_csv(file_path)

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

    def get_random_sentences(sentences, num_sentences=2):
        return ' '.join(random.sample(sentences, num_sentences))

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
            f"{get_random_sentences(additional_sentences)}"
        )
        paragraphs.append(paragraph)

    with open('uploads/company_paragraphs.txt', 'w') as f:
        for paragraph in paragraphs:
            f.write(paragraph + "\n\n")

    return 'uploads/company_paragraphs.txt'

if __name__ == "__main__":
    # file_path = "./uploads/application_form_sample.csv"
    # txt_file_path = transform_csv_to_txt(file_path)
    # print(txt_file_path)
    file_path = "./uploads/company_data.txt"
    process_startup_descriptions(file_path)