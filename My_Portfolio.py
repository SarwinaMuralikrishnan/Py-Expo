import streamlit as st
import time

st.write("# MY_PORTFOLIO")

name = st.text_input("Name :")
st.write(name)

dob = st.text_input("Date of Birth :")
st.write(dob)

rll_no = st.text_input("Roll Number :")
st.write(rll_no)

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

phone = st.text_input("Mobile :")
st.write(phone)

marks = st.text_input("Marks Secured in 12th :")
st.write(marks)

marks1 = st.text_input("Marks Seured in 10th :")
st.write(marks1)

hobbies = st.text_input("Hobbies")
st.write(hobbies)

skills = st.text_input("Skills")
st.write(skills)

if st.button("Submit"):
    with st.spinner("Submission Completing"):
        time.sleep(2)
        st.write("Your Response has been Submited")