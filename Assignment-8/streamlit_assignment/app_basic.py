import streamlit as st
class Introduction:
    def intro():
        st.title("Welcome to Streamlit! ")
        name=st.text_input("Enter your name: ")
        if st.button("Greet Me"):
            st.write(f"Hello!, {name}")

if __name__ == "__main__":
    Introduction.intro()
