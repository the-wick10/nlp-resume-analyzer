
def extract_skills(text, skills):

    detected_skills = []

    for skill in skills:
        if skill in text:
            detected_skills.append(skill)

    return detected_skills

def find_missing_skills(detected_skills, skills):

    missing_skills = []

    for skill in skills:
        if skill not in detected_skills:
            missing_skills.append(skill)

    return missing_skills