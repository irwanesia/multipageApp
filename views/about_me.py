import streamlit as st 

from forms.contact import contact_form

# Please replace st.experimental_dialog with st.dialog. st.experimental_dialog will be removed after 2025-01-01.
# @st.experimental_dialog("Contact Me") 
@st.dialog("Contact Me") 
def show_contact_form():
    contact_form()

st.title("About Me")
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/profile.png", width=230)
with col2:
    st.title("Irwan", anchor=False)
    st.write("I am a software engineer with a passion for building innovative solutions. I have experience 3 years")

    if st.button(":material/call: Contact Me"):
        show_contact_form()
        
# --- EXPERIENCe & QUALIFICATIONS
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - I have 3 years of experience in software engineering and have worked on various projects
    - including web development
    - mobile app development, and data analysis. 
    - I have a strong foundation in computer science and have a passion for learning new technologies and techniques.
    """
)

# --- SKILS ---
st.write("\n")
st.subheader("Hard Skils", anchor=False)
st.write(
    """
    - Pemrograman Python
    - Pengembangan Web (Django, Flask)
    - Analisis Data (Pandas, NumPy)
    - Machine Learning (scikit-learn, TensorFlow)
    - Automasi Skrip
    - Pengujian Perangkat Lunak (unittest, pytest)
    - Basis Data (SQL, SQLAlchemy)
    - Pengembangan API (Flask-RESTful, FastAPI)
    - Penggunaan Virtual Environment
    - Pemrograman Asinkron (asyncio)
    """
)