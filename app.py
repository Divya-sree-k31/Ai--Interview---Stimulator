import streamlit as st
from resume_parser import parse_resume
from interview_engine import InterviewEngine

st.set_page_config(page_title="AI Interview Simulator", layout="centered")
st.title("AI Interview Simulator (Resume-Based)")

st.write("""
Welcome! Upload your resume (PDF or text) to begin a realistic technical interview simulation based on your actual experience and skills.
""")

uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])

if uploaded_file:
    resume_text = parse_resume(uploaded_file)
    st.success("Resume parsed successfully!")
    st.subheader("Extracted Information:")
    st.write(resume_text['summary'])

    if 'engine' not in st.session_state:
        st.session_state.engine = InterviewEngine(resume_text)
        st.session_state.q_idx = 0
        st.session_state.feedback = ""

    engine = st.session_state.engine
    q_idx = st.session_state.q_idx
    feedback = st.session_state.feedback

    if q_idx < len(engine.questions):
        st.subheader(f"Question {q_idx+1}:")
        st.write(engine.questions[q_idx]['question'])
        user_answer = st.text_area("Your answer:", key=f"answer_{q_idx}")
        if st.button("Submit Answer"):
            feedback = engine.get_feedback(q_idx, user_answer)
            st.session_state.feedback = feedback
            st.session_state.q_idx += 1
        if feedback:
            st.info(f"Feedback: {feedback}")
    else:
        st.success("Interview complete! Well done.")
        if st.button("Restart Interview"):
            del st.session_state.engine
            st.session_state.q_idx = 0
            st.session_state.feedback = ""
else:
    st.info("Please upload your resume to start.")
