import streamlit as st

# 1. PAGE SETUP
st.set_page_config(page_title="Vijay Modi | Senior AI Engineer", page_icon="🌐", layout="wide")

# 2. THEME & STYLING
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;700&display=swap');
    
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
        font-family: 'JetBrains Mono', monospace;
    }
    .name-header {
        font-size: 3.2rem;
        font-weight: 700;
        color: #58a6ff;
        margin-bottom: 0px;
    }
    .card {
        background-color: #161b22;
        padding: 25px;
        border-radius: 12px;
        border: 1px solid #30363d;
        margin-bottom: 20px;
    }
    .card-title { color: #58a6ff; font-size: 1.5rem; font-weight: 700; }
    .card-subtitle { color: #8b949e; font-size: 0.9rem; margin-bottom: 12px; }
    
    .badge-green { background-color: #238636; color: white; padding: 4px 10px; border-radius: 15px; font-size: 0.7rem; font-weight: bold; }
    .badge-purple { background-color: #8957e5; color: white; padding: 4px 10px; border-radius: 15px; font-size: 0.7rem; font-weight: bold; }
    
    .sub-project {
        background: #0d1117; 
        padding: 15px; 
        border-radius: 8px; 
        border: 1px solid #30363d; 
        margin-top: 10px;
    }
    .impact-highlight {
        color: #3fb950;
        font-weight: bold;
        border-left: 3px solid #3fb950;
        padding-left: 10px;
        margin-top: 10px;
    }
    .tag {
        display: inline-block;
        background: #21262d;
        border: 1px solid #30363d;
        color: #c9d1d9;
        padding: 3px 8px;
        border-radius: 5px;
        margin: 3px;
        font-size: 0.8rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    st.markdown("### ⚡ Profile")
    st.write("📍 Ahmedabad, India")
    st.markdown("[🐙 GitHub](https://github.com/VijayM0di)")
    st.markdown("[🔗 LinkedIn](https://linkedin.com/in/vijaymodi174)")
    st.write("---")
    st.write("**Expertise:**")
    st.caption("Prompt Engineering (OpenAI)")
    st.caption("Industrial Computer Vision (DP World)")
    st.caption("Audio RAG Architecture")

# 4. HEADER & CLIENTS
st.markdown("<h1 class='name-header'>VIJAY MODI</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size:1.2rem; color:#8b949e;'>Senior AI Engineer | Scalable Intelligence & Architecture</p>", unsafe_allow_html=True)

st.write("---")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Client", "OpenAI")
c2.metric("Client", "DP World")
c3.metric("Partner", "ISRO")
c4.metric("Partner", "Tata Group")
st.write("---")

# 5. EXPERIENCE SECTION
st.header("💼 Enterprise Engineering")

# --- DRYTIS (OpenAI) ---
st.markdown("""
<div class='card'>
    <div style='display: flex; justify-content: space-between;'>
        <span class='card-title'>Drytis | Senior AI Engineer</span>
        <span class='badge-green'>ACTIVE PIPELINE LEAD</span>
    </div>
    <div class='card-subtitle'>Feb 2026 – Present</div>
    <p>Managing AI/ML pipelines for global enterprise clients.</p>
    <ul>
        <li><b>OpenAI Engagement:</b> Leading Prompt Engineering and model optimization for high-scale apps.</li>
        <li>Architecting automated pipelines for multi-modal data processing and inference.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# --- CODISTE (DIALORA) ---
st.markdown("""
<div class='card'>
    <div style='display: flex; justify-content: space-between;'>
        <span class='card-title'>Dialora | Lead AI Engineer</span>
        <span class='badge-purple'>WORLDWIDE RELEASE</span>
    </div>
    <div class='card-subtitle'>Codiste | Nov 2025 – Jan 2026</div>
    <p><b>Voice AI Platform</b></p>
    <ul>
        <li><b>Worldwide Feature Release:</b> Engineered the Global RAG module for worldwide deployment.</li>
        <li>Optimized voice latency to sub-0.6s, achieving a global industry benchmark.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# --- QUANTUM BOT (DP WORLD & QBBOT) ---
st.markdown("""
<div class='card'>
    <div style='display: flex; justify-content: space-between;'>
        <span class='card-title'>Quantum Bot | AI Product Architect</span>
        <span class='badge-green'>5 LIVE PRODUCTS</span>
    </div>
    <div class='card-subtitle'>Jun 2024 – Oct 2025</div>
    <p>Led end-to-end architecture for a suite of 5 stakeholder-facing live products.</p>
    
    <div class='sub-project'>
        <p style='color: #58a6ff; font-weight: bold; margin-bottom:5px;'>🏗️ DP World: CCTV AI Suite</p>
        <p style='font-size:0.9rem; margin:0;'>Architected real-time safety monitoring for <b>DP World</b> ports. Optimized CV throughput from 5 to 25 FPS using Cython modules for safety kit detection.</p>
    </div>

    <div class='sub-project'>
        <p style='color: #58a6ff; font-weight: bold; margin-bottom:5px;'>📊 Qbbot: GenBI Platform</p>
        <p style='font-size:0.9rem; margin:0;'>Full-stack development of a live <b>Generative BI platform</b>. Built custom Text-to-SQL engines for executive data interrogation.</p>
    </div>

    <div class='impact-highlight'>Impact: 100% successful deployment across 5 distinct business sectors.</div>
</div>
""", unsafe_allow_html=True)

# --- RESEARCH ---
st.header("🔬 Research")
st.markdown("""
<div class='card'>
    <span class='card-title' style='font-size:1.2rem;'>ISRO | Research Intern</span>
    <div class='card-subtitle'>Jan 2024 – Jul 2024</div>
    <p>Developed computational origami structures for deployable Mars habitats.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><center style='color:#8b949e; font-size:0.8rem;'>VIJAY MODI | SENIOR AI ENGINEER | 2026</center>", unsafe_allow_html=True)
