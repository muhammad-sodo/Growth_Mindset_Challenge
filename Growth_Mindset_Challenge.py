import streamlit as st
import random

# Custom CSS styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# App title and header
st.title("🌱 Growth Mindset Challenge")
st.header("Develop Your Potential Through Continuous Learning")

# Introduction section
with st.expander("What is a Growth Mindset?"):
    st.write("""
    A **growth mindset** is the belief that your abilities and intelligence can be developed through:
    - Hard work
    - Perseverance 
    - Learning from mistakes
    
    This concept was popularized by psychologist **Carol Dweck**. It challenges the fixed mindset notion that our skills are static.
    """)

# Benefits section
st.subheader("Why Adopt a Growth Mindset?")
col1, col2, col3 = st.columns(3)
with col1:
    st.info("""
    **Embrace Challenges**  
    View obstacles as opportunities to learn
    """)
with col2:
    st.info("""
    **Learn from Mistakes**  
    Errors are chances to improve
    """)
with col3:
    st.info("""
    **Persist Through Difficulties**  
    Hard work leads to growth
    """)

# Interactive challenge section
st.subheader("Daily Growth Mindset Challenge")

# Challenge generator
challenges = [
    "Set one learning goal for today (not just a performance goal)",
    "Reflect on a recent mistake and write down what you learned from it",
    "Give genuine praise to someone for their effort, not just their talent",
    "Try a new approach to a problem you've been stuck on",
    "Ask for constructive feedback on your work today",
    "Practice saying 'not yet' instead of 'I can't do this'",
    "Teach someone else something you recently learned"
]

if st.button("Get Today's Challenge"):
    challenge = random.choice(challenges)
    st.session_state.challenge = challenge

if 'challenge' in st.session_state:
    st.markdown(f"""
    <div class="challenge-box">
        <h3>Your Challenge:</h3>
        <p>{st.session_state.challenge}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Challenge completion tracker
    completed = st.checkbox("I completed today's challenge!")
    if completed:
        st.balloons()
        st.success("Great job! You're developing your growth mindset.")

# Reflection journal
st.subheader("Growth Reflection Journal")
journal_entry = st.text_area("What did you learn today? How did you grow?", height=150)
if st.button("Save Reflection"):
    if journal_entry:
        st.session_state.journal = st.session_state.get('journal', []) + [journal_entry]
        st.success("Reflection saved! Review your progress below.")
    else:
        st.warning("Please write something before saving.")

# Display past journal entries
if 'journal' in st.session_state and st.session_state.journal:
    st.subheader("Your Growth Journey")
    for i, entry in enumerate(reversed(st.session_state.journal), 1):
        st.markdown(f"""
        <div class="journal-entry">
            <h4>Reflection #{len(st.session_state.journal)-i+1}</h4>
            <p>{entry}</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<center>
    <p>Keep growing every day! Remember, your potential is limitless.</p>
</center>
""", unsafe_allow_html=True)