import streamlit as st
import pandas as pd
import sqlite3

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Praveen Portfolio",
    page_icon="🚀",
    layout="wide"
)

# ---------------- HIDE STREAMLIT UI ----------------
st.markdown("""
<style>
footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
menu = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "💻 Projects",
        "📄 Resume",
        "📝 Form",
        "🔐 Stored Data"
    ]
)

# ---------------- DATABASE ----------------
conn = sqlite3.connect("form.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    email TEXT,
    phone TEXT,
    purpose TEXT
)
""")

# ---------------- HOME ----------------
if menu == "🏠 Home":

    st.title("🚀 Praveen Portfolio")

    st.header("Welcome")

    st.write("""
    Hello! I am Praveen.

    Skills:
    - Python
    - Streamlit
    - Flask
    - SQLite
    - Socket Programming
    - IoT Projects
    """)

# ---------------- PROJECTS ----------------
elif menu == "💻 Projects":

    st.title("💻 My Projects")

    st.subheader("1. TCP Socket Chat Application")

    st.write("""
    Real-time chat application using Python Socket Programming.
    """)

    st.subheader("2. Employee Management System")

    st.write("""
    Features:
    - Add Employee
    - View Employee
    - Update Employee
    - Delete Employee

    Technologies:
    - Python
    - SQLite
    - Streamlit
    """)

    st.subheader("3. IoT-Based Smart Room Simulator")

    st.write("""
    Features:
    - Temperature Monitoring
    - Light Control
    - Fan ON/OFF Automation
    - Dashboard Visualization
    """)

    st.link_button(
        "🔗 View IoT Dashboard",
        "https://thingspeak.mathworks.com/channels/3034626/private_show"
    )

# ---------------- RESUME ----------------
elif menu == "📄 Resume":

    st.title("📄 My Resume")

    with open("resume.pdf", "rb") as file:
        resume_data = file.read()

    st.download_button(
        label="📥 Download My Resume",
        data=resume_data,
        file_name="Praveen_Resume.pdf",
        mime="application/pdf"
    )

# ---------------- FORM ----------------
elif menu == "📝 Form":

    st.title("📝 Contact Form")

    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    purpose = st.text_area("Purpose")

    if st.button("Submit"):

        if not name or not email or not phone or not purpose:
            st.error("Please fill all fields")

        elif not phone.isdigit():
            st.error("Phone number must contain only digits")

        else:
            cursor.execute(
                "INSERT INTO users VALUES (?, ?, ?, ?)",
                (name, email, phone, purpose)
            )

            conn.commit()

            st.success("Data Saved Successfully")

# ---------------- STORED DATA ----------------
elif menu == "🔐 Stored Data":

    st.title("🔐 Admin Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    ADMIN_USER = "admin"
    ADMIN_PASS = "1234"

    if st.button("Login"):

        if username == ADMIN_USER and password == ADMIN_PASS:

            st.success("Login Successful")

            cursor.execute("SELECT * FROM users")

            data = cursor.fetchall()

            if len(data) == 0:
                st.warning("No Data Found")

            else:
                df = pd.DataFrame(
                    data,
                    columns=["Name", "Email", "Phone", "Purpose"]
                )

                st.dataframe(df, use_container_width=True)

        else:
            st.error("Invalid Username or Password")

# ---------------- CLOSE DATABASE ----------------
conn.close()
