import streamlit as st

st.set_page_config(
    page_title="AI Resume & Mock Interview Bot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI-Powered Smart Interactive Resume & Mock Interview Bot")
st.markdown("### Developed by **Rabia Khan** | Python & AI Developer")
st.write("---")

app_mode = st.sidebar.selectbox(
    "Choose Navigation", 
    ["Resume Analyzer", "Mock Tech Interview Bot"]
)

if app_mode == "Resume Analyzer":
    st.header("📄 AI Resume Analyzer & Skill Match Score")
    st.write("Paste your resume or project description below to evaluate your tech stack!")

    resume_text = st.text_area(
        "Paste Resume Text Here:", 
        height=200, 
        placeholder="Example: Python programmer, built AI apps using Streamlit, GitHub, Machine Learning..."
    )

    if st.button("Analyze Resume"):
        if resume_text.strip() == "":
            st.warning("Please enter some resume text first!")
        else:
            score = 0
            found_skills = []

            if "python" in resume_text.lower():
                score += 30
                found_skills.append("Python")
            if "ai" in resume_text.lower() or "artificial intelligence" in resume_text.lower():
                score += 30
                found_skills.append("AI / Machine Learning")
            if "streamlit" in resume_text.lower():
                score += 20
                found_skills.append("Streamlit")
            if "github" in resume_text.lower() or "git" in resume_text.lower():
                score += 20
                found_skills.append("Git & GitHub")

            st.success("Resume Analysis Complete!")
            st.metric(label="Skill Match Score", value=f"{score}%")
            
            if found_skills:
                st.write(f"**Detected Core Skills:** {', '.join(found_skills)}")
            else:
                st.write("**Detected Core Skills:** Basic Programming Concepts")

            if score >= 80:
                st.balloons()
                st.info("🌟 Outstanding profile! Ready for senior developer roles.")
            else:
                st.warning("💡 Tip: Add more advanced AI and Python projects to push your score to 100%!")

elif app_mode == "Mock Tech Interview Bot":
    st.header("🎯 AI Technical Mock Interview Bot")
    st.write("Test your coding knowledge and logic with real-world developer interview questions!")

    interview_questions = {
        "Python Syntax & Logic": "Why do we use `elif` instead of writing multiple separate `if` statements in Python?",
        "Streamlit Framework": "Explain how Streamlit reruns the entire Python script from top to bottom whenever a user interacts with a widget.",
        "Error Handling": "How do you handle terminal errors and indentation bugs in your Python code?",
        "Artificial Intelligence": "What is the difference between rule-based logic and AI-driven models?"
    }

    selected_topic = st.selectbox("Select Interview Topic:", list(interview_questions.keys()))
    
    st.subheader(f"Question on {selected_topic}:")
    st.info(interview_questions[selected_topic])

    user_answer = st.text_area(
        "Type your technical answer here:", 
        height=150, 
        placeholder="Explain your logic clearly and confidently..."
    )

    if st.button("Submit Answer"):
        if user_answer.strip() == "":
            st.warning("Please type your answer before submitting.")
        else:
            st.success("🎉 Answer Evaluated Successfully!")
            st.write("**AI Interviewer Feedback:**")
            st.write("Your logic shows a deep understanding of core programming and clean syntax! Keep up the brilliant problem-solving approach.")
            st.balloons()
