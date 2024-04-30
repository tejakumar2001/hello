import streamlit as st


def main():
    st.title("Resume Builder")

    # Get user input for personal information
    st.header("Personal Information")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")

    st.header("Education")
    education = st.text_input("Education")
    st.header("Work Experience")
    work_experience = st.text_area("Work Experience")

    st.header("Skills")
    skills = st.text_area("Skills")

    if st.button("Generate Resume"):
        st.write("### Resume")
        st.write(f"**Name:** {name}")
        st.write(f"**Email:** {email}")
        st.write(f"**Phone:** {phone}")
        st.write(f"**Education:** {education}")
        st.write(f"**Work Experience:** {work_experience}")
        st.write(f"**Skills:** {skills}")


if __name__ == "__main__":
    main()
