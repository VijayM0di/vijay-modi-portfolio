import streamlit as st

# 1. PAGE SETUP
st.set_page_config(page_title="Vijay Modi | Senior AI Architect", page_icon="⚡", layout="wide")

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
    
    .comp-box {
        background: #161b22;
        border: 1px solid #30363d;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    .comp-title { color: #58a6ff; font-weight: bold; font-size: 0.9rem; margin-bottom: 5px; }
    .comp-desc { color: #8b949e; font-size: 0.8rem; }

    .success-text { color: #3fb950; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: FULL SPECTRUM COMPETENCIES ---
with st.sidebar:
    st.markdown("## ⚡ Core Competencies")
    
    competencies = {
        "👁️ Video": "Action Understanding & Industrial CV",
        "🔊 Audio": "Real-time Voice AI & Low-Latency RAG",
        "📝 Text": "Worldwide RAG & Agentic Workflows",
        "📈 Time-Series": "Predictive Pharma Sales Forecasting",
        "🧠 Prompting": "Advanced Prompt Eng (OpenAI Standards)",
        "🚀 Deployment": "Worldwide Product Releases"
    }
    
    for title, desc in competencies.items():
        st.markdown(f"""
        <div class='comp-box'>
            <div class='comp-title'>{title}</div>
            <div class='comp-desc'>{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")
    st.markdown("### 🛠️ Contact")
    st.write("📧 vijaymodi2002@gmail.com")
    st.markdown("[🔗 LinkedIn](https://linkedin.com/in/vijaymodi174)")
    st.markdown("[🐙 GitHub](https://github.com/VijayM0di)")

# --- HEADER ---
st.title("VIJAY MODI")
st.subheader("Senior AI Architect | Full-Spectrum Intelligence Systems")

# --- MARQUEE CLIENTS ---
st.write("---")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Enterprise Client", "OpenAI")
m2.metric("Enterprise Client", "DP World")
m3.metric("Research Partner", "ISRO")
m4.metric("Corporate Partner", "Tata Group")
st.write("---")

# --- SECTION 1: DRYTIS (CURRENT) ---
st.header("💼 Current Engagement: Drytis")
with st.container():
    col1, col2 = st.columns([4, 1])
    col1.markdown("### Senior AI Engineer | **Portfolio Pipeline Lead**")
    col2.write("Feb 2026 – Present")
    
    st.write("Orchestrating end-to-end **AI/ML Pipelines** for high-growth enterprise stakeholders.")
    st.markdown("""
    - Designing automated workflows for model fine-tuning, data-ingestion, and distributed inference.
    - Implementing architectural standards for production-ready Generative AI across client tech-stacks.
    """)
    st.markdown("<span class='tag'>MLOps</span> <span class='tag'>Pipeline Orchestration</span> <span class='tag'>Scale Architecture</span>", unsafe_allow_html=True)

st.write("---")

# --- SECTION 2: CODISTE (DIALORA) ---
st.header("💼 Enterprise Engineering: Codiste")
with st.container():
    col1, col2 = st.columns([4, 1])
    col1.markdown("### Dialora | **Worldwide Product Feature Release**")
    col2.write("Nov 2025 – Jan 2026")
    
    st.write("**Product: Global Voice AI Platform**")
    st.markdown("""
    - **Global Impact:** Engineered and released the **Worldwide RAG** module, a flagship feature serving a global user base.
    - **Audio Precision:** Optimized the voice-RAG pipeline to hit sub-0.6s latency, establishing a worldwide industry benchmark for low-latency conversational AI.
    """)
    st.markdown("<span class='tag'>Worldwide RAG</span> <span class='tag'>Voice AI</span> <span class='tag'>Low-Latency Audio</span>", unsafe_allow_html=True)

st.write("---")

# --- SECTION 3: QUANTUM BOT (STAKEHOLDER SUITE) ---
st.header("💼 Enterprise Engineering: Quantum Bot")
with st.container():
    col1, col2 = st.columns([4, 1])
    col1.markdown("### AI Product Architect | **5 Live Enterprise Products**")
    col2.write("Jun 2024 – Oct 2025")
    
    # 1. OPENAI PROJECT
    st.info("**🌐 OPENAI: MULTIMODAL VIDEO REASONING**")
    st.markdown("""
    - **Multimodal Synthesis:** Architected a pipeline to process raw video and extract high-reasoning frames.
    - **Advanced Prompt Logic:** Developed four-dimensional synthesis (**Intent, Action, Reason, Result**) for training Large Multimodal Models (LMMs).
    """)

    # 2. DP WORLD PROJECT
    st.info("**🏗️ DP WORLD: INDUSTRIAL CCTV SUITE**")
    st.markdown("""
    - **Computer Vision:** Architected the real-time safety monitor for **DP World** ports.
    - **Performance:** Optimized processing throughput from **5 to 25 FPS** via Cython and GPU acceleration.
    """)

    # 3. GOLBOT PROJECT
    st.info("**📈 GOLBOT: PREDICTIVE FORECASTING**")
    st.markdown("""
    - **Time-Series Analysis:** Developed predictive analytics for pharmaceutical sales/demand forecasting.
    - **Impact:** Improved accuracy by **20%** and reduced manual analysis time by **60%** for business stakeholders.
    """)

    # 4. QBBOT PROJECT
    st.info("**📊 QBBOT: GENBI PLATFORM**")
    st.markdown("""
    - **Generative BI:** Full-stack development of a live "Chat-with-Data" platform utilizing custom Text-to-SQL engines.
    """)

    st.markdown("<p class='success-text'>✓ Delivered 5 Successive Global Stakeholder Launches</p>", unsafe_allow_html=True)

st.write("---")

# --- SECTION 4: RESEARCH ---
st.header("🔬 Academic Research")
with st.container():
    st.markdown("### **ISRO | Research Intern**")
    st.write("Jan 2024 – Jul 2024")
    st.write("Developed computational origami-based structures for deployable Mars habitats, adhering to rigorous industry mechanical standards.")

st.write("---")
st.markdown("<center style='color:#8b949e; font-size:0.8rem;'>VIJAY MODI | SENIOR AI ENGINEER | 2026</center>", unsafe_allow_html=True)
