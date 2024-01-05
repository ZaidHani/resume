import streamlit as st

st.set_page_config(page_title='Home Page',
                   layout='wide',
                   page_icon='👋')

st.title('Home Page')

with open('Resume.pdf', 'rb') as file:
    st.download_button('PDF Resume', data=file, file_name='Zaid_resume.pdf')

about_me_html = '''
    <h3>😃 About Me</h3>
    <p>
    Hello, I’m Zaid and I am a AI and Data Science student. I am currently taking my Bachelor’s degree in Data Scince from Al-Balqaa Applied University.
    I’m passionate about working with huge datasets and making an effective use out of them.\n
    With a solid foundation in programming and statistics, I’m able to do data analysis tasks effectively to extract meaningful insights from data.\n
    As a data science enthusiast, I harness the power of machine learning algorithms and predictive modeling to explore the potential within datasets.
    My work is grounded in a commitment to ethical data practices, ensuring that the insights generated contribute positively to the broader landscape.
    </p>    
'''

tools_html = '''
    <h3>🛠 Tools and Skills</h3>

    <ul> Programming Langauges:
        <li>Python</li>
        <li>SQL</li>
        <li>Bash</li>
        <li>JavaScript</li>
        <li>Java</li>
    </ul>

    <ul> Skills:
        <li>Machine Learning</li>
        <li>Natural Language Processing</li>
        <li>ETL Pipelines</li>
        <li>Data Modeling</li>
        <li>Data Analysis</li>
        <li>Data Mining</li>
        <li>Data Visualization</li>
    </ul>

    <ul> Tools:
        <li>Linux Terminal</li>
        <li>Pandas</li>
        <li>Numpy</li>
        <li>NLTK</li>
        <li>Sci-Kit Learn</li>
        <li>TensorFlow</li>
        <li>Apache Airflow and Kafka</li>
        <li>Tableau</li>
        <li>Power BI</li>
    </ul>
'''

st.markdown(about_me_html, unsafe_allow_html=True)

st.markdown(tools_html, unsafe_allow_html=True)
