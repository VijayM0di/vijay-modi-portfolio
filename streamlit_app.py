import streamlit as st

# 1. PAGE SETUP
st.set_page_config(page_title="Vijay Modi | Senior AI Engineer", page_icon="🌐", layout="wide")

# 2. THEME & STYLING
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;700&display=swap');
    
    /* Force Dark Theme */
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
        font-family: 'JetBrains Mono', monospace;
    }
    
    /* Professional Typography */
    h1, h2, h3 { color: #58a6ff !important; font-family: 'JetBrains Mono', monospace; }
    p, li { color: #c9d1d9 !important; font-size: 1rem; }
    
    /* Metrics / Clients Bar */
    [data-testid="stMetricValue"] { color: #58a6ff !important; font-size: 1.5rem !important; }
    [data-testid="stMetricLabel"] { color: #8b949e !important; }

    /* Custom Tags */
    .tag {
        display: inline-block;
        background: #21262d;
        border: 1px solid #30363d;
        color: #c9d1d9;
        padding: 4px 12px;
        border-radius: 6px;
        margin-right: 8px;
        margin-bottom: 8px;
        font-size: 0.85rem;
    }
    
    /* Success highlight */
    .success-text { color: #3fb950; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("## ⚡ Profile")
    st.write("Senior AI Engineer specializing in high-scale enterprise architecture.")
    st.write("📧 vijaymodi2002@gmail.com")
    st.write("📱 +91 9033701984")
    st.markdown("[🔗 LinkedIn](https://linkedin.com/in/vijaymodi174)")
    st.markdown("[🐙 GitHub](https://github.com/VijayM0di)")
    st.write("---")
    st.write("**Core Stack:**")
    st.caption("OpenAI | Prompt Engineering")
    st.caption("DP World | Computer Vision")
    st.caption("Dialora | Worldwide RAG")

# --- HEADER ---
st.title("VIJAY MODI")
st.subheader("Architecting Global Intelligence & Scalable AI Pipelines")

# --- CLIENTS BAR ---
st.write("---")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Client", "OpenAI")
m2.metric("Client", "DP World")
m3.metric("Partner", "ISRO")
m4.metric("Partner", "Tata Group")
st.write("---")

# --- SECTION 1: DRYTIS (OpenAI) ---
st.header("💼 Enterprise Engineering: Drytis")
with st.container():
    col1, col2 = st.columns([4, 1])
    col1.markdown("### Senior AI Engineer | **Lead Pipeline Architect**")
    col2.write("Feb 2026 – Present")
    
    st.write("Currently managing high-concurrency **AI/ML Pipelines** for a diverse portfolio of enterprise clients.")
    st.write("**Key Focus: OpenAI Engagement**")
    st.markdown("""
    - Leading **Prompt Engineering** and LLM optimization for Tier-1 applications.
    - Architecting end-to-end multi-modal data pipelines for real-time inference.
    """)
    st.markdown("<span class='tag'>GPT-4o</span> <span class='tag'>Prompt Engineering</span> <span class='tag'>System Design</span>", unsafe_allow_html=True)

st.write("---")

# --- SECTION 2: CODISTE (Dialora) ---
st.header("💼 Enterprise Engineering: Codiste")
with st.container():
    col1, col2 = st.columns([4, 1])
    col1.markdown("### Dialora | **Worldwide Product Release**")
    col2.write("Nov 2025 – Jan 2026")
    
    st.write("**Role: Lead AI Engineer**")
    st.markdown("""
    - **Global Feature Launch:** Engineered and deployed the flagship **Worldwide RAG** module for the Dialora Voice AI Platform.
    - Achieved a sub-0.6s latency benchmark for voice-interaction RAG, serving a global user base.
    """)
    st.markdown("<span class='tag'>Worldwide RAG</span> <span class='tag'>Voice AI</span> <span class='tag'>Global Scale</span>", unsafe_allow_html=True)

st.write("---")

# --- SECTION 3: QUANTUM BOT (QB) ---
st.header("💼 Enterprise Engineering: Quantum Bot")
with st.container():
    col1, col2 = st.columns([4, 1])
    col1.markdown("### AI Product Architect | **5 Live Products**")
    col2.write("Jun 2024 – Oct 2025")
    
    st.write("Led the end-to-end architecture for **5 stakeholder-facing products**, all successfully deployed and live.")

    # Industrial Project
    st.info("**🏗️ DP WORLD: CCTV AI SUITE**")
    st.markdown("""
    - Architected real-time safety monitoring for **DP World** industrial port infrastructure.
    - Optimized processing from **5 FPS to 25 FPS** using Cython and GPU acceleration.
    """)

    # GenBI Project
    st.info("**📊 QBBOT: GENBI PLATFORM**")
    st.markdown("""
    - Full-stack development of the live **Generative BI platform**.
    - Engineered custom Text-to-SQL engines for automated enterprise data analytics.
    """)

    st.markdown("<p class='success-text'>✓ 100% Successful Deployment Rate Across 5 Distinct Sectors</p>", unsafe_allow_html=True)
    st.markdown("<span class='tag'>Industrial CV</span> <span class='tag'>GenBI</span> <span class='tag'>Cython Ops</span> <span class='tag'>Stakeholder Management</span>", unsafe_allow_html=True)

st.write("---")

# --- SECTION 4: RESEARCH ---
st.header("🔬 Academic Research")
with st.container():
    st.markdown("### **ISRO | Research Intern**")
    st.write("Jan 2024 – Jul 2024")
    st.write("Computational design for deployable Mars habitats utilizing origami-based mechanical engineering.")

st.write("---")
st.markdown("<center style='color:#8b949e; font-size:0.8rem;'>VIJAY MODI | SENIOR AI ENGINEER | 2026</center>", unsafe_allow_html=True)
