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
    st.markdown("### 🧠 Expertise")
    st.caption("Prompt Engineering")
    st.caption("Computer Vision")
    st.caption("Audio AI / RAG")
    st.caption("MLOps")

# --- TOP HEADER ---
st.markdown("<h1 class='name-header'>VIJAY MODI</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size:1.2rem; color:#8b949e;'>Senior AI Engineer | Scalable Intelligence & Architecture</p>", unsafe_allow_html=True)

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
st.header("⚡ Enterprise Experience")

# 1. OpenAI Engagement
st.markdown("""
    <div class='card'>
        <div class='card-title'>OpenAI | Prompt Engineering Specialist</div>
        <div class='card-subtitle'>via Drytis | Feb 2026 – Present</div>
        <ul>
            <li>Leading <b>Prompt Engineering</b> initiatives and LLM optimization for high-performance AI applications.</li>
            <li>Designing complex system-level prompts and multi-agent interaction protocols.</li>
            <li>Providing technical leadership and architectural support for OpenAI-integrated stacks.</li>
        </ul>
        <span class='tag'>GPT-4o</span> <span class='tag'>Prompt Engineering</span> <span class='tag'>LLM Ops</span> <span class='tag'>System Design</span>
    </div>
    """, unsafe_allow_html=True)

# 2. DP World Engagement
st.markdown("""
    <div class='card'>
        <div class='card-title'>DP World | Computer Vision Lead</div>
        <div class='card-subtitle'>CCTV AI Suite (Quantum Bot) | Jun 2024 – Oct 2025</div>
        <ul>
            <li>Architected the real-time safety monitoring suite for <b>DP World</b> industrial ports.</li>
            <li>Developed <b>Cython-optimized</b> modules, increasing CV throughput from 5 to 25 FPS for industrial-grade safety monitoring.</li>
            <li>Deployed multi-zone vehicle tracking and PPE detection using GPU-accelerated YOLO v10.</li>
        </ul>
        <span class='impact-text'>Result: 40% reduction in incident response time for stakeholders.</span><br><br>
        <span class='tag'>YOLO v10</span> <span class='tag'>Cython</span> <span class='tag'>CUDA</span> <span class='tag'>Industrial CV</span>
    </div>
    """, unsafe_allow_html=True)

# 3. Qbbot (In-house Live)
st.markdown("""
    <div class='card'>
        <div class='card-title'>Qbbot <span class='live-badge'>LIVE PRODUCT</span></div>
        <div class='card-subtitle'>GenBI AI Agent Platform | In-House Engineering</div>
        <ul>
            <li>Engineered a production-ready <b>GenBI platform</b> for "Chat-with-Data" analytics.</li>
            <li>Built custom text-to-SQL engines and integrated multi-LLM support (OpenAI, Gemini, Bedrock).</li>
            <li>Architected modular RAG pipelines for semantic indexing and explainable analytics.</li>
        </ul>
        <span class='impact-text'>Impact: 60% reduction in manual BI reporting workload.</span><br><br>
        <span class='tag'>LangChain</span> <span class='tag'>Vector DBs</span> <span class='tag'>RAG</span> <span class='tag'>SQL-LLM</span>
    </div>
    """, unsafe_allow_html=True)

# 4. Dialora (Audio AI)
st.markdown("""
    <div class='card'>
        <div class='card-title'>Dialora | Lead AI Engineer</div>
        <div class='card-subtitle'>Voice Agent platform (Codiste) | Nov 2025 – Jan 2026</div>
        <ul>
            <li>Developed sub-0.6s latency <b>Audio RAG</b> pipelines for real-time voice conversations.</li>
            <li>Orchestrated n8n workflows for agent state management and automated CRM triggers.</li>
        </ul>
        <span class='tag'>Audio AI</span> <span class='tag'>Deepgram</span> <span class='tag'>Low-Latency RAG</span> <span class='tag'>n8n</span>
    </div>
    """, unsafe_allow_html=True)

# --- RESEARCH SECTION ---
st.header("🔬 Research Foundation")
st.markdown("""
    <div class='card'>
        <div class='card-title' style='font-size:1.1rem;'>ISRO | Research Intern</div>
        <p style='font-size:0.9rem; color:#8b949e;'>Computational Design & Mars Habitat Engineering (Jan 2024 – Jul 2024)</p>
        <p style='font-size:0.85rem;'>Developed software for deployable Mars habitats using origami-based engineering and 3D modeling to industry standards.</p>
    </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><hr><center style='color:#8b949e; font-size:0.8rem;'>VIJAY MODI | SENIOR AI ENGINEER | AHMEDABAD, INDIA | 2026</center>", unsafe_allow_html=True)
