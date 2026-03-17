import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vijay Modi | Senior AI Engineer", page_icon="⚡", layout="wide")

# --- CLEAN DARK THEME CSS ---
st.markdown("""
    <style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;700&display=swap');
    
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Header */
    .name-header {
        font-size: 3rem;
        font-weight: 700;
        color: #58a6ff;
        margin-bottom: 0px;
    }
    
    /* Client Bar */
    .client-bar {
        background-color: #161b22;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #30363d;
        display: flex;
        justify-content: space-around;
        align-items: center;
        margin-bottom: 30px;
    }
    .client-item {
        color: #8b949e;
        font-weight: 700;
        font-size: 1.1rem;
    }
    .client-highlight {
        color: #f0f6fc;
        border-bottom: 2px solid #58a6ff;
    }

    /* Experience Cards */
    .card {
        background-color: #161b22;
        padding: 25px;
        border-radius: 10px;
        border: 1px solid #30363d;
        margin-bottom: 20px;
    }
    .card:hover {
        border-color: #58a6ff;
    }
    .card-title {
        color: #58a6ff;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 5px;
    }
    .card-subtitle {
        color: #8b949e;
        font-size: 0.9rem;
        margin-bottom: 15px;
    }
    .live-badge {
        background-color: #238636;
        color: white;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.7rem;
        font-weight: bold;
        vertical-align: middle;
        margin-left: 10px;
    }
    .impact-text {
        color: #3fb950;
        font-weight: bold;
    }

    /* Skill Tags */
    .tag {
        display: inline-block;
        background: #21262d;
        border: 1px solid #30363d;
        color: #c9d1d9;
        padding: 3px 10px;
        border-radius: 5px;
        margin: 3px;
        font-size: 0.8rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 🛠️ Contact")
    st.write("📧 vijaymodi2002@gmail.com")
    st.write("📱 +91 9033701984")
    st.markdown("[🔗 LinkedIn](https://linkedin.com/in/vijaymodi174)")
    st.markdown("[🐙 GitHub](https://github.com/VijayM0di)")
    st.write("---")
    st.markdown("### 🧠 Core Stack")
    st.caption("GenAI | Prompt Eng | Computer Vision | Audio AI | RAG Architecture")

# --- TOP HEADER ---
st.markdown("<h1 class='name-header'>VIJAY MODI</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size:1.2rem; color:#8b949e;'>Senior AI Engineer | Expert in Production-Scale Intelligence</p>", unsafe_allow_html=True)

# --- CLIENT MARQUEE ---
st.markdown("""
    <div class='client-bar'>
        <span class='client-item'>Client: <span class='client-highlight'>OpenAI</span></span>
        <span class='client-item'>Client: <span class='client-highlight'>DP World</span></span>
        <span class='client-item'>Partner: <span class='client-highlight'>ISRO</span></span>
        <span class='client-item'>Partner: <span class='client-highlight'>Tata Group</span></span>
    </div>
    """, unsafe_allow_html=True)

# --- MAIN WORK FEED ---
st.header("⚡ Core Engagements & Live Products")

# 1. OpenAI Engagement
st.markdown("""
    <div class='card'>
        <div class='card-title'>OpenAI | Prompt Engineering Specialist</div>
        <div class='card-subtitle'>via Drytis | Feb 2025 – Present</div>
        <ul>
            <li>Executing advanced <b>Prompt Engineering</b> and LLM optimization for high-stakes AI applications.</li>
            <li>Architecting complex system prompts and multi-turn interaction models for production environments.</li>
            <li>Providing live architectural support for OpenAI-integrated tech stacks.</li>
        </ul>
        <span class='tag'>GPT-4</span> <span class='tag'>Prompt Engineering</span> <span class='tag'>LLM Ops</span> <span class='tag'>System Architecture</span>
    </div>
    """, unsafe_allow_html=True)

# 2. DP World Engagement
st.markdown("""
    <div class='card'>
        <div class='card-title'>DP World | Computer Vision Lead</div>
        <div class='card-subtitle'>CCTV AI Suite (Quantum Bot) | 2024 – 2026</div>
        <ul>
            <li>Architected a real-time safety monitoring suite for <b>DP World</b> industrial ports/warehouses.</li>
            <li>Engineered <b>Cython-accelerated</b> CV modules, jumping from 5 to 25 FPS for real-time safety kit detection.</li>
            <li>Implemented PPE detection and multi-zone vehicle tracking with GPU-optimized YOLO v10.</li>
        </ul>
        <span class='impact-text'>Result: 40% reduction in incident response time.</span><br><br>
        <span class='tag'>YOLO v10</span> <span class='tag'>Cython</span> <span class='tag'>CUDA</span> <span class='tag'>Industrial CV</span>
    </div>
    """, unsafe_allow_html=True)

# 3. Qbbot (In-house Live)
st.markdown("""
    <div class='card'>
        <div class='card-title'>Qbbot <span class='live-badge'>LIVE</span></div>
        <div class='card-subtitle'>GenBI AI Agent Platform | In-House Project</div>
        <ul>
            <li>Developed an end-to-end <b>GenBI platform</b> enabling natural language "Chat-with-Data."</li>
            <li>Built custom text-to-SQL engines and automated BI report generation.</li>
            <li>Integrated multiple LLMs (OpenAI, Gemini, Bedrock) with a modular RAG architecture.</li>
        </ul>
        <span class='impact-text'>Impact: 60% reduction in manual BI reporting workload.</span><br><br>
        <span class='tag'>LangChain</span> <span class='tag'>SQL-LLM</span> <span class='tag'>RAG</span> <span class='tag'>Full-Stack AI</span>
    </div>
    """, unsafe_allow_html=True)

# 4. Dialora (Audio AI)
st.markdown("""
    <div class='card'>
        <div class='card-title'>Dialora | Lead AI Engineer</div>
        <div class='card-subtitle'>Voice Agent Platform | 2025</div>
        <ul>
            <li>Optimized <b>Audio RAG</b> pipelines to achieve sub-0.6s latency for voice conversations.</li>
            <li>Integrated <b>Deepgram</b> for high-accuracy STT and managed real-time agent state via n8n.</li>
        </ul>
        <span class='tag'>Audio AI</span> <span class='tag'>Deepgram</span> <span class='tag'>Low Latency RAG</span> <span class='tag'>n8n</span>
    </div>
    """, unsafe_allow_html=True)

# --- OPEN SOURCE & EXTRAS ---
st.header("🌐 Open Source & Research")
c1, c2 = st.columns(2)

with c1:
    st.markdown("""
        <div class='card'>
            <div class='card-title' style='font-size:1.1rem;'>🍜 Ramen-Shop</div>
            <p style='font-size:0.8rem;'>High-concurrency full-stack architecture showcase.</p>
            <a href='https://github.com/enderh3art/Ramen-Shop' style='color:#58a6ff; font-size:0.8rem;'>View on GitHub →</a>
        </div>
        """, unsafe_allow_html=True)

with c2:
    st.markdown("""
        <div class='card'>
            <div class='card-title' style='font-size:1.1rem;'>🚀 ISRO Research</div>
            <p style='font-size:0.8rem;'>Mars Habitat Computational Design & Origami-based structures.</p>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><hr><center style='color:#8b949e; font-size:0.8rem;'>VIJAY MODI | SENIOR AI ENGINEER | AHMEDABAD, INDIA | 2026</center>", unsafe_allow_html=True)
