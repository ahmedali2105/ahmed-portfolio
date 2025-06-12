import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Syed Ahmed Ali Portfolio", layout="wide")

# CSS Styles
st.markdown("""
<style>
body {
    background-color: #f0f2f6;
    color: #222222;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
h1 {
    color: #4a90e2;
    font-weight: 700;
    font-size: 3.5rem;
    text-align: center;
    margin-bottom: 0;
}
h3 {
    color: #333333;
    margin-top: 10px;
}
.subtitle {
    color: #777777;
    font-size: 1.5rem;
    text-align: center;
    margin-bottom: 40px;
}
.project {
    background: white;
    border-radius: 10px;
    padding: 25px;
    margin-bottom: 25px;
    box-shadow: 0 5px 10px rgba(74, 144, 226, 0.2);
}
a {
    color: #4a90e2;
    font-weight: 600;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
.skills {
    margin-bottom: 40px;
}
.icon {
    font-size: 22px;
    margin-right: 8px;
    color: #4a90e2;
}
.contact-links a {
    margin-right: 20px;
    font-weight: 600;
    color: #4a90e2;
    text-decoration: none;
}
.contact-links a:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# Title and Subtitle
st.markdown("<h1>Syed Ahmed Ali</h1>", unsafe_allow_html=True)
st.markdown('<div class="subtitle">Aspiring AI / ML Engineer</div>', unsafe_allow_html=True)

# Profile Picture and Intro
col1, col2 = st.columns([1,3])

with col1:
    github_username = "ahmedali2105"
    url = f"https://github.com/{github_username}.png?size=200"
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    st.image(img, width=180, caption="GitHub Profile Picture")

with col2:
    st.write("""
    Hello! I'm Syed Ahmed Ali, an aspiring AI and Machine Learning engineer passionate about solving real-world problems using Python, Data Science, and Machine Learning techniques.
    
    I build interactive dashboards and predictive models that provide actionable insights.
    
    Explore my projects below or get in touch!
    """)

# Skills with Icons (using emojis for simplicity)
st.markdown('<h3>🛠 Skills & Tools</h3>', unsafe_allow_html=True)
st.markdown("""
<ul>
<li>🐍 Python & Bash/Shell</li>
<li>📊 Pandas, NumPy, Matplotlib, Seaborn, Plotly</li>
<li>🤖 Scikit-learn (Machine Learning)</li>
<li>🛠 Git & GitHub, Streamlit, VS Code</li>
</ul>
""", unsafe_allow_html=True)

st.markdown("---")

# Projects Section
st.markdown('<h3>📂 Projects</h3>', unsafe_allow_html=True)

projects = [
    {
        "name": "SpaceX Launch Analysis & Prediction Platform",
        "link": "https://github.com/ahmedali2105/SpaceX-Launch-Analysis-Prediction-Platform",
        "desc": "An advanced Python application that visualizes SpaceX launch data and predicts future launches using machine learning."
    },
    {
        "name": "OOP Banking System",
        "link": "https://github.com/ahmedali2105/OOP-Banking-System",
        "desc": "Console-based banking application simulating real-world banking operations using core OOP concepts."
    }
]

for proj in projects:
    st.markdown(f"""
    <div class="project">
    <h4><a href="{proj['link']}" target="_blank">{proj['name']}</a></h4>
    <p>{proj['desc']}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Contact Info with icons
st.markdown('<h3>📬 Contact Me</h3>', unsafe_allow_html=True)
st.markdown("""
<div class="contact-links">
<a href="mailto:aleahmed21005@gmail.com" target="_blank">📧 Email</a>
<a href="https://www.linkedin.com/in/syed-ahmed-ali-/" target="_blank">🔗 LinkedIn</a>
<a href="https://github.com/ahmedali2105" target="_blank">🐱 GitHub</a>
</div>
""", unsafe_allow_html=True)
