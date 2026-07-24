import streamlit as st

# ---------------- Page Configuration ----------------
st.set_page_config(page_title="Quiz App", page_icon="📝")

st.title("📝 Interactive Quiz & Score Tracker")

# ---------------- Questions ----------------
questions = [
    {
        "question": "1. Which keyword is used to define a function in Python?",
        "options": ["function", "def", "fun", "define"],
        "answer": "def"
    },
    {
        "question": "2. Which data type stores True or False values?",
        "options": ["int", "str", "bool", "list"],
        "answer": "bool"
    },
    {
        "question": "3. Which symbol is used for comments in Python?",
        "options": ["//", "/* */", "#", "--"],
        "answer": "#"
    },
    {
        "question": "4. Which function is used to display output?",
        "options": ["display()", "echo()", "print()", "show()"],
        "answer": "print()"
    },
    {
        "question": "5. Which collection stores key-value pairs?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": "Dictionary"
    }
]

# ---------------- Session State ----------------
if "submitted" not in st.session_state:
    st.session_state.submitted = False

if "score" not in st.session_state:
    st.session_state.score = 0

# ---------------- Display Questions ----------------
answers = []

for i, q in enumerate(questions):

    st.write("**Choose one option:**")

    answer = st.radio(
        q["question"],
        q["options"],
        index=None,
        key=f"question_{i}"
    )

    answers.append(answer)

# ---------------- Submit Button ----------------
if st.button("Submit Quiz"):

    if None in answers:
        st.warning("⚠ Please answer all the questions before submitting.")
    else:

        score = 0

        for i in range(len(questions)):
            if answers[i] == questions[i]["answer"]:
                score += 1

        st.session_state.score = score
        st.session_state.submitted = True

# ---------------- Result ----------------
if st.session_state.submitted:

    st.success("🎉 Quiz Submitted Successfully!")

    total = len(questions)

    percentage = (st.session_state.score / total) * 100

    st.subheader(f"Score : {st.session_state.score} / {total}")

    st.progress(percentage / 100)

    st.write(f"Percentage : {percentage:.2f}%")

    if percentage == 100:
        st.balloons()
        st.success("🏆 Excellent! Perfect Score!")

    elif percentage >= 80:
        st.success("👏 Very Good!")

    elif percentage >= 60:
        st.info("👍 Good Job!")

    elif percentage >= 40:
        st.warning("🙂 Keep Practicing!")

    else:
        st.error("❌ Better Luck Next Time!")

    st.markdown("---")

    st.subheader("Answer Review")

    for i, q in enumerate(questions):

        if answers[i] == q["answer"]:
            st.success(f"Q{i+1}: Correct ✅")
        else:
            st.error(
                f"Q{i+1}: Wrong ❌ | Correct Answer: {q['answer']}"
            )

# ---------------- Reset Button ----------------
if st.button("Reset Quiz"):

    for i in range(len(questions)):
        if f"question_{i}" in st.session_state:
            del st.session_state[f"question_{i}"]

    st.session_state.score = 0
    st.session_state.submitted = False

    st.rerun()