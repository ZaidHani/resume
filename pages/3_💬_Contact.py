import streamlit as st

st.set_page_config(page_title='Contact',
                   page_icon='💬',
                   layout='wide')

st.title('Contact Me!')

contact_paragraph = '<h3>You can reach me on:<h3>'
st.markdown(contact_paragraph, unsafe_allow_html=True)

contacts = '<h6><a href="https://www.linkedin.com/in/zaid-allwansah/">LinkedIn</a></h6><h6><a href="https://github.com/ZaidHani">GitHub</a></h6>'

st.markdown(contacts, unsafe_allow_html=True)
st.markdown('or contact me directly on my email: allwazaid1@gmail.com')

