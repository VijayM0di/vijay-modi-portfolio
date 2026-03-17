import streamlit as st
from PIL import Image

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
        color: #2e7d32;
        font-weight: bold;
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
    st.markdown("[GitHub](https://github.com/your-username)") # Update this
    st.write("---")
    st.download_button("📄 Download Resume", data="Your Resume Content", file_name="Vijay_Modi_Resume.pdf")

# --- HEADER ---
st.title("AI & ML Engineer")
st.subheader("Specializing in GenAI, Computer Vision, and Agentic Workflows")
st.write("""
I build production-ready AI systems. From RAG pipelines with 0.3s latency to 
real-time Computer Vision suites optimized for industrial safety.
""")

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["🚀 Experience", "🛠 Projects", "📜 Education & Certs"])

with tab1:
    st.header("Work Experience")
    
    with st.expander("Codiste | AI Developer (Nov'25 - Jan'26)"):
        st.write("**Dialora: AI Voice Agent Platform**")
        st.write("- Designed RAG pipeline achieving 0.3s–0.6s latency using Qdrant.")
        st.write("- Architected n8n workflow for real-time state management.")
        st.markdown("<span class='impact-text'>Impact: Enabled 24/7 voice automation and reduced lead leakage.</span>", unsafe_content_type=True)

    with st.expander("Quantum Bot | ML & AI Developer (Jun'24 - Oct'25)"):
        st.write("**AI Sante & AI Agent Chatbot**")
        st.write("- Developed a modular conversational AI suite using CrewAI, LangGraph, and AutoGen.")
        st.write("- Built a healthcare automation suite on Azure.")
        st.markdown("<span class='impact-text'>Impact: Reduced manual workload by 70% and integration time by 50%.</span>", unsafe_content_type=True)

with tab2:
    st.header("Key Technical Projects")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("CCTV AI Suite")
        st.write("Real-time CV for safety and monitoring.")
        st.write("- Tech: Python, Cython, GPU Acceleration, YOLO.")
        st.markdown("<span class='impact-text'>Result: Increased FPS from 5 to 25.</span>", unsafe_content_type=True)
        
    with col2:
        st.subheader("Qbbot: GenBI Platform")
        st.write("Chat-with-data platform for BI reports.")
        st.write("- Tech: OpenAI, Bedrock, LangChain, Vector DBs.")
        st.markdown("<span class='impact-text'>Result: Reduced manual reporting workload by 60%.</span>", unsafe_content_type=True)

with tab3:
    st.header("Education")
    st.write("**NIRMA University** | B.Tech in CSE (2020 - 2024)")
    
    st.header("Certifications")
    st.write("- NVIDIA: Getting Started with AI on Jetson Nano")
    st.write("- NVIDIA: Building Video AI Applications at the Edge")

# --- SKILLS (GRID) ---
st.write("---")
st.header("Technical Skills")
k1, k2, k3 = st.columns(3)
with k1:
    st.write("**AI/ML**")
    st.caption("PyTorch, TensorFlow, LangChain, LLMs (Claude, GPT), RAG")
with k2:
    st.write("**DataBases**")
    st.caption("PostgreSQL, MongoDB, Qdrant, ChromaDB")
with k3:
    st.write("**DevOps & Tools**")
    st.caption("Docker, FastAPI, Azure, Git, Streamlit")
