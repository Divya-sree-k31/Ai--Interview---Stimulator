import re
import io
from typing import Dict
from PyPDF2 import PdfReader

def extract_text_from_pdf(file) -> str:
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_txt(file) -> str:
    return file.read().decode("utf-8")

def extract_skills(text: str) -> list:
    # Simple skill extraction (replace with ML/NLP for production)
    skills_keywords = ["python", "java", "c++", "machine learning", "data analysis", "sql", "aws", "azure", "docker", "react", "node.js"]
    found = [skill for skill in skills_keywords if re.search(rf"\\b{re.escape(skill)}\\b", text, re.I)]
    return found

def extract_projects(text: str) -> list:
    # Naive project extraction: look for 'project' or bullet points
    projects = re.findall(r"(?i)(project:.*?)(?:\n|$)", text)
    if not projects:
        projects = re.findall(r"• (.*?)\n", text)
    return projects

def extract_experience(text: str) -> list:
    # Naive experience extraction: look for 'experience' section
    exp_section = re.search(r"(?is)experience(.*?)(education|skills|$)", text)
    if exp_section:
        lines = exp_section.group(1).splitlines()
        return [line.strip() for line in lines if line.strip()]
    return []

def parse_resume(file) -> Dict:
    if file.type == "application/pdf":
        text = extract_text_from_pdf(file)
    else:
        text = extract_text_from_txt(file)
    skills = extract_skills(text)
    projects = extract_projects(text)
    experience = extract_experience(text)
    summary = f"**Skills:** {', '.join(skills) if skills else 'N/A'}\n\n**Projects:** {', '.join(projects) if projects else 'N/A'}\n\n**Experience:** {', '.join(experience) if experience else 'N/A'}"
    return {"skills": skills, "projects": projects, "experience": experience, "summary": summary, "raw_text": text}
