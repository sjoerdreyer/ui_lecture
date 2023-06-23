import streamlit as st

st.set_page_config(page_title="WagonPage", page_icon='📸')

if st.button('click ;)'):
    st.image('raw_data/wagon.jpeg')
