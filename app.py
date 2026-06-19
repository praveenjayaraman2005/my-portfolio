import streamlit as st
import pandas as pd
import sqlite3



menu = st.sidebar.radio(
    "Navigation",
    ["Home", "Projects","resume", "Form", "Stored Data"]
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
if menu == "Home":
    st.header("🏠 Home Page")
    st.write("Welcome to dashboard")
    

# ---------------- PROJECTS ----------------
elif menu == "Projects":
    st.header("📁 My Projects")

    st.subheader("1. TCP Socket Chat Application")
    
    
    
    st.write("Real-time chat system using Python sockets.")

    st.subheader("2. Employee Management System")
    st.write("""
    Features:
    - Add Employee
    - View Employee
    - Update Employee
    - Delete Employee
    Built using Python + SQLite + Streamlit
    """)

    st.subheader("3. IoT-Based Smart Room Simulator")
    st.write("""
    Features:
    - Temperature monitoring
    - Light control simulation
    - Fan ON/OFF logic
    - Dashboard visualization using Streamlit
    """)
    st.link_button(
    "Click",
    "https://thingspeak.mathworks.com/channels/3034626/private_show"
)


elif menu=="resume":
    st.header("My Resume")

    with open("resume.pdf","rb") as file:
        resume_data=file.read()

    st.download_button(
    label="📄 Download My Resume",
    data=resume_data,
    file_name="My_Resume.pdf",
    mime="application/pdf"
)
    

# ---------------- FORM ----------------
elif menu == "Form":
    st.header("📝 User Form")

    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    purpose = st.text_area("Purpose")

    if st.button("Submit"):
        if not name or not email or not phone or not purpose:
            st.error("Fill all fields")
        elif not phone.isdigit():
            st.error("Phone must be numbers only")
        else:
            cursor.execute(
                "INSERT INTO users VALUES (?, ?, ?, ?)",
                (name, email, phone, purpose)
            )
            conn.commit()
            st.success("Data Saved")

# ---------------- STORED DATA WITH LOGIN ----------------
elif menu == "Stored Data":
    st.header("🔐 Admin Login Required")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # fixed login (you can improve later using DB)
    ADMIN_USER = "admin"
    ADMIN_PASS = "1234"

    if st.button("Login"):

        if username == ADMIN_USER and password == ADMIN_PASS:
            st.success("Login Successful 🎉")

            cursor.execute("SELECT * FROM users")
            data = cursor.fetchall()

            if len(data) == 0:
                st.warning("No data found")
            else:
                df = pd.DataFrame(data, columns=["Name", "Email", "Phone", "Purpose"])
                st.table(df)

        else:
            st.error("Invalid Username or Password")

conn.close()