import streamlit as st
import plotly.express as px

from resume_parser import extract_text
from skill_extractor import extract_skills, find_missing_skills
from scoring import calculate_score
from skills_db import ds_skills, software_skills, ece_skills

# Title and Description
st.title("NLP-Based Resume Analyzer")
st.markdown("### Skill Extraction and Resume Evaluation System")

# Domain Selection
domain = st.selectbox(
    "Select Domain",
    ["Data Science", "Software Development", "ECE"]
)

# File Upload
uploaded_file = st.file_uploader("Upload your resume", type=["pdf"])

if uploaded_file is not None:

    # Select skills based on domain
    if domain == "Data Science":
        skills = ds_skills
    elif domain == "Software Development":
        skills = software_skills
    else:
        skills = ece_skills

    # Extract text
    text = extract_text(uploaded_file)

    st.success("Resume uploaded successfully!")

    # Show Resume Text
    st.subheader("Extracted Resume Text")
    st.text_area("Resume Content", text, height=400)

    # Detect Skills
    detected_skills = extract_skills(text, skills)

    st.subheader("Detected Skills")
    for skill in detected_skills:
        st.markdown(f"- {skill}")

    # Calculate Score
    score = calculate_score(detected_skills, skills)

    st.subheader("Resume Score")
    st.write(f"{score}%")

    # Resume Strength
    if score < 40:
        strength = "Weak"
    elif score < 70:
        strength = "Average"
    else:
        strength = "Strong"

    st.subheader("Resume Strength")
    st.write(strength)

    # Progress Bar
    st.progress(score / 100)

    # Missing Skills
    missing_skills = find_missing_skills(detected_skills, skills)

    st.subheader("Missing Skills")
    for skill in missing_skills:
        st.markdown(f"- {skill}")

    # Chart
    found_count = len(detected_skills)
    missing_count = len(missing_skills)

    data = {
        "Category": ["Skills Found", "Missing Skills"],
        "Count": [found_count, missing_count]
    }

    fig = px.bar(
        data,
        x="Category",
        y="Count",
        color="Category",
        title="Skill Coverage"
    )

    st.plotly_chart(fig)

# Footer
st.markdown("---")
st.markdown("Built by Hemanth | Data Science Project")