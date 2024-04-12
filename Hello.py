

import streamlit as st
import json


def run():
    st.set_page_config(
        page_title="Streamlit quizz app",
        page_icon="❓",
    )

if __name__ == "__main__":
    run()

def next_question():
    st.session_state.current_index += 1
st.session_state.current_index=1
st.button('Next', on_click=next_question)