import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vijay Modi | Senior AI Engineer", page_icon="🌐", layout="wide")

# --- HIGH-CONTRAST DARK THEME CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;700&display=swap');
    
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
        font-family: 'JetBrains Mono', monospace;
    }

    .name-header {
        font-size: 3.5rem;
        font-weight: 700;
        color: #58a6ff;
        margin-bottom: 0px;
        letter-spacing: -1px;
    }
    
    .client-bar {
        background-color: #161b22;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #30363d;
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        margin-bottom: 40px;
    }

    .card {
        background-color: #161b22;
        padding: 30px;
        border-radius: 12px;
        border: 1px solid #30363d;
        margin-bottom: 25px;
    }

    .card-title { color: #58a6ff; font-size: 1.6rem; font-weight: 700; }
    .card-subtitle { color: #8b949e; font-size: 0.95rem; margin-bottom: 15px; }
    
    .live-badge {
        background-color: #238636;
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: bold;
        text-transform: uppercase;
    }
    
    .world-badge {
        background-color: #8957e5;
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: bold;
        text-transform: uppercase;
    }

    .tag {
        display: inline-block;
        background: #21262d;
        border: 1px solid #30363d;
        color: #c9d1d9;
        padding: 4px 12px;
        border-radius: 6px;
        margin: 4px;
        font-size: 0.85rem;
    }
    
    .impact-highlight {
        color: #3fb950;
        border-left: 3px solid #3fb950;
        padding-left: 10px;
        margin-top: 15px;
        font-weight: 600;
    }

    .sub-card {
        background: #0d1117; 
        padding: 15px; 
        border-radius: 8px; 
        border: 1px solid #30363d; 
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("## ⚡ Profile")
    st.write("📍 Ahmedabad, India")
    st.markdown("[🐙 GitHub](https://github.com/VijayM0di)")
    st.markdown("[🔗 LinkedIn](https://linkedin.com/in/vijaymodi174)")
    st.write("---")
    st.markdown("### 🏆 Core Expertise")
    st.caption("AI/ML Pipeline Architecture")
    st.caption("Worldwide Product Deployment")
    st.caption("Prompt Engineering (OpenAI)")
    st.caption("Industrial Computer Vision")

# --- HEADER ---
st.markdown("<h1 class='name-header'>VIJAY MODI</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size:1.4rem; color:#8b949e; margin-bottom:20px;'>Senior AI Engineer | Architecting Global Intelligence</p>", unsafe_allow_html=True)

# --- CLIENT MARQUEE ---
st.markdown("""
    <div class='client-bar'>
        <div style='text-align:center'><small style='color:#8b949e'>Client</small><br><b>OpenAI</b></div>
        <div style='text-align:center'><small style='color:#8b949e'>Client</small><br><b>DP World</b></div>
        <div style='text-align:center'><small style='color:#8b949e'>Partner</small><br><b>ISRO</b></div>
        <div style='text-align:center'><small style='color:#8b949e'>Partner</small><br><b>Tata Group</b></div>
    </div>
    """, unsafe_allow_html=True)

# --- EXPERIENCE SECTION ---
st.header("💼 Enterprise Engineering")

# 1. DRYTIS (OpenAI)
st.markdown("""
    <div class='card'>
        <div style='display: flex; justify-content: space-between; align-items: center;'>
            <span class='card-title'>Drytis | Senior AI Engineer</span>
            <span class='live-badge'>Pipeline Lead</span>
        </div>
        <div class='card-subtitle'>Feb 2026 – Present</div>
        <p>Architecting and managing <b>AI/ML Pipelines</b> for a diverse portfolio of enterprise clients.</p>
        <ul>
            <li><b>OpenAI Engagement:</b> Spearheading Prompt Engineering and LLM optimization for high-scale applications.</li>
            <li>Designing end-to-end automated pipelines for multi-modal data processing and inference.</li>
        </ul>
        <div class='tag'>AI/ML Pipelines</div> <span class='tag'>Prompt Engineering</span>
    </div>
    """, unsafe_allow_html=True)

# 2. CODISTE (Dialora)
st.markdown("""
    <div class='card'>
        <div style='display: flex; justify-content: space-between; align-items: center;'>
            <span class='card-title'>Dialora | Lead AI Engineer</span>
            <span class='world-badge'>Worldwide Product Release</span>
        </div>
        <div class='card-subtitle'>Codiste | Nov 2025 – Jan 2026</div>
        <p><b>Product: Dialora Voice AI Platform</b></p>
        <ul>
            <li><b>Feature Release:</b> Engineered and deployed the <b>Global RAG</b> module, a flagship feature serving users worldwide.</li>
            <li>Optimized voice-interaction latency to sub-0.6s, setting a worldwide industry benchmark.</li>
        </ul>
        <div class='tag'>Worldwide RAG</div> <span class='tag'>Voice AI</span>
    </div>
    """, unsafe_allow_html=True)

# 3. QUANTUM BOT (QB)
st.markdown("""
    <div class='card'>
        <div style='display: flex; justify-content: space-between; align-items: center;'>
            <span class='card-title'>Quantum Bot | AI Product Architect</span>
            <span class='live-badge'>5 LIVE ENTERPRISE PRODUCTS</span>
        </div>
        <div class='card-subtitle'>Jun 2024 – Oct 2025</div>
        <p>Led end-to-end architecture for a suite of <b>5 stakeholder-facing products</b> delivered across multiple sectors.</p>
        
        <div class='sub-card'>
            <p style='margin:0; color: #58a6ff; font-weight: bold;'>🏗️ Industrial Excellence: DP World CCTV AI Suite</p>
            <ul style='margin-top: 5px; font-size: 0.9rem;'>
                <li>Architected real-time safety monitoring for <b>DP World</b> port infrastructure.</li>
                <li>Increased CV throughput from <b>5 FPS to 25 FPS</b> using Cython-optimized modules.</li>
            </ul>
        </div>

        <div class='sub-card'>
            <p style='margin:0; color: #58a6ff; font-weight: bold;'>📊 Business Intelligence: Qbbot (GenBI Platform)</p>
            <ul style='margin-top: 5px; font-size: 0.9rem;'>
                <li>Full-stack development of a live <b>Generative BI platform</b> for enterprise analytics.</li>
                <li>Built custom Text-to-SQL engine and automated visualization pipeline.</li>
            </ul>
        </div>

        <div class='impact-highlight'>Result: 100% successful deployment rate across 5 distinct business sectors.</div>
        <br>
        <div class='tag'>DP World</div> <div class='tag'>GenBI</div> <div class='tag'>Cython</div>
    </div>
    """, unsafe_allow_html=True)

# 4. RESEARCH
st.header("🔬 Research")
st.markdown("""
    <div class='card'>
        <div class='card-title'>ISRO | Research Intern</div>
        <div class='card-subtitle'>Jan 2024 – Jul 2024</div>
        <p>Developed software for deployable Mars habitats using origami-based engineering and 3D modeling.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><hr><center style='color:#8b949e; font-size:0.8rem;'>VIJAY MODI | SENIOR AI ENGINEER | 2026</center>", unsafe_allow_html=True)
