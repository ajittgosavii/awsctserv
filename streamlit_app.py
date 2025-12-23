"""
AWS Enterprise Assessment Platform v3.0
Comprehensive Control Tower & Golden Architecture Assessment
130+ Questions | 22 Domains | AI-Powered Analysis
"""

import streamlit as st
import json
import os
import io
import numpy as np
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, 
    PageBreak, Image, ListFlowable, ListItem, KeepTogether
)
from reportlab.graphics.shapes import Drawing, Rect, String, Line
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.pdfgen import canvas
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Wedge
from matplotlib.collections import PatchCollection
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

st.set_page_config(
    page_title="AWS Enterprise Assessment Platform",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# ENTERPRISE PROFESSIONAL CSS
# =============================================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --primary: #0284c7;
    --primary-dark: #0369a1;
    --primary-light: #38bdf8;
    --secondary: #6366f1;
    --success: #059669;
    --success-light: #d1fae5;
    --warning: #d97706;
    --warning-light: #fef3c7;
    --danger: #dc2626;
    --danger-light: #fee2e2;
    --info: #0891b2;
    --aws-orange: #ff9900;
    --aws-dark: #232f3e;
    --bg-primary: #f1f5f9;
    --bg-secondary: #ffffff;
    --bg-tertiary: #f8fafc;
    --border-light: #e2e8f0;
    --border-dark: #cbd5e1;
    --text-primary: #0f172a;
    --text-secondary: #475569;
    --text-muted: #94a3b8;
    --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
    --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
    --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
    --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
}

* { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }
.stApp { background: var(--bg-primary) !important; }
[data-testid="stSidebar"] { 
    background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%) !important; 
    border-right: 1px solid var(--border-light) !important; 
}

/* ===== MAIN HEADER ===== */
.main-header {
    background: linear-gradient(135deg, var(--aws-dark) 0%, #1e3a5f 50%, #0f172a 100%);
    padding: 2.5rem 3rem;
    border-radius: 20px;
    margin-bottom: 2rem;
    box-shadow: var(--shadow-xl);
    position: relative;
    overflow: hidden;
}
.main-header::before {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    width: 40%;
    height: 100%;
    background: linear-gradient(135deg, transparent 0%, rgba(255,153,0,0.1) 100%);
}
.main-header h1 {
    font-weight: 800;
    font-size: 2rem;
    color: #ffffff;
    margin: 0;
    letter-spacing: -0.5px;
    position: relative;
    z-index: 1;
}
.main-header p {
    color: rgba(255,255,255,0.7);
    font-size: 1.05rem;
    margin: 0.75rem 0 0 0;
    font-weight: 400;
    position: relative;
    z-index: 1;
}
.header-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: linear-gradient(135deg, var(--aws-orange) 0%, #f59e0b 100%);
    color: var(--aws-dark);
    padding: 0.4rem 1rem;
    border-radius: 8px;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 1px;
    margin-left: 1rem;
    box-shadow: 0 2px 8px rgba(255,153,0,0.3);
}
.header-stats {
    display: flex;
    gap: 2rem;
    margin-top: 1.5rem;
    position: relative;
    z-index: 1;
}
.header-stat {
    text-align: center;
}
.header-stat-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--aws-orange);
}
.header-stat-label {
    font-size: 0.75rem;
    color: rgba(255,255,255,0.6);
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* ===== METRIC CARDS ===== */
.metric-card {
    background: var(--bg-secondary);
    padding: 1.75rem;
    border-radius: 16px;
    text-align: center;
    border: 1px solid var(--border-light);
    box-shadow: var(--shadow-md);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}
.metric-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, var(--primary) 0%, var(--secondary) 100%);
    opacity: 0;
    transition: opacity 0.3s ease;
}
.metric-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-xl);
}
.metric-card:hover::before {
    opacity: 1;
}
.metric-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 3rem;
    font-weight: 700;
    line-height: 1;
    background: linear-gradient(135deg, var(--text-primary) 0%, var(--text-secondary) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.metric-value.success { background: linear-gradient(135deg, #059669 0%, #10b981 100%); -webkit-background-clip: text; background-clip: text; }
.metric-value.warning { background: linear-gradient(135deg, #d97706 0%, #f59e0b 100%); -webkit-background-clip: text; background-clip: text; }
.metric-value.danger { background: linear-gradient(135deg, #dc2626 0%, #ef4444 100%); -webkit-background-clip: text; background-clip: text; }
.metric-label {
    font-size: 0.75rem;
    font-weight: 600;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 0.75rem;
}
.metric-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    margin-top: 0.75rem;
    padding: 0.4rem 1rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
}
.badge-success { background: var(--success-light); color: var(--success); }
.badge-warning { background: var(--warning-light); color: var(--warning); }
.badge-danger { background: var(--danger-light); color: var(--danger); }
.badge-neutral { background: #f1f5f9; color: var(--text-secondary); }

/* ===== SECTION HEADERS ===== */
.section-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1.5rem;
    padding-bottom: 1rem;
    border-bottom: 2px solid var(--border-light);
}
.section-icon {
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    border-radius: 12px;
    font-size: 1.5rem;
    box-shadow: var(--shadow-md);
}
.section-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-primary);
    margin: 0;
}
.section-subtitle {
    font-size: 0.9rem;
    color: var(--text-secondary);
    margin: 0.25rem 0 0 0;
}

/* ===== DOMAIN CARDS ===== */
.domain-card {
    background: var(--bg-secondary);
    border: 1px solid var(--border-light);
    border-radius: 12px;
    padding: 1rem 1.25rem;
    margin-bottom: 0.75rem;
    transition: all 0.2s ease;
}
.domain-card:hover {
    border-color: var(--primary);
    box-shadow: var(--shadow-md);
}
.domain-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.domain-name {
    font-weight: 600;
    color: var(--text-primary);
    font-size: 0.95rem;
}
.domain-score {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600;
    font-size: 0.9rem;
}
.domain-meta {
    display: flex;
    gap: 1rem;
    margin-top: 0.5rem;
    font-size: 0.8rem;
    color: var(--text-muted);
}

/* ===== QUESTION CARDS ===== */
.question-card {
    background: var(--bg-secondary);
    border: 1px solid var(--border-light);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1rem 0;
    transition: all 0.2s ease;
    position: relative;
}
.question-card::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 4px;
    border-radius: 12px 0 0 12px;
    background: var(--border-light);
    transition: background 0.2s ease;
}
.question-card.answered::before {
    background: linear-gradient(180deg, var(--success) 0%, #10b981 100%);
}
.question-card.answered {
    background: linear-gradient(90deg, rgba(5,150,105,0.03) 0%, var(--bg-secondary) 100%);
    border-color: rgba(5,150,105,0.2);
}
.question-card:hover {
    box-shadow: var(--shadow-md);
    border-color: var(--primary);
}
.question-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 1rem;
    margin-bottom: 0.75rem;
}
.question-id {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    font-weight: 600;
    color: var(--primary);
    background: rgba(2,132,199,0.1);
    padding: 0.25rem 0.6rem;
    border-radius: 6px;
}
.question-text {
    font-size: 1rem;
    font-weight: 600;
    color: var(--text-primary);
    line-height: 1.5;
    margin-bottom: 0.5rem;
}
.question-context {
    font-size: 0.875rem;
    color: var(--text-secondary);
    line-height: 1.6;
    padding: 1rem;
    background: var(--bg-tertiary);
    border-radius: 8px;
    border-left: 3px solid var(--primary);
    margin: 0.75rem 0;
}

/* ===== RISK BADGES ===== */
.risk-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
    padding: 0.25rem 0.6rem;
    border-radius: 6px;
    font-size: 0.65rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.risk-critical { 
    background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%); 
    color: #b91c1c; 
    border: 1px solid #fecaca;
}
.risk-high { 
    background: linear-gradient(135deg, #fff7ed 0%, #ffedd5 100%); 
    color: #c2410c; 
    border: 1px solid #fed7aa;
}
.risk-medium { 
    background: linear-gradient(135deg, #fefce8 0%, #fef9c3 100%); 
    color: #a16207; 
    border: 1px solid #fef08a;
}
.risk-low { 
    background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%); 
    color: #15803d; 
    border: 1px solid #bbf7d0;
}

/* ===== PILLAR TAGS ===== */
.pillar-container { display: flex; flex-wrap: wrap; gap: 0.35rem; margin: 0.5rem 0; }
.pillar-tag {
    display: inline-flex;
    align-items: center;
    padding: 0.2rem 0.5rem;
    border-radius: 6px;
    font-size: 0.65rem;
    font-weight: 600;
}
.pillar-SEC { background: #fef2f2; color: #dc2626; }
.pillar-REL { background: #eff6ff; color: #2563eb; }
.pillar-PERF { background: #faf5ff; color: #9333ea; }
.pillar-COST { background: #f0fdf4; color: #16a34a; }
.pillar-OPS { background: #fff7ed; color: #ea580c; }
.pillar-SUS { background: #ecfdf5; color: #059669; }

/* ===== GAP CARDS ===== */
.gap-card {
    background: var(--bg-secondary);
    border: 1px solid var(--border-light);
    border-radius: 12px;
    padding: 1.25rem;
    margin: 0.75rem 0;
    position: relative;
    overflow: hidden;
}
.gap-card::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 4px;
}
.gap-card.critical::before { background: linear-gradient(180deg, #dc2626 0%, #ef4444 100%); }
.gap-card.high::before { background: linear-gradient(180deg, #ea580c 0%, #f97316 100%); }
.gap-card.medium::before { background: linear-gradient(180deg, #ca8a04 0%, #eab308 100%); }

/* ===== TABS ===== */
.stTabs [data-baseweb="tab-list"] {
    background: var(--bg-secondary);
    padding: 0.5rem;
    border-radius: 16px;
    border: 1px solid var(--border-light);
    gap: 0.25rem;
    box-shadow: var(--shadow-sm);
}
.stTabs [data-baseweb="tab"] {
    font-weight: 600;
    font-size: 0.9rem;
    color: var(--text-secondary);
    border-radius: 12px;
    padding: 0.75rem 1.5rem;
    transition: all 0.2s ease;
}
.stTabs [data-baseweb="tab"]:hover {
    background: var(--bg-tertiary);
    color: var(--text-primary);
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%) !important;
    color: white !important;
    box-shadow: var(--shadow-md);
}

/* ===== BUTTONS ===== */
.stButton > button {
    font-weight: 600;
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px;
    padding: 0.6rem 1.5rem;
    box-shadow: 0 4px 14px rgba(2,132,199,0.25);
    transition: all 0.2s ease;
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(2,132,199,0.35);
}
.stDownloadButton > button {
    background: linear-gradient(135deg, var(--success) 0%, #047857 100%) !important;
    box-shadow: 0 4px 14px rgba(5,150,105,0.25);
}

/* ===== EXPANDERS ===== */
div[data-testid="stExpander"] {
    background: var(--bg-secondary);
    border: 1px solid var(--border-light);
    border-radius: 12px;
    margin-bottom: 0.75rem;
    box-shadow: var(--shadow-sm);
    overflow: hidden;
}
div[data-testid="stExpander"] details summary {
    font-weight: 600;
    color: var(--text-primary);
    padding: 1rem 1.25rem;
}
div[data-testid="stExpander"] details summary:hover {
    color: var(--primary);
}

/* ===== PROGRESS BARS ===== */
.stProgress > div > div > div { 
    background: linear-gradient(90deg, var(--primary) 0%, var(--secondary) 100%) !important; 
    border-radius: 10px;
}
.stProgress > div > div { 
    background: var(--border-light) !important; 
    border-radius: 10px;
}

/* ===== AI RESPONSE ===== */
.ai-response {
    background: var(--bg-secondary);
    border: 1px solid var(--border-light);
    border-radius: 16px;
    padding: 2rem;
    margin-top: 1.5rem;
    box-shadow: var(--shadow-md);
}
.ai-response h2 {
    color: var(--text-primary);
    font-size: 1.25rem;
    font-weight: 700;
    border-bottom: 2px solid var(--border-light);
    padding-bottom: 0.75rem;
    margin-top: 2rem;
}
.ai-response h3 {
    color: var(--primary);
    font-size: 1.1rem;
    font-weight: 600;
}
.ai-response ul, .ai-response ol {
    color: var(--text-secondary);
}
.ai-response code {
    background: var(--bg-tertiary);
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85em;
}

/* ===== SIDEBAR ===== */
[data-testid="stSidebar"] .stMarkdown h3 {
    font-size: 0.7rem !important;
    font-weight: 700 !important;
    color: var(--text-muted) !important;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 1.5rem;
    margin-bottom: 0.75rem;
}

/* ===== FORM ELEMENTS ===== */
.stSelectbox > div > div {
    border-radius: 10px !important;
    border-color: var(--border-light) !important;
}
.stSelectbox > div > div:focus-within {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px rgba(2,132,199,0.1) !important;
}
.stTextInput > div > div > input {
    border-radius: 10px !important;
}

/* ===== ALERTS ===== */
.stAlert { border-radius: 12px; }

/* ===== SCROLLBAR ===== */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: var(--bg-tertiary); border-radius: 4px; }
::-webkit-scrollbar-thumb { background: var(--border-dark); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--text-muted); }

/* ===== HIDE STREAMLIT DEFAULTS ===== */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# CONSTANTS
# =============================================================================
WA_PILLARS = {
    "SEC": "Security",
    "REL": "Reliability",
    "PERF": "Performance Efficiency",
    "COST": "Cost Optimization",
    "OPS": "Operational Excellence",
    "SUS": "Sustainability"
}

BENCHMARKS = {
    "financial": {"name": "Financial Services", "avg": 72, "top": 88},
    "healthcare": {"name": "Healthcare & Life Sciences", "avg": 65, "top": 82},
    "technology": {"name": "Technology & Software", "avg": 78, "top": 92},
    "retail": {"name": "Retail & E-Commerce", "avg": 62, "top": 78},
    "government": {"name": "Government & Public Sector", "avg": 58, "top": 75},
    "manufacturing": {"name": "Manufacturing & Industrial", "avg": 55, "top": 72}
}

NOT_ANSWERED = "⊘ Not yet assessed"

# =============================================================================
# CONTROL TOWER ASSESSMENT - 12 DOMAINS, 75+ QUESTIONS
# =============================================================================
CT_QUESTIONS = {
    "Organizational Strategy & Governance": {
        "weight": 0.10, "pillars": ["OPS", "SEC"],
        "description": "Multi-account strategy, governance frameworks, and organizational readiness for Control Tower.",
        "questions": [
            {"id": "CT-ORG-001", "question": "What is your current AWS multi-account strategy maturity level?",
             "context": "A well-defined multi-account strategy is fundamental for Control Tower success. AWS recommends separating workloads by function, compliance requirements, and SDLC stages.",
             "risk": "critical", "options": ["No strategy - single account or ad-hoc creation", "Basic dev/prod separation without formal design", "Documented OU hierarchy aligned with AWS best practices", "Comprehensive workload isolation with dedicated shared services accounts", "Mature automated lifecycle with self-service and CMDB integration"]},
            {"id": "CT-ORG-002", "question": "How well-documented and enforced is your Organizational Unit (OU) structure?",
             "context": "Control Tower relies on OU structure for policy inheritance and guardrail application. Poor OU design leads to security gaps and operational complexity.",
             "risk": "high", "options": ["No OU structure - all accounts at root", "Basic OUs without inheritance strategy", "SDLC-aligned OUs with policy differentiation", "Nested hierarchy with Security, Infrastructure, Workloads OUs", "Enterprise architecture with business unit separation and automation"]},
            {"id": "CT-ORG-003", "question": "What cloud governance bodies and decision-making frameworks exist?",
             "context": "Effective Control Tower adoption requires clear governance for policy decisions, exception handling, and cross-functional coordination.",
             "risk": "high", "options": ["No formal governance - ad-hoc decisions", "IT-led decisions without stakeholder input", "Emerging CCoE with key team representatives", "Mature CCoE with RACI, escalation paths, multi-team representation", "Federated governance with self-service and executive sponsorship"]},
            {"id": "CT-ORG-004", "question": "How are cloud security and compliance policies documented and maintained?",
             "context": "Control Tower guardrails enforce policies, but organizations need clear documentation mapping business requirements to technical controls.",
             "risk": "high", "options": ["No documented policies - tribal knowledge only", "Informal wiki/SharePoint rarely updated", "Formal policies with annual review cycle", "Policies in GRC platform linked to guardrails", "Policy-as-Code in version control with drift detection"]},
            {"id": "CT-ORG-005", "question": "What is your process for managing policy exceptions and guardrail deviations?",
             "context": "Even with strong guardrails, legitimate business needs may require exceptions. Without formal process, exceptions become permanent security debt.",
             "risk": "medium", "options": ["No process - guardrails bypassed without approval", "Ad-hoc email/Slack approvals without tracking", "Documented process with tracking spreadsheet", "Workflow automation with approval chains and reminders", "Risk-based automation with self-service and auto-expiration"]},
            {"id": "CT-ORG-006", "question": "How is account ownership and accountability managed across the organization?",
             "context": "Clear ownership ensures security accountability, cost management, and operational support at scale when managing hundreds of accounts.",
             "risk": "medium", "options": ["No ownership model - accounts orphaned", "Informal assignments tracked manually", "Documented ownership in spreadsheet/wiki", "CMDB-tracked with regular validation", "Automated HR integration with lifecycle management"]},
        ]
    },
    "Account Factory & Provisioning": {
        "weight": 0.09, "pillars": ["OPS", "SEC", "REL"],
        "description": "Account provisioning automation, baseline configurations, and Infrastructure as Code maturity.",
        "questions": [
            {"id": "CT-ACC-001", "question": "How are new AWS accounts currently provisioned?",
             "context": "Control Tower Account Factory provides automated, governed provisioning. Organizations with manual processes benefit most but need change management.",
             "risk": "high", "options": ["Manual console creation without templates", "CLI scripts with manual baseline configuration", "Semi-automated IaC with manual steps required", "Service Catalog products with approval workflows", "Account Factory for Terraform with GitOps workflow"]},
            {"id": "CT-ACC-002", "question": "What is your average time from account request to production-ready?",
             "context": "Provisioning speed directly impacts developer productivity. Control Tower with AFT can achieve under 4 hours.",
             "risk": "medium", "options": ["2+ weeks with multiple approval chains", "1-2 weeks with significant manual work", "3-5 business days with manual validation", "1-2 business days with minimal gates", "Under 4 hours with full automation"]},
            {"id": "CT-ACC-003", "question": "What baseline security configurations are automatically applied?",
             "context": "Account baselines are critical for security posture. Control Tower applies foundational baselines but organizations need additional customizations.",
             "risk": "critical", "options": ["No baselines - teams configure independently", "Basic security (password policy, IAM roles)", "Security baseline (CloudTrail, Config, GuardDuty, Security Hub)", "Comprehensive (security + networking + logging + cost controls)", "Full enterprise baseline with compliance controls and integrations"]},
            {"id": "CT-ACC-004", "question": "How is configuration drift from baselines detected and remediated?",
             "context": "Without automated detection, baseline configurations degrade over time. Auto-remediation reduces operational burden.",
             "risk": "high", "options": ["No detection - discovered during audits only", "Manual periodic reviews", "Config rules with alerting for manual remediation", "Automated detection with prioritized queue and SLAs", "Auto-remediation with preventive SCPs"]},
            {"id": "CT-ACC-005", "question": "What Infrastructure as Code approach manages account baselines?",
             "context": "IaC enables version-controlled, repeatable infrastructure. AFT uses Terraform while alternatives include CloudFormation StackSets.",
             "risk": "medium", "options": ["No IaC - manual console configuration", "Partial IaC with significant manual work", "CloudFormation StackSets with manual updates", "Terraform with remote state and basic CI/CD", "GitOps with AFT, automated testing, PR-based deployments"]},
            {"id": "CT-ACC-006", "question": "How is the account request and approval workflow managed?",
             "context": "Well-defined request workflows ensure governance while enabling agility. Integration with ITSM provides audit trails.",
             "risk": "medium", "options": ["No process - requests via email/ad-hoc", "Basic ticketing with manual routing", "ITSM workflow with defined approvers and SLAs", "Automated routing based on request type", "Self-service portal with pre-approved patterns"]},
        ]
    },
    "Guardrails & Service Control Policies": {
        "weight": 0.12, "pillars": ["SEC", "OPS"],
        "description": "SCP implementation, Control Tower guardrail strategy, and preventive control maturity.",
        "questions": [
            {"id": "CT-GRD-001", "question": "What is your current Service Control Policy (SCP) implementation maturity?",
             "context": "SCPs are the primary mechanism for preventive guardrails. Control Tower deploys mandatory SCPs but organizations need custom policies.",
             "risk": "critical", "options": ["No SCPs beyond default FullAWSAccess", "Basic deny policies (root usage, leave organization)", "Security guardrails (region restriction, service protection)", "Comprehensive OU-specific with documented exceptions", "Enterprise SCP framework with version control and CI/CD testing"]},
            {"id": "CT-GRD-002", "question": "How are SCPs tested before production deployment?",
             "context": "SCP mistakes can cause organization-wide outages. Testing in sandbox OUs and using Policy Simulator are essential.",
             "risk": "high", "options": ["Direct deployment without testing", "Manual peer review only", "Sandbox OU testing before deployment", "Policy Simulator plus sandbox with test cases", "CI/CD pipeline with syntax checking and gradual rollout"]},
            {"id": "CT-GRD-003", "question": "What categories of controls are enforced through SCPs?",
             "context": "SCPs can enforce security, compliance, cost control, and operational standards across the organization.",
             "risk": "high", "options": ["None or allow-all only", "Region and basic service restrictions", "Comprehensive security controls and encryption requirements", "Security + compliance + cost controls", "Full coverage including network, tagging, and resource configuration"]},
            {"id": "CT-GRD-004", "question": "What is your strategy for enabling Control Tower guardrails?",
             "context": "Control Tower provides mandatory, strongly recommended, and elective guardrails. The appropriate mix depends on risk tolerance.",
             "risk": "high", "options": ["Mandatory guardrails only", "Mandatory plus select strongly recommended", "All strongly recommended across all OUs", "Selective elective based on risk assessment", "Comprehensive plus custom controls for organization needs"]},
            {"id": "CT-GRD-005", "question": "How are guardrail violations detected and remediated?",
             "context": "Detective guardrails identify non-compliant resources. Organizations need processes to handle violations with proper SLAs.",
             "risk": "high", "options": ["No monitoring - discovered during audits", "Periodic manual dashboard review", "Automated alerting with severity prioritization", "Ticketing integration with SLAs and escalation", "Auto-remediation with exception workflow"]},
            {"id": "CT-GRD-006", "question": "How is SCP versioning and change history managed?",
             "context": "SCPs require change management and rollback capabilities. Version control enables audit trails and recovery.",
             "risk": "medium", "options": ["No versioning - direct edits", "Manual documentation of changes", "Git-based version control", "Full change history with rollback capability", "GitOps with automated deployment and testing"]},
            {"id": "CT-GRD-007", "question": "What approach exists for custom Control Tower controls?",
             "context": "AWS-provided guardrails cover common requirements but organizations often have custom needs for industry regulations.",
             "risk": "medium", "options": ["No custom controls planned", "Future consideration without plan", "Requirements documented without implementation", "Key custom controls via Config rules", "Comprehensive custom framework with CI/CD"]},
        ]
    },
    "Detective Controls & Compliance": {
        "weight": 0.10, "pillars": ["SEC", "OPS"],
        "description": "AWS Config, Security Hub, compliance framework alignment, and evidence collection.",
        "questions": [
            {"id": "CT-DET-001", "question": "What is your AWS Config deployment and rule coverage?",
             "context": "AWS Config is foundational for Control Tower detective controls, recording configurations and enabling compliance assessment.",
             "risk": "critical", "options": ["Not enabled or few accounts only", "Partial deployment without aggregation", "Organization-wide via Control Tower with basic aggregator", "Aggregator plus custom rules for organization needs", "Conformance packs with auto-remediation"]},
            {"id": "CT-DET-002", "question": "How is AWS Config data aggregated and analyzed?",
             "context": "Centralized Config aggregation is essential for organization-wide visibility. Delegated administrator reduces management account usage.",
             "risk": "high", "options": ["No aggregation - data in individual accounts", "Manual periodic collection", "Organization aggregator in management account", "Delegated administrator with advanced queries", "Analytics platform with ML anomaly detection"]},
            {"id": "CT-DET-003", "question": "What is your AWS Security Hub deployment status?",
             "context": "Security Hub aggregates findings from AWS services and third-party tools. It's the primary dashboard for security posture.",
             "risk": "critical", "options": ["Not enabled or few accounts", "Partial deployment without aggregation", "Organization-wide with AWS Foundational Security", "Multiple standards (FSBP, CIS, PCI-DSS)", "Custom insights plus third-party integrations"]},
            {"id": "CT-DET-004", "question": "How are Security Hub findings triaged and remediated?",
             "context": "Without proper triage, teams become overwhelmed and critical findings get missed. Integration with ticketing enables tracking.",
             "risk": "high", "options": ["No triage - console checked during audits", "Periodic manual review", "Automated alerting for critical findings", "Ticketing integration with SLAs by severity", "Auto-remediation with exception workflow"]},
            {"id": "CT-DET-005", "question": "What compliance frameworks apply to your AWS environment?",
             "context": "Compliance requirements drive guardrail selection, evidence collection, and audit processes.",
             "risk": "critical", "options": ["None - internal policies only", "Internal security policies without certification", "Single framework (e.g., SOC 2)", "Multiple frameworks with mapped controls", "Complex multi-framework with automated mapping"]},
            {"id": "CT-DET-006", "question": "How is compliance evidence collected for audits?",
             "context": "Auditors require evidence of control effectiveness. Manual collection is time-consuming. AWS Audit Manager automates collection.",
             "risk": "high", "options": ["Ad-hoc during audits", "Manual screenshots in shared drives", "Periodic exports with organized repository", "AWS Audit Manager with assessment reports", "GRC platform with continuous monitoring"]},
        ]
    },
    "Identity & Access Management": {
        "weight": 0.10, "pillars": ["SEC"],
        "description": "Identity federation, IAM Identity Center readiness, permission management, and privileged access.",
        "questions": [
            {"id": "CT-IAM-001", "question": "What is your current identity management approach for AWS access?",
             "context": "Control Tower strongly recommends IAM Identity Center for centralized identity. Legacy IAM users or SAML need migration.",
             "risk": "critical", "options": ["Local IAM users per account", "Partial federation - inconsistent approach", "IAM Identity Center with single identity source", "Full IdP integration (Okta, Azure AD) with automated provisioning", "SCIM plus JIT provisioning with ABAC"]},
            {"id": "CT-IAM-002", "question": "Which identity provider will integrate with IAM Identity Center?",
             "context": "Identity Center supports external IdPs with SCIM for automated user provisioning. Choice impacts implementation complexity.",
             "risk": "high", "options": ["Native Identity Center directory", "Active Directory Connector", "Azure AD with SCIM", "Okta with SCIM", "Multiple IdPs for different populations"]},
            {"id": "CT-IAM-003", "question": "How is multi-factor authentication (MFA) enforced?",
             "context": "MFA prevents unauthorized access from compromised credentials. Enterprise best practice extends to all human access.",
             "risk": "critical", "options": ["No MFA requirement", "Encouraged but not enforced", "Required for console access only", "Required for all human access (console + CLI)", "Hardware MFA for privileged accounts and root users"]},
            {"id": "CT-IAM-004", "question": "How are IAM Identity Center permission sets designed?",
             "context": "Well-designed permission sets follow least privilege and are modular for reuse. Complex custom policies increase burden.",
             "risk": "high", "options": ["Not using Identity Center", "AWS managed policies only", "Custom inline policies per set", "Modular managed policies version controlled", "ABAC-enabled with dynamic permissions"]},
            {"id": "CT-IAM-005", "question": "How is least privilege enforced and maintained?",
             "context": "Permissions accumulate over time. Without active enforcement, users have far more access than needed.",
             "risk": "high", "options": ["No enforcement - broad permissions", "Annual manual reviews", "Access Analyzer with manual review", "Quarterly right-sizing with documented process", "Continuous automated analysis and JIT access"]},
            {"id": "CT-IAM-006", "question": "How is privileged access managed and controlled?",
             "context": "Privileged access requires additional controls. Zero standing privilege reduces blast radius of compromised credentials.",
             "risk": "critical", "options": ["No distinction - similar access levels", "Separate privileged accounts always available", "JIT for some operations with manual approval", "PAM solution with session recording", "Zero standing privilege with full audit trail"]},
            {"id": "CT-IAM-007", "question": "How are machine/service identities managed?",
             "context": "Workload identity should use IAM roles, not long-lived access keys. Roles Anywhere extends to on-premises and hybrid.",
             "risk": "high", "options": ["Long-lived access keys", "Some IAM roles for AWS workloads", "Role chaining for cross-account", "Roles Anywhere for hybrid workloads", "Short-lived credentials only with automated rotation"]},
            {"id": "CT-IAM-008", "question": "How are cross-account access roles managed?",
             "context": "Multi-account architectures require cross-account roles for shared services, deployment, and security.",
             "risk": "medium", "options": ["Manual role creation per account", "StackSets for role deployment", "Centralized IaC for cross-account roles", "Role vending machine with self-service", "Automated trust relationship management"]},
        ]
    },
    "Network Architecture": {
        "weight": 0.09, "pillars": ["SEC", "REL", "PERF"],
        "description": "Multi-account network topology, connectivity, security controls, and hybrid architecture.",
        "questions": [
            {"id": "CT-NET-001", "question": "What is your multi-account network architecture?",
             "context": "Hub-spoke with Transit Gateway is recommended for most enterprises, providing centralized connectivity and inspection.",
             "risk": "high", "options": ["Independent VPCs per account", "VPC peering for selected accounts", "Transit Gateway with basic routing", "Hub-spoke with shared services and centralized egress", "Advanced multi-TGW with Network Firewall inspection"]},
            {"id": "CT-NET-002", "question": "How is IP address management handled across accounts?",
             "context": "IP conflicts prevent VPC connectivity. AWS VPC IPAM provides centralized management with automated allocation.",
             "risk": "high", "options": ["No IPAM - ad-hoc with conflicts", "Spreadsheet tracking with manual coordination", "AWS VPC IPAM with defined pools", "Automated IPAM with account provisioning integration", "Enterprise IPAM integration (Infoblox, BlueCat)"]},
            {"id": "CT-NET-003", "question": "What is your VPC design pattern standard?",
             "context": "Consistent VPC design enables automation and reduces troubleshooting. Blueprints with IaC ensure reproducibility.",
             "risk": "medium", "options": ["No standard - inconsistent designs", "Basic guidelines loosely followed", "Standard multi-AZ design documented", "Standardized with blueprints and validation", "Full IaC blueprints with automated provisioning"]},
            {"id": "CT-NET-004", "question": "What is your on-premises connectivity architecture?",
             "context": "Hybrid connectivity is essential during migration. Direct Connect provides consistent performance; VPN provides backup.",
             "risk": "high", "options": ["No on-premises connectivity needed", "Per-account VPN connections", "Centralized VPN via Transit Gateway", "Direct Connect with VPN backup", "Redundant Direct Connect with automated failover"]},
            {"id": "CT-NET-005", "question": "How is hybrid DNS resolution handled?",
             "context": "Route 53 Resolver endpoints enable bi-directional DNS. Centralized architecture reduces complexity.",
             "risk": "medium", "options": ["No hybrid DNS resolution", "Manual forwarding rules per account", "Route 53 Resolver outbound endpoints", "Centralized Resolver with RAM sharing", "Full bi-directional with Private Hosted Zones"]},
            {"id": "CT-NET-006", "question": "How is network traffic inspection implemented?",
             "context": "Defense in depth requires inspection beyond security groups. AWS Network Firewall enables stateful inspection.",
             "risk": "high", "options": ["Security groups and NACLs only", "Third-party perimeter firewall only", "Network Firewall for critical workloads", "Centralized inspection VPC for all traffic", "Full IDS/IPS with threat intelligence integration"]},
            {"id": "CT-NET-007", "question": "How is egress traffic controlled and monitored?",
             "context": "Uncontrolled egress risks data exfiltration. Centralized proxy enables URL filtering and DLP integration.",
             "risk": "critical", "options": ["No controls - NAT Gateways per VPC", "Centralized NAT with VPC Flow Logs", "Basic proxy with URL categorization", "Full proxy plus Network Firewall for all protocols", "Zero-trust egress with DLP and certificate inspection"]},
        ]
    },
    "Logging & Security Operations": {
        "weight": 0.09, "pillars": ["OPS", "SEC", "REL"],
        "description": "Centralized logging, monitoring, alerting, and security operations integration.",
        "questions": [
            {"id": "CT-LOG-001", "question": "What is your CloudTrail configuration?",
             "context": "CloudTrail is foundational for security and compliance. Control Tower creates an organization trail automatically.",
             "risk": "critical", "options": ["Incomplete coverage with gaps", "Account-level trails stored locally", "Organization trail with management events", "Organization trail with data events for critical resources", "CloudTrail Lake with Insights for anomaly detection"]},
            {"id": "CT-LOG-002", "question": "How are VPC Flow Logs managed across accounts?",
             "context": "Flow Logs provide network visibility for security and troubleshooting. Centralized collection enables correlation.",
             "risk": "high", "options": ["Not enabled consistently", "Partial coverage stored locally", "All VPCs with centralized storage", "Centralized with CloudWatch Insights analysis", "Real-time analysis with Traffic Mirroring for sensitive workloads"]},
            {"id": "CT-LOG-003", "question": "What is your log retention and lifecycle strategy?",
             "context": "Retention must balance compliance requirements with cost. S3 lifecycle policies automate tiering.",
             "risk": "medium", "options": ["No defined policy - default retention", "Basic retention without lifecycle", "S3 lifecycle policies for hot/warm tiers", "Tiered with Glacier for long-term", "Compliance-driven with legal hold capability"]},
            {"id": "CT-LOG-004", "question": "How are logs correlated and analyzed?",
             "context": "Security investigations require correlation across CloudTrail, Flow Logs, and application logs. SIEM enables automation.",
             "risk": "high", "options": ["Manual isolated review", "Manual correlation during investigations", "CloudWatch Logs Insights queries", "SIEM integration with correlation rules", "Advanced analytics with ML threat detection"]},
            {"id": "CT-LOG-005", "question": "What is your CloudWatch monitoring configuration?",
             "context": "Cross-account observability provides centralized visibility. X-Ray and ServiceLens add application performance insight.",
             "risk": "medium", "options": ["Default metrics only per account", "Some custom metrics inconsistently", "Cross-account access with central dashboards", "Centralized observability account", "Full APM with X-Ray and ServiceLens"]},
            {"id": "CT-LOG-006", "question": "What is your alerting and incident response strategy?",
             "context": "Effective alerting requires threshold tuning to reduce noise. Integration with incident management enables automation.",
             "risk": "medium", "options": ["No automated alerting", "Email alerts with high noise", "SNS to Slack/PagerDuty with basic routing", "Tiered severity with SLAs and runbooks", "AIOps with automated remediation"]},
        ]
    },
    "Cost Management & FinOps": {
        "weight": 0.07, "pillars": ["COST", "OPS"],
        "description": "Cost visibility, allocation, optimization, and FinOps maturity.",
        "questions": [
            {"id": "CT-FIN-001", "question": "What is your cost visibility across AWS accounts?",
             "context": "Multi-account environments require consolidated visibility. FinOps platforms provide advanced capabilities.",
             "risk": "medium", "options": ["Per-account billing without consolidation", "Consolidated billing with basic Cost Explorer", "Cost Explorer advanced with anomaly detection", "CUR with Athena for detailed analysis", "FinOps platform with automated recommendations"]},
            {"id": "CT-FIN-002", "question": "How are costs allocated to business units?",
             "context": "Cost allocation enables accountability. Tagging is primary mechanism but requires enforcement.",
             "risk": "medium", "options": ["No allocation - central IT budget", "Account-based allocation only", "Partial tagging with manual gap-filling", "Comprehensive enforced tagging with shared cost rules", "Full FinOps with showback/chargeback automation"]},
            {"id": "CT-FIN-003", "question": "How are budgets and forecasting managed?",
             "context": "AWS Budgets enable proactive cost management. Integration with provisioning ensures controls from day one.",
             "risk": "medium", "options": ["No budgets configured", "Organization-level budget only", "Account-level budgets with alerts", "Granular budgets with automated deployment", "ML-based anomaly detection and forecasting"]},
            {"id": "CT-FIN-004", "question": "How are Reserved Instances and Savings Plans managed?",
             "context": "Commitment-based discounts reduce costs 30-72%. Centralized management enables organizational benefit sharing.",
             "risk": "medium", "options": ["No commitments - all on-demand", "Reactive occasional purchases", "Periodic coverage review with manual decisions", "Optimized coverage with benefit sharing", "Automated recommendations with continuous optimization"]},
            {"id": "CT-FIN-005", "question": "What optimization recommendations processes exist?",
             "context": "AWS provides recommendations through Trusted Advisor and Compute Optimizer. Actioning requires process.",
             "risk": "low", "options": ["None - no optimization review", "Ad-hoc review when issues arise", "Periodic Trusted Advisor review", "Compute Optimizer integration with rightsizing", "Automated implementation for approved changes"]},
        ]
    },
    "Backup & Disaster Recovery": {
        "weight": 0.07, "pillars": ["REL", "SEC"],
        "description": "Backup strategy, policy enforcement, testing, and disaster recovery readiness.",
        "questions": [
            {"id": "CT-BDR-001", "question": "How is backup managed across accounts?",
             "context": "AWS Backup enables centralized management. Cross-account vaults protect against ransomware.",
             "risk": "critical", "options": ["No consistent strategy - team dependent", "Per-account management inconsistent", "AWS Backup per account with policies", "Centralized policies via Organizations", "Organization-wide with cross-account vault"]},
            {"id": "CT-BDR-002", "question": "How is backup policy compliance enforced?",
             "context": "Backup policies are ineffective if workloads can opt out. SCPs can require backup configurations.",
             "risk": "high", "options": ["No enforcement - backups optional", "Documentation only without verification", "Config rules for detection", "Mandatory with compliance dashboards", "Preventive SCPs with automated assignment"]},
            {"id": "CT-BDR-003", "question": "How frequently are backup restores tested?",
             "context": "Backups are useless if they can't be restored. Regular testing validates integrity and procedures.",
             "risk": "high", "options": ["Never tested", "Ad-hoc during incidents only", "Annual for critical systems", "Quarterly automated with documentation", "Continuous validation with DR drills"]},
            {"id": "CT-BDR-004", "question": "What is your multi-region DR strategy?",
             "context": "DR strategy depends on RTO/RPO requirements. Active-active provides near-zero RTO but highest complexity.",
             "risk": "high", "options": ["Single region only", "Backup to secondary region", "Pilot light with manual scaling", "Warm standby with automated failover", "Active-active with automatic routing"]},
            {"id": "CT-BDR-005", "question": "How is Control Tower resilience addressed?",
             "context": "Control Tower runs in home region. Organizations should document procedures and maintain IaC for configurations.",
             "risk": "high", "options": ["Not considered", "Documented manual procedures", "IaC backup of customizations", "Automated recovery with monitoring", "Full DR tested with regular drills"]},
        ]
    },
    "Migration Readiness": {
        "weight": 0.07, "pillars": ["OPS", "REL"],
        "description": "Existing account inventory, enrollment prerequisites, and migration planning.",
        "questions": [
            {"id": "CT-MIG-001", "question": "How complete is your existing AWS account inventory?",
             "context": "Control Tower enrollment requires understanding existing accounts. Shadow IT may have created unknown accounts.",
             "risk": "high", "options": ["Unknown account count - possible shadow IT", "Partial list with gaps", "Complete list with limited metadata", "Detailed inventory with ownership and dependencies", "Dynamic automated inventory with CMDB integration"]},
            {"id": "CT-MIG-002", "question": "What is your total AWS account count?",
             "context": "Account count impacts enrollment timeline. Large organizations (500+) may need custom tooling.",
             "risk": "high", "options": ["Unknown", "1-25 accounts (straightforward)", "26-100 accounts (phased approach)", "101-500 accounts (significant planning)", "500+ accounts (major program)"]},
            {"id": "CT-MIG-003", "question": "How prevalent are non-standard configurations?",
             "context": "Non-standard configurations (existing Config, CloudTrail) can conflict with Control Tower enrollment.",
             "risk": "high", "options": ["Unknown - not assessed", "Many non-standard likely to conflict", "Some identified with unclear scope", "Few exceptions documented with plan", "All standards-compliant and ready"]},
            {"id": "CT-MIG-004", "question": "Have accounts been assessed for enrollment prerequisites?",
             "context": "Control Tower has specific prerequisites. Pre-flight assessment identifies blockers before enrollment.",
             "risk": "critical", "options": ["No assessment performed", "Partial assessment only", "Full assessment with blockers identified", "Most ready with remediation in progress", "All verified ready with pre-flight passed"]},
            {"id": "CT-MIG-005", "question": "Are there Config Recorder or CloudTrail conflicts?",
             "context": "Control Tower creates its own Config Recorder and trail. Existing configurations must be resolved.",
             "risk": "critical", "options": ["Unknown status", "Many conflicts exist", "Conflicts identified with plan developing", "Most resolved with few remaining", "All clear and ready"]},
            {"id": "CT-MIG-006", "question": "What approach exists for accounts that cannot be enrolled?",
             "context": "Some accounts may not be enrollable. Legacy account strategy ensures consistent governance.",
             "risk": "medium", "options": ["No approach defined", "To be determined during implementation", "Identified with documented rationale", "Legacy governance plan developed", "Comprehensive strategy with monitoring"]},
        ]
    },
    "Operational Readiness": {
        "weight": 0.05, "pillars": ["OPS"],
        "description": "Team skills, operational processes, runbooks, and change management.",
        "questions": [
            {"id": "CT-OPS-001", "question": "What is your team's Control Tower experience level?",
             "context": "Control Tower operations require specific knowledge. Deep expertise enables troubleshooting and customization.",
             "risk": "high", "options": ["No experience", "Documentation/presentation awareness only", "Sandbox hands-on experience", "Production experience elsewhere", "Deep expertise with advanced capabilities"]},
            {"id": "CT-OPS-002", "question": "What training plan exists for Control Tower operations?",
             "context": "Sustainable operations require documented knowledge and trained team members.",
             "risk": "medium", "options": ["No training planned", "Self-paced documentation only", "AWS instructor-led training", "Comprehensive program with workshops", "Certification plus documented knowledge transfer"]},
            {"id": "CT-OPS-003", "question": "How mature are operational runbooks?",
             "context": "Runbooks document standard procedures. SSM Automation enables automated runbooks.",
             "risk": "medium", "options": ["No runbooks - tribal knowledge", "Basic documentation with gaps", "Comprehensive runbooks regularly reviewed", "Integrated with alerts and version controlled", "SSM Automation with self-healing"]},
            {"id": "CT-OPS-004", "question": "What is your incident response process for AWS?",
             "context": "AWS-specific incident response includes escalation to AWS Support and integration with monitoring.",
             "risk": "medium", "options": ["No defined process", "Ad-hoc response", "Documented escalation paths", "Playbooks with automated detection", "Full automation with AWS Support integration"]},
            {"id": "CT-OPS-005", "question": "How will Control Tower changes be managed?",
             "context": "Control Tower changes have organization-wide impact. GitOps provides audit trail and rollback.",
             "risk": "medium", "options": ["No process - direct changes", "Informal team discussion", "Ticket-based with basic approval", "CAB review with rollback plans", "GitOps with automated validation"]},
            {"id": "CT-OPS-006", "question": "What is your Control Tower upgrade approach?",
             "context": "Control Tower releases updates regularly. Systematic approach ensures stability with access to new features.",
             "risk": "medium", "options": ["No strategy defined", "Upgrade only when issues arise", "Monitor releases with periodic updates", "Scheduled testing before production", "Automated validation with staged rollout"]},
        ]
    },
    "Data Protection": {
        "weight": 0.05, "pillars": ["SEC"],
        "description": "Encryption strategy, key management, and data classification.",
        "questions": [
            {"id": "CT-DAT-001", "question": "What is your encryption-at-rest strategy?",
             "context": "Encryption protects data if storage is compromised. Customer managed keys provide more control.",
             "risk": "critical", "options": ["Not required - service defaults only", "AWS managed keys (SSE-S3)", "Customer managed KMS keys per account", "Centralized key management cross-account", "Enterprise hierarchy with multi-region and HSM"]},
            {"id": "CT-DAT-002", "question": "How is KMS managed across accounts?",
             "context": "Multi-account environments need KMS strategy for key sharing and lifecycle management.",
             "risk": "high", "options": ["No strategy - ad-hoc keys", "Per-account keys without sharing", "Some cross-account via key policies", "Centralized key management account with RAM", "Automated management with rotation"]},
            {"id": "CT-DAT-003", "question": "Does your organization have a data classification framework?",
             "context": "Classification enables appropriate protection levels. Technical controls should map to classifications.",
             "risk": "high", "options": ["No classification defined", "Basic framework with limited enforcement", "Classification with handling procedures", "Technical controls mapped to classifications", "Automated DLP with continuous discovery"]},
            {"id": "CT-DAT-004", "question": "How is sensitive data discovered and protected?",
             "context": "Macie provides automated sensitive data discovery for S3. Custom identifiers enable organization-specific detection.",
             "risk": "high", "options": ["No discovery process", "Manual identification only", "Macie for S3 discovery", "Macie with custom identifiers", "Comprehensive DLP integration"]},
        ]
    },
}

# =============================================================================
# GOLDEN ARCHITECTURE (SERVERLESS) - 10 DOMAINS, 55+ QUESTIONS
# =============================================================================
GA_QUESTIONS = {
    "Serverless Compute Strategy": {
        "weight": 0.12, "pillars": ["PERF", "COST", "OPS"],
        "description": "Lambda adoption, runtime management, Fargate usage, and compute decision frameworks.",
        "questions": [
            {"id": "GA-CMP-001", "question": "What is your Lambda adoption and standardization maturity?",
             "context": "Lambda-first strategies prioritize serverless for new workloads. Standardization covers runtime selection, layers, and patterns.",
             "risk": "medium", "options": ["No Lambda usage", "Experimental POCs only", "Production for specific use cases", "Significant usage with Lambda-default policy", "Lambda-first with comprehensive patterns library"]},
            {"id": "GA-CMP-002", "question": "How are Lambda functions organized and discovered?",
             "context": "At scale, function organization becomes critical. Domain-driven design aligns functions with business capabilities.",
             "risk": "medium", "options": ["Ad-hoc naming without organization", "Naming conventions inconsistently applied", "Consistent naming with application grouping", "Domain-driven organization with service discovery", "Full service mesh with dependency mapping"]},
            {"id": "GA-CMP-003", "question": "How is Lambda runtime management handled?",
             "context": "Runtime deprecation requires migration planning. Containers provide more control but add complexity.",
             "risk": "medium", "options": ["Default runtimes without management", "Standard runtimes defined", "Versioning with deprecation tracking", "Automated runtime updates in CI/CD", "Custom containers with full control"]},
            {"id": "GA-CMP-004", "question": "How are Lambda cold starts managed?",
             "context": "Cold starts impact user experience. Provisioned Concurrency eliminates cold starts; SnapStart helps Java.",
             "risk": "low", "options": ["Not considered - discovered in production", "Awareness without mitigation", "Basic optimizations (package size, runtime)", "Provisioned Concurrency for critical functions", "Comprehensive strategy with SnapStart and warming"]},
            {"id": "GA-CMP-005", "question": "What is your Lambda layers strategy?",
             "context": "Layers enable shared code and dependencies. Versioning prevents breaking changes.",
             "risk": "low", "options": ["No layers used", "Some layers without management", "Standard layers for common dependencies", "Versioned layers with CI/CD", "Automated layer updates with testing"]},
            {"id": "GA-CMP-006", "question": "What is your Fargate adoption level?",
             "context": "Fargate provides serverless containers for workloads exceeding Lambda limits. Spot provides cost savings.",
             "risk": "medium", "options": ["No Fargate - EC2 or no containers", "Experimental usage", "Specific workloads in production", "Default for containers with Spot integration", "Full serverless container strategy"]},
            {"id": "GA-CMP-007", "question": "Do you have a Lambda vs Fargate vs EC2 decision framework?",
             "context": "Each compute option has trade-offs. Clear frameworks ensure optimal choices and consistent architecture.",
             "risk": "medium", "options": ["No framework - ad-hoc decisions", "Informal guidelines", "Documented decision tree for reviews", "Comprehensive with cost modeling", "Automated recommendations with optimization"]},
        ]
    },
    "API & Integration Layer": {
        "weight": 0.10, "pillars": ["PERF", "SEC", "REL"],
        "description": "API Gateway patterns, EventBridge adoption, and messaging architecture.",
        "questions": [
            {"id": "GA-API-001", "question": "What is your API Gateway architecture?",
             "context": "REST APIs are feature-rich; HTTP APIs cost 70% less. Type selection significantly impacts cost.",
             "risk": "medium", "options": ["No API Gateway usage", "REST API for everything", "HTTP APIs where features sufficient", "Right-sized selection with multi-stage", "Comprehensive with WAF and developer portal"]},
            {"id": "GA-API-002", "question": "How is API versioning managed?",
             "context": "API versioning enables evolution without breaking clients. Strategies include path, header, and stage-based.",
             "risk": "medium", "options": ["No versioning", "URL path versioning only", "Stage-based versioning", "Header-based with documentation", "Comprehensive with sunset policies"]},
            {"id": "GA-API-003", "question": "How are APIs documented?",
             "context": "API documentation enables adoption. OpenAPI specifications enable code generation and testing.",
             "risk": "low", "options": ["No documentation", "Manual often outdated", "OpenAPI specifications maintained", "Auto-generated with internal portal", "Full developer portal with SDKs"]},
            {"id": "GA-API-004", "question": "How is API rate limiting configured?",
             "context": "Rate limiting protects backends and enables fair usage. Usage plans enable API monetization.",
             "risk": "high", "options": ["No rate limiting", "Basic API-level throttling", "Custom per-stage throttling", "Usage plans with API keys", "Dynamic adaptive rate limiting"]},
            {"id": "GA-API-005", "question": "What is your EventBridge adoption level?",
             "context": "EventBridge enables loosely-coupled event-driven architectures. Schema registry provides discovery.",
             "risk": "medium", "options": ["No EventBridge - point-to-point", "Basic default bus usage", "Custom buses with event rules", "Event-driven patterns with schema registry", "Full event mesh with governance"]},
            {"id": "GA-API-006", "question": "How is event schema management handled?",
             "context": "Schema registry enables event discovery and validation. Versioning supports evolution.",
             "risk": "medium", "options": ["No schema management", "Informal documentation", "Schema registry enabled", "Versioning with compatibility checks", "Full governance with evolution policies"]},
            {"id": "GA-API-007", "question": "How are SQS/SNS messaging patterns implemented?",
             "context": "SQS provides reliable queuing; SNS enables pub/sub. FIFO guarantees ordering and exactly-once.",
             "risk": "medium", "options": ["No async messaging", "Basic SQS queues", "Fan-out patterns (SNS to SQS)", "DLQ with retry and visibility tuning", "FIFO with exactly-once processing"]},
        ]
    },
    "Workflow Orchestration": {
        "weight": 0.08, "pillars": ["REL", "OPS"],
        "description": "Step Functions adoption, workflow patterns, and error handling.",
        "questions": [
            {"id": "GA-WRK-001", "question": "What is your Step Functions adoption level?",
             "context": "Step Functions provides visual workflow orchestration. Express workflows suit high-volume, short-duration needs.",
             "risk": "medium", "options": ["No Step Functions", "Experimental usage", "Standard workflows for orchestration", "Standard and Express appropriately", "Express with callbacks and human approval"]},
            {"id": "GA-WRK-002", "question": "How is workflow error handling implemented?",
             "context": "Proper error handling prevents data loss. Saga patterns enable distributed transaction compensation.",
             "risk": "high", "options": ["No error handling", "Basic try-catch", "Retry with exponential backoff", "Fallbacks and error states", "Saga patterns for transactions"]},
            {"id": "GA-WRK-003", "question": "What workflow patterns are implemented?",
             "context": "Step Functions supports sequential, parallel, choice, and map patterns. Human approval enables oversight.",
             "risk": "medium", "options": ["None - Lambda chaining only", "Sequential workflows", "Parallel and choice patterns", "Dynamic map for variable input", "Human approval integration"]},
            {"id": "GA-WRK-004", "question": "How are long-running workflows managed?",
             "context": "Standard workflows can run up to 1 year. Callback patterns enable external system integration.",
             "risk": "medium", "options": ["No long-running workflows", "Standard workflows only", "Callback patterns for external waits", "Wait states with proper timeout handling", "Full async patterns with notifications"]},
        ]
    },
    "Serverless Data Layer": {
        "weight": 0.10, "pillars": ["PERF", "REL", "COST"],
        "description": "DynamoDB patterns, Aurora Serverless usage, and connection management.",
        "questions": [
            {"id": "GA-DAT-001", "question": "What is your DynamoDB adoption level?",
             "context": "DynamoDB excels for key-value and document workloads. Single-table design maximizes efficiency.",
             "risk": "medium", "options": ["No DynamoDB usage", "Specific simple use cases", "Default for appropriate workloads", "Advanced with GSI overloading", "Single-table design patterns"]},
            {"id": "GA-DAT-002", "question": "How is DynamoDB capacity managed?",
             "context": "On-demand suits variable traffic; provisioned with auto-scaling suits predictable workloads. Reserved capacity reduces cost.",
             "risk": "medium", "options": ["Not using DynamoDB", "Provisioned without auto-scaling", "On-demand for all tables", "Right-sized with auto-scaling", "Optimized with reserved capacity"]},
            {"id": "GA-DAT-003", "question": "What DynamoDB design patterns are used?",
             "context": "Access pattern-driven design is key. Single-table with GSI overloading reduces cost and latency.",
             "risk": "medium", "options": ["N/A - not using DynamoDB", "Simple key-value only", "Multiple tables per entity", "Single-table for related data", "Advanced GSI overloading patterns"]},
            {"id": "GA-DAT-004", "question": "How is DynamoDB caching implemented?",
             "context": "DAX provides microsecond latency. ElastiCache Serverless offers flexible caching options.",
             "risk": "low", "options": ["No caching", "Application-level caching", "ElastiCache for specific patterns", "DAX for read-heavy workloads", "Multi-layer caching strategy"]},
            {"id": "GA-DAT-005", "question": "What is your Aurora Serverless usage?",
             "context": "Aurora Serverless v2 scales automatically. Data API eliminates connection management for Lambda.",
             "risk": "medium", "options": ["No Aurora Serverless", "Evaluating for use cases", "Dev/test environments", "Production with scaling config", "Data API for serverless apps"]},
            {"id": "GA-DAT-006", "question": "How are database connections managed from serverless?",
             "context": "Lambda cold starts can exhaust connections. RDS Proxy manages connection pooling. Data API eliminates connections.",
             "risk": "high", "options": ["Direct connections from Lambda", "Lambda pooling patterns", "RDS Proxy for connection management", "RDS Proxy with IAM auth", "Data API - no connections needed"]},
            {"id": "GA-DAT-007", "question": "What serverless analytics approach is used?",
             "context": "Athena provides serverless SQL on S3. Data lake architectures enable comprehensive analytics.",
             "risk": "low", "options": ["No serverless analytics", "Traditional provisioned services", "Athena for ad-hoc queries", "Data lake with Lake Formation", "Comprehensive serverless analytics stack"]},
        ]
    },
    "Serverless Security": {
        "weight": 0.12, "pillars": ["SEC"],
        "description": "Lambda security, secrets management, API protection, and vulnerability management.",
        "questions": [
            {"id": "GA-SEC-001", "question": "How are Lambda execution roles designed?",
             "context": "Each function should have unique minimal permissions. Shared roles create excessive access.",
             "risk": "critical", "options": ["Single shared role for all functions", "Broad roles per application", "Function-specific manually managed", "Least-privilege with Access Analyzer", "Automated with permission boundaries"]},
            {"id": "GA-SEC-002", "question": "How is Lambda code signing implemented?",
             "context": "Code signing ensures only trusted code deploys. Validation can warn or enforce.",
             "risk": "high", "options": ["No code signing", "Evaluating implementation", "Some functions signed", "Validation on deployment", "Mandatory with CI/CD enforcement"]},
            {"id": "GA-SEC-003", "question": "How are Lambda vulnerabilities managed?",
             "context": "Dependencies can introduce vulnerabilities. Inspector provides runtime scanning; CI/CD catches issues early.",
             "risk": "high", "options": ["No vulnerability scanning", "Manual periodic review", "CI/CD scanning for critical issues", "Inspector continuous scanning", "Automated remediation pipeline"]},
            {"id": "GA-SEC-004", "question": "How is secrets management implemented?",
             "context": "Secrets must never be in code or plaintext environment variables. Lambda extensions enable cached retrieval.",
             "risk": "critical", "options": ["Plaintext environment variables", "Encrypted environment variables", "Parameter Store for configuration", "Secrets Manager with rotation", "Lambda extension with caching"]},
            {"id": "GA-SEC-005", "question": "How is secret rotation implemented?",
             "context": "Credential rotation limits exposure window. Secrets Manager provides automated rotation.",
             "risk": "high", "options": ["No rotation", "Manual periodic rotation", "Scheduled rotation reminders", "Automated for some secrets", "Automated for all credentials"]},
            {"id": "GA-SEC-006", "question": "How is API authentication implemented?",
             "context": "APIs require authentication for access control. Cognito handles users; Lambda authorizers enable custom logic.",
             "risk": "critical", "options": ["No authentication - public APIs", "API keys only (not authentication)", "Cognito User Pools", "Lambda authorizers with JWT", "Multi-method with fine-grained authorization"]},
            {"id": "GA-SEC-007", "question": "How is API traffic protected?",
             "context": "APIs are attack targets. WAF protects against OWASP attacks; Shield provides DDoS protection.",
             "risk": "high", "options": ["No protection beyond throttling", "Basic throttling only", "WAF with managed rules", "WAF with custom rules and Shield", "Comprehensive with Bot Control"]},
            {"id": "GA-SEC-008", "question": "How is input validation implemented?",
             "context": "Input validation prevents injection attacks. API Gateway validates structure; application validates logic.",
             "risk": "high", "options": ["No systematic validation", "Basic application validation", "API Gateway request validation", "Schema validation with sanitization", "Defense in depth - WAF, gateway, application"]},
        ]
    },
    "Observability & Monitoring": {
        "weight": 0.08, "pillars": ["OPS", "REL"],
        "description": "Logging, tracing, metrics, and SLO management for serverless.",
        "questions": [
            {"id": "GA-OBS-001", "question": "How is logging structured across serverless apps?",
             "context": "Structured JSON logging enables querying. Lambda Powertools provides standardized patterns.",
             "risk": "medium", "options": ["Console.log - unstructured", "Basic structured with inconsistent format", "JSON with standard fields", "Correlation IDs with Powertools", "Comprehensive with sampling and aggregation"]},
            {"id": "GA-OBS-002", "question": "How are logs aggregated and analyzed?",
             "context": "Centralized aggregation enables cross-function analysis. SIEM integration supports security investigation.",
             "risk": "medium", "options": ["CloudWatch console only", "Logs Insights queries", "Centralized in observability account", "Real-time streaming analysis", "SIEM with ML anomaly detection"]},
            {"id": "GA-OBS-003", "question": "How is distributed tracing implemented?",
             "context": "X-Ray shows request flow across services. Custom segments add business context.",
             "risk": "medium", "options": ["No tracing", "X-Ray for some functions", "X-Ray for all serverless", "Custom segments and annotations", "Full tracing with OpenTelemetry"]},
            {"id": "GA-OBS-004", "question": "How are custom metrics captured?",
             "context": "AWS provides default Lambda metrics. EMF enables efficient custom metric publishing.",
             "risk": "medium", "options": ["Default metrics only", "Some custom with PutMetric", "Business metrics via EMF", "Comprehensive with dashboards", "Real-time with anomaly detection"]},
            {"id": "GA-OBS-005", "question": "What serverless dashboards exist?",
             "context": "Dashboards provide operational visibility. Service-level views enable quick issue identification.",
             "risk": "low", "options": ["No dashboards", "Basic Lambda console", "Application-specific dashboards", "Service dashboards with SLIs", "Comprehensive with drill-down"]},
            {"id": "GA-OBS-006", "question": "Are SLOs defined and tracked?",
             "context": "SLOs define reliability targets. Error budgets enable data-driven decisions.",
             "risk": "medium", "options": ["No SLOs defined", "Informal targets", "Key SLIs tracked", "SLOs with error budgets", "Comprehensive with automated actions"]},
        ]
    },
    "CI/CD & DevOps": {
        "weight": 0.08, "pillars": ["OPS"],
        "description": "Deployment automation, testing strategies, and DevOps practices.",
        "questions": [
            {"id": "GA-DEV-001", "question": "What is your serverless deployment approach?",
             "context": "SAM and CDK simplify Lambda deployment. GitOps provides automated, auditable deployments.",
             "risk": "medium", "options": ["Manual console deployments", "CLI-based with scripts", "SAM or Serverless Framework", "CDK with multi-environment", "Full GitOps with automation"]},
            {"id": "GA-DEV-002", "question": "How is Infrastructure as Code implemented?",
             "context": "IaC enables repeatable infrastructure. Testing and security scanning improve quality.",
             "risk": "medium", "options": ["No IaC - manual configuration", "Partial IaC coverage", "Full IaC with basic CI/CD", "IaC with linting and testing", "Security scanning integrated"]},
            {"id": "GA-DEV-003", "question": "What deployment strategies are used?",
             "context": "All-at-once risks widespread outages. Canary deployments reduce blast radius.",
             "risk": "high", "options": ["All-at-once deployments", "Manual staged rollout", "Blue-green with manual shift", "Canary with CloudWatch alarms", "Progressive with automated rollback"]},
            {"id": "GA-DEV-004", "question": "How is rollback handled?",
             "context": "Quick rollback minimizes impact. Lambda aliases enable instant traffic shifting.",
             "risk": "high", "options": ["No rollback capability", "Manual redeployment", "Automated version rollback", "Aliases for instant rollback", "Blast radius limitation with feature flags"]},
            {"id": "GA-DEV-005", "question": "How comprehensive is serverless testing?",
             "context": "Serverless testing includes unit, integration, and local testing. SAM Local and LocalStack simulate AWS.",
             "risk": "high", "options": ["No automated testing", "Unit tests only", "Unit plus integration", "Comprehensive with local environment", "Full pyramid with chaos engineering"]},
            {"id": "GA-DEV-006", "question": "How is local development handled?",
             "context": "Deploying to AWS for every change slows development. Local tooling accelerates iteration.",
             "risk": "low", "options": ["Deploy to AWS for all testing", "Limited mocking", "SAM Local for Lambda", "LocalStack for AWS simulation", "Comprehensive local development environment"]},
        ]
    },
    "Cost Optimization": {
        "weight": 0.06, "pillars": ["COST"],
        "description": "Serverless cost visibility, optimization, and efficiency.",
        "questions": [
            {"id": "GA-CST-001", "question": "What is your serverless cost visibility?",
             "context": "Serverless costs can be difficult to attribute. Per-invocation understanding enables optimization.",
             "risk": "medium", "options": ["No tracking - aggregate bill only", "Service-level visibility", "Function-level with tagging", "Per-application dashboards with alerts", "Per-invocation cost analysis"]},
            {"id": "GA-CST-002", "question": "How is cost anomaly detection implemented?",
             "context": "Unexpected cost spikes can indicate misconfiguration or attack. Early detection prevents budget impact.",
             "risk": "medium", "options": ["No anomaly detection", "Manual bill review", "AWS Cost Anomaly Detection", "Custom thresholds with alerts", "Auto-remediation for anomalies"]},
            {"id": "GA-CST-003", "question": "How is Lambda memory optimization performed?",
             "context": "Lambda pricing depends on memory and duration. Power Tuning finds optimal configuration.",
             "risk": "low", "options": ["Default memory settings", "Manual one-time testing", "Power Tuning for critical functions", "Regular optimization cycles", "Automated continuous optimization"]},
            {"id": "GA-CST-004", "question": "How is unused resource cleanup managed?",
             "context": "Orphaned resources accumulate cost. Automated cleanup prevents waste.",
             "risk": "low", "options": ["No cleanup process", "Manual periodic review", "Reporting of unused resources", "Scheduled cleanup jobs", "Automated with approval for production"]},
            {"id": "GA-CST-005", "question": "What is your Graviton (ARM) utilization?",
             "context": "Graviton2 provides 20% better price-performance for most workloads. Lambda supports ARM.",
             "risk": "low", "options": ["Not aware of Graviton", "Evaluating for use cases", "Some workloads on Graviton", "Default for new workloads", "Comprehensive adoption with optimization"]},
        ]
    },
    "Resilience & Reliability": {
        "weight": 0.10, "pillars": ["REL"],
        "description": "Fault tolerance patterns, retry logic, idempotency, and multi-region.",
        "questions": [
            {"id": "GA-REL-001", "question": "How is error handling and retry logic implemented?",
             "context": "Serverless apps must handle transient failures. Circuit breakers prevent cascade failures.",
             "risk": "high", "options": ["No systematic error handling", "Default Lambda retries only", "Custom retry with backoff", "Circuit breakers and DLQs", "Full patterns with bulkheads and fallbacks"]},
            {"id": "GA-REL-002", "question": "How is dead-letter queue handling implemented?",
             "context": "DLQs capture failed events for analysis. Reprocessing enables recovery without data loss.",
             "risk": "medium", "options": ["No DLQ configuration", "DLQ for some functions", "DLQ for all async operations", "Monitoring and alerting on DLQ", "Automated reprocessing pipeline"]},
            {"id": "GA-REL-003", "question": "How is idempotency implemented?",
             "context": "Serverless platforms may invoke functions multiple times. Idempotency ensures repeated invocations are safe.",
             "risk": "high", "options": ["Not considered - duplicates possible", "Awareness without implementation", "Critical operations only", "Idempotency tokens implemented", "Powertools with comprehensive coverage"]},
            {"id": "GA-REL-004", "question": "What is your multi-region strategy for serverless?",
             "context": "Multi-region provides regional failure resilience. DynamoDB Global Tables enable multi-region data.",
             "risk": "high", "options": ["Single region only", "Data replicated to secondary", "Passive with manual failover", "Automated failover with Global Tables", "Active-active with traffic routing"]},
            {"id": "GA-REL-005", "question": "How is global data consistency handled?",
             "context": "Multi-region requires consistency decisions. Eventually consistent is simpler; strong consistency adds complexity.",
             "risk": "high", "options": ["N/A - single region", "Eventually consistent accepted", "Global Tables for replication", "Defined consistency per data type", "Comprehensive with conflict resolution"]},
            {"id": "GA-REL-006", "question": "How is chaos engineering applied to serverless?",
             "context": "Chaos engineering validates resilience assumptions. AWS Fault Injection Simulator enables controlled experiments.",
             "risk": "medium", "options": ["No chaos engineering", "Manual failure testing", "Periodic game days", "FIS for serverless experiments", "Continuous chaos in non-production"]},
        ]
    },
    "Event-Driven Architecture": {
        "weight": 0.06, "pillars": ["REL", "PERF"],
        "description": "Event-driven patterns, async processing, and event sourcing.",
        "questions": [
            {"id": "GA-EVT-001", "question": "What is your event-driven architecture maturity?",
             "context": "Event-driven architecture enables loose coupling and scalability. Mature implementations use event sourcing.",
             "risk": "medium", "options": ["Request-response only", "Some async processing", "Event-driven for appropriate workloads", "Event-first design approach", "Full event sourcing where appropriate"]},
            {"id": "GA-EVT-002", "question": "How is event ordering handled?",
             "context": "Some use cases require ordered processing. SQS FIFO and Kinesis provide ordering guarantees.",
             "risk": "medium", "options": ["Ordering not considered", "Best-effort ordering", "FIFO queues for critical paths", "Kinesis for streaming with order", "Comprehensive ordering strategy"]},
            {"id": "GA-EVT-003", "question": "How is event replay capability implemented?",
             "context": "Event replay enables debugging and recovery. EventBridge Archive provides replay capability.",
             "risk": "medium", "options": ["No replay capability", "Manual log replay", "EventBridge Archive enabled", "Replay with filtering", "Full event sourcing with rebuild"]},
            {"id": "GA-EVT-004", "question": "How is backpressure handled in event processing?",
             "context": "High-volume events can overwhelm consumers. Batching and reserved concurrency provide control.",
             "risk": "medium", "options": ["No backpressure handling", "Default Lambda concurrency", "Reserved concurrency limits", "Batching with batch size tuning", "Comprehensive flow control"]},
        ]
    },
}

# =============================================================================
# APPLICATION LOGIC WITH BUG FIX
# Key fix: Questions only count as answered when user explicitly selects an option
# =============================================================================

def init_state():
    """Initialize session state"""
    if 'initialized' not in st.session_state:
        st.session_state.initialized = True
        st.session_state.ct_responses = {}  # {question_id: score}
        st.session_state.ga_responses = {}
        st.session_state.ai_analysis = None
        st.session_state.org_name = ''
        st.session_state.assessor_name = ''
        st.session_state.industry = 'technology'
        st.session_state.report = None
        st.session_state.pdf_report = None

def count_questions(domains: dict) -> int:
    """Count total questions across all domains"""
    return sum(len(d["questions"]) for d in domains.values())

def count_answered(responses: dict) -> int:
    """Count answered questions - only those with actual responses"""
    return len(responses)

def calc_scores(responses: dict, domains: dict) -> dict:
    """Calculate weighted scores across domains"""
    if not responses:
        return {"overall": 0, "domains": {}, "total_answered": 0, "total_questions": count_questions(domains)}
    
    domain_scores = {}
    for dname, ddata in domains.items():
        total, answered = 0, 0
        for q in ddata["questions"]:
            if q["id"] in responses:
                total += responses[q["id"]]
                answered += 1
        
        score = (total / (answered * 5) * 100) if answered > 0 else 0
        domain_scores[dname] = {
            "score": score,
            "answered": answered,
            "total": len(ddata["questions"]),
            "weight": ddata["weight"]
        }
    
    # Weighted overall
    weighted_sum = sum(d["score"] * d["weight"] for d in domain_scores.values() if d["answered"] > 0)
    weight_sum = sum(d["weight"] for d in domain_scores.values() if d["answered"] > 0)
    overall = weighted_sum / weight_sum if weight_sum > 0 else 0
    
    return {
        "overall": overall,
        "domains": domain_scores,
        "total_answered": sum(d["answered"] for d in domain_scores.values()),
        "total_questions": count_questions(domains)
    }

def get_maturity(score: float) -> tuple:
    """Get maturity level, CSS class, and description"""
    if score >= 80:
        return "Optimized", "success", "Industry-leading with continuous improvement"
    elif score >= 60:
        return "Managed", "warning", "Proactive management with defined processes"
    elif score >= 40:
        return "Developing", "warning", "Emerging practices with inconsistent adoption"
    elif score >= 20:
        return "Initial", "danger", "Ad-hoc processes with limited governance"
    return "Not Assessed", "neutral", "Assessment not yet complete"

def find_gaps(responses: dict, domains: dict) -> list:
    """Find gaps (low scores) prioritized by risk"""
    gaps = []
    for dname, ddata in domains.items():
        for q in ddata["questions"]:
            qid = q["id"]
            if qid in responses and responses[qid] <= 2:
                gaps.append({
                    "id": qid,
                    "domain": dname,
                    "question": q["question"],
                    "context": q.get("context", ""),
                    "score": responses[qid],
                    "risk": q["risk"]
                })
    
    risk_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    return sorted(gaps, key=lambda x: (risk_order.get(x["risk"], 3), -x["score"]))

def handle_response_change(qid: str, responses: dict, options: list):
    """Callback handler for question response changes - KEY BUG FIX"""
    key = f"sel_{qid}"
    if key in st.session_state:
        selected = st.session_state[key]
        if selected == NOT_ANSWERED:
            # Remove from responses if user selects "Not yet assessed"
            responses.pop(qid, None)
        else:
            # Find index (1-5) for the selected option
            try:
                idx = options.index(selected)
                responses[qid] = idx  # 1-5 for actual answers
            except ValueError:
                pass

def render_metric_card(value: float, label: str, suffix: str = "%"):
    """Render a professional metric card"""
    level, level_class, desc = get_maturity(value)
    
    value_class = ""
    if level_class == "success":
        value_class = "success"
    elif level_class == "warning":
        value_class = "warning"
    elif level_class == "danger":
        value_class = "danger"
    
    st.markdown(f'''
    <div class="metric-card">
        <div class="metric-value {value_class}">{value:.0f}{suffix}</div>
        <div class="metric-label">{label}</div>
        <div class="metric-badge badge-{level_class}">{level}</div>
    </div>
    ''', unsafe_allow_html=True)

def render_questions(domains: dict, responses: dict, prefix: str):
    """Render assessment questions with proper state management"""
    for dname, ddata in domains.items():
        answered = sum(1 for q in ddata["questions"] if q["id"] in responses)
        total = len(ddata["questions"])
        pct = (answered / total * 100) if total > 0 else 0
        
        pillars_html = " ".join([f'<span class="pillar-tag pillar-{p}">{WA_PILLARS.get(p, p)}</span>' for p in ddata["pillars"]])
        
        with st.expander(f"📁 {dname} — {answered}/{total} answered ({pct:.0f}%) • Weight: {ddata['weight']*100:.0f}%"):
            st.markdown(f"**{ddata.get('description', '')}**")
            st.markdown(f'<div class="pillar-container">{pillars_html}</div>', unsafe_allow_html=True)
            st.markdown("---")
            
            for q in ddata["questions"]:
                qid = q["id"]
                is_answered = qid in responses
                card_class = "answered" if is_answered else ""
                
                st.markdown(f'''
                <div class="question-card {card_class}">
                    <div class="question-header">
                        <span class="question-id">{qid}</span>
                        <span class="risk-badge risk-{q['risk']}">{q['risk']}</span>
                    </div>
                    <div class="question-text">{q['question']}</div>
                </div>
                ''', unsafe_allow_html=True)
                
                # Show context in expander
                if q.get("context"):
                    with st.expander("💡 Why this matters", expanded=False):
                        st.markdown(f'<div class="question-context">{q["context"]}</div>', unsafe_allow_html=True)
                
                # Build options list with placeholder first
                options = [NOT_ANSWERED] + q["options"]
                
                # Get current selection index
                current_idx = 0
                if qid in responses:
                    current_idx = responses[qid]  # 1-5 maps to index 1-5
                
                # Selectbox with on_change callback
                st.selectbox(
                    f"Select response for {qid}",
                    options=options,
                    index=current_idx,
                    key=f"sel_{qid}",
                    label_visibility="collapsed",
                    on_change=handle_response_change,
                    args=(qid, responses, options)
                )
                
                st.markdown("")  # Spacing

def call_claude(prompt: str) -> str:
    """Call Claude API for AI analysis"""
    try:
        import anthropic
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            return """⚠️ **API Key Required**

To enable AI-powered analysis, add your Anthropic API key:

**Streamlit Cloud:** Go to Settings → Secrets → Add `ANTHROPIC_API_KEY = "sk-ant-..."`

**Local:** Set environment variable `ANTHROPIC_API_KEY`"""
        
        client = anthropic.Anthropic(api_key=api_key)
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=8192,
            system="""You are an expert AWS Solutions Architect with deep expertise in:
- AWS Control Tower implementation and migration
- Serverless architecture patterns and best practices
- AWS Well-Architected Framework
- Enterprise cloud governance and security

Provide detailed, actionable recommendations with:
- Specific AWS services and configurations
- Effort estimates (person-weeks)
- Risk considerations and dependencies
- Prioritized sequencing with quick wins identified
- Success metrics and KPIs""",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text
    except Exception as e:
        return f"⚠️ **Error**: {str(e)}"

# =============================================================================
# CHART GENERATION FUNCTIONS
# =============================================================================

def create_gauge_chart(score, title, size=(4, 3)):
    """Create a beautiful gauge/speedometer chart for scores"""
    fig, ax = plt.subplots(figsize=size, subplot_kw={'projection': 'polar'})
    
    # Colors for different score ranges
    colors_gradient = ['#DC2626', '#EA580C', '#D97706', '#CA8A04', '#65A30D', '#059669']
    
    # Set up the gauge
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_thetamin(0)
    ax.set_thetamax(180)
    
    # Create the background arc segments
    theta_ranges = np.linspace(0, np.pi, 7)
    for i in range(6):
        theta = np.linspace(theta_ranges[i], theta_ranges[i+1], 50)
        r = np.ones_like(theta) * 0.9
        ax.fill_between(theta, 0.6, r, color=colors_gradient[i], alpha=0.3)
    
    # Add the score indicator
    score_angle = np.pi * (1 - score / 100)
    ax.annotate('', xy=(score_angle, 0.85), xytext=(np.pi/2, 0),
                arrowprops=dict(arrowstyle='->', color='#1e293b', lw=3))
    
    # Add score text in center
    ax.text(np.pi/2, 0.25, f'{score:.0f}%', ha='center', va='center', 
            fontsize=24, fontweight='bold', color='#1e293b')
    ax.text(np.pi/2, 0.05, title, ha='center', va='center', 
            fontsize=10, color='#64748b')
    
    # Clean up the chart
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.spines['polar'].set_visible(False)
    
    # Save to buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close(fig)
    buf.seek(0)
    return buf

def create_score_gauges(ct_score, ga_score, combined_score, benchmark):
    """Create a combined gauge chart showing all three scores"""
    fig, axes = plt.subplots(1, 4, figsize=(14, 3.5))
    
    scores = [ct_score, ga_score, combined_score, benchmark]
    titles = ['Control Tower', 'Golden Architecture', 'Combined Score', 'Industry Benchmark']
    main_colors = ['#0284c7', '#7c3aed', '#059669', '#f59e0b']
    
    for ax, score, title, color in zip(axes, scores, titles, main_colors):
        # Create a semi-circular gauge
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-0.2, 1.3)
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Background arc
        theta = np.linspace(np.pi, 0, 100)
        x_bg = np.cos(theta)
        y_bg = np.sin(theta)
        ax.fill(np.append(x_bg, [0]), np.append(y_bg, [0]), color='#e2e8f0', alpha=0.5)
        
        # Score arc
        score_theta = np.linspace(np.pi, np.pi - (np.pi * score / 100), 100)
        x_score = np.cos(score_theta)
        y_score = np.sin(score_theta)
        ax.fill(np.append(x_score, [0]), np.append(y_score, [0]), color=color, alpha=0.8)
        
        # Add gradient effect segments
        for i, (start, end, c) in enumerate([
            (0, 20, '#DC2626'), (20, 40, '#EA580C'), (40, 60, '#D97706'),
            (60, 80, '#65A30D'), (80, 100, '#059669')
        ]):
            seg_start = np.pi - (np.pi * start / 100)
            seg_end = np.pi - (np.pi * end / 100)
            seg_theta = np.linspace(seg_start, seg_end, 20)
            ax.plot(1.1 * np.cos(seg_theta), 1.1 * np.sin(seg_theta), color=c, linewidth=8, alpha=0.6)
        
        # Score text
        ax.text(0, 0.4, f'{score:.0f}%', ha='center', va='center', 
                fontsize=28, fontweight='bold', color='#1e293b')
        ax.text(0, -0.1, title, ha='center', va='center', 
                fontsize=11, fontweight='bold', color='#64748b')
        
        # Maturity label
        if score >= 80:
            maturity = "Optimized"
            mat_color = '#059669'
        elif score >= 60:
            maturity = "Managed"
            mat_color = '#65A30D'
        elif score >= 40:
            maturity = "Developing"
            mat_color = '#D97706'
        elif score >= 20:
            maturity = "Initial"
            mat_color = '#EA580C'
        else:
            maturity = "Not Assessed"
            mat_color = '#64748b'
        
        ax.text(0, 0.15, maturity, ha='center', va='center', 
                fontsize=9, color=mat_color, fontweight='bold')
    
    plt.tight_layout()
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close(fig)
    buf.seek(0)
    return buf

def create_radar_chart(domain_scores, title, color='#0284c7'):
    """Create a radar/spider chart for domain analysis"""
    # Prepare data
    categories = list(domain_scores.keys())
    values = [domain_scores[cat]['score'] for cat in categories]
    
    # Truncate long category names
    categories = [cat[:20] + '...' if len(cat) > 20 else cat for cat in categories]
    
    # Number of variables
    num_vars = len(categories)
    
    # Compute angle for each category
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    values += values[:1]  # Complete the loop
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    
    # Draw the chart
    ax.fill(angles, values, color=color, alpha=0.25)
    ax.plot(angles, values, color=color, linewidth=2, marker='o', markersize=6)
    
    # Add reference circles
    for level in [20, 40, 60, 80, 100]:
        circle_color = '#059669' if level >= 80 else '#65A30D' if level >= 60 else '#D97706' if level >= 40 else '#EA580C' if level >= 20 else '#DC2626'
        ax.plot(angles, [level] * len(angles), color=circle_color, linewidth=0.5, linestyle='--', alpha=0.5)
    
    # Set category labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=8)
    
    # Set radial limits
    ax.set_ylim(0, 100)
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(['20%', '40%', '60%', '80%', '100%'], fontsize=7, color='#64748b')
    
    # Title
    ax.set_title(title, fontsize=14, fontweight='bold', color='#1e293b', pad=20)
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close(fig)
    buf.seek(0)
    return buf

def create_horizontal_bar_chart(domain_scores, title, color='#0284c7'):
    """Create a horizontal bar chart for domain scores"""
    categories = list(domain_scores.keys())
    values = [domain_scores[cat]['score'] for cat in categories]
    
    # Truncate long names
    categories = [cat[:30] + '...' if len(cat) > 30 else cat for cat in categories]
    
    fig, ax = plt.subplots(figsize=(10, max(6, len(categories) * 0.5)))
    
    # Create color gradient based on score
    colors_list = []
    for v in values:
        if v >= 80:
            colors_list.append('#059669')
        elif v >= 60:
            colors_list.append('#65A30D')
        elif v >= 40:
            colors_list.append('#D97706')
        elif v >= 20:
            colors_list.append('#EA580C')
        else:
            colors_list.append('#DC2626')
    
    y_pos = np.arange(len(categories))
    
    # Background bars (100%)
    ax.barh(y_pos, [100] * len(categories), color='#e2e8f0', height=0.6)
    
    # Score bars
    bars = ax.barh(y_pos, values, color=colors_list, height=0.6, alpha=0.85)
    
    # Add value labels
    for i, (bar, val) in enumerate(zip(bars, values)):
        ax.text(val + 2, bar.get_y() + bar.get_height()/2, f'{val:.0f}%', 
                va='center', ha='left', fontsize=10, fontweight='bold', color='#1e293b')
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories, fontsize=9)
    ax.set_xlim(0, 110)
    ax.set_xlabel('Score (%)', fontsize=10, color='#64748b')
    ax.set_title(title, fontsize=14, fontweight='bold', color='#1e293b', pad=15)
    
    # Add vertical lines for reference
    for x in [20, 40, 60, 80]:
        ax.axvline(x=x, color='#cbd5e1', linestyle='--', linewidth=0.5, alpha=0.7)
    
    # Clean up
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('#e2e8f0')
    ax.spines['left'].set_color('#e2e8f0')
    
    plt.tight_layout()
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close(fig)
    buf.seek(0)
    return buf

def create_gap_pie_chart(ct_gaps, ga_gaps):
    """Create a pie chart showing gap distribution by risk level"""
    # Count gaps by risk level
    critical = len([g for g in ct_gaps + ga_gaps if g['risk'] == 'critical'])
    high = len([g for g in ct_gaps + ga_gaps if g['risk'] == 'high'])
    medium = len([g for g in ct_gaps + ga_gaps if g['risk'] == 'medium'])
    
    if critical + high + medium == 0:
        # No gaps - create a "No Gaps" chart
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.text(0.5, 0.5, 'No Gaps\nIdentified', ha='center', va='center', 
                fontsize=20, fontweight='bold', color='#059669', transform=ax.transAxes)
        ax.axis('off')
    else:
        fig, ax = plt.subplots(figsize=(8, 6))
        
        sizes = [critical, high, medium]
        labels = [f'Critical\n({critical})', f'High\n({high})', f'Medium\n({medium})']
        colors_pie = ['#DC2626', '#EA580C', '#D97706']
        explode = (0.05, 0.02, 0)
        
        # Filter out zero values
        non_zero = [(s, l, c, e) for s, l, c, e in zip(sizes, labels, colors_pie, explode) if s > 0]
        if non_zero:
            sizes, labels, colors_pie, explode = zip(*non_zero)
            
            wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors_pie, 
                                               explode=explode, autopct='%1.0f%%',
                                               shadow=True, startangle=90,
                                               textprops={'fontsize': 11, 'fontweight': 'bold'})
            
            for autotext in autotexts:
                autotext.set_color('white')
                autotext.set_fontweight('bold')
        
        ax.set_title('Gap Distribution by Risk Level', fontsize=14, fontweight='bold', 
                    color='#1e293b', pad=20)
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close(fig)
    buf.seek(0)
    return buf

def create_industry_comparison_chart(combined_score, benchmarks, current_industry):
    """Create a bar chart comparing score against industry benchmarks"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    industries = [b['name'] for b in benchmarks.values()]
    averages = [b['avg'] for b in benchmarks.values()]
    top_performers = [b['top'] for b in benchmarks.values()]
    
    x = np.arange(len(industries))
    width = 0.35
    
    # Create bars
    bars1 = ax.bar(x - width/2, averages, width, label='Industry Average', 
                   color='#94a3b8', alpha=0.7)
    bars2 = ax.bar(x + width/2, top_performers, width, label='Top Performers', 
                   color='#64748b', alpha=0.7)
    
    # Add your score line
    ax.axhline(y=combined_score, color='#0284c7', linestyle='-', linewidth=3, 
               label=f'Your Score ({combined_score:.0f}%)')
    
    # Highlight current industry
    current_idx = list(benchmarks.keys()).index(current_industry)
    bars1[current_idx].set_color('#0284c7')
    bars1[current_idx].set_alpha(1.0)
    bars2[current_idx].set_color('#0369a1')
    bars2[current_idx].set_alpha(1.0)
    
    ax.set_ylabel('Score (%)', fontsize=11, color='#64748b')
    ax.set_title('Industry Benchmark Comparison', fontsize=14, fontweight='bold', 
                color='#1e293b', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(industries, rotation=25, ha='right', fontsize=9)
    ax.legend(loc='upper right', fontsize=9)
    ax.set_ylim(0, 100)
    
    # Add value labels on bars
    for bar in bars1:
        height = bar.get_height()
        ax.annotate(f'{height:.0f}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                   xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', 
                   fontsize=8, color='#64748b')
    
    # Clean up
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('#e2e8f0')
    ax.spines['left'].set_color('#e2e8f0')
    ax.yaxis.grid(True, linestyle='--', alpha=0.3)
    
    plt.tight_layout()
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close(fig)
    buf.seek(0)
    return buf

def create_maturity_roadmap_chart():
    """Create a visual roadmap showing maturity phases"""
    fig, ax = plt.subplots(figsize=(12, 5))
    
    phases = ['Phase 1\nFoundation', 'Phase 2\nStandardization', 
              'Phase 3\nOptimization', 'Phase 4\nExcellence']
    timelines = ['0-3 months', '3-6 months', '6-12 months', '12+ months']
    colors_phases = ['#DC2626', '#D97706', '#65A30D', '#059669']
    
    # Draw timeline
    ax.axhline(y=0.5, color='#e2e8f0', linewidth=8, zorder=1)
    
    for i, (phase, timeline, color) in enumerate(zip(phases, timelines, colors_phases)):
        # Phase circles
        circle = plt.Circle((i * 2 + 1, 0.5), 0.4, color=color, zorder=2)
        ax.add_patch(circle)
        
        # Phase number
        ax.text(i * 2 + 1, 0.5, str(i + 1), ha='center', va='center', 
                fontsize=16, fontweight='bold', color='white', zorder=3)
        
        # Phase name
        ax.text(i * 2 + 1, 1.1, phase, ha='center', va='center', 
                fontsize=11, fontweight='bold', color='#1e293b')
        
        # Timeline
        ax.text(i * 2 + 1, -0.1, timeline, ha='center', va='center', 
                fontsize=9, color='#64748b')
        
        # Connect circles
        if i < len(phases) - 1:
            ax.annotate('', xy=(i * 2 + 2.6, 0.5), xytext=(i * 2 + 1.4, 0.5),
                       arrowprops=dict(arrowstyle='->', color=color, lw=2))
    
    ax.set_xlim(-0.5, 8)
    ax.set_ylim(-0.5, 1.5)
    ax.axis('off')
    ax.set_title('Maturity Improvement Roadmap', fontsize=14, fontweight='bold', 
                color='#1e293b', pad=20)
    
    plt.tight_layout()
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close(fig)
    buf.seek(0)
    return buf

def create_score_comparison_bars(ct_score, ga_score, combined, benchmark):
    """Create a clean horizontal comparison bar chart"""
    fig, ax = plt.subplots(figsize=(10, 4))
    
    categories = ['Control Tower', 'Golden Architecture', 'Combined Score', f'Industry Benchmark']
    values = [ct_score, ga_score, combined, benchmark]
    colors_bars = ['#0284c7', '#7c3aed', '#059669', '#f59e0b']
    
    y_pos = np.arange(len(categories))
    
    # Background bars
    ax.barh(y_pos, [100] * len(categories), color='#f1f5f9', height=0.6)
    
    # Score bars
    bars = ax.barh(y_pos, values, color=colors_bars, height=0.6, alpha=0.9)
    
    # Add value labels
    for bar, val in zip(bars, values):
        ax.text(val + 2, bar.get_y() + bar.get_height()/2, f'{val:.0f}%', 
                va='center', ha='left', fontsize=12, fontweight='bold', color='#1e293b')
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories, fontsize=11, fontweight='bold')
    ax.set_xlim(0, 115)
    ax.set_xlabel('Score (%)', fontsize=10, color='#64748b')
    ax.set_title('Assessment Score Overview', fontsize=14, fontweight='bold', 
                color='#1e293b', pad=15)
    
    # Reference lines
    for x, label in [(40, 'Developing'), (60, 'Managed'), (80, 'Optimized')]:
        ax.axvline(x=x, color='#cbd5e1', linestyle='--', linewidth=1, alpha=0.7)
        ax.text(x, len(categories) - 0.3, label, fontsize=8, color='#94a3b8', 
                ha='center', va='bottom')
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('#e2e8f0')
    ax.spines['left'].set_color('#e2e8f0')
    
    plt.tight_layout()
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close(fig)
    buf.seek(0)
    return buf

# =============================================================================
# PLOTLY INTERACTIVE UI CHARTS
# =============================================================================

def create_ui_gauge_chart(score, title, color="#0284c7"):
    """Create a beautiful gauge chart for the UI"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        number={'suffix': '%', 'font': {'size': 40, 'color': '#1e293b', 'family': 'Inter, sans-serif'}},
        title={'text': title, 'font': {'size': 16, 'color': '#64748b', 'family': 'Inter, sans-serif'}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#e2e8f0",
                    'tickvals': [0, 20, 40, 60, 80, 100],
                    'ticktext': ['0', '20', '40', '60', '80', '100']},
            'bar': {'color': color, 'thickness': 0.75},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "#e2e8f0",
            'steps': [
                {'range': [0, 20], 'color': '#fee2e2'},
                {'range': [20, 40], 'color': '#ffedd5'},
                {'range': [40, 60], 'color': '#fef3c7'},
                {'range': [60, 80], 'color': '#d1fae5'},
                {'range': [80, 100], 'color': '#a7f3d0'}
            ],
            'threshold': {
                'line': {'color': "#1e293b", 'width': 4},
                'thickness': 0.75,
                'value': score
            }
        }
    ))
    
    fig.update_layout(
        height=250,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        font={'family': 'Inter, sans-serif'}
    )
    return fig

def create_ui_score_gauges(ct_score, ga_score, combined, benchmark, bench_name):
    """Create a row of 4 gauge charts"""
    fig = make_subplots(
        rows=1, cols=4,
        specs=[[{'type': 'indicator'}, {'type': 'indicator'}, 
                {'type': 'indicator'}, {'type': 'indicator'}]],
        horizontal_spacing=0.05
    )
    
    configs = [
        (ct_score, "Control Tower", "#0284c7"),
        (ga_score, "Golden Architecture", "#7c3aed"),
        (combined, "Combined Score", "#059669"),
        (benchmark, f"{bench_name}", "#f59e0b")
    ]
    
    for i, (score, title, color) in enumerate(configs, 1):
        fig.add_trace(go.Indicator(
            mode="gauge+number",
            value=score,
            number={'suffix': '%', 'font': {'size': 28, 'color': '#1e293b'}},
            title={'text': title, 'font': {'size': 12, 'color': '#64748b'}},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#e2e8f0",
                        'tickvals': [0, 50, 100], 'ticktext': ['0', '50', '100']},
                'bar': {'color': color, 'thickness': 0.7},
                'bgcolor': "white",
                'borderwidth': 1,
                'bordercolor': "#e2e8f0",
                'steps': [
                    {'range': [0, 40], 'color': '#fee2e2'},
                    {'range': [40, 60], 'color': '#fef3c7'},
                    {'range': [60, 80], 'color': '#d1fae5'},
                    {'range': [80, 100], 'color': '#a7f3d0'}
                ],
            }
        ), row=1, col=i)
    
    fig.update_layout(
        height=280,
        margin=dict(l=20, r=20, t=40, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
    )
    return fig

def create_ui_radar_chart(domain_scores, title, color="#0284c7"):
    """Create an interactive radar chart for domain analysis"""
    categories = list(domain_scores.keys())
    values = [domain_scores[cat]['score'] for cat in categories]
    
    # Truncate long names
    display_categories = [cat[:25] + '...' if len(cat) > 25 else cat for cat in categories]
    
    # Close the radar
    values_closed = values + [values[0]]
    categories_closed = display_categories + [display_categories[0]]
    
    fig = go.Figure()
    
    # Add filled area
    fig.add_trace(go.Scatterpolar(
        r=values_closed,
        theta=categories_closed,
        fill='toself',
        fillcolor=f'rgba({int(color[1:3], 16)}, {int(color[3:5], 16)}, {int(color[5:7], 16)}, 0.25)',
        line=dict(color=color, width=2),
        name='Score',
        hovertemplate='<b>%{theta}</b><br>Score: %{r:.0f}%<extra></extra>'
    ))
    
    # Add markers
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=display_categories,
        mode='markers',
        marker=dict(color=color, size=10, symbol='circle'),
        showlegend=False,
        hovertemplate='<b>%{theta}</b><br>Score: %{r:.0f}%<extra></extra>'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickvals=[20, 40, 60, 80, 100],
                ticktext=['20%', '40%', '60%', '80%', '100%'],
                tickfont=dict(size=10, color='#94a3b8'),
                gridcolor='#e2e8f0',
                linecolor='#e2e8f0'
            ),
            angularaxis=dict(
                tickfont=dict(size=11, color='#1e293b'),
                gridcolor='#e2e8f0',
                linecolor='#e2e8f0'
            ),
            bgcolor='rgba(0,0,0,0)'
        ),
        showlegend=False,
        title=dict(text=title, font=dict(size=16, color='#1e293b'), x=0.5),
        height=450,
        margin=dict(l=80, r=80, t=80, b=60),
        paper_bgcolor='rgba(0,0,0,0)',
    )
    return fig

def create_ui_horizontal_bar_chart(domain_scores, title, color="#0284c7"):
    """Create an interactive horizontal bar chart for domain scores"""
    categories = list(domain_scores.keys())
    values = [domain_scores[cat]['score'] for cat in categories]
    answered = [f"{domain_scores[cat]['answered']}/{domain_scores[cat]['total']}" for cat in categories]
    
    # Color based on score
    colors_list = []
    for v in values:
        if v >= 80:
            colors_list.append('#059669')
        elif v >= 60:
            colors_list.append('#65a30d')
        elif v >= 40:
            colors_list.append('#d97706')
        elif v >= 20:
            colors_list.append('#ea580c')
        else:
            colors_list.append('#dc2626')
    
    fig = go.Figure()
    
    # Background bars (100%)
    fig.add_trace(go.Bar(
        y=categories,
        x=[100] * len(categories),
        orientation='h',
        marker_color='#f1f5f9',
        showlegend=False,
        hoverinfo='skip'
    ))
    
    # Score bars
    fig.add_trace(go.Bar(
        y=categories,
        x=values,
        orientation='h',
        marker_color=colors_list,
        text=[f'{v:.0f}%' for v in values],
        textposition='outside',
        textfont=dict(size=12, color='#1e293b', family='Inter, sans-serif'),
        hovertemplate='<b>%{y}</b><br>Score: %{x:.0f}%<br>Answered: %{customdata}<extra></extra>',
        customdata=answered,
        showlegend=False
    ))
    
    # Add maturity reference lines
    for x, label, clr in [(40, 'Developing', '#d97706'), (60, 'Managed', '#65a30d'), (80, 'Optimized', '#059669')]:
        fig.add_vline(x=x, line_dash="dash", line_color='#cbd5e1', line_width=1)
        fig.add_annotation(x=x, y=len(categories)-0.5, text=label, showarrow=False, 
                          font=dict(size=9, color='#94a3b8'), yshift=15)
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=16, color='#1e293b'), x=0),
        xaxis=dict(
            title='Score (%)',
            range=[0, 110],
            gridcolor='#f1f5f9',
            tickfont=dict(color='#64748b')
        ),
        yaxis=dict(
            tickfont=dict(size=11, color='#1e293b'),
            categoryorder='total ascending'
        ),
        height=max(350, len(categories) * 45),
        margin=dict(l=20, r=40, t=60, b=40),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        barmode='overlay'
    )
    return fig

def create_ui_gap_donut_chart(ct_gaps, ga_gaps):
    """Create an interactive donut chart for gap distribution"""
    critical = len([g for g in ct_gaps + ga_gaps if g['risk'] == 'critical'])
    high = len([g for g in ct_gaps + ga_gaps if g['risk'] == 'high'])
    medium = len([g for g in ct_gaps + ga_gaps if g['risk'] == 'medium'])
    
    total = critical + high + medium
    
    if total == 0:
        # No gaps - create a success chart
        fig = go.Figure(go.Indicator(
            mode="number",
            value=0,
            number={'suffix': ' Gaps', 'font': {'size': 48, 'color': '#059669'}},
            title={'text': '✓ No Gaps Identified', 'font': {'size': 18, 'color': '#059669'}}
        ))
        fig.update_layout(height=300, paper_bgcolor='rgba(0,0,0,0)')
        return fig
    
    labels = ['Critical', 'High', 'Medium']
    values = [critical, high, medium]
    colors_pie = ['#dc2626', '#ea580c', '#d97706']
    
    # Filter out zeros
    non_zero = [(l, v, c) for l, v, c in zip(labels, values, colors_pie) if v > 0]
    if non_zero:
        labels, values, colors_pie = zip(*non_zero)
    
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.5,
        marker_colors=colors_pie,
        textinfo='label+value',
        textfont=dict(size=14, color='white'),
        hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}<extra></extra>',
        pull=[0.05 if l == 'Critical' else 0 for l in labels]
    )])
    
    fig.add_annotation(
        text=f'<b>{total}</b><br>Total<br>Gaps',
        x=0.5, y=0.5,
        font=dict(size=16, color='#1e293b'),
        showarrow=False
    )
    
    fig.update_layout(
        title=dict(text='Gap Distribution by Risk Level', font=dict(size=16, color='#1e293b'), x=0.5),
        height=350,
        margin=dict(l=20, r=20, t=60, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=True,
        legend=dict(orientation='h', yanchor='bottom', y=-0.1, xanchor='center', x=0.5)
    )
    return fig

def create_ui_industry_comparison_chart(combined, benchmarks, current_industry):
    """Create an interactive bar chart for industry comparison"""
    industries = [b['name'] for b in benchmarks.values()]
    averages = [b['avg'] for b in benchmarks.values()]
    top_performers = [b['top'] for b in benchmarks.values()]
    industry_keys = list(benchmarks.keys())
    
    # Highlight current industry
    avg_colors = ['#0284c7' if k == current_industry else '#94a3b8' for k in industry_keys]
    top_colors = ['#0369a1' if k == current_industry else '#64748b' for k in industry_keys]
    
    fig = go.Figure()
    
    # Average bars
    fig.add_trace(go.Bar(
        name='Industry Average',
        x=industries,
        y=averages,
        marker_color=avg_colors,
        text=[f'{a}%' for a in averages],
        textposition='outside',
        textfont=dict(size=10),
        hovertemplate='<b>%{x}</b><br>Average: %{y}%<extra></extra>'
    ))
    
    # Top performer bars
    fig.add_trace(go.Bar(
        name='Top Performers',
        x=industries,
        y=top_performers,
        marker_color=top_colors,
        text=[f'{t}%' for t in top_performers],
        textposition='outside',
        textfont=dict(size=10),
        hovertemplate='<b>%{x}</b><br>Top Performers: %{y}%<extra></extra>'
    ))
    
    # Your score line
    fig.add_hline(y=combined, line_dash="solid", line_color="#059669", line_width=3,
                  annotation_text=f"Your Score: {combined:.0f}%", 
                  annotation_position="right",
                  annotation_font=dict(color="#059669", size=12, family='Inter, sans-serif'))
    
    fig.update_layout(
        title=dict(text='Industry Benchmark Comparison', font=dict(size=16, color='#1e293b'), x=0),
        xaxis=dict(
            tickfont=dict(size=10, color='#64748b'),
            tickangle=-25
        ),
        yaxis=dict(
            title='Score (%)',
            range=[0, 105],
            gridcolor='#f1f5f9',
            tickfont=dict(color='#64748b')
        ),
        height=400,
        margin=dict(l=40, r=40, t=60, b=100),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        barmode='group',
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
    )
    return fig

def create_ui_maturity_progress_chart(ct_score, ga_score, combined, bench_avg):
    """Create a progress/bullet chart showing maturity progress"""
    categories = ['Control Tower', 'Golden Architecture', 'Combined', 'Industry Benchmark']
    scores = [ct_score, ga_score, combined, bench_avg]
    colors = ['#0284c7', '#7c3aed', '#059669', '#f59e0b']
    
    fig = go.Figure()
    
    for i, (cat, score, color) in enumerate(zip(categories, scores, colors)):
        # Determine maturity level
        if score >= 80:
            maturity = "Optimized"
        elif score >= 60:
            maturity = "Managed"
        elif score >= 40:
            maturity = "Developing"
        elif score >= 20:
            maturity = "Initial"
        else:
            maturity = "Not Assessed"
        
        fig.add_trace(go.Bar(
            y=[cat],
            x=[score],
            orientation='h',
            marker=dict(
                color=color,
                line=dict(color=color, width=1)
            ),
            text=f'{score:.0f}% - {maturity}',
            textposition='outside',
            textfont=dict(size=12, color='#1e293b'),
            hovertemplate=f'<b>{cat}</b><br>Score: {score:.0f}%<br>Maturity: {maturity}<extra></extra>',
            showlegend=False
        ))
    
    # Add maturity level backgrounds
    shapes = [
        dict(type='rect', x0=0, x1=20, y0=-0.5, y1=3.5, fillcolor='#fee2e2', opacity=0.3, line_width=0, layer='below'),
        dict(type='rect', x0=20, x1=40, y0=-0.5, y1=3.5, fillcolor='#ffedd5', opacity=0.3, line_width=0, layer='below'),
        dict(type='rect', x0=40, x1=60, y0=-0.5, y1=3.5, fillcolor='#fef3c7', opacity=0.3, line_width=0, layer='below'),
        dict(type='rect', x0=60, x1=80, y0=-0.5, y1=3.5, fillcolor='#d1fae5', opacity=0.3, line_width=0, layer='below'),
        dict(type='rect', x0=80, x1=100, y0=-0.5, y1=3.5, fillcolor='#a7f3d0', opacity=0.3, line_width=0, layer='below'),
    ]
    
    fig.update_layout(
        shapes=shapes,
        xaxis=dict(
            range=[0, 110],
            title='Score (%)',
            gridcolor='#e2e8f0',
            tickfont=dict(color='#64748b'),
            tickvals=[0, 20, 40, 60, 80, 100]
        ),
        yaxis=dict(
            tickfont=dict(size=12, color='#1e293b')
        ),
        height=250,
        margin=dict(l=20, r=100, t=30, b=40),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    # Add maturity labels at top
    for x, label in [(10, 'Initial'), (30, 'Developing'), (50, 'Defined'), (70, 'Managed'), (90, 'Optimized')]:
        fig.add_annotation(x=x, y=4, text=label, showarrow=False,
                          font=dict(size=9, color='#94a3b8'), yshift=5)
    
    return fig

def create_ui_gap_heatmap(ct_gaps, ga_gaps, ct_questions, ga_questions):
    """Create a heatmap showing gaps by domain and risk level"""
    all_domains = list(ct_questions.keys()) + list(ga_questions.keys())
    risk_levels = ['Critical', 'High', 'Medium']
    
    # Build matrix
    matrix = []
    for domain in all_domains:
        row = []
        for risk in ['critical', 'high', 'medium']:
            count = len([g for g in ct_gaps + ga_gaps if g['domain'] == domain and g['risk'] == risk])
            row.append(count)
        matrix.append(row)
    
    # Truncate domain names
    display_domains = [d[:30] + '...' if len(d) > 30 else d for d in all_domains]
    
    fig = go.Figure(data=go.Heatmap(
        z=matrix,
        x=risk_levels,
        y=display_domains,
        colorscale=[
            [0, '#f0fdf4'],
            [0.25, '#fef3c7'],
            [0.5, '#fed7aa'],
            [0.75, '#fecaca'],
            [1, '#dc2626']
        ],
        showscale=True,
        colorbar=dict(title='Gap Count', tickfont=dict(size=10)),
        hovertemplate='<b>%{y}</b><br>Risk: %{x}<br>Gaps: %{z}<extra></extra>',
        text=matrix,
        texttemplate='%{text}',
        textfont=dict(size=11, color='#1e293b')
    ))
    
    fig.update_layout(
        title=dict(text='Gap Heatmap by Domain & Risk Level', font=dict(size=16, color='#1e293b'), x=0),
        xaxis=dict(tickfont=dict(size=12, color='#1e293b')),
        yaxis=dict(tickfont=dict(size=10, color='#1e293b'), autorange='reversed'),
        height=max(400, len(all_domains) * 25),
        margin=dict(l=20, r=20, t=60, b=40),
        paper_bgcolor='rgba(0,0,0,0)'
    )
    return fig

# =============================================================================
# COMPREHENSIVE PDF REPORT GENERATOR
# =============================================================================
def generate_pdf_report(org_name, assessor_name, industry, ct_responses, ga_responses, 
                        ct_questions, ga_questions, benchmarks, ai_analysis):
    """Generate a comprehensive 30+ page PDF assessment report"""
    
    buffer = io.BytesIO()
    
    # Document setup
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )
    
    # Custom styles
    styles = getSampleStyleSheet()
    
    # Define custom colors
    aws_orange = colors.HexColor('#FF9900')
    aws_dark = colors.HexColor('#232F3E')
    primary_blue = colors.HexColor('#0284C7')
    success_green = colors.HexColor('#059669')
    warning_amber = colors.HexColor('#D97706')
    danger_red = colors.HexColor('#DC2626')
    text_gray = colors.HexColor('#475569')
    light_gray = colors.HexColor('#F1F5F9')
    border_gray = colors.HexColor('#E2E8F0')
    
    # Custom paragraph styles
    styles.add(ParagraphStyle(
        name='CoverTitle',
        parent=styles['Title'],
        fontSize=32,
        textColor=aws_dark,
        alignment=TA_CENTER,
        spaceAfter=20,
        fontName='Helvetica-Bold'
    ))
    
    styles.add(ParagraphStyle(
        name='CoverSubtitle',
        parent=styles['Normal'],
        fontSize=16,
        textColor=text_gray,
        alignment=TA_CENTER,
        spaceAfter=40
    ))
    
    styles.add(ParagraphStyle(
        name='SectionTitle',
        parent=styles['Heading1'],
        fontSize=20,
        textColor=aws_dark,
        spaceBefore=30,
        spaceAfter=15,
        fontName='Helvetica-Bold',
        borderColor=primary_blue,
        borderWidth=2,
        borderPadding=5
    ))
    
    styles.add(ParagraphStyle(
        name='SubSectionTitle',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=primary_blue,
        spaceBefore=20,
        spaceAfter=10,
        fontName='Helvetica-Bold'
    ))
    
    styles.add(ParagraphStyle(
        name='DomainTitle',
        parent=styles['Heading3'],
        fontSize=12,
        textColor=aws_dark,
        spaceBefore=15,
        spaceAfter=8,
        fontName='Helvetica-Bold'
    ))
    
    styles.add(ParagraphStyle(
        name='BodyText',
        parent=styles['Normal'],
        fontSize=10,
        textColor=text_gray,
        alignment=TA_JUSTIFY,
        spaceAfter=8,
        leading=14
    ))
    
    styles.add(ParagraphStyle(
        name='SmallText',
        parent=styles['Normal'],
        fontSize=8,
        textColor=text_gray,
        spaceAfter=4
    ))
    
    styles.add(ParagraphStyle(
        name='TOCEntry',
        parent=styles['Normal'],
        fontSize=11,
        textColor=aws_dark,
        leftIndent=20,
        spaceAfter=8
    ))
    
    styles.add(ParagraphStyle(
        name='TOCSection',
        parent=styles['Normal'],
        fontSize=12,
        textColor=aws_dark,
        fontName='Helvetica-Bold',
        spaceBefore=10,
        spaceAfter=5
    ))
    
    styles.add(ParagraphStyle(
        name='QuestionText',
        parent=styles['Normal'],
        fontSize=9,
        textColor=text_gray,
        leftIndent=15,
        spaceAfter=4
    ))
    
    styles.add(ParagraphStyle(
        name='Footer',
        parent=styles['Normal'],
        fontSize=8,
        textColor=text_gray,
        alignment=TA_CENTER
    ))
    
    # Calculate scores
    ct_scores = calc_scores(ct_responses, ct_questions)
    ga_scores = calc_scores(ga_responses, ga_questions)
    combined = (ct_scores["overall"] + ga_scores["overall"]) / 2 if (ct_scores["overall"] > 0 or ga_scores["overall"] > 0) else 0
    
    # Find gaps
    ct_gaps = find_gaps(ct_responses, ct_questions)
    ga_gaps = find_gaps(ga_responses, ga_questions)
    
    bench = benchmarks[industry]
    
    story = []
    
    # =========================================================================
    # COVER PAGE
    # =========================================================================
    story.append(Spacer(1, 1.5*inch))
    
    # AWS Logo placeholder (orange bar)
    cover_header = Drawing(500, 60)
    cover_header.add(Rect(0, 20, 500, 40, fillColor=aws_orange, strokeColor=None))
    cover_header.add(String(20, 35, "AWS", fontSize=24, fillColor=colors.white, fontName='Helvetica-Bold'))
    cover_header.add(String(70, 35, "Enterprise Assessment Platform", fontSize=16, fillColor=colors.white))
    story.append(cover_header)
    
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("AWS Enterprise Assessment", styles['CoverTitle']))
    story.append(Paragraph("Control Tower & Golden Architecture Readiness Report", styles['CoverSubtitle']))
    
    story.append(Spacer(1, 0.5*inch))
    
    # Cover info table
    cover_data = [
        ['Organization:', org_name or 'Not Specified'],
        ['Assessment Date:', datetime.now().strftime('%B %d, %Y')],
        ['Assessor:', assessor_name or 'Not Specified'],
        ['Industry Vertical:', bench['name']],
        ['Report Version:', 'v3.0 - Comprehensive Analysis'],
    ]
    
    cover_table = Table(cover_data, colWidths=[2*inch, 4*inch])
    cover_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('TEXTCOLOR', (0, 0), (0, -1), aws_dark),
        ('TEXTCOLOR', (1, 0), (1, -1), text_gray),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
    ]))
    story.append(cover_table)
    
    story.append(Spacer(1, 0.75*inch))
    
    # Executive Score Summary Box
    score_color = success_green if combined >= 60 else (warning_amber if combined >= 40 else danger_red)
    maturity_level, _, maturity_desc = get_maturity(combined)
    
    exec_summary_data = [
        ['COMBINED ASSESSMENT SCORE'],
        [f'{combined:.0f}%'],
        [f'Maturity Level: {maturity_level}'],
        [maturity_desc]
    ]
    
    exec_table = Table(exec_summary_data, colWidths=[4*inch])
    exec_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), aws_dark),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 1), (0, 1), 48),
        ('FONTNAME', (0, 1), (0, 1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (0, 1), (0, 1), score_color),
        ('FONTSIZE', (0, 2), (0, 2), 14),
        ('FONTNAME', (0, 2), (0, 2), 'Helvetica-Bold'),
        ('TEXTCOLOR', (0, 2), (0, 2), aws_dark),
        ('FONTSIZE', (0, 3), (0, 3), 10),
        ('TEXTCOLOR', (0, 3), (0, 3), text_gray),
        ('TOPPADDING', (0, 0), (-1, -1), 15),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 15),
        ('BOX', (0, 0), (-1, -1), 2, aws_dark),
    ]))
    story.append(exec_table)
    
    story.append(Spacer(1, 0.5*inch))
    
    # Add Score Gauges Visualization
    try:
        gauges_img = create_score_gauges(ct_scores["overall"], ga_scores["overall"], combined, bench["avg"])
        story.append(Image(gauges_img, width=7*inch, height=1.8*inch))
    except Exception as e:
        pass  # Skip if chart generation fails
    
    story.append(Spacer(1, 0.3*inch))
    
    # Confidentiality notice
    story.append(Paragraph(
        "<b>CONFIDENTIAL</b> - This report contains proprietary assessment data and recommendations. "
        "Distribution should be limited to authorized personnel only.",
        styles['SmallText']
    ))
    
    story.append(PageBreak())
    
    # =========================================================================
    # TABLE OF CONTENTS
    # =========================================================================
    story.append(Paragraph("Table of Contents", styles['SectionTitle']))
    story.append(Spacer(1, 0.25*inch))
    
    toc_items = [
        ("1.", "Executive Summary", "3"),
        ("2.", "Assessment Methodology", "5"),
        ("3.", "Overall Score Analysis", "7"),
        ("4.", "Control Tower Assessment", "9"),
        ("    4.1", "Domain Analysis", "10"),
        ("    4.2", "Detailed Findings", "12"),
        ("5.", "Golden Architecture Assessment", "15"),
        ("    5.1", "Domain Analysis", "16"),
        ("    5.2", "Detailed Findings", "18"),
        ("6.", "Gap Analysis", "21"),
        ("    6.1", "Critical Gaps", "22"),
        ("    6.2", "High Priority Gaps", "23"),
        ("    6.3", "Medium Priority Gaps", "24"),
        ("7.", "Industry Benchmark Comparison", "25"),
        ("8.", "Maturity Roadmap", "26"),
        ("9.", "Implementation Recommendations", "28"),
        ("10.", "Risk Assessment", "30"),
        ("11.", "AI-Powered Analysis", "31"),
        ("A.", "Appendix: Question Details", "33"),
        ("B.", "Appendix: Scoring Methodology", "35"),
    ]
    
    for num, title, page in toc_items:
        is_sub = num.startswith("    ")
        style = styles['TOCEntry'] if is_sub else styles['TOCSection']
        dots = "." * (60 - len(num) - len(title))
        story.append(Paragraph(f"{num} {title} {dots} {page}", style))
    
    story.append(PageBreak())
    
    # =========================================================================
    # EXECUTIVE SUMMARY
    # =========================================================================
    story.append(Paragraph("1. Executive Summary", styles['SectionTitle']))
    
    story.append(Paragraph(
        f"This comprehensive assessment evaluates {org_name or 'the organization'}'s readiness for "
        f"AWS Control Tower migration and Golden Architecture (serverless) adoption. The assessment "
        f"covers 130+ evaluation criteria across 22 domains, providing a detailed view of current "
        f"capabilities, gaps, and recommended improvements.",
        styles['BodyText']
    ))
    
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Key Findings", styles['SubSectionTitle']))
    
    # Key metrics table
    key_metrics = [
        ['Metric', 'Value', 'Status'],
        ['Control Tower Score', f'{ct_scores["overall"]:.1f}%', get_maturity(ct_scores["overall"])[0]],
        ['Golden Architecture Score', f'{ga_scores["overall"]:.1f}%', get_maturity(ga_scores["overall"])[0]],
        ['Combined Enterprise Score', f'{combined:.1f}%', get_maturity(combined)[0]],
        ['vs Industry Benchmark', f'{combined - bench["avg"]:+.1f}%', 'Above' if combined >= bench["avg"] else 'Below'],
        ['Assessment Completion', f'{((ct_scores["total_answered"] + ga_scores["total_answered"]) / (ct_scores["total_questions"] + ga_scores["total_questions"]) * 100):.0f}%', ''],
    ]
    
    metrics_table = Table(key_metrics, colWidths=[2.5*inch, 1.5*inch, 2*inch])
    metrics_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), aws_dark),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 0.5, border_gray),
        ('BACKGROUND', (0, 1), (-1, -1), light_gray),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(metrics_table)
    
    story.append(Spacer(1, 0.2*inch))
    
    # Gap summary
    story.append(Paragraph("Gap Summary", styles['SubSectionTitle']))
    
    critical_ct = len([g for g in ct_gaps if g['risk'] == 'critical'])
    high_ct = len([g for g in ct_gaps if g['risk'] == 'high'])
    medium_ct = len([g for g in ct_gaps if g['risk'] == 'medium'])
    critical_ga = len([g for g in ga_gaps if g['risk'] == 'critical'])
    high_ga = len([g for g in ga_gaps if g['risk'] == 'high'])
    medium_ga = len([g for g in ga_gaps if g['risk'] == 'medium'])
    
    gap_summary = [
        ['Risk Level', 'Control Tower', 'Golden Architecture', 'Total'],
        ['Critical', str(critical_ct), str(critical_ga), str(critical_ct + critical_ga)],
        ['High', str(high_ct), str(high_ga), str(high_ct + high_ga)],
        ['Medium', str(medium_ct), str(medium_ga), str(medium_ct + medium_ga)],
        ['Total Gaps', str(critical_ct + high_ct + medium_ct), str(critical_ga + high_ga + medium_ga), 
         str(critical_ct + high_ct + medium_ct + critical_ga + high_ga + medium_ga)],
    ]
    
    gap_table = Table(gap_summary, colWidths=[1.5*inch, 1.5*inch, 1.75*inch, 1.25*inch])
    gap_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), aws_dark),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 1), (0, 1), colors.HexColor('#FEE2E2')),
        ('BACKGROUND', (0, 2), (0, 2), colors.HexColor('#FFEDD5')),
        ('BACKGROUND', (0, 3), (0, 3), colors.HexColor('#FEF3C7')),
        ('BACKGROUND', (0, 4), (-1, 4), light_gray),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 0.5, border_gray),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(gap_table)
    
    story.append(Spacer(1, 0.3*inch))
    
    # Executive Recommendations
    story.append(Paragraph("Executive Recommendations", styles['SubSectionTitle']))
    
    recommendations = []
    if critical_ct + critical_ga > 0:
        recommendations.append("• <b>Immediate Action Required:</b> Address critical gaps in security and governance before proceeding with Control Tower migration.")
    if ct_scores["overall"] < 40:
        recommendations.append("• <b>Foundation Building:</b> Establish basic multi-account governance and OU structure before Control Tower adoption.")
    if ga_scores["overall"] < 40:
        recommendations.append("• <b>Serverless Readiness:</b> Develop serverless competencies through training and pilot projects.")
    if combined < bench["avg"]:
        recommendations.append(f"• <b>Industry Gap:</b> Score is {bench['avg'] - combined:.0f}% below the {bench['name']} average. Prioritize assessment completion and gap remediation.")
    if combined >= bench["avg"]:
        recommendations.append(f"• <b>Competitive Position:</b> Organization performs at or above {bench['name']} average. Focus on optimization and advanced capabilities.")
    
    if not recommendations:
        recommendations.append("• Complete the assessment to receive tailored recommendations.")
    
    for rec in recommendations:
        story.append(Paragraph(rec, styles['BodyText']))
    
    story.append(PageBreak())
    
    # =========================================================================
    # ASSESSMENT METHODOLOGY
    # =========================================================================
    story.append(Paragraph("2. Assessment Methodology", styles['SectionTitle']))
    
    story.append(Paragraph(
        "This assessment follows AWS Well-Architected Framework principles and incorporates "
        "industry best practices for enterprise cloud adoption. The methodology evaluates organizational "
        "readiness across multiple dimensions:",
        styles['BodyText']
    ))
    
    story.append(Spacer(1, 0.15*inch))
    
    # Well-Architected Pillars
    story.append(Paragraph("AWS Well-Architected Framework Pillars", styles['SubSectionTitle']))
    
    pillars_data = [
        ['Pillar', 'Description', 'Focus Areas'],
        ['Operational Excellence', 'Run and monitor systems to deliver business value', 'Automation, monitoring, incident response'],
        ['Security', 'Protect information, systems, and assets', 'IAM, encryption, compliance, detective controls'],
        ['Reliability', 'Recover from failures and meet demand', 'Fault tolerance, disaster recovery, scaling'],
        ['Performance Efficiency', 'Use resources efficiently', 'Right-sizing, caching, serverless optimization'],
        ['Cost Optimization', 'Avoid unnecessary costs', 'Reserved capacity, rightsizing, waste elimination'],
        ['Sustainability', 'Minimize environmental impact', 'Efficient architectures, managed services'],
    ]
    
    pillars_table = Table(pillars_data, colWidths=[1.75*inch, 2.25*inch, 2*inch])
    pillars_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, border_gray),
        ('BACKGROUND', (0, 1), (-1, -1), light_gray),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(pillars_table)
    
    story.append(Spacer(1, 0.2*inch))
    
    # Scoring methodology
    story.append(Paragraph("Scoring Methodology", styles['SubSectionTitle']))
    
    story.append(Paragraph(
        "Each question is scored on a 5-point maturity scale, with domain scores weighted by "
        "their relative importance to overall enterprise readiness:",
        styles['BodyText']
    ))
    
    scoring_data = [
        ['Score', 'Level', 'Description'],
        ['1 (0-20%)', 'Initial', 'Ad-hoc processes, limited documentation, reactive approach'],
        ['2 (21-40%)', 'Developing', 'Basic processes emerging, inconsistent implementation'],
        ['3 (41-60%)', 'Defined', 'Documented processes, partial implementation across org'],
        ['4 (61-80%)', 'Managed', 'Consistent implementation, metrics-driven improvement'],
        ['5 (81-100%)', 'Optimized', 'Industry-leading practices, continuous optimization'],
    ]
    
    scoring_table = Table(scoring_data, colWidths=[1.25*inch, 1.25*inch, 3.5*inch])
    scoring_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), aws_dark),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, border_gray),
        ('BACKGROUND', (0, 1), (-1, -1), light_gray),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(scoring_table)
    
    story.append(Spacer(1, 0.2*inch))
    
    # Assessment coverage
    story.append(Paragraph("Assessment Coverage", styles['SubSectionTitle']))
    
    coverage_data = [
        ['Assessment', 'Domains', 'Questions', 'Focus'],
        ['Control Tower', str(len(ct_questions)), str(ct_scores['total_questions']), 'Multi-account governance, security, compliance'],
        ['Golden Architecture', str(len(ga_questions)), str(ga_scores['total_questions']), 'Serverless maturity, event-driven patterns'],
        ['Total', str(len(ct_questions) + len(ga_questions)), str(ct_scores['total_questions'] + ga_scores['total_questions']), 'Comprehensive enterprise readiness'],
    ]
    
    coverage_table = Table(coverage_data, colWidths=[1.5*inch, 1*inch, 1*inch, 2.5*inch])
    coverage_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, border_gray),
        ('BACKGROUND', (0, 1), (-1, -2), light_gray),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#DBEAFE')),
        ('ALIGN', (1, 0), (2, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(coverage_table)
    
    story.append(PageBreak())
    
    # =========================================================================
    # OVERALL SCORE ANALYSIS
    # =========================================================================
    story.append(Paragraph("3. Overall Score Analysis", styles['SectionTitle']))
    
    # Score comparison visualization using matplotlib
    story.append(Paragraph("Assessment Score Comparison", styles['SubSectionTitle']))
    
    # Add beautiful comparison bar chart
    try:
        comparison_img = create_score_comparison_bars(ct_scores["overall"], ga_scores["overall"], combined, bench["avg"])
        story.append(Image(comparison_img, width=6.5*inch, height=2.6*inch))
    except Exception as e:
        # Fallback to simple text if chart fails
        story.append(Paragraph(f"Control Tower: {ct_scores['overall']:.1f}% | Golden Architecture: {ga_scores['overall']:.1f}% | Combined: {combined:.1f}%", styles['BodyText']))
    
    story.append(Spacer(1, 0.3*inch))
    
    # Maturity distribution
    story.append(Paragraph("Maturity Level Assessment", styles['SubSectionTitle']))
    
    maturity_data = [
        ['Assessment', 'Score', 'Maturity Level', 'Description'],
        ['Control Tower', f'{ct_scores["overall"]:.1f}%', get_maturity(ct_scores["overall"])[0], get_maturity(ct_scores["overall"])[2]],
        ['Golden Architecture', f'{ga_scores["overall"]:.1f}%', get_maturity(ga_scores["overall"])[0], get_maturity(ga_scores["overall"])[2]],
        ['Combined', f'{combined:.1f}%', get_maturity(combined)[0], get_maturity(combined)[2]],
    ]
    
    maturity_table = Table(maturity_data, colWidths=[1.5*inch, 1*inch, 1.25*inch, 2.25*inch])
    maturity_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), aws_dark),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, border_gray),
        ('BACKGROUND', (0, 1), (-1, -1), light_gray),
        ('ALIGN', (1, 0), (2, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(maturity_table)
    
    story.append(Spacer(1, 0.3*inch))
    
    # Industry comparison
    story.append(Paragraph("Industry Benchmark Comparison", styles['SubSectionTitle']))
    
    story.append(Paragraph(
        f"Your organization's combined score of <b>{combined:.1f}%</b> compares to the "
        f"<b>{bench['name']}</b> industry average of <b>{bench['avg']}%</b> and top performers "
        f"at <b>{bench['top']}%</b>.",
        styles['BodyText']
    ))
    
    variance = combined - bench["avg"]
    if variance >= 0:
        story.append(Paragraph(
            f"<font color='#059669'><b>Positive Variance: +{variance:.1f}%</b></font> - "
            f"Your organization performs above the industry average.",
            styles['BodyText']
        ))
    else:
        story.append(Paragraph(
            f"<font color='#DC2626'><b>Negative Variance: {variance:.1f}%</b></font> - "
            f"Gap to industry average should be addressed through prioritized remediation.",
            styles['BodyText']
        ))
    
    story.append(PageBreak())
    
    # =========================================================================
    # CONTROL TOWER ASSESSMENT DETAILS
    # =========================================================================
    story.append(Paragraph("4. Control Tower Assessment", styles['SectionTitle']))
    
    story.append(Paragraph(
        "AWS Control Tower provides the easiest way to set up and govern a secure, multi-account "
        "AWS environment. This section evaluates organizational readiness across 12 key domains.",
        styles['BodyText']
    ))
    
    # Overall CT metrics
    ct_metrics = [
        ['Metric', 'Value'],
        ['Overall Score', f'{ct_scores["overall"]:.1f}%'],
        ['Maturity Level', get_maturity(ct_scores["overall"])[0]],
        ['Questions Answered', f'{ct_scores["total_answered"]} / {ct_scores["total_questions"]}'],
        ['Completion Rate', f'{(ct_scores["total_answered"]/ct_scores["total_questions"]*100):.0f}%'],
        ['Critical Gaps', str(critical_ct)],
        ['High Priority Gaps', str(high_ct)],
    ]
    
    ct_metrics_table = Table(ct_metrics, colWidths=[2.5*inch, 2*inch])
    ct_metrics_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 0.5, border_gray),
        ('BACKGROUND', (0, 1), (-1, -1), light_gray),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(ct_metrics_table)
    
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("4.1 Domain Analysis", styles['SubSectionTitle']))
    
    # Add Domain Radar Chart
    if ct_scores["total_answered"] > 0:
        try:
            ct_radar_img = create_radar_chart(ct_scores["domains"], "Control Tower Domain Maturity", color='#0284c7')
            story.append(Image(ct_radar_img, width=5*inch, height=5*inch))
        except Exception as e:
            pass
    
    story.append(Spacer(1, 0.2*inch))
    
    # Add Horizontal Bar Chart for domains
    if ct_scores["total_answered"] > 0:
        try:
            ct_bar_img = create_horizontal_bar_chart(ct_scores["domains"], "Control Tower Domain Scores", color='#0284c7')
            story.append(Image(ct_bar_img, width=6.5*inch, height=4*inch))
        except Exception as e:
            pass
    
    story.append(Spacer(1, 0.2*inch))
    
    # Domain scores table
    domain_data = [['Domain', 'Score', 'Maturity', 'Answered', 'Weight']]
    for dname, data in ct_scores["domains"].items():
        level = get_maturity(data["score"])[0]
        domain_data.append([
            dname[:35] + "..." if len(dname) > 35 else dname,
            f'{data["score"]:.0f}%',
            level,
            f'{data["answered"]}/{data["total"]}',
            f'{data["weight"]*100:.0f}%'
        ])
    
    domain_table = Table(domain_data, colWidths=[2.25*inch, 0.75*inch, 1*inch, 1*inch, 0.75*inch])
    domain_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), aws_dark),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, border_gray),
        ('BACKGROUND', (0, 1), (-1, -1), light_gray),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(domain_table)
    
    story.append(PageBreak())
    
    # Detailed domain findings
    story.append(Paragraph("4.2 Detailed Domain Findings", styles['SubSectionTitle']))
    
    for dname, ddata in ct_questions.items():
        if dname not in ct_scores["domains"]:
            continue
        domain_score = ct_scores["domains"][dname]
        
        story.append(Paragraph(f"<b>{dname}</b>", styles['DomainTitle']))
        story.append(Paragraph(f"<i>{ddata['description']}</i>", styles['SmallText']))
        story.append(Paragraph(
            f"Score: {domain_score['score']:.0f}% | Maturity: {get_maturity(domain_score['score'])[0]} | "
            f"Answered: {domain_score['answered']}/{domain_score['total']}",
            styles['SmallText']
        ))
        
        # Show questions with low scores (gaps)
        low_score_questions = [q for q in ddata['questions'] if q['id'] in ct_responses and ct_responses[q['id']] <= 2]
        if low_score_questions:
            story.append(Paragraph("<font color='#DC2626'>Identified Gaps:</font>", styles['SmallText']))
            for q in low_score_questions[:3]:  # Limit to 3 per domain
                score = ct_responses.get(q['id'], 0)
                story.append(Paragraph(
                    f"• [{q['risk'].upper()}] {q['question'][:100]}... (Score: {score}/5)",
                    styles['QuestionText']
                ))
        
        story.append(Spacer(1, 0.1*inch))
    
    story.append(PageBreak())
    
    # =========================================================================
    # GOLDEN ARCHITECTURE ASSESSMENT DETAILS
    # =========================================================================
    story.append(Paragraph("5. Golden Architecture Assessment", styles['SectionTitle']))
    
    story.append(Paragraph(
        "The Golden Architecture assessment evaluates serverless and event-driven architecture "
        "maturity. This modern approach enables scalability, cost efficiency, and operational excellence.",
        styles['BodyText']
    ))
    
    # Overall GA metrics
    ga_metrics = [
        ['Metric', 'Value'],
        ['Overall Score', f'{ga_scores["overall"]:.1f}%'],
        ['Maturity Level', get_maturity(ga_scores["overall"])[0]],
        ['Questions Answered', f'{ga_scores["total_answered"]} / {ga_scores["total_questions"]}'],
        ['Completion Rate', f'{(ga_scores["total_answered"]/ga_scores["total_questions"]*100):.0f}%'],
        ['Critical Gaps', str(critical_ga)],
        ['High Priority Gaps', str(high_ga)],
    ]
    
    ga_metrics_table = Table(ga_metrics, colWidths=[2.5*inch, 2*inch])
    ga_metrics_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), aws_orange),
        ('TEXTCOLOR', (0, 0), (-1, 0), aws_dark),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 0.5, border_gray),
        ('BACKGROUND', (0, 1), (-1, -1), light_gray),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(ga_metrics_table)
    
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("5.1 Domain Analysis", styles['SubSectionTitle']))
    
    # Add Domain Radar Chart for Golden Architecture
    if ga_scores["total_answered"] > 0:
        try:
            ga_radar_img = create_radar_chart(ga_scores["domains"], "Golden Architecture Domain Maturity", color='#7c3aed')
            story.append(Image(ga_radar_img, width=5*inch, height=5*inch))
        except Exception as e:
            pass
    
    story.append(Spacer(1, 0.2*inch))
    
    # Add Horizontal Bar Chart for GA domains
    if ga_scores["total_answered"] > 0:
        try:
            ga_bar_img = create_horizontal_bar_chart(ga_scores["domains"], "Golden Architecture Domain Scores", color='#7c3aed')
            story.append(Image(ga_bar_img, width=6.5*inch, height=3.5*inch))
        except Exception as e:
            pass
    
    story.append(Spacer(1, 0.2*inch))
    
    # Domain scores table
    ga_domain_data = [['Domain', 'Score', 'Maturity', 'Answered', 'Weight']]
    for dname, data in ga_scores["domains"].items():
        level = get_maturity(data["score"])[0]
        ga_domain_data.append([
            dname[:35] + "..." if len(dname) > 35 else dname,
            f'{data["score"]:.0f}%',
            level,
            f'{data["answered"]}/{data["total"]}',
            f'{data["weight"]*100:.0f}%'
        ])
    
    ga_domain_table = Table(ga_domain_data, colWidths=[2.25*inch, 0.75*inch, 1*inch, 1*inch, 0.75*inch])
    ga_domain_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), aws_dark),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, border_gray),
        ('BACKGROUND', (0, 1), (-1, -1), light_gray),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(ga_domain_table)
    
    story.append(PageBreak())
    
    # Detailed domain findings for GA
    story.append(Paragraph("5.2 Detailed Domain Findings", styles['SubSectionTitle']))
    
    for dname, ddata in ga_questions.items():
        if dname not in ga_scores["domains"]:
            continue
        domain_score = ga_scores["domains"][dname]
        
        story.append(Paragraph(f"<b>{dname}</b>", styles['DomainTitle']))
        story.append(Paragraph(f"<i>{ddata['description']}</i>", styles['SmallText']))
        story.append(Paragraph(
            f"Score: {domain_score['score']:.0f}% | Maturity: {get_maturity(domain_score['score'])[0]} | "
            f"Answered: {domain_score['answered']}/{domain_score['total']}",
            styles['SmallText']
        ))
        
        # Show questions with low scores (gaps)
        low_score_questions = [q for q in ddata['questions'] if q['id'] in ga_responses and ga_responses[q['id']] <= 2]
        if low_score_questions:
            story.append(Paragraph("<font color='#DC2626'>Identified Gaps:</font>", styles['SmallText']))
            for q in low_score_questions[:3]:
                score = ga_responses.get(q['id'], 0)
                story.append(Paragraph(
                    f"• [{q['risk'].upper()}] {q['question'][:100]}... (Score: {score}/5)",
                    styles['QuestionText']
                ))
        
        story.append(Spacer(1, 0.1*inch))
    
    story.append(PageBreak())
    
    # =========================================================================
    # GAP ANALYSIS
    # =========================================================================
    story.append(Paragraph("6. Gap Analysis", styles['SectionTitle']))
    
    story.append(Paragraph(
        "This section details identified gaps prioritized by risk level. Gaps are questions "
        "scored at 2 or below (Initial or Developing maturity). Addressing these gaps should "
        "be the primary focus of improvement efforts.",
        styles['BodyText']
    ))
    
    all_gaps = ct_gaps + ga_gaps
    
    # Add Gap Distribution Pie Chart
    try:
        gap_pie_img = create_gap_pie_chart(ct_gaps, ga_gaps)
        story.append(Image(gap_pie_img, width=5*inch, height=3.75*inch))
    except Exception as e:
        pass
    
    story.append(Spacer(1, 0.2*inch))
    
    # Critical Gaps
    story.append(Paragraph("6.1 Critical Gaps", styles['SubSectionTitle']))
    critical_gaps = [g for g in all_gaps if g['risk'] == 'critical']
    
    if critical_gaps:
        story.append(Paragraph(
            f"<font color='#DC2626'><b>{len(critical_gaps)} critical gap(s) identified requiring immediate attention.</b></font>",
            styles['BodyText']
        ))
        
        for gap in critical_gaps[:10]:
            story.append(Paragraph(f"<b>{gap['id']}</b> - {gap['domain']}", styles['DomainTitle']))
            story.append(Paragraph(f"Question: {gap['question']}", styles['QuestionText']))
            if gap.get('context'):
                story.append(Paragraph(f"<i>Impact: {gap['context'][:200]}...</i>", styles['SmallText']))
            story.append(Paragraph(f"Current Score: {gap['score']}/5 | Target: 4-5", styles['SmallText']))
            story.append(Spacer(1, 0.1*inch))
    else:
        story.append(Paragraph("No critical gaps identified.", styles['BodyText']))
    
    story.append(PageBreak())
    
    # High Priority Gaps
    story.append(Paragraph("6.2 High Priority Gaps", styles['SubSectionTitle']))
    high_gaps = [g for g in all_gaps if g['risk'] == 'high']
    
    if high_gaps:
        story.append(Paragraph(
            f"<font color='#EA580C'><b>{len(high_gaps)} high priority gap(s) identified.</b></font>",
            styles['BodyText']
        ))
        
        for gap in high_gaps[:10]:
            story.append(Paragraph(f"<b>{gap['id']}</b> - {gap['domain']}", styles['DomainTitle']))
            story.append(Paragraph(f"Question: {gap['question']}", styles['QuestionText']))
            story.append(Paragraph(f"Current Score: {gap['score']}/5", styles['SmallText']))
            story.append(Spacer(1, 0.05*inch))
    else:
        story.append(Paragraph("No high priority gaps identified.", styles['BodyText']))
    
    # Medium Priority Gaps
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("6.3 Medium Priority Gaps", styles['SubSectionTitle']))
    medium_gaps = [g for g in all_gaps if g['risk'] == 'medium']
    
    if medium_gaps:
        story.append(Paragraph(
            f"<font color='#CA8A04'><b>{len(medium_gaps)} medium priority gap(s) identified.</b></font>",
            styles['BodyText']
        ))
        
        # List in compact format
        for gap in medium_gaps[:15]:
            story.append(Paragraph(
                f"• <b>{gap['id']}</b>: {gap['question'][:80]}... (Score: {gap['score']}/5)",
                styles['QuestionText']
            ))
    else:
        story.append(Paragraph("No medium priority gaps identified.", styles['BodyText']))
    
    story.append(PageBreak())
    
    # =========================================================================
    # INDUSTRY BENCHMARK
    # =========================================================================
    story.append(Paragraph("7. Industry Benchmark Comparison", styles['SectionTitle']))
    
    story.append(Paragraph(
        f"This section compares your assessment results against industry benchmarks for the "
        f"<b>{bench['name']}</b> sector.",
        styles['BodyText']
    ))
    
    # Add Industry Comparison Bar Chart
    try:
        industry_chart_img = create_industry_comparison_chart(combined, benchmarks, industry)
        story.append(Image(industry_chart_img, width=6.5*inch, height=4*inch))
    except Exception as e:
        pass
    
    story.append(Spacer(1, 0.2*inch))
    
    # All industries comparison
    story.append(Paragraph("Cross-Industry Comparison", styles['SubSectionTitle']))
    
    industry_data = [['Industry', 'Average', 'Top Performers', 'Your Score', 'Variance']]
    for ind_key, ind_data in benchmarks.items():
        var = combined - ind_data['avg']
        industry_data.append([
            ind_data['name'],
            f"{ind_data['avg']}%",
            f"{ind_data['top']}%",
            f'{combined:.0f}%',
            f'{var:+.0f}%'
        ])
    
    industry_table = Table(industry_data, colWidths=[2*inch, 1*inch, 1.25*inch, 1*inch, 1*inch])
    industry_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), aws_dark),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, border_gray),
        ('BACKGROUND', (0, 1), (-1, -1), light_gray),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(industry_table)
    
    story.append(Spacer(1, 0.3*inch))
    
    # Key insights
    story.append(Paragraph("Benchmark Insights", styles['SubSectionTitle']))
    
    insights = []
    if combined >= bench['top']:
        insights.append(f"• <b>Top Performer:</b> Your score exceeds the top performer benchmark of {bench['top']}%.")
    elif combined >= bench['avg']:
        insights.append(f"• <b>Above Average:</b> Your score exceeds the industry average by {combined - bench['avg']:.0f}%.")
        insights.append(f"• <b>Path to Excellence:</b> {bench['top'] - combined:.0f}% improvement needed to reach top performer status.")
    else:
        insights.append(f"• <b>Below Average:</b> Your score is {bench['avg'] - combined:.0f}% below the industry average.")
        insights.append(f"• <b>Priority Focus:</b> Address critical and high-priority gaps to improve competitive position.")
    
    for insight in insights:
        story.append(Paragraph(insight, styles['BodyText']))
    
    story.append(PageBreak())
    
    # =========================================================================
    # MATURITY ROADMAP
    # =========================================================================
    story.append(Paragraph("8. Maturity Roadmap", styles['SectionTitle']))
    
    # Add Maturity Roadmap Visualization
    try:
        roadmap_img = create_maturity_roadmap_chart()
        story.append(Image(roadmap_img, width=7*inch, height=3*inch))
    except Exception as e:
        pass
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph(
        "This roadmap provides a phased approach to improving maturity across assessed domains. "
        "Timeline estimates are based on typical enterprise implementations.",
        styles['BodyText']
    ))
    
    # Phase 1: Foundation (0-3 months)
    story.append(Paragraph("Phase 1: Foundation (0-3 months)", styles['SubSectionTitle']))
    story.append(Paragraph(
        "Focus on addressing critical gaps and establishing foundational governance:",
        styles['BodyText']
    ))
    foundation_items = [
        "• Remediate all critical security and compliance gaps",
        "• Document and formalize multi-account strategy",
        "• Establish Cloud Center of Excellence (CCoE)",
        "• Implement basic guardrails and preventive controls",
        "• Deploy centralized logging and monitoring",
    ]
    for item in foundation_items:
        story.append(Paragraph(item, styles['QuestionText']))
    
    story.append(Spacer(1, 0.15*inch))
    
    # Phase 2: Standardization (3-6 months)
    story.append(Paragraph("Phase 2: Standardization (3-6 months)", styles['SubSectionTitle']))
    story.append(Paragraph(
        "Establish consistent processes and expand Control Tower adoption:",
        styles['BodyText']
    ))
    standard_items = [
        "• Deploy Control Tower with customized guardrails",
        "• Implement Account Factory for standardized provisioning",
        "• Establish OU hierarchy aligned with business structure",
        "• Deploy detective controls and security automation",
        "• Begin serverless pattern adoption for new workloads",
    ]
    for item in standard_items:
        story.append(Paragraph(item, styles['QuestionText']))
    
    story.append(Spacer(1, 0.15*inch))
    
    # Phase 3: Optimization (6-12 months)
    story.append(Paragraph("Phase 3: Optimization (6-12 months)", styles['SubSectionTitle']))
    story.append(Paragraph(
        "Optimize operations and expand advanced capabilities:",
        styles['BodyText']
    ))
    optimize_items = [
        "• Migrate existing accounts into Control Tower management",
        "• Implement advanced cost optimization and FinOps practices",
        "• Deploy comprehensive serverless observability",
        "• Establish self-service capabilities with guardrails",
        "• Implement continuous compliance and drift detection",
    ]
    for item in optimize_items:
        story.append(Paragraph(item, styles['QuestionText']))
    
    story.append(Spacer(1, 0.15*inch))
    
    # Phase 4: Excellence (12+ months)
    story.append(Paragraph("Phase 4: Excellence (12+ months)", styles['SubSectionTitle']))
    story.append(Paragraph(
        "Achieve industry-leading practices and continuous improvement:",
        styles['BodyText']
    ))
    excellence_items = [
        "• Policy-as-Code with automated enforcement",
        "• Full event-driven architecture adoption",
        "• Advanced ML/AI for operations optimization",
        "• Continuous maturity assessment and improvement",
        "• Knowledge sharing and industry thought leadership",
    ]
    for item in excellence_items:
        story.append(Paragraph(item, styles['QuestionText']))
    
    story.append(PageBreak())
    
    # =========================================================================
    # IMPLEMENTATION RECOMMENDATIONS
    # =========================================================================
    story.append(Paragraph("9. Implementation Recommendations", styles['SectionTitle']))
    
    story.append(Paragraph(
        "Based on the assessment results, the following prioritized recommendations are provided:",
        styles['BodyText']
    ))
    
    # Quick Wins
    story.append(Paragraph("Quick Wins (0-30 days)", styles['SubSectionTitle']))
    quick_wins = [
        ("Enable AWS CloudTrail", "Centralize audit logging across all accounts", "Low", "1-2 days"),
        ("Enable AWS Config", "Track configuration changes and compliance", "Low", "2-3 days"),
        ("Review IAM policies", "Identify and remediate overly permissive policies", "Medium", "1 week"),
        ("Enable GuardDuty", "Deploy threat detection across accounts", "Low", "1-2 days"),
        ("Document OU structure", "Formalize organizational unit hierarchy", "Low", "3-5 days"),
    ]
    
    quick_win_data = [['Action', 'Description', 'Effort', 'Timeline']]
    for qw in quick_wins:
        quick_win_data.append(list(qw))
    
    qw_table = Table(quick_win_data, colWidths=[1.5*inch, 2.5*inch, 0.75*inch, 1*inch])
    qw_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), success_green),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, border_gray),
        ('BACKGROUND', (0, 1), (-1, -1), light_gray),
        ('ALIGN', (2, 0), (-1, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(qw_table)
    
    story.append(Spacer(1, 0.2*inch))
    
    # Strategic Initiatives
    story.append(Paragraph("Strategic Initiatives (1-6 months)", styles['SubSectionTitle']))
    strategic = [
        ("Control Tower Deployment", "Deploy AWS Control Tower with customized guardrails", "High", "4-6 weeks"),
        ("Account Factory Setup", "Automate account provisioning with templates", "Medium", "2-3 weeks"),
        ("Security Hub Integration", "Centralize security findings and compliance", "Medium", "2-3 weeks"),
        ("Serverless Framework", "Establish serverless development standards", "Medium", "3-4 weeks"),
        ("Cost Optimization", "Implement FinOps practices and tools", "Medium", "4-6 weeks"),
    ]
    
    strategic_data = [['Initiative', 'Description', 'Effort', 'Timeline']]
    for s in strategic:
        strategic_data.append(list(s))
    
    s_table = Table(strategic_data, colWidths=[1.5*inch, 2.5*inch, 0.75*inch, 1*inch])
    s_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, border_gray),
        ('BACKGROUND', (0, 1), (-1, -1), light_gray),
        ('ALIGN', (2, 0), (-1, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(s_table)
    
    story.append(PageBreak())
    
    # =========================================================================
    # RISK ASSESSMENT
    # =========================================================================
    story.append(Paragraph("10. Risk Assessment", styles['SectionTitle']))
    
    story.append(Paragraph(
        "This section identifies key risks associated with the current assessment state and "
        "provides mitigation strategies.",
        styles['BodyText']
    ))
    
    # Risk matrix
    risks = [
        ["Security & Compliance", "HIGH" if critical_ct + critical_ga > 0 else "MEDIUM", 
         "Unaddressed critical gaps expose organization to security incidents and compliance failures",
         "Prioritize critical gap remediation; implement detective controls"],
        ["Operational Efficiency", "MEDIUM" if ct_scores["overall"] < 60 else "LOW",
         "Inconsistent governance leads to operational overhead and slow delivery",
         "Standardize through Control Tower; automate account provisioning"],
        ["Cost Management", "MEDIUM",
         "Lack of centralized visibility leads to cost overruns",
         "Deploy Cost Explorer; implement tagging strategy; enable budgets"],
        ["Skills Gap", "HIGH" if ga_scores["overall"] < 40 else "MEDIUM",
         "Limited serverless expertise constrains modernization",
         "Invest in training; partner with AWS; start with pilot projects"],
        ["Vendor Lock-in", "LOW",
         "Heavy AWS investment may limit flexibility",
         "Use abstraction layers; maintain multi-cloud strategy where needed"],
    ]
    
    risk_data = [['Risk Area', 'Level', 'Description', 'Mitigation']]
    for r in risks:
        risk_data.append(r)
    
    risk_table = Table(risk_data, colWidths=[1.25*inch, 0.6*inch, 2.25*inch, 2*inch])
    risk_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), aws_dark),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, border_gray),
        ('BACKGROUND', (0, 1), (-1, -1), light_gray),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(risk_table)
    
    story.append(PageBreak())
    
    # =========================================================================
    # AI ANALYSIS
    # =========================================================================
    story.append(Paragraph("11. AI-Powered Analysis", styles['SectionTitle']))
    
    if ai_analysis and not ai_analysis.startswith("⚠️"):
        story.append(Paragraph(
            "The following analysis was generated using AI to provide additional insights "
            "based on the assessment data:",
            styles['BodyText']
        ))
        story.append(Spacer(1, 0.2*inch))
        
        # Parse and format AI analysis (split into paragraphs)
        ai_paragraphs = ai_analysis.split('\n\n')
        for para in ai_paragraphs[:30]:  # Limit to prevent overflow
            if para.strip():
                # Clean up markdown formatting for PDF
                clean_para = para.replace('**', '').replace('##', '').replace('#', '').replace('*', '')
                if clean_para.strip():
                    story.append(Paragraph(clean_para.strip(), styles['BodyText']))
                    story.append(Spacer(1, 0.1*inch))
    else:
        story.append(Paragraph(
            "AI analysis has not been generated for this assessment. Generate AI insights "
            "from the AI Insights tab to include detailed recommendations in future reports.",
            styles['BodyText']
        ))
    
    story.append(PageBreak())
    
    # =========================================================================
    # APPENDIX A: Question Details
    # =========================================================================
    story.append(Paragraph("Appendix A: Assessment Question Details", styles['SectionTitle']))
    
    story.append(Paragraph(
        "This appendix provides a summary of all assessment questions with responses.",
        styles['BodyText']
    ))
    
    story.append(Paragraph("Control Tower Questions", styles['SubSectionTitle']))
    
    ct_question_data = [['ID', 'Domain', 'Risk', 'Score']]
    for dname, ddata in ct_questions.items():
        for q in ddata['questions']:
            score = ct_responses.get(q['id'], '-')
            if score != '-':
                score = f"{score}/5"
            ct_question_data.append([q['id'], dname[:20], q['risk'].upper(), str(score)])
    
    # Split into chunks to avoid page overflow
    chunk_size = 30
    for i in range(0, len(ct_question_data), chunk_size):
        chunk = ct_question_data[i:i+chunk_size]
        if i > 0:
            chunk.insert(0, ['ID', 'Domain', 'Risk', 'Score'])
        
        ct_q_table = Table(chunk, colWidths=[1*inch, 2.5*inch, 0.75*inch, 0.75*inch])
        ct_q_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), aws_dark),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 7),
            ('GRID', (0, 0), (-1, -1), 0.5, border_gray),
            ('BACKGROUND', (0, 1), (-1, -1), light_gray),
            ('ALIGN', (2, 0), (-1, -1), 'CENTER'),
            ('TOPPADDING', (0, 0), (-1, -1), 3),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ]))
        story.append(ct_q_table)
        story.append(Spacer(1, 0.1*inch))
    
    story.append(PageBreak())
    
    story.append(Paragraph("Golden Architecture Questions", styles['SubSectionTitle']))
    
    ga_question_data = [['ID', 'Domain', 'Risk', 'Score']]
    for dname, ddata in ga_questions.items():
        for q in ddata['questions']:
            score = ga_responses.get(q['id'], '-')
            if score != '-':
                score = f"{score}/5"
            ga_question_data.append([q['id'], dname[:20], q['risk'].upper(), str(score)])
    
    for i in range(0, len(ga_question_data), chunk_size):
        chunk = ga_question_data[i:i+chunk_size]
        if i > 0:
            chunk.insert(0, ['ID', 'Domain', 'Risk', 'Score'])
        
        ga_q_table = Table(chunk, colWidths=[1*inch, 2.5*inch, 0.75*inch, 0.75*inch])
        ga_q_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), aws_dark),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 7),
            ('GRID', (0, 0), (-1, -1), 0.5, border_gray),
            ('BACKGROUND', (0, 1), (-1, -1), light_gray),
            ('ALIGN', (2, 0), (-1, -1), 'CENTER'),
            ('TOPPADDING', (0, 0), (-1, -1), 3),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ]))
        story.append(ga_q_table)
        story.append(Spacer(1, 0.1*inch))
    
    story.append(PageBreak())
    
    # =========================================================================
    # APPENDIX B: Scoring Methodology
    # =========================================================================
    story.append(Paragraph("Appendix B: Scoring Methodology", styles['SectionTitle']))
    
    story.append(Paragraph(
        "This appendix details the scoring methodology used in this assessment.",
        styles['BodyText']
    ))
    
    story.append(Paragraph("Maturity Levels", styles['SubSectionTitle']))
    
    maturity_levels = [
        ['Level', 'Score Range', 'Characteristics'],
        ['Initial', '0-20%', 'Ad-hoc processes, reactive approach, minimal documentation'],
        ['Developing', '21-40%', 'Basic processes emerging, inconsistent implementation'],
        ['Defined', '41-60%', 'Documented processes, partial organizational adoption'],
        ['Managed', '61-80%', 'Consistent implementation, metrics-driven improvement'],
        ['Optimized', '81-100%', 'Industry-leading, continuous optimization, automation'],
    ]
    
    maturity_table = Table(maturity_levels, colWidths=[1.25*inch, 1*inch, 3.75*inch])
    maturity_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), aws_dark),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, border_gray),
        ('BACKGROUND', (0, 1), (-1, -1), light_gray),
        ('ALIGN', (1, 0), (1, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(maturity_table)
    
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("Risk Prioritization", styles['SubSectionTitle']))
    
    risk_levels = [
        ['Risk Level', 'Definition', 'Response Time'],
        ['Critical', 'Immediate security or compliance exposure', 'Immediate (0-7 days)'],
        ['High', 'Significant operational or security risk', 'Short-term (1-4 weeks)'],
        ['Medium', 'Moderate impact on efficiency or compliance', 'Medium-term (1-3 months)'],
        ['Low', 'Minor improvement opportunity', 'Long-term (3-6 months)'],
    ]
    
    risk_table = Table(risk_levels, colWidths=[1.25*inch, 2.75*inch, 2*inch])
    risk_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), aws_dark),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 0.5, border_gray),
        ('BACKGROUND', (0, 1), (0, 1), colors.HexColor('#FEE2E2')),
        ('BACKGROUND', (0, 2), (0, 2), colors.HexColor('#FFEDD5')),
        ('BACKGROUND', (0, 3), (0, 3), colors.HexColor('#FEF3C7')),
        ('BACKGROUND', (0, 4), (0, 4), colors.HexColor('#DCFCE7')),
        ('BACKGROUND', (1, 1), (-1, -1), light_gray),
        ('ALIGN', (2, 0), (2, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(risk_table)
    
    story.append(Spacer(1, 0.3*inch))
    
    story.append(Paragraph("Domain Weights", styles['SubSectionTitle']))
    
    story.append(Paragraph(
        "Domain scores are weighted based on their relative importance to overall enterprise readiness. "
        "The overall score is calculated as the weighted average of individual domain scores.",
        styles['BodyText']
    ))
    
    # Footer
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph(
        f"<b>Report Generated:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | "
        f"<b>Platform Version:</b> AWS Enterprise Assessment Platform v3.0",
        styles['Footer']
    ))
    story.append(Paragraph(
        f"© {datetime.now().year} AWS Enterprise Assessment Platform - Confidential",
        styles['Footer']
    ))
    
    # Build PDF
    doc.build(story)
    
    buffer.seek(0)
    return buffer.getvalue()

# =============================================================================
# MAIN APPLICATION
# =============================================================================
def main():
    init_state()
    
    # Calculate stats for header
    ct_total = count_questions(CT_QUESTIONS)
    ga_total = count_questions(GA_QUESTIONS)
    ct_answered = count_answered(st.session_state.ct_responses)
    ga_answered = count_answered(st.session_state.ga_responses)
    total_domains = len(CT_QUESTIONS) + len(GA_QUESTIONS)
    
    # Professional Header
    st.markdown(f'''
    <div class="main-header">
        <h1>☁️ AWS Enterprise Assessment Platform <span class="header-badge">ENTERPRISE v3.0</span></h1>
        <p>Comprehensive Control Tower Migration & Golden Architecture (Serverless) Readiness Assessment</p>
        <div class="header-stats">
            <div class="header-stat">
                <div class="header-stat-value">{ct_total + ga_total}</div>
                <div class="header-stat-label">Questions</div>
            </div>
            <div class="header-stat">
                <div class="header-stat-value">{total_domains}</div>
                <div class="header-stat-label">Domains</div>
            </div>
            <div class="header-stat">
                <div class="header-stat-value">{ct_answered + ga_answered}</div>
                <div class="header-stat-label">Answered</div>
            </div>
            <div class="header-stat">
                <div class="header-stat-value">{((ct_answered + ga_answered) / (ct_total + ga_total) * 100):.0f}%</div>
                <div class="header-stat-label">Complete</div>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("### ⚙️ Assessment Configuration")
        st.session_state.org_name = st.text_input("Organization Name", st.session_state.org_name, placeholder="Enter organization name")
        st.session_state.assessor_name = st.text_input("Assessor Name", st.session_state.assessor_name, placeholder="Enter assessor name")
        st.session_state.industry = st.selectbox(
            "Industry Vertical",
            options=list(BENCHMARKS.keys()),
            format_func=lambda x: BENCHMARKS[x]["name"],
            index=list(BENCHMARKS.keys()).index(st.session_state.industry)
        )
        
        st.markdown("### 📊 Assessment Progress")
        
        # Control Tower Progress
        ct_pct = (ct_answered / ct_total * 100) if ct_total > 0 else 0
        st.markdown(f"**Control Tower** ({ct_answered}/{ct_total})")
        st.progress(ct_pct / 100)
        
        # Golden Architecture Progress
        ga_pct = (ga_answered / ga_total * 100) if ga_total > 0 else 0
        st.markdown(f"**Golden Architecture** ({ga_answered}/{ga_total})")
        st.progress(ga_pct / 100)
        
        st.markdown("---")
        
        # Summary metrics
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total", ct_total + ga_total)
        with col2:
            st.metric("Answered", ct_answered + ga_answered)
        
        st.markdown("---")
        
        # Reset button
        if st.button("🔄 Reset Assessment", type="secondary", use_container_width=True):
            st.session_state.ct_responses = {}
            st.session_state.ga_responses = {}
            st.session_state.ai_analysis = None
            st.session_state.report = None
            st.rerun()
    
    # Main Tabs
    tabs = st.tabs([
        "📊 Executive Dashboard",
        "🎛️ Control Tower",
        "⚡ Golden Architecture",
        "🔍 Gap Analysis",
        "🤖 AI Insights",
        "📄 Reports & Export"
    ])
    
    # ==========================================================================
    # TAB 1: Executive Dashboard
    # ==========================================================================
    with tabs[0]:
        st.markdown('''
        <div class="section-header">
            <div class="section-icon">📊</div>
            <div>
                <div class="section-title">Executive Dashboard</div>
                <div class="section-subtitle">Real-time assessment scores and maturity analysis</div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        ct_scores = calc_scores(st.session_state.ct_responses, CT_QUESTIONS)
        ga_scores = calc_scores(st.session_state.ga_responses, GA_QUESTIONS)
        combined = (ct_scores["overall"] + ga_scores["overall"]) / 2 if (ct_scores["overall"] > 0 or ga_scores["overall"] > 0) else 0
        bench = BENCHMARKS[st.session_state.industry]
        
        # Metric Cards
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            render_metric_card(ct_scores["overall"], "Control Tower Score")
        with col2:
            render_metric_card(ga_scores["overall"], "Golden Architecture Score")
        with col3:
            render_metric_card(combined, "Combined Enterprise Score")
        with col4:
            # Check if any questions have been answered
            has_responses = ct_scores["total_answered"] > 0 or ga_scores["total_answered"] > 0
            if has_responses:
                vs_avg = combined - bench["avg"]
                st.markdown(f'''
                <div class="metric-card">
                    <div class="metric-value" style="background: linear-gradient(135deg, {'#059669' if vs_avg >= 0 else '#dc2626'} 0%, {'#10b981' if vs_avg >= 0 else '#ef4444'} 100%); -webkit-background-clip: text; background-clip: text;">{vs_avg:+.0f}%</div>
                    <div class="metric-label">vs {bench["name"]} Average</div>
                    <div class="metric-badge badge-neutral">Industry Benchmark: {bench["avg"]}%</div>
                </div>
                ''', unsafe_allow_html=True)
            else:
                st.markdown(f'''
                <div class="metric-card">
                    <div class="metric-value">N/A</div>
                    <div class="metric-label">vs {bench["name"]} Average</div>
                    <div class="metric-badge badge-neutral">Industry Benchmark: {bench["avg"]}%</div>
                </div>
                ''', unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Interactive Score Gauges
        st.markdown("#### 📈 Score Overview")
        try:
            gauge_fig = create_ui_score_gauges(
                ct_scores["overall"], 
                ga_scores["overall"], 
                combined, 
                bench["avg"],
                bench["name"]
            )
            st.plotly_chart(gauge_fig, use_container_width=True)
        except Exception as e:
            st.warning(f"Could not render gauge charts: {e}")
        
        # Maturity Progress Chart
        st.markdown("#### 📊 Maturity Progress")
        try:
            progress_fig = create_ui_maturity_progress_chart(
                ct_scores["overall"],
                ga_scores["overall"],
                combined,
                bench["avg"]
            )
            st.plotly_chart(progress_fig, use_container_width=True)
        except Exception as e:
            pass
        
        st.markdown("---")
        
        # Domain Analysis Charts
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🎛️ Control Tower Domains")
            if ct_scores["total_answered"] > 0:
                try:
                    ct_radar_fig = create_ui_radar_chart(ct_scores["domains"], "Control Tower Domain Maturity", "#0284c7")
                    st.plotly_chart(ct_radar_fig, use_container_width=True)
                except Exception as e:
                    st.warning(f"Could not render radar chart: {e}")
                
                try:
                    ct_bar_fig = create_ui_horizontal_bar_chart(ct_scores["domains"], "Domain Scores", "#0284c7")
                    st.plotly_chart(ct_bar_fig, use_container_width=True)
                except Exception as e:
                    pass
            else:
                st.info("📝 Complete Control Tower assessment questions to see domain analysis")
        
        with col2:
            st.markdown("#### ⚡ Golden Architecture Domains")
            if ga_scores["total_answered"] > 0:
                try:
                    ga_radar_fig = create_ui_radar_chart(ga_scores["domains"], "Golden Architecture Domain Maturity", "#7c3aed")
                    st.plotly_chart(ga_radar_fig, use_container_width=True)
                except Exception as e:
                    st.warning(f"Could not render radar chart: {e}")
                
                try:
                    ga_bar_fig = create_ui_horizontal_bar_chart(ga_scores["domains"], "Domain Scores", "#7c3aed")
                    st.plotly_chart(ga_bar_fig, use_container_width=True)
                except Exception as e:
                    pass
            else:
                st.info("📝 Complete Golden Architecture assessment questions to see domain analysis")
        
        st.markdown("---")
        
        # Industry Benchmark Comparison
        st.markdown("#### 🏆 Industry Benchmark Comparison")
        try:
            industry_fig = create_ui_industry_comparison_chart(combined, BENCHMARKS, st.session_state.industry)
            st.plotly_chart(industry_fig, use_container_width=True)
        except Exception as e:
            st.warning(f"Could not render industry comparison: {e}")
    
    # ==========================================================================
    # TAB 2: Control Tower Assessment
    # ==========================================================================
    with tabs[1]:
        st.markdown('''
        <div class="section-header">
            <div class="section-icon">🎛️</div>
            <div>
                <div class="section-title">Control Tower Migration Readiness</div>
                <div class="section-subtitle">Comprehensive assessment across 12 domains</div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Questions", ct_total)
        with col2:
            st.metric("Answered", ct_answered)
        with col3:
            st.metric("Completion", f"{ct_pct:.0f}%")
        with col4:
            st.metric("Domains", len(CT_QUESTIONS))
        
        st.info("💡 **Instructions:** Expand each domain and answer questions. Select '⊘ Not yet assessed' to skip. Progress is saved automatically.")
        st.markdown("---")
        
        render_questions(CT_QUESTIONS, st.session_state.ct_responses, "ct")
    
    # ==========================================================================
    # TAB 3: Golden Architecture Assessment
    # ==========================================================================
    with tabs[2]:
        st.markdown('''
        <div class="section-header">
            <div class="section-icon">⚡</div>
            <div>
                <div class="section-title">Golden Architecture (Serverless) Assessment</div>
                <div class="section-subtitle">Serverless maturity evaluation across 10 domains</div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Questions", ga_total)
        with col2:
            st.metric("Answered", ga_answered)
        with col3:
            st.metric("Completion", f"{ga_pct:.0f}%")
        with col4:
            st.metric("Domains", len(GA_QUESTIONS))
        
        st.info("💡 **Instructions:** Expand each domain and answer questions. Select '⊘ Not yet assessed' to skip. Progress is saved automatically.")
        st.markdown("---")
        
        render_questions(GA_QUESTIONS, st.session_state.ga_responses, "ga")
    
    # ==========================================================================
    # TAB 4: Gap Analysis
    # ==========================================================================
    with tabs[3]:
        st.markdown('''
        <div class="section-header">
            <div class="section-icon">🔍</div>
            <div>
                <div class="section-title">Gap Analysis & Prioritization</div>
                <div class="section-subtitle">Critical gaps requiring immediate attention</div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        ct_gaps = find_gaps(st.session_state.ct_responses, CT_QUESTIONS)
        ga_gaps = find_gaps(st.session_state.ga_responses, GA_QUESTIONS)
        
        # Gap Distribution Charts
        st.markdown("#### 📊 Gap Overview")
        col1, col2 = st.columns(2)
        
        with col1:
            try:
                gap_donut_fig = create_ui_gap_donut_chart(ct_gaps, ga_gaps)
                st.plotly_chart(gap_donut_fig, use_container_width=True)
            except Exception as e:
                st.warning(f"Could not render gap chart: {e}")
        
        with col2:
            # Summary metrics
            total_gaps = len(ct_gaps) + len(ga_gaps)
            crit_total = len([g for g in ct_gaps + ga_gaps if g["risk"] == "critical"])
            high_total = len([g for g in ct_gaps + ga_gaps if g["risk"] == "high"])
            med_total = len([g for g in ct_gaps + ga_gaps if g["risk"] == "medium"])
            
            st.markdown("""
            <div style="background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%); padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;">
                <h4 style="color: #dc2626; margin: 0 0 0.5rem 0;">🔴 Critical Gaps</h4>
                <p style="font-size: 2rem; font-weight: bold; color: #1e293b; margin: 0;">{}</p>
                <p style="color: #64748b; margin: 0;">Require immediate attention</p>
            </div>
            """.format(crit_total), unsafe_allow_html=True)
            
            st.markdown("""
            <div style="background: linear-gradient(135deg, #fff7ed 0%, #ffedd5 100%); padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem;">
                <h4 style="color: #ea580c; margin: 0 0 0.5rem 0;">🟠 High Priority</h4>
                <p style="font-size: 2rem; font-weight: bold; color: #1e293b; margin: 0;">{}</p>
                <p style="color: #64748b; margin: 0;">Address within 1-4 weeks</p>
            </div>
            """.format(high_total), unsafe_allow_html=True)
            
            st.markdown("""
            <div style="background: linear-gradient(135deg, #fefce8 0%, #fef3c7 100%); padding: 1.5rem; border-radius: 12px;">
                <h4 style="color: #d97706; margin: 0 0 0.5rem 0;">🟡 Medium Priority</h4>
                <p style="font-size: 2rem; font-weight: bold; color: #1e293b; margin: 0;">{}</p>
                <p style="color: #64748b; margin: 0;">Plan for 1-3 months</p>
            </div>
            """.format(med_total), unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Gap Heatmap
        if len(ct_gaps) + len(ga_gaps) > 0:
            st.markdown("#### 🗺️ Gap Heatmap by Domain")
            try:
                heatmap_fig = create_ui_gap_heatmap(ct_gaps, ga_gaps, CT_QUESTIONS, GA_QUESTIONS)
                st.plotly_chart(heatmap_fig, use_container_width=True)
            except Exception as e:
                pass
        
        st.markdown("---")
        
        # Detailed Gap Lists
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🎛️ Control Tower Gaps")
            
            if ct_gaps:
                crit = len([g for g in ct_gaps if g["risk"] == "critical"])
                high = len([g for g in ct_gaps if g["risk"] == "high"])
                med = len([g for g in ct_gaps if g["risk"] == "medium"])
                
                c1, c2, c3 = st.columns(3)
                with c1:
                    st.metric("🔴 Critical", crit)
                with c2:
                    st.metric("🟠 High", high)
                with c3:
                    st.metric("🟡 Medium", med)
                
                for g in ct_gaps[:10]:
                    risk_class = g["risk"]
                    st.markdown(f'''
                    <div class="gap-card {risk_class}">
                        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.5rem">
                            <strong style="color:var(--primary)">{g["id"]}</strong>
                            <span class="risk-badge risk-{risk_class}">{risk_class}</span>
                        </div>
                        <div style="color:var(--text-primary);font-weight:500;margin-bottom:0.25rem">{g["question"][:100]}...</div>
                        <div style="color:var(--text-muted);font-size:0.8rem">Score: {g["score"]}/5 • {g["domain"]}</div>
                    </div>
                    ''', unsafe_allow_html=True)
            else:
                if count_answered(st.session_state.ct_responses) > 0:
                    st.success("✅ No critical gaps identified! All answered questions scored above threshold.")
                else:
                    st.info("📝 Complete assessment questions to identify gaps")
        
        with col2:
            st.markdown("#### ⚡ Golden Architecture Gaps")
            
            if ga_gaps:
                crit = len([g for g in ga_gaps if g["risk"] == "critical"])
                high = len([g for g in ga_gaps if g["risk"] == "high"])
                med = len([g for g in ga_gaps if g["risk"] == "medium"])
                
                c1, c2, c3 = st.columns(3)
                with c1:
                    st.metric("🔴 Critical", crit)
                with c2:
                    st.metric("🟠 High", high)
                with c3:
                    st.metric("🟡 Medium", med)
                
                for g in ga_gaps[:10]:
                    risk_class = g["risk"]
                    st.markdown(f'''
                    <div class="gap-card {risk_class}">
                        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.5rem">
                            <strong style="color:var(--primary)">{g["id"]}</strong>
                            <span class="risk-badge risk-{risk_class}">{risk_class}</span>
                        </div>
                        <div style="color:var(--text-primary);font-weight:500;margin-bottom:0.25rem">{g["question"][:100]}...</div>
                        <div style="color:var(--text-muted);font-size:0.8rem">Score: {g["score"]}/5 • {g["domain"]}</div>
                    </div>
                    ''', unsafe_allow_html=True)
            else:
                if count_answered(st.session_state.ga_responses) > 0:
                    st.success("✅ No critical gaps identified! All answered questions scored above threshold.")
                else:
                    st.info("📝 Complete assessment questions to identify gaps")
    
    # ==========================================================================
    # TAB 5: AI Insights
    # ==========================================================================
    with tabs[4]:
        st.markdown('''
        <div class="section-header">
            <div class="section-icon">🤖</div>
            <div>
                <div class="section-title">AI-Powered Analysis</div>
                <div class="section-subtitle">Claude-powered recommendations and roadmap generation</div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        analysis_type = st.selectbox(
            "Select Analysis Type",
            options=[
                "🎯 Comprehensive Gap Analysis & Prioritization",
                "🗺️ 12-Month Implementation Roadmap",
                "⚠️ Risk Assessment Matrix",
                "💰 Cost-Benefit Analysis",
                "🏗️ Architecture Recommendations",
                "📋 Executive Summary for Leadership"
            ]
        )
        
        context = st.text_area(
            "Additional Context (optional)",
            placeholder="Provide any additional context such as:\n• Budget constraints\n• Timeline requirements\n• Team size and skills\n• Regulatory requirements\n• Current pain points",
            height=120
        )
        
        col1, col2 = st.columns([1, 3])
        with col1:
            generate_btn = st.button("🚀 Generate Analysis", type="primary", use_container_width=True)
        
        if generate_btn:
            total_answered = count_answered(st.session_state.ct_responses) + count_answered(st.session_state.ga_responses)
            
            if total_answered < 5:
                st.warning("⚠️ Please answer at least 5 questions to generate meaningful AI analysis.")
            else:
                with st.spinner("🔄 Generating comprehensive analysis... This may take 30-60 seconds."):
                    ct_scores = calc_scores(st.session_state.ct_responses, CT_QUESTIONS)
                    ga_scores = calc_scores(st.session_state.ga_responses, GA_QUESTIONS)
                    ct_gaps = find_gaps(st.session_state.ct_responses, CT_QUESTIONS)
                    ga_gaps = find_gaps(st.session_state.ga_responses, GA_QUESTIONS)
                    combined = (ct_scores["overall"] + ga_scores["overall"]) / 2
                    
                    prompt = f"""
# AWS Enterprise Assessment Analysis Request

## Analysis Type
{analysis_type}

## Organization Context
- **Organization:** {st.session_state.org_name or 'Not specified'}
- **Assessor:** {st.session_state.assessor_name or 'Not specified'}
- **Industry:** {BENCHMARKS[st.session_state.industry]['name']}
- **Industry Average:** {BENCHMARKS[st.session_state.industry]['avg']}%
- **Industry Top Quartile:** {BENCHMARKS[st.session_state.industry]['top']}%

## Assessment Results

### Control Tower Assessment
- **Overall Score:** {ct_scores['overall']:.1f}%
- **Maturity Level:** {get_maturity(ct_scores['overall'])[0]}
- **Questions Answered:** {ct_scores['total_answered']}/{ct_scores['total_questions']}
- **Critical Gaps:** {len([g for g in ct_gaps if g['risk']=='critical'])}
- **High Priority Gaps:** {len([g for g in ct_gaps if g['risk']=='high'])}

**Domain Breakdown:**
{json.dumps({k: f"{v['score']:.0f}%" for k,v in ct_scores.get('domains',{}).items() if v['answered']>0}, indent=2)}

**Top Gaps (Critical & High):**
{json.dumps([{"id": g["id"], "question": g["question"][:80], "risk": g["risk"], "score": g["score"]} for g in ct_gaps[:8] if g["risk"] in ["critical", "high"]], indent=2)}

### Golden Architecture Assessment
- **Overall Score:** {ga_scores['overall']:.1f}%
- **Maturity Level:** {get_maturity(ga_scores['overall'])[0]}
- **Questions Answered:** {ga_scores['total_answered']}/{ga_scores['total_questions']}
- **Critical Gaps:** {len([g for g in ga_gaps if g['risk']=='critical'])}
- **High Priority Gaps:** {len([g for g in ga_gaps if g['risk']=='high'])}

**Domain Breakdown:**
{json.dumps({k: f"{v['score']:.0f}%" for k,v in ga_scores.get('domains',{}).items() if v['answered']>0}, indent=2)}

**Top Gaps (Critical & High):**
{json.dumps([{"id": g["id"], "question": g["question"][:80], "risk": g["risk"], "score": g["score"]} for g in ga_gaps[:8] if g["risk"] in ["critical", "high"]], indent=2)}

### Combined Assessment
- **Combined Score:** {combined:.1f}%
- **vs Industry Average:** {combined - BENCHMARKS[st.session_state.industry]['avg']:+.1f}%

## Additional Context from User
{context or 'None provided'}

## Instructions
Please provide a comprehensive analysis that includes:

1. **Executive Summary** (2-3 paragraphs)
   - Key findings and overall assessment
   - Comparison to industry benchmarks
   - Critical areas requiring immediate attention

2. **Detailed Analysis** based on the selected type above
   - Specific to the analysis type requested
   - Data-driven insights from assessment scores

3. **Prioritized Recommendations**
   - For each recommendation include:
     - Specific AWS services and configurations
     - Effort estimate (person-weeks)
     - Dependencies and prerequisites
     - Expected outcome/benefit

4. **Implementation Roadmap**
   - Quick wins (0-30 days)
   - Short-term (1-3 months)
   - Medium-term (3-6 months)
   - Long-term (6-12 months)

5. **Risk Considerations**
   - Technical risks
   - Organizational risks
   - Mitigation strategies

6. **Success Metrics**
   - KPIs to track progress
   - Target improvements
   - Measurement approach

Format with clear markdown headers and bullet points for readability.
"""
                    st.session_state.ai_analysis = call_claude(prompt)
        
        if st.session_state.ai_analysis:
            st.markdown("---")
            st.markdown('<div class="ai-response">', unsafe_allow_html=True)
            st.markdown(st.session_state.ai_analysis)
            st.markdown('</div>', unsafe_allow_html=True)
    
    # ==========================================================================
    # TAB 6: Reports & Export
    # ==========================================================================
    with tabs[5]:
        st.markdown('''
        <div class="section-header">
            <div class="section-icon">📄</div>
            <div>
                <div class="section-title">Reports & Export</div>
                <div class="section-subtitle">Generate comprehensive PDF reports and export assessment data</div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        ct_scores = calc_scores(st.session_state.ct_responses, CT_QUESTIONS)
        ga_scores = calc_scores(st.session_state.ga_responses, GA_QUESTIONS)
        combined = (ct_scores["overall"] + ga_scores["overall"]) / 2 if (ct_scores["overall"] > 0 or ga_scores["overall"] > 0) else 0
        
        # Summary metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            render_metric_card(ct_scores["overall"], "Control Tower")
        with col2:
            render_metric_card(ga_scores["overall"], "Golden Architecture")
        with col3:
            render_metric_card(combined, "Combined Score")
        with col4:
            total_ans = count_answered(st.session_state.ct_responses) + count_answered(st.session_state.ga_responses)
            total_q = count_questions(CT_QUESTIONS) + count_questions(GA_QUESTIONS)
            completion = (total_ans / total_q * 100) if total_q > 0 else 0
            render_metric_card(completion, "Completion")
        
        st.markdown("---")
        
        # PDF Report Section
        st.markdown("#### 📑 Comprehensive PDF Report")
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); padding: 1rem; border-radius: 12px; border-left: 4px solid #0284c7; margin-bottom: 1rem;">
            <p style="margin: 0; color: #0369a1;">
                <strong>Professional 30+ Page Report</strong> - Includes executive summary, detailed domain analysis, 
                gap assessment, industry benchmarks, maturity roadmap, implementation recommendations, and appendices.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📊 Generate Comprehensive PDF Report", type="primary", use_container_width=True):
                with st.spinner("Generating comprehensive PDF report... This may take a moment."):
                    try:
                        pdf_data = generate_pdf_report(
                            org_name=st.session_state.org_name,
                            assessor_name=st.session_state.assessor_name,
                            industry=st.session_state.industry,
                            ct_responses=st.session_state.ct_responses,
                            ga_responses=st.session_state.ga_responses,
                            ct_questions=CT_QUESTIONS,
                            ga_questions=GA_QUESTIONS,
                            benchmarks=BENCHMARKS,
                            ai_analysis=st.session_state.ai_analysis
                        )
                        st.session_state.pdf_report = pdf_data
                        st.success("✅ Comprehensive PDF report generated successfully! (~30 pages)")
                    except Exception as e:
                        st.error(f"Error generating PDF: {str(e)}")
        
        with col2:
            if 'pdf_report' in st.session_state and st.session_state.pdf_report:
                st.download_button(
                    "⬇️ Download PDF Report",
                    st.session_state.pdf_report,
                    f"AWS_Enterprise_Assessment_Report_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf",
                    "application/pdf",
                    use_container_width=True
                )
        
        st.markdown("---")
        
        # Markdown Report (Secondary option)
        st.markdown("#### 📝 Quick Markdown Report")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📄 Generate Markdown Summary", use_container_width=True):
                ct_gaps = find_gaps(st.session_state.ct_responses, CT_QUESTIONS)
                ga_gaps = find_gaps(st.session_state.ga_responses, GA_QUESTIONS)
                
                report = f"""# AWS Enterprise Assessment Report

## Executive Summary

| **Field** | **Value** |
|-----------|-----------|
| **Organization** | {st.session_state.org_name or 'Not specified'} |
| **Assessor** | {st.session_state.assessor_name or 'Not specified'} |
| **Assessment Date** | {datetime.now().strftime('%Y-%m-%d %H:%M')} |
| **Industry Vertical** | {BENCHMARKS[st.session_state.industry]['name']} |
| **Industry Benchmark** | {BENCHMARKS[st.session_state.industry]['avg']}% |

---

## Assessment Scores

| **Assessment** | **Score** | **Maturity Level** | **vs Industry** |
|----------------|-----------|-------------------|-----------------|
| Control Tower | {ct_scores['overall']:.1f}% | {get_maturity(ct_scores['overall'])[0]} | {ct_scores['overall'] - BENCHMARKS[st.session_state.industry]['avg']:+.1f}% |
| Golden Architecture | {ga_scores['overall']:.1f}% | {get_maturity(ga_scores['overall'])[0]} | {ga_scores['overall'] - BENCHMARKS[st.session_state.industry]['avg']:+.1f}% |
| **Combined** | **{combined:.1f}%** | **{get_maturity(combined)[0]}** | **{combined - BENCHMARKS[st.session_state.industry]['avg']:+.1f}%** |

---

## Gap Summary

### Control Tower
- 🔴 **Critical Gaps:** {len([g for g in ct_gaps if g['risk']=='critical'])}
- 🟠 **High Priority Gaps:** {len([g for g in ct_gaps if g['risk']=='high'])}
- 🟡 **Medium Priority Gaps:** {len([g for g in ct_gaps if g['risk']=='medium'])}

### Golden Architecture
- 🔴 **Critical Gaps:** {len([g for g in ga_gaps if g['risk']=='critical'])}
- 🟠 **High Priority Gaps:** {len([g for g in ga_gaps if g['risk']=='high'])}
- 🟡 **Medium Priority Gaps:** {len([g for g in ga_gaps if g['risk']=='medium'])}

---

## Domain Analysis

### Control Tower Domains
"""
                for dname, data in ct_scores["domains"].items():
                    if data["answered"] > 0:
                        report += f"- **{dname}**: {data['score']:.0f}% ({get_maturity(data['score'])[0]}) - {data['answered']}/{data['total']} answered\n"
                
                report += "\n### Golden Architecture Domains\n"
                for dname, data in ga_scores["domains"].items():
                    if data["answered"] > 0:
                        report += f"- **{dname}**: {data['score']:.0f}% ({get_maturity(data['score'])[0]}) - {data['answered']}/{data['total']} answered\n"
                
                report += f"""

---

## Top Priority Gaps

### Control Tower - Critical & High
"""
                for g in [gap for gap in ct_gaps if gap['risk'] in ['critical', 'high']][:5]:
                    report += f"- **{g['id']}** ({g['risk'].upper()}): {g['question']}\n"
                
                report += "\n### Golden Architecture - Critical & High\n"
                for g in [gap for gap in ga_gaps if gap['risk'] in ['critical', 'high']][:5]:
                    report += f"- **{g['id']}** ({g['risk'].upper()}): {g['question']}\n"
                
                report += f"""

---

## AI Analysis & Recommendations

{st.session_state.ai_analysis or '*Generate AI analysis in the AI Insights tab for detailed recommendations.*'}

---

## Assessment Completion

| **Category** | **Answered** | **Total** | **Completion** |
|--------------|--------------|-----------|----------------|
| Control Tower | {ct_scores['total_answered']} | {ct_scores['total_questions']} | {(ct_scores['total_answered']/ct_scores['total_questions']*100):.0f}% |
| Golden Architecture | {ga_scores['total_answered']} | {ga_scores['total_questions']} | {(ga_scores['total_answered']/ga_scores['total_questions']*100):.0f}% |
| **Total** | **{ct_scores['total_answered'] + ga_scores['total_answered']}** | **{ct_scores['total_questions'] + ga_scores['total_questions']}** | **{((ct_scores['total_answered'] + ga_scores['total_answered'])/(ct_scores['total_questions'] + ga_scores['total_questions'])*100):.0f}%** |

---

*Report generated by AWS Enterprise Assessment Platform v3.0*
*© {datetime.now().year} - Enterprise Cloud Assessment*
"""
                st.session_state.report = report
                st.success("✅ Markdown summary generated!")
        
        with col2:
            if st.session_state.report:
                st.download_button(
                    "⬇️ Download Markdown",
                    st.session_state.report,
                    f"aws_assessment_summary_{datetime.now().strftime('%Y%m%d_%H%M')}.md",
                    "text/markdown",
                    use_container_width=True
                )
        
        st.markdown("---")
        st.markdown("#### 📦 Data Export")
        
        # JSON Export
        export_data = {
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "platform_version": "3.0",
                "organization": st.session_state.org_name,
                "assessor": st.session_state.assessor_name,
                "industry": st.session_state.industry
            },
            "control_tower": {
                "responses": st.session_state.ct_responses,
                "scores": {k: v for k, v in ct_scores.items() if k != "domains"},
                "domain_scores": {k: {"score": v["score"], "answered": v["answered"], "total": v["total"]} 
                                 for k, v in ct_scores.get("domains", {}).items()},
                "gaps": [{"id": g["id"], "question": g["question"], "risk": g["risk"], "score": g["score"]} 
                        for g in find_gaps(st.session_state.ct_responses, CT_QUESTIONS)]
            },
            "golden_architecture": {
                "responses": st.session_state.ga_responses,
                "scores": {k: v for k, v in ga_scores.items() if k != "domains"},
                "domain_scores": {k: {"score": v["score"], "answered": v["answered"], "total": v["total"]} 
                                 for k, v in ga_scores.get("domains", {}).items()},
                "gaps": [{"id": g["id"], "question": g["question"], "risk": g["risk"], "score": g["score"]} 
                        for g in find_gaps(st.session_state.ga_responses, GA_QUESTIONS)]
            }
        }
        
        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                "📦 Export Assessment Data (JSON)",
                json.dumps(export_data, indent=2, default=str),
                f"aws_assessment_data_{datetime.now().strftime('%Y%m%d_%H%M')}.json",
                "application/json",
                use_container_width=True
            )
        
        # Report Preview
        if st.session_state.report:
            st.markdown("---")
            st.markdown("#### 📋 Report Preview")
            with st.expander("View Generated Report", expanded=False):
                st.markdown(st.session_state.report)

if __name__ == "__main__":
    main()