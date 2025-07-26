# parser.py
import re
from pdfminer.high_level import extract_text

SKILLS_DB = [
    'python', 'java', 'c++', 'html', 'css', 'javascript',
    'flask', 'django', 'sql', 'mongodb', 'excel', 'machine learning'
]

def extract_email(text):
    match = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return match[0] if match else None

def extract_phone(text):
    match = re.findall(r'\+?\d[\d -]{8,12}\d', text)
    return match[0] if match else None

def extract_skills(text):
    text = text.lower()
    return list({skill for skill in SKILLS_DB if skill in text})

def extract_name(text):
    lines = text.strip().split('\n')
    for line in lines:
        if line.strip() and len(line.strip().split(" ")) <= 4:
            return line.strip()
    return "Not Found"

def parse_resume(file_path):
    text = extract_text(file_path)
    return {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "Skills": extract_skills(text)
    }
