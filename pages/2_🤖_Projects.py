import streamlit as st

st.set_page_config(page_title='Projects',
                   page_icon='🤖',
                   layout='wide')

st.title('Projects')

projects_html = '''
    <h3>🎭 Amazon Reviews Sentiment Analysis</h3>
    <p>I used Amazon's product review data from Kaggle to construct a machine learning model that gives a rating over the reviews written by the user, you could test the model yourself on <a href="https://sentimentzaid.streamlit.app">this link!</a></p>
    <ul>Tools used:
        <li>Pandas</li>
        <li>NLTK</li>
        <li>Sci-Kit Learn</li>
    </ul>
    <h3>👾 Data Science Chatbot</h3>
    <p>This chatbot was a part of a Hackathon held by <a href="https://lablab.me">lablab.me</a>. The chatbot was built to answer your questions related to data science or the data field in general, you can ask the chatbot yourself <a href="https://datachatbot.streamlit.app">here!</a></p>
    <ul>Tools used:
        <li>TensorFlow</li>
        <li>NLTK</li>
    </ul>
    <h3>🚕 Batch ETL Pipeline on NYC Taxi Data</h3>
    <p>Built an ETL pipeline that automatically downloads parquet files from NYC's Taxi and Limousine Commission <a href="https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page">website</a> every month and then transformed the data by making it suitable to be stored in a PostgreSQL database finally storing it in said database, you can check the <a href="https://github.com/ZaidHani/nyc_taxis">GitHub repo</a> for more info.</p>
    <ul>Tools used:
        <li>Polars</li>
        <li>PostgreSQL</li>
        <li>Apache Airflow</li>
        <li>Power BI</li>
    </ul>
'''

st.markdown(projects_html, unsafe_allow_html=True)
