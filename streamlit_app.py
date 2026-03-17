import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vijay Modi | AI/ML Engineer", page_icon="🤖", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    .impact-text {
        color: #1b5e20;
        font-weight: bold;
        background-color: #e8f5e9;
        padding: 5px;
        border-radius: 5px;
    }
    .company-header {
        font-size: 1.2rem;
        font-weight: bold;
        color: #0d47a1;
    }
    </style>
    """, unsafe_content_type=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("Vijay Modi")
    st.write("📍 Ahmedabad, Gujarat")
    st.write("📧 vijaymodi2002@gmail.com")
    st.write("📞 +91 9033701984")
    st.markdown("[LinkedIn](https://linkedin.com/in/vijaymodi174)")
    st.markdown("[GitHub](https://github.com/VijayM0di)")
    st.write("---")
    st.write("Specializing in:")
    st.caption("✅ Generative AI & RAG")
    st.caption("✅ Computer Vision (YOLO/OpenCV)")
    st.caption("✅ Agentic AI (LangGraph/CrewAI)")

# --- HEADER ---
st.title("AI & ML Engineer")
st.subheader("Building production-ready AI systems with measurable impact.")
st.write("""
I specialize in computer vision, predictive analytics, and conversational AI. 
I leverage PyTorch, TensorFlow, and Agentic frameworks to deliver client-focused solutions 
in healthcare, safety, and business automation.
""")

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["🚀 Experience", "🛠 Projects", "📜 Education & Certs"])

with tab1:
    st.header("Work Experience")
    
    # --- DRYTIS (Current Role) ---
    with st.expander("Drytis | AI Developer (Feb'26 - Present)", expanded=True):
        st.markdown("<span class='company-header'>Drytisai - Client-Facing AI Engineering Platform</span>", unsafe_content_type=True)
        st.write("- Delivered AI-assisted software engineering support via live pair programming and async sessions.")
        st.write("- Handled debugging, feature implementation, and full-stack deployment across diverse tech stacks.")
        st.write("- Maintained documentation and contributed to platform optimization on the proprietary 'Vibe Coding' platform.")
        st.markdown("<span class='impact-text'>🚀 Impact: Enabled rapid, production-ready delivery by reducing client blockers and improving project velocity.</span>", unsafe_content_type=True)

    # --- CODISTE ---
    with st.expander("Codiste | AI Developer (Nov'25 - Jan'26)"):
        st.markdown("<span class='company-header'>Dialora - AI Voice Agent Platform</span>", unsafe_content_type=True)
        st.write("- Designed and deployed RAG pipeline achieving **0.3s–0.6s latency** using Qdrant.")
        st.write("- Architected **n8n workflow** orchestration with real-time agent state management.")
        st.write("- Enabled voice agents to trigger API calls and CRM updates with sub-second response times.")
        st.markdown("<span class='impact-text'>🚀 Impact: Enabled 24/7 voice automation, reducing lead leakage and automating business workflows.</span>", unsafe_content_type=True)

    # --- QUANTUM BOT ---
    with st.expander("Quantum Bot | ML & AI Developer (Jun'24 - Oct'25)"):
        st.markdown("<span class='company-header'>AI Sante (Healthcare) & AI Agent Chatbot</span>", unsafe_content_type=True)
        st.write("- Developed a modular AI Agent suite using **CrewAI, LangGraph, and AutoGen**.")
        st.write("- Built a LangGraph-powered sales bot and integrated voice navigation for hands-free use.")
        st.write("- Deployed a healthcare automation suite on Azure with React and Django.")
        st.markdown("<span class='impact-text'>🚀 Impact: Reduced manual workload by 70%, boosted efficiency by 30%, and reduced integration time by 50%.</span>", unsafe_content_type=True)

with tab2:
    st.header("Key Technical Projects")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("CCTV AI Suite (Safety/Surveillance)")
        st.write("- Built a real-time computer vision suite for monitoring industrial environments.")
        st.write("- **Increased processing speed from 5 to 25 FPS** using Cython and GPU acceleration.")
        st.markdown("<span class='impact-text'>Result: Reduced incident response time by 40%.</span>", unsafe_content_type=True)
        
    with col2:
        st.subheader("Qbbot (GenBI AI Agent Platform)")
        st.write("- Developed platform for 'Chat with Data', text-to-SQL, and automated BI reports.")
        st.write("- Integrated OpenAI, Azure, Gemini, and Bedrock.")
        st.markdown("<span class='impact-text'>Result: Reduced manual BI reporting workload by 60%.</span>", unsafe_content_type=True)

    st.write("---")
    st.subheader("Golbot (Pharma Forecasting)")
    st.write("- Created predictive analytics for sales/demand prediction in the pharmaceutical sector.")
    st.markdown("<span class='impact-text'>Result: Improved forecasting accuracy by 20%.</span>", unsafe_content_type=True)

with tab3:
    st.header("Internships")
    st.write("**ISRO** | Research Intern (Jan'24 - Jul'24)")
    st.caption("Developed software for deployable Mars habitat dimensions and origami-based structures.")
    
    st.write("**Tata Group** | Data Analyst (Jul'23 - Aug'23)")
    st.caption("Generated strategic queries for HR and executives.")

    st.header("Education")
    st.write("**NIRMA University** | B.Tech in CSE (2020 - 2024)")
    
    st.header("Certifications")
    st.write("🏆 NVIDIA: Getting Started with AI on Jetson Nano")
    st.write("🏆 NVIDIA: Disaster Risk Monitoring Using Satellite Imagery")
    st.write("🏆 NVIDIA: Building Video AI Applications at the Edge")

# --- SKILLS SECTION ---
st.write("---")
st.header("Technical Stack")
s1, s2, s3 = st.columns(3)
with s1:
    st.write("**AI/ML & GenAI**")
    st.info("PyTorch, Transformers, LangChain, LangGraph, RAG, Llama-Index, YOLO, CrewAI")
with s2:
    st.write("**Databases**")
    st.info("Qdrant, MongoDB, PostgreSQL, ChromaDB, LanceDB")
with s3:
    st.write("**Development**")
    st.info("FastAPI, Flask, Streamlit, Docker, Azure, Git, Cython")

st.write("---")
st.markdown("<center>Built by Vijay Modi | 2026</center>", unsafe_content_type=True)
