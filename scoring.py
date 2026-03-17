def calculate_score(detected_skills, skills):

    total_skills = len(skills)
    found_skills = len(detected_skills)

    score = (found_skills / total_skills) * 100

    return round(score, 2)