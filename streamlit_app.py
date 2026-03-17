import streamlit as st

# 1. PAGE SETUP
st.set_page_config(page_title="Vijay Modi | Senior AI Engineer", page_icon="⚡", layout="wide")

# 2. THEME & STYLING
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;700&display=swap');
    
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
        font-family: 'JetBrains Mono', monospace;
    }
    
    h1, h2, h3 { color: #58a6ff !important; font-family: 'JetBrains Mono', monospace; }
    p, li { color: #c9d1d9 !important; font-size: 1rem; }
    
    [data-testid="stMetricValue"] { color: #58a6ff !important; font-size: 1.5rem !important; }
    [data-testid="stMetricLabel"] { color: #8b949e !important; }

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
    
    .success-text { color: #3fb950; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("## ⚡ Profile")
    st.write("Senior AI Engineer | Architecture & Intelligence")
    st.write("📧 vijaymodi2002@gmail.com")
    st.write("📱 +91 9033701984")
    st.markdown("[🔗 LinkedIn](https://linkedin.com/in/vijaymodi174)")
    st.markdown("[🐙 GitHub](https://github.com/VijayM0di)")
    st.write("---")
    st.write("**Core Competencies:**")
    st.caption("Multimodal Video Understanding")
    st.caption("Prompt Engineering (OpenAI)")
    st.caption("Worldwide Product Deployment")

# --- HEADER ---
st.title("VIJAY MODI")
st.subheader("Architecting Enterprise-Grade AI Pipelines & Multimodal Systems")

# --- CLIENTS BAR ---
st.write("---")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Key Client", "OpenAI")
m2.metric("Key Client", "DP World")
m3.metric("Research Partner", "ISRO")
m4.metric("Corporate Partner", "Tata Group")
st.write("---")

# --- SECTION 1: DRYTIS (CURRENT) ---
st.header("💼 Enterprise Engineering: Drytis")
with st.container():
    col1, col2 = st.columns([4, 1])
    col1.markdown("### Senior AI Engineer | **Multi-Client Pipeline Lead**")
    col2.write("Feb 2026 – Present")
    
    st.write("Leading the development of end-to-end **AI/ML Pipelines** for a diverse portfolio of enterprise clients.")
    st.markdown("""
    - Designing automated workflows for data ingestion, model fine-tuning, and production-scale inference.
    - Providing high-level architectural governance for client-side AI integration and infrastructure optimization.
    """)
    st.markdown("<span class='tag'>Pipeline Architecture</span> <span class='tag'>MLOps</span> <span class='tag'>Scalable Intelligence</span>", unsafe_allow_html=True)

st.write("---")

# --- SECTION 2: CODISTE (DIALORA) ---
st.header("💼 Enterprise Engineering: Codiste")
with st.container():
    col1, col2 = st.columns([4, 1])
    col1.markdown("### Dialora | **Worldwide Product Release**")
    col2.write("Nov 2025 – Jan 2026")
    
    st.write("**Role: Lead AI Engineer**")
    st.markdown("""
    - **Global Feature Launch:** Engineered and deployed the flagship **Worldwide RAG** module for the Dialora Voice AI Platform.
    - Successfully optimized voice-interaction latency to sub-0.6s, achieving a global industry benchmark for real-time low-latency response.
    """)
    st.markdown("<span class='tag'>Worldwide RAG</span> <span class='tag'>Voice AI</span> <span class='tag'>Deepgram</span>", unsafe_allow_html=True)

st.write("---")

# --- SECTION 3: QUANTUM BOT (QB) ---
st.header("💼 Enterprise Engineering: Quantum Bot")
with st.container():
    col1, col2 = st.columns([4, 1])
    col1.markdown("### AI Product Architect | **5 Live Stakeholder Products**")
    col2.write("Jun 2024 – Oct 2025")
    
    st.write("Orchestrated the development and deployment of **5 distinct enterprise products**, all successfully delivered and currently live.")

    # OPENAI PROJECT
    st.info("**🌐 OPENAI: MULTIMODAL VIDEO UNDERSTANDING**")
    st.markdown("""
    - **Multimodal Prompt Engineering:** Built a system to process raw video feeds and segment specific "Action Frames" for high-accuracy labeling.
    - **Structured Synthesis:** Developed advanced prompt logic to describe frames across four dimensions: **Intent, Action, Reason, and Result**.
    - Optimized the pipeline to translate visual cues into precise, structured metadata for training sophisticated action-recognition models.
    """)

    # DP WORLD PROJECT
    st.info("**🏗️ DP WORLD: CCTV AI SUITE**")
    st.markdown("""
    - Architected the real-time safety monitoring suite for **DP World** port infrastructure.
    - Optimized throughput from **5 FPS to 25 FPS** using Cython and GPU acceleration for industrial safety monitoring.
    """)

    # GENBI PROJECT
    st.info("**📊 QBBOT: GENBI PLATFORM**")
    st.markdown("""
    - Full-stack development of the live **Generative BI platform**.
    - Engineered custom Text-to-SQL engines to enable natural-language data interrogation for executive stakeholders.
    """)

    st.markdown("<p class='success-text'>✓ Delivered 5 Successive Enterprise Launches Across Manufacturing, Logistics, and SaaS</p>", unsafe_allow_html=True)
    st.markdown("<span class='tag'>Prompt Engineering</span> <span class='tag'>Video AI</span> <span class='tag'>DP World</span> <span class='tag'>OpenAI</span>", unsafe_allow_html=True)

st.write("---")

# --- SECTION 4: RESEARCH ---
st.header("🔬 Research & Education")
with st.container():
    st.markdown("### **ISRO | Research Intern**")
    st.write("Jan 2024 – Jul 2024")
    st.write("Applied computational origami engineering to design deployable Mars habitats, meeting rigorous industry structural standards.")
    
    st.markdown("### **NIRMA University**")
    st.caption("Bachelor of Technology (B.Tech) in Computer Science & Engineering | 2020 – 2024")

st.write("---")
st.markdown("<center style='color:#8b949e; font-size:0.8rem;'>VIJAY MODI | SENIOR AI ENGINEER | 2026</center>", unsafe_allow_html=True)
