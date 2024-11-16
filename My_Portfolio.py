import streamlit as st
import time

st.write("# WELCOME TO KG - KITE")
st.write("Student Verification Form")

name = st.text_input("Name :")
st.write(name)

dob = st.text_input("Date of Birth :")
st.write(dob)

gen = st.text_input("Gender :")
st.write(gen)

admn = st.text_input("Admission Number :")
st.write(admn)

rno = st.text_input("Roll Number :")
st.write(rno)

reg_no = st.text_input("Register Number :")
st.write(reg_no)

comm = st.text_input("Community :")
st.write(comm)

grad = st.text_input("Batch :")
st.write(grad)

dept = st.text_input("Department :")
st.write(dept)

fname = st.text_input("Father's Name :")
st.write(fname)

mname = st.text_input("Mother's Name :")
st.write(mname)

adrs = st.text_input("Address :")
st.write(adrs)

phone = st.text_input("Student's Mobile :")
st.write(phone)

phone1 = st.text_input("Parent's Mobile ")
st.write(phone1)

fincome = st.text_input("Family Income :")
st.write(fincome)

cof = st.text_input("Cut off :")
st.write(cof)

srm = st.text_input("Stream in 12th std :")
st.write(srm)

marks = st.text_input("Marks Secured in 12th :")
st.write(marks)

marks1 = st.text_input("Marks Seured in 10th :")
st.write(marks1)

hobbies = st.text_input("Hobbies")
st.write(hobbies)

skills = st.text_input("Skills")
st.write(skills)

if st.button("Verify"):
    st.write("The above details are correct and Verified")

if st.button("Submit"):
    with st.spinner("Submission Completing"):
        time.sleep(2)
        st.write("Your Response has been Submited")