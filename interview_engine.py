import random

HR_QUESTIONS = [
    "Tell me about yourself.",
    "What motivates you in your career?",
    "Describe a challenge you faced and how you overcame it.",
    "How do you handle tight deadlines or pressure?"
]

TECH_TEMPLATES = [
    "Can you explain how you have used {skill} in your work?",
    "What are the main challenges when working with {skill}?",
    "Describe a project where you applied {skill}.",
    "How would you troubleshoot an issue with {skill}?"
]

PROJECT_TEMPLATES = [
    "Tell me about your project: {project}.",
    "What was your role in {project}?",
    "What technical challenges did you face in {project}?",
    "How did you measure the success of {project}?"
]

class InterviewEngine:
    def __init__(self, resume_info):
        self.resume_info = resume_info
        self.questions = self.generate_questions()

    def generate_questions(self):
        questions = []
        # Technical questions from skills
        for skill in self.resume_info.get("skills", []):
            for template in random.sample(TECH_TEMPLATES, min(2, len(TECH_TEMPLATES))):
                questions.append({"type": "technical", "question": template.format(skill=skill)})
        # Project-based questions
        for project in self.resume_info.get("projects", []):
            for template in random.sample(PROJECT_TEMPLATES, min(2, len(PROJECT_TEMPLATES))):
                questions.append({"type": "project", "question": template.format(project=project)})
        # HR-style questions (pick 2 random)
        for q in random.sample(HR_QUESTIONS, min(2, len(HR_QUESTIONS))):
            questions.append({"type": "hr", "question": q})
        random.shuffle(questions)
        return questions

    def get_feedback(self, q_idx, answer):
        # Simple feedback logic (placeholder for AI)
        if not answer.strip():
            return "Try to provide a detailed answer."
        if len(answer.split()) < 10:
            return "Expand your answer with more details."
        return "Good answer!"
