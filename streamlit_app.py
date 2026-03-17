import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vijay Modi | Senior AI Engineer", page_icon="🚀", layout="wide")

# --- MODERN PROFESSIONAL CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main { background-color: #fcfcfc; }
    
    /* Hero Card */
    .hero-container {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 40px;
        border-radius: 20px;
        color: white;
        margin-bottom: 30px;
    }
    
    /* Metric Cards */
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .metric-value {
        font-size: 24px;
        font-weight: 700;
        color: #2563eb;
    }
    .metric-label {
        font-size: 14px;
        color: #6b7280;
        font-weight: 500;
    }

    /* Project/Work Cards */
    .work-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border-left: 6px solid #2563eb;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    .client-tag {
        background: #eff6ff;
        color: #1e40af;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .skill-pill {
        background: #f3f4f6;
        color: #374151;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 13px;
        margin: 2px;
        display: inline-block;
        border: 1px solid #e5e7eb;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("## 👨‍💻 Profile")
    st.info("Senior AI Architect specializing in high-concurrency GenAI and Real-time CV.")
    st.write("📍 Ahmedabad, India")
    st.write("📫 vijaymodi2002@gmail.com")
    st.markdown("[🔗 LinkedIn](https://linkedin.com/in/vijaymodi174)")
    st.markdown("[🐙 GitHub](https://github.com/VijayM0di)")
    st.write("---")
    st.write("### 🛠 Tech Radar")
    st.caption("GenAI: LangGraph, RAG, CrewAI")
    st.caption("CV: YOLO v10, CUDA, Cython")
    st.caption("Voice: Deepgram, vLLMs, n8n")
    st.caption("Ops: Azure, Docker, FastAPI")

# --- HERO SECTION ---
st.markdown("""
    <div class='hero-container'>
        <h1 style='margin:0;'>Vijay Modi</h1>
        <p style='font-size:20px; opacity:0.9;'>Senior AI & Machine Learning Engineer</p>
        <div style='margin-top:20px;'>
            <span style='margin-right:20px;'>🤝 <b>Clients:</b> OpenAI, DP World, ISRO, Tata Group</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- KEY PERFORMANCE INDICATORS ---
cols = st.columns(4)
with cols[0]:
    st.markdown("<div class='metric-card'><div class='metric-value'>0.3s</div><div class='metric-label'>RAG Latency</div></div>", unsafe_allow_html=True)
with cols[1]:
    st.markdown("<div class='metric-card'><div class='metric-value'>25 FPS</div><div class='metric-label'>Industrial CV Speed</div></div>", unsafe_allow_html=True)
with cols[2]:
    st.markdown("<div class='metric-card'><div class='metric-value'>70%</div><div class='metric-label'>Workload Reduction</div></div>", unsafe_allow_html=True)
with cols[3]:
    st.markdown("<div class='metric-card'><div class='metric-value'>50%</div><div class='metric-label'>Integration Speedup</div></div>", unsafe_allow_html=True)

st.write("---")

# --- PROFESSIONAL EXPERIENCE ---
st.header("💎 Enterprise Engagements")

# Engagement 1: OpenAI
st.markdown("""
    <div class='work-card'>
        <span class='client-tag'>Tier 1 Engagement</span>
        <h3>Drytis | AI Developer (Contract)</h3>
        <p style='color:#6b7280;'>Feb 2025 – Present</p>
        <p><b>Core Focus: OpenAI Ecosystem & High-Growth Startups</b></p>
        <ul>
            <li>Providing architectural leadership for <b>OpenAI-centric</b> software engineering solutions.</li>
            <li>Delivering production-ready AI features via "Vibe Coding" platform for global stakeholders.</li>
            <li>Optimizing full-stack deployment pipelines for LLM-based applications.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Engagement 2: DP World / Industrial
st.markdown("""
    <div class='work-card'>
        <span class='client-tag'>Global Logistics</span>
        <h3>DP World Portfolio | AI Architect</h3>
        <p style='color:#6b7280;'>Quantum Bot Engagement (2024 – 2026)</p>
        <p><b>Core Focus: Computer Vision & Logistics Infrastructure</b></p>
        <ul>
            <li>Architected a real-time computer vision suite for safety monitoring in <b>DP World</b> industrial environments.</li>
            <li>Implemented <b>Cython-optimized</b> modules, increasing processing throughput from 5 FPS to 25 FPS.</li>
            <li>Engineered multi-zone tracking and safety kit detection using GPU-accelerated YOLO frameworks.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Engagement 3: Audio AI
st.markdown("""
    <div class='work-card'>
        <span class='client-tag'>Voice Intelligence</span>
        <h3>Dialora | Lead AI Engineer</h3>
        <p style='color:#6b7280;'>Codiste Engagement (2025)</p>
        <p><b>Core Focus: Real-time Audio RAG & Voice Automation</b></p>
        <ul>
            <li>Designed a voice-AI orchestration layer using <b>Deepgram</b> and <b>n8n</b> for sub-second agent responses.</li>
            <li>Deployed <b>Qdrant</b> vector databases on high-performance infrastructure to minimize RAG retrieval latency.</li>
            <li>Automated complex CRM workflows through function-calling and agentic state management.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- OPEN SOURCE & EXTRAORDINARY WORK ---
st.header("🌐 Open Source & Research")
col_os1, col_os2 = st.columns(2)

with col_os1:
    st.markdown("""
    <div style='background: white; padding:20px; border-radius:12px; border:1px solid #eee;'>
        <h4>🍜 Ramen-Shop (Open Source)</h4>
        <p>A sophisticated full-stack architecture showcase demonstrating high-performance web integration and state management.</p>
        <a href='https://github.com/enderh3art/Ramen-Shop'>View Repository →</a>
    </div>
    """, unsafe_allow_html=True)

with col_os2:
    st.markdown("""
    <div style='background: white; padding:20px; border-radius:12px; border:1px solid #eee;'>
        <h4>🚀 ISRO Research</h4>
        <p>Computational structural design for extraterrestrial habitats. Applied origami-based engineering for Mars deployable structures.</p>
        <p><i>Research Intern (2024)</i></p>
    </div>
    """, unsafe_allow_html=True)

# --- TECHNICAL FOOTER ---
st.write("---")
st.subheader("🛠 Technical Expertise")
skills = [
    "PyTorch", "Transformers", "LangGraph", "Deepgram", "YOLO v10", "CUDA", "Cython", 
    "FastAPI", "Docker", "Qdrant", "PostgreSQL", "n8n", "Azure Cloud", "XGBoost"
]
for s in skills:
    st.markdown(f"<span class='skill-pill'>{s}</span>", unsafe_allow_html=True)

st.markdown("<br><br><center style='opacity:0.5;'>Vijay Modi | Senior AI Engineer | 2026</center>", unsafe_allow_html=True)
