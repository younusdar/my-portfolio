import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Younus Dar | Portfolio",
    page_icon="🚀",
    layout="wide",
)

# 2. Premium Hybrid Galaxy Background (Using a reliable cloud image URL)
bg_url = "https://images.unsplash.com/photo-1506318137071-a8e063b4bec0?q=80&w=1920"

# Fallback profile picture from your official LinkedIn asset profile context
profile_url = "https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=400" 

# Inject the dynamic & fully responsive mobile styling
st.markdown(f"""
<style>
/* Base Theme */
.stApp {{
    background: linear-gradient(135deg, rgba(6, 10, 26, 0.94) 0%, rgba(11, 19, 43, 0.96) 50%, rgba(27, 38, 59, 0.94) 100%), 
                url('{bg_url}') no-repeat center center fixed;
    background-size: cover;
    color: #cbd5e1;
}}

/* Responsive Profile Container */
.profile-sidebar {{
    background: rgba(15, 23, 42, 0.7);
    backdrop-filter: blur(20px);
    padding: 25px;
    border-radius: 20px;
    border: 1px solid rgba(129, 140, 248, 0.2);
    text-align: center;
    box-shadow: 0 20px 50px -15px rgba(0, 0, 0, 0.8);
    width: 100%;
}}

/* Structural Information Blocks */
.skills-card {{
    background: rgba(11, 19, 43, 0.75);
    backdrop-filter: blur(12px);
    padding: 18px;
    border-radius: 14px;
    border: 1px solid rgba(129, 140, 248, 0.15);
    margin-bottom: 15px;
}}
.web-card {{
    background: rgba(15, 23, 42, 0.8);
    backdrop-filter: blur(12px);
    padding: 22px;
    border-radius: 16px;
    border: 1px solid rgba(129, 140, 248, 0.2);
    margin-bottom: 20px;
    box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.6);
}}
h1, h2, h3, h4, h5 {{
    color: #ffffff !important;
    font-family: 'Inter', sans-serif;
}}
.accent-text {{
    color: #818cf8;
    font-weight: 600;
    font-size: 14px;
}}
.timeline-badge {{
    float: right;
    background: rgba(129, 140, 248, 0.25);
    color: #c7d2fe;
    padding: 4px 14px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 600;
    border: 1px solid rgba(129, 140, 248, 0.4);
}}
.project-card {{
    background: rgba(129, 140, 248, 0.05);
    border-left: 3px solid #818cf8;
    padding: 12px 16px;
    margin-top: 12px;
    border-radius: 0 8px 8px 0;
}}
.profile-pic-container {{
    display: flex;
    justify-content: center;
    margin-bottom: 15px;
}}
.profile-img-styled {{
    width: 140px;
    height: 140px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid rgba(129, 140, 248, 0.5);
    box-shadow: 0 4px 20px rgba(129, 140, 248, 0.3);
}}
@media (max-width: 768px) {{
    .timeline-badge {{
        float: none;
        display: inline-block;
        margin-top: 5px;
        margin-bottom: 10px;
    }}
    .profile-sidebar, .web-card, .skills-card {{
        padding: 15px;
    }}
    h1 {{
        font-size: 24px !important;
    }}
}}
</style>
""", unsafe_allow_html=True)

# 3. Main Web Page Layout Grid
col_profile, col_skills, col_experience = st.columns([1, 1.2, 2.3], gap="medium")

# ==============================================================================
# --- COLUMN 1: STATIC PROFILE CARD ---
# ==============================================================================
with col_profile:
    st.markdown('<div class="profile-sidebar">', unsafe_allow_html=True)
    
    # Renders the image directly inside the sidebar container using the stable URL path
    st.markdown(f"""
    <div class="profile-pic-container">
        <img src="{profile_url}" class="profile-img-styled" alt="Younus Dar">
    </div>
    """, unsafe_allow_html=True)
        
    st.markdown("""
<h1 style="margin-bottom:2px; font-size:28px; margin-top:10px;">Younus Dar</h1>
<p class="accent-text" style="font-size:14px; margin-bottom:15px; text-transform: uppercase; letter-spacing:0.5px;">Data Engineer</p>
<hr style="border-color:rgba(255,255,255,0.08); margin:15px 0;">
<p style="color: #cbd5e1; font-size: 13px; text-align: left; margin-bottom:8px;">📍 Bangalore, India 560043</p>
<p style="color: #cbd5e1; font-size: 13px; text-align: left; margin-bottom:8px;">📞 +91 7780828706</p>
<p style="color: #cbd5e1; font-size: 13px; text-align: left; margin-bottom:0px;">✉️ DARYOUNUS767@GMAIL.COM</p>
</div>
""", unsafe_allow_html=True)
    
    st.write("")
    
    # Action Navigation Buttons
    st.link_button("🔗 Connect on LinkedIn", "https://www.linkedin.com/in/younus-dar-a51574147/", width="stretch")
    st.link_button("💻 GitHub Repository", "https://github.com/YOUR_GITHUB_ID", width="stretch")
    st.link_button("📝 Read on Medium", "https://medium.com/@YOUR_MEDIUM_ID", width="stretch")
    st.link_button("💬 Message via WhatsApp", "https://wa.me/917780828706", width="stretch")
    st.link_button("🌐 View Facebook Profile", "https://facebook.com/YOUR_FACEBOOK_ID", width="stretch")
    st.link_button("✉️ Open Direct Email", "mailto:DARYOUNUS767@GMAIL.COM", width="stretch")
    
    st.write("")
    
    st.markdown("### Credentials")
    st.markdown("""
<div class="skills-card" style="border-color: rgba(251, 191, 36, 0.3);">
<p style="margin:0; font-size:13.5px; font-weight:600; color:#fff;">🏆 AWS Certified Cloud Practitioner</p>
<span style="font-size:11px; color:#64748b;">Issued 2024</span>
</div>
<div class="skills-card" style="border-color: rgba(56, 189, 248, 0.3);">
<p style="margin:0; font-size:13.5px; font-weight:600; color:#fff;">❄️ SnowPro Core Certification</p>
<span style="font-size:11px; color:#64748b;">Snowflake | Issued 2023</span>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
# --- COLUMN 2: STRUCTURED CORE STACK MATRICES ---
# ==============================================================================
with col_skills:
    st.markdown("## Summary & Stack")
    
    st.markdown("""
<div class="skills-card" style="background: rgba(30, 41, 59, 0.2); border-color: rgba(129, 140, 248, 0.3);">
<h4 style="margin-top:0; font-size:15px; color:#ffffff !important;">Professional Summary</h4>
<p style="font-size:12.5px; line-height:1.6; margin:0; color:#cbd5e1; text-align: justify;">
Data Engineer with 4+ years of experience designing, building, and optimizing scalable ETL/ELT pipelines, cloud data warehouses, and automated analytics solutions using SQL, Python, AWS, and Snowflake. Expertise in embedding Generative AI into the data engineering lifecycle, utilizing OpenAI and Gemini APIs for synthetic data generation, time-series synthesis, data augmentation, and automated pipeline edge-case testing. Proven ability to partner with business stakeholders to transform unstructured data and deliver resilient, high-quality data solutions that accelerate decision-making.
</p>
</div>
<div class="skills-card">
<h4 style="margin-top:0; font-size:15px; color:#818cf8 !important;">Technical Skills & Infrastructure</h4>
<p style="font-size:13px; line-height:1.6; margin:0; color:#94a3b8;">
• Python, SQL, MySQL<br>
• AWS Lambda, AWS Glue, S3, EC2<br>
• Snowflake Data Warehouse<br>
• Git, Version Control & CI/CD Pipelines<br>
• Pandas, NumPy Data Ecosystem
</p>
</div>
<div class="skills-card">
<h4 style="margin-top:0; font-size:15px; color:#34d399 !important;">Generative AI & Data</h4>
<p style="font-size:13px; line-height:1.6; margin:0; color:#94a3b8;">
• Synthetic Data Generation<br>
• Data Augmentation (OpenAI / Gemini)<br>
• Time-Series Data Synthesis<br>
• AI-Driven Edge-Case Simulation
</p>
</div>
<div class="skills-card">
<h4 style="margin-top:0; font-size:15px; color:#f43f5e !important;">Analytics & Monitoring</h4>
<p style="font-size:13px; line-height:1.6; margin:0; color:#94a3b8;">
• Data Validation & Quality Check<br>
• Root Cause Analysis (RCA)<br>
• Automated Pipeline Monitoring<br>
• Business Intelligence (BI) via Tableau
</p>
</div>
""", unsafe_allow_html=True)
    
    st.markdown("### Schooling")
    st.markdown("""
<div class="skills-card" style="background: rgba(30, 41, 59, 0.25);">
<h5 style="margin:0; font-size:14px;">Master of Computer Science</h5>
<p style="font-size:11.5px; color:#818cf8; margin:2px 0;">University of Kashmir — Srinagar, India</p>
<p style="font-size:11px; color:#64748b; margin:0; line-height:1.4;">
<b>Specializations:</b> Database Management Systems, AI, Data Mining, Machine Learning, Information Storage and Management (Graduated 07/2021).
</p>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
# --- COLUMN 3: DEEP TIMELINE & COMPREHENSIVE EXPERIENCES ---
# ==============================================================================
with col_experience:
    st.markdown("## Professional Experience")
    
    st.markdown("""
<div class="web-card">
<span class="timeline-badge">Oct 2024 – Present</span>
<h4 style="margin:0; font-size:16px;">Platform / Data Engineer</h4>
<div class="accent-text" style="margin-bottom:8px;">Tata Consultancy Services</div>
<p style="font-size: 13px; color: #cbd5e1; margin: 0; line-height: 1.5;">
• DESIGNED and IMPLEMENTED production code changes based on business requirements using Python, Git, and CI/CD pipelines, ensuring reliable deployment across multiple environments.<br>
• ANALYZED operational logs and AWS Lambda exceptions to IDENTIFY root causes, RESOLVE issues, and IMPROVE system reliability.<br>
• DEVELOPED automated reporting solutions by EXTRACTING and TRANSFORMING AWS billing and cost data across multiple accounts, enabling data-driven decision making.<br>
• BUILT and MAINTAINED scalable cloud-based workflows using AWS services including Lambda, CloudWatch, IAM, Route 53, and CodePipeline.<br>
• AUTOMATED monitoring and incident management processes using AWS CloudWatch and ServiceNow, improving response times and operational efficiency.
</p>

<h5 style="margin:15px 0 5px 0; font-size:13.5px; color:#34d399 !important;">💡 Highlighted GenAI Lifecycle Projects (Present):</h5>

<div class="project-card">
<p style="margin:0; font-size:12.5px; color:#fff; font-weight:600;">🚀 Multi-Format Document RAG Infrastructure Pipeline</p>
<p style="margin:3px 0 0 0; font-size:12px; color:#94a3b8; line-height:1.4;">
Architected an end-to-end multi-format ingestion ecosystem to extract and process complex semi-structured enterprise documents (PDFs, DOCX, CSVs). Engineered smart structural semantic text-splitting, hierarchical document chunking, and embedding workflows to map content into scalable vector spaces, drastically boosting extraction accuracy for downstream LLMs.
</p>
</div>

<div class="project-card">
<p style="margin:0; font-size:12.5px; color:#fff; font-weight:600;">Enterprise Retrieval-Augmented Generation (RAG) Pipeline</p>
<p style="margin:3px 0 0 0; font-size:12px; color:#94a3b8; line-height:1.4;">
Architected and deployed an end-to-end RAG system to query unstructured organizational data. Engineered the data ingestion layer to extract, chunk, and embed text into a vector database, optimizing retrieval accuracy and context window utilization for downstream LLMs.
</p>
</div>

<div class="project-card">
<p style="margin:0; font-size:12.5px; color:#fff; font-weight:600;">Synthetic and Time-Series DATA Generation</p>
<p style="margin:3px 0 0 0; font-size:12px; color:#94a3b8; line-height:1.4;">
Designed and engineered automated workflows to synthesize chronological, high-fidelity transactional and weather metrics to stress-test cloud storage and pipeline scaling limits without risking real-world PII data.
</p>
</div>

<div class="project-card">
<p style="margin:0; font-size:12.5px; color:#fff; font-weight:600;">Contextual Data Augmentation</p>
<p style="margin:3px 0 0 0; font-size:12px; color:#94a3b8; line-height:1.4;">
Built scalable prompt-engineering frameworks utilizing LLM APIs to programmatically read small textual data samples and generate massive, balanced variations to enhance training and testing datasets.
</p>
</div>

<div class="project-card">
<p style="margin:0; font-size:12.5px; color:#fff; font-weight:600;">Automated Pipeline Edge-Case Injectors</p>
<p style="margin:3px 0 0 0; font-size:12px; color:#94a3b8; line-height:1.4;">
Developed custom automated testing blocks designed to inject intentional data anomalies—such as extreme negative values, corrupt datetime formats, and dirty text scripts—proactively verifying pipeline exception handling before code reached production.
</p>
</div>
</div>

<div class="web-card">
<span class="timeline-badge">Mar 2023 – Sep 2024</span>
<h4 style="margin:0; font-size:16px;">Data Engineer</h4>
<div class="accent-text" style="margin-bottom:8px;">Quantiphi Analytics</div>
<p style="font-size: 13px; color: #cbd5e1; margin: 0; line-height: 1.5;">
• DESIGNED, DEVELOPED, and MAINTAINED scalable ETL pipelines using AWS Glue, AWS Lambda, Python, and SQL to process large-scale datasets.<br>
• BUILT robust data integration frameworks for extracting, transforming, validating, and loading data from multiple source systems.<br>
• DEVELOPED and OPTIMIZED SQL stored procedures, functions, and complex queries to improve data processing performance and scalability.<br>
• CREATED interactive Tableau dashboards and analytical reports that enabled stakeholders to monitor KPIs and make data-driven decisions.<br>
• AUTOMATED data extraction, quality validation, and reporting workflows using Python, reducing manual effort and improving delivery efficiency.<br>
• PARTNERED with business stakeholders to GATHER requirements, DEFINE reporting needs, and DELIVER end-to-end data solutions.<br>
• PERFORMED data quality checks and validation processes to ensure accuracy, consistency, and reliability of enterprise datasets.
</p>
</div>

<div class="web-card">
<span class="timeline-badge">Nov 2022 – Mar 2023</span>
<h4 style="margin:0; font-size:16px;">Trainee Data Engineer</h4>
<div class="accent-text" style="margin-bottom:8px;">Quantiphi Analytics</div>
<p style="font-size: 13px; color: #cbd5e1; margin: 0; line-height: 1.5;">
• DEVELOPED ETL workflows using Python, SQL, AWS, and Snowflake to support enterprise data warehousing initiatives.<br>
• CREATED data models and optimized SQL queries for reporting and analytics workloads.<br>
• BUILT Tableau dashboards and visualizations to transform raw datasets into actionable business insights.<br>
• IMPLEMENTED data transformation and cleansing processes using Python libraries including Pandas and NumPy.<br>
• SUPPORTED cloud-based data processing solutions leveraging AWS services such as S3, Lambda, and EC2.
</p>
</div>

<div class="web-card">
<span class="timeline-badge">Oct 2021 – Oct 2022</span>
<h4 style="margin:0; font-size:16px;">ETL Tester / Software Engineer</h4>
<div class="accent-text" style="margin-bottom:8px;">Merkle</div>
<p style="font-size: 13px; color: #cbd5e1; margin: 0; line-height: 1.5;">
• VALIDATED ETL workflows and enterprise datasets using SQL and MySQL to ensure data integrity and quality.<br>
• EXECUTED complex SQL queries to verify dimensional and fact table accuracy across data warehouse environments.<br>
• COLLABORATED with business analysts and development teams to INVESTIGATE data issues and DELIVER timely resolutions.<br>
• PERFORMED end-to-end testing of data pipelines, ensuring successful data movement across source and target systems.<br>
• UTILIZED JIRA and Agile methodologies to TRACK defects, MANAGE releases, and SUPPORT continuous delivery processes.
</p>
</div>
""", unsafe_allow_html=True)
