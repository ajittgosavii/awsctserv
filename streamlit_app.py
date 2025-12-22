"""
AWS Enterprise Assessment Platform v2.0
Control Tower Migration & Golden Architecture (Serverless) Assessment
Professional Light Theme Edition
"""

import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(
    page_title="AWS Enterprise Assessment Platform",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Light Theme CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

/* Force Light Theme */
.stApp {
    background: #f8fafc !important;
}

[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 1px solid #e2e8f0 !important;
}

/* Root Variables */
:root {
    --aws-orange: #ff9900;
    --aws-dark: #232f3e;
    --aws-blue: #2563eb;
    --bg-white: #ffffff;
    --bg-gray: #f8fafc;
    --bg-light: #f1f5f9;
    --border: #e2e8f0;
    --border-dark: #cbd5e1;
    --text-dark: #0f172a;
    --text-gray: #475569;
    --text-light: #64748b;
    --success: #059669;
    --warning: #d97706;
    --danger: #dc2626;
}

/* Main Header - AWS Style */
.main-header {
    background: linear-gradient(135deg, #232f3e 0%, #37475a 100%);
    padding: 1.75rem 2rem;
    border-radius: 12px;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06);
}

.main-header h1 {
    font-family: 'Inter', sans-serif;
    font-weight: 700;
    font-size: 1.75rem;
    color: #ffffff;
    margin: 0;
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.aws-badge {
    background: #ff9900;
    color: #232f3e;
    padding: 0.35rem 0.75rem;
    border-radius: 6px;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.5px;
}

.main-header p {
    color: rgba(255,255,255,0.8);
    font-size: 0.9rem;
    margin: 0.5rem 0 0 0;
    font-weight: 400;
}

/* Metric Cards */
.metric-card {
    background: #ffffff;
    padding: 1.5rem;
    border-radius: 12px;
    text-align: center;
    border: 1px solid #e2e8f0;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    transition: all 0.2s ease;
}

.metric-card:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    transform: translateY(-2px);
}

.metric-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 2.5rem;
    font-weight: 700;
    line-height: 1.1;
}

.metric-label {
    font-family: 'Inter', sans-serif;
    font-size: 0.7rem;
    font-weight: 600;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.75px;
    margin-top: 0.5rem;
}

.metric-badge {
    display: inline-block;
    margin-top: 0.5rem;
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
}

.badge-success { background: #ecfdf5; color: #059669; }
.badge-warning { background: #fffbeb; color: #d97706; }
.badge-danger { background: #fef2f2; color: #dc2626; }
.badge-neutral { background: #f1f5f9; color: #475569; }

.color-success { color: #059669; }
.color-warning { color: #d97706; }
.color-danger { color: #dc2626; }

/* Section Headers */
.section-title {
    font-family: 'Inter', sans-serif;
    font-size: 1.35rem;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.section-subtitle {
    font-family: 'Inter', sans-serif;
    font-size: 1rem;
    font-weight: 600;
    color: #334155;
    margin: 1.25rem 0 0.75rem 0;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid #e2e8f0;
}

/* Domain Cards */
.domain-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 1rem 1.25rem;
    margin-bottom: 0.75rem;
}

.domain-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.5rem;
}

.domain-name {
    font-weight: 600;
    color: #1e293b;
    font-size: 0.9rem;
}

.domain-score {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600;
    font-size: 0.85rem;
}

/* Progress Bar Override */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #2563eb, #3b82f6) !important;
}

.stProgress > div > div {
    background: #e2e8f0 !important;
}

/* Expander Styling */
div[data-testid="stExpander"] {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    margin-bottom: 0.5rem;
    box-shadow: 0 1px 2px rgba(0,0,0,0.03);
}

div[data-testid="stExpander"] details summary {
    font-family: 'Inter', sans-serif;
    font-weight: 500;
    color: #1e293b;
}

div[data-testid="stExpander"] details summary:hover {
    color: #2563eb;
}

/* Question Styling */
.question-box {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 1rem;
    margin: 0.75rem 0;
}

.question-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 0.5rem;
}

.question-id {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: #94a3b8;
    font-weight: 500;
}

.question-text {
    font-weight: 500;
    color: #1e293b;
    font-size: 0.9rem;
    line-height: 1.4;
}

/* Risk Badges */
.risk-badge {
    display: inline-block;
    padding: 0.15rem 0.5rem;
    border-radius: 4px;
    font-size: 0.6rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.risk-critical { background: #fef2f2; color: #dc2626; border: 1px solid #fecaca; }
.risk-high { background: #fff7ed; color: #ea580c; border: 1px solid #fed7aa; }
.risk-medium { background: #fefce8; color: #ca8a04; border: 1px solid #fef08a; }
.risk-low { background: #f0fdf4; color: #16a34a; border: 1px solid #bbf7d0; }

/* Pillar Tags */
.pillar-container { margin: 0.5rem 0; }

.pillar-tag {
    display: inline-block;
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    font-size: 0.65rem;
    font-weight: 600;
    margin-right: 0.35rem;
    margin-bottom: 0.25rem;
}

.pillar-SEC { background: #fef2f2; color: #dc2626; }
.pillar-REL { background: #eff6ff; color: #2563eb; }
.pillar-PERF { background: #faf5ff; color: #9333ea; }
.pillar-COST { background: #f0fdf4; color: #16a34a; }
.pillar-OPS { background: #fff7ed; color: #ea580c; }

/* Subcategory Header */
.subcat-header {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: 0.85rem;
    color: #2563eb;
    margin: 1.25rem 0 0.75rem 0;
    padding: 0.5rem 0.75rem;
    background: linear-gradient(90deg, #eff6ff, transparent);
    border-left: 3px solid #2563eb;
    border-radius: 0 6px 6px 0;
}

/* Gap Cards */
.gap-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-left: 4px solid #dc2626;
    border-radius: 0 8px 8px 0;
    padding: 0.875rem;
    margin: 0.5rem 0;
}

.gap-card.high { border-left-color: #ea580c; }
.gap-card.medium { border-left-color: #ca8a04; }

/* Buttons */
.stButton > button {
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
    color: white !important;
    border: none !important;
    padding: 0.5rem 1.25rem;
    border-radius: 8px;
    transition: all 0.2s ease;
    box-shadow: 0 2px 4px rgba(37,99,235,0.2);
}

.stButton > button:hover {
    background: linear-gradient(135deg, #1d4ed8, #1e40af) !important;
    box-shadow: 0 4px 12px rgba(37,99,235,0.3);
    transform: translateY(-1px);
}

.stDownloadButton > button {
    background: linear-gradient(135deg, #059669, #047857) !important;
    box-shadow: 0 2px 4px rgba(5,150,105,0.2);
}

.stDownloadButton > button:hover {
    background: linear-gradient(135deg, #047857, #065f46) !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 0.25rem;
    background: #ffffff;
    padding: 0.35rem;
    border-radius: 10px;
    border: 1px solid #e2e8f0;
}

.stTabs [data-baseweb="tab"] {
    font-family: 'Inter', sans-serif;
    font-weight: 500;
    font-size: 0.85rem;
    color: #64748b;
    background: transparent;
    border-radius: 8px;
    padding: 0.5rem 1rem;
}

.stTabs [aria-selected="true"] {
    background: #2563eb !important;
    color: white !important;
}

/* Radio Buttons */
.stRadio > div {
    gap: 0.5rem;
}

.stRadio > div > label {
    background: #ffffff;
    padding: 0.6rem 1rem;
    border-radius: 8px;
    border: 1px solid #e2e8f0;
    font-size: 0.85rem;
    color: #334155;
    transition: all 0.15s ease;
}

.stRadio > div > label:hover {
    border-color: #2563eb;
    background: #f8fafc;
}

.stRadio > div > label[data-checked="true"] {
    border-color: #2563eb;
    background: #eff6ff;
    color: #1d4ed8;
}

/* Input Fields */
.stTextInput > div > div > input,
.stTextArea textarea,
.stSelectbox > div > div {
    font-family: 'Inter', sans-serif;
    border: 1px solid #e2e8f0 !important;
    border-radius: 8px !important;
    background: #ffffff !important;
}

.stTextInput > div > div > input:focus,
.stTextArea textarea:focus {
    border-color: #2563eb !important;
    box-shadow: 0 0 0 3px rgba(37,99,235,0.1) !important;
}

/* Metrics */
div[data-testid="stMetric"] {
    background: #ffffff;
    padding: 1rem;
    border-radius: 10px;
    border: 1px solid #e2e8f0;
}

div[data-testid="stMetric"] label {
    color: #64748b !important;
    font-weight: 600 !important;
}

div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
    font-family: 'JetBrains Mono', monospace;
    color: #0f172a !important;
}

/* Sidebar Styling */
[data-testid="stSidebar"] .stMarkdown h3 {
    font-size: 0.75rem !important;
    font-weight: 700 !important;
    color: #64748b !important;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-top: 1.5rem;
    margin-bottom: 0.75rem;
}

/* AI Response Box */
.ai-response-box {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 1.5rem;
    margin-top: 1rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

.ai-response-box h2 {
    color: #1e293b;
    font-size: 1.15rem;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 0.5rem;
    margin-top: 1.5rem;
}

.ai-response-box h3 {
    color: #2563eb;
    font-size: 1rem;
}

/* Alerts */
.stAlert {
    border-radius: 8px;
}

/* Dividers */
hr {
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 1.5rem 0;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: #f1f5f9;
}

::-webkit-scrollbar-thumb {
    background: #cbd5e1;
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: #94a3b8;
}

/* Hide default Streamlit elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Well-Architected Pillars
WA_PILLARS = {
    "SEC": "Security", "REL": "Reliability", "PERF": "Performance",
    "COST": "Cost Optimization", "OPS": "Operations"
}

# Industry Benchmarks
BENCHMARKS = {
    "financial": {"name": "Financial Services", "avg": 72, "top": 85},
    "healthcare": {"name": "Healthcare", "avg": 65, "top": 80},
    "technology": {"name": "Technology", "avg": 78, "top": 90},
    "retail": {"name": "Retail", "avg": 60, "top": 75},
    "government": {"name": "Government", "avg": 58, "top": 72}
}

# Control Tower Assessment Questions
CT_DOMAINS = {
    "Organizational Strategy": {
        "weight": 0.12, "pillars": ["OPS", "SEC"],
        "subcategories": {
            "Multi-Account Strategy": [
                {"id": "CT-ORG-001", "q": "What is your AWS multi-account strategy maturity?", "risk": "high",
                 "opts": {"No strategy": 1, "Basic dev/prod separation": 2, "Defined OU structure": 3, "Comprehensive with workload isolation": 4, "Mature with automated lifecycle": 5}},
                {"id": "CT-ORG-002", "q": "How are Organizational Units structured?", "risk": "high",
                 "opts": {"No OU structure": 1, "Basic OUs": 2, "SDLC-aligned OUs": 3, "Nested OUs with separation": 4, "Comprehensive hierarchy": 5}},
                {"id": "CT-ORG-003", "q": "What is your account naming and metadata approach?", "risk": "medium",
                 "opts": {"No convention": 1, "Informal guidelines": 2, "Documented partially followed": 3, "Enforced with validation": 4, "Automated with enrichment": 5}},
                {"id": "CT-ORG-004", "q": "How is account ownership managed?", "risk": "medium",
                 "opts": {"No ownership model": 1, "Informal assignments": 2, "Documented manual": 3, "CMDB tracked": 4, "Automated HR integration": 5}},
            ],
            "Governance Framework": [
                {"id": "CT-ORG-005", "q": "What governance bodies oversee cloud operations?", "risk": "high",
                 "opts": {"No governance": 1, "Ad-hoc decisions": 2, "CCoE established": 3, "CCoE with RACI": 4, "Federated governance": 5}},
                {"id": "CT-ORG-006", "q": "How are cloud policies documented?", "risk": "medium",
                 "opts": {"No policies": 1, "Informal wikis": 2, "Formal with review": 3, "Compliance integrated": 4, "Policy-as-Code": 5}},
                {"id": "CT-ORG-007", "q": "What is your exception management process?", "risk": "medium",
                 "opts": {"No process": 1, "Ad-hoc approvals": 2, "Documented process": 3, "Time-bound workflow": 4, "Automated risk scoring": 5}},
            ]
        }
    },
    "Account Factory & Provisioning": {
        "weight": 0.10, "pillars": ["OPS", "SEC", "REL"],
        "subcategories": {
            "Account Provisioning": [
                {"id": "CT-ACC-001", "q": "How are new AWS accounts provisioned?", "risk": "high",
                 "opts": {"Manual console": 1, "CLI scripts": 2, "Semi-automated IaC": 3, "Service Catalog": 4, "Fully automated AFT": 5}},
                {"id": "CT-ACC-002", "q": "What is your account request workflow?", "risk": "medium",
                 "opts": {"No process": 1, "Email requests": 2, "ITSM tickets": 3, "Automated approval": 4, "Self-service portal": 5}},
                {"id": "CT-ACC-003", "q": "Average time to provision a new account?", "risk": "medium",
                 "opts": {"2+ weeks": 1, "1-2 weeks": 2, "3-5 days": 3, "1-2 days": 4, "<4 hours": 5}},
            ],
            "Baseline Configuration": [
                {"id": "CT-ACC-004", "q": "What baseline configurations are applied?", "risk": "critical",
                 "opts": {"No baselines": 1, "Basic IAM/logging": 2, "Security baseline": 3, "Comprehensive": 4, "Full compliance": 5}},
                {"id": "CT-ACC-005", "q": "How is baseline drift detected?", "risk": "high",
                 "opts": {"No detection": 1, "Manual audits": 2, "Config alerting": 3, "Automated detection": 4, "Auto-remediation": 5}},
                {"id": "CT-ACC-006", "q": "What IaC approach for baselines?", "risk": "medium",
                 "opts": {"No IaC": 1, "Partial": 2, "StackSets": 3, "Terraform": 4, "GitOps": 5}},
            ]
        }
    },
    "Guardrails & Controls": {
        "weight": 0.15, "pillars": ["SEC", "OPS"],
        "subcategories": {
            "Service Control Policies": [
                {"id": "CT-GRD-001", "q": "What is your SCP implementation maturity?", "risk": "critical",
                 "opts": {"No SCPs": 1, "Basic deny": 2, "Security guardrails": 3, "Comprehensive": 4, "Layered inheritance": 5}},
                {"id": "CT-GRD-002", "q": "How are SCPs tested before deployment?", "risk": "high",
                 "opts": {"No testing": 1, "Manual review": 2, "Sandbox testing": 3, "Policy Simulator": 4, "CI/CD validation": 5}},
                {"id": "CT-GRD-003", "q": "What SCP categories are enforced?", "risk": "high",
                 "opts": {"None": 1, "Region/service": 2, "Security": 3, "Security+compliance+cost": 4, "Full coverage": 5}},
                {"id": "CT-GRD-004", "q": "How is SCP versioning managed?", "risk": "medium",
                 "opts": {"No versioning": 1, "Manual docs": 2, "Git-based": 3, "Change history": 4, "GitOps rollback": 5}},
            ],
            "Control Tower Guardrails": [
                {"id": "CT-GRD-005", "q": "Which guardrail categories will you enable?", "risk": "high",
                 "opts": {"Mandatory only": 1, "Some recommended": 2, "All recommended": 3, "Selective elective": 4, "Comprehensive+custom": 5}},
                {"id": "CT-GRD-006", "q": "How will guardrail violations be handled?", "risk": "high",
                 "opts": {"No process": 1, "Manual review": 2, "Automated alerting": 3, "Escalation workflow": 4, "Auto-remediation": 5}},
                {"id": "CT-GRD-007", "q": "Approach to custom Control Tower controls?", "risk": "medium",
                 "opts": {"No custom": 1, "Evaluate later": 2, "Identified": 3, "Key requirements": 4, "Comprehensive CI/CD": 5}},
            ]
        }
    },
    "Detective Controls & Compliance": {
        "weight": 0.12, "pillars": ["SEC", "OPS"],
        "subcategories": {
            "AWS Config": [
                {"id": "CT-DET-001", "q": "AWS Config deployment status?", "risk": "critical",
                 "opts": {"Not enabled": 1, "Some accounts": 2, "Org-wide": 3, "Aggregator+custom": 4, "Conformance packs": 5}},
                {"id": "CT-DET-002", "q": "How many Config rules deployed?", "risk": "high",
                 "opts": {"None": 1, "1-20": 2, "21-50": 3, "51-100": 4, "100+ custom": 5}},
                {"id": "CT-DET-003", "q": "How is Config data aggregated?", "risk": "medium",
                 "opts": {"No aggregation": 1, "Manual": 2, "Aggregator": 3, "Delegated admin": 4, "Advanced analytics": 5}},
            ],
            "Security Hub": [
                {"id": "CT-DET-004", "q": "Security Hub deployment status?", "risk": "critical",
                 "opts": {"Not enabled": 1, "Some accounts": 2, "Org-wide": 3, "Multiple standards": 4, "Custom insights": 5}},
                {"id": "CT-DET-005", "q": "Security Hub standards enabled?", "risk": "high",
                 "opts": {"None": 1, "Foundational": 2, "CIS": 3, "Multiple": 4, "All+custom": 5}},
                {"id": "CT-DET-006", "q": "How are findings triaged?", "risk": "high",
                 "opts": {"No triage": 1, "Periodic": 2, "Alerting": 3, "Ticketing": 4, "Auto-remediation": 5}},
            ],
            "Compliance": [
                {"id": "CT-DET-007", "q": "Compliance frameworks required?", "risk": "critical",
                 "opts": {"None": 1, "Internal": 2, "Single": 3, "Multiple": 4, "Complex multi": 5}},
                {"id": "CT-DET-008", "q": "How is compliance evidence collected?", "risk": "high",
                 "opts": {"No collection": 1, "Manual": 2, "Periodic exports": 3, "Audit Manager": 4, "GRC integration": 5}},
            ]
        }
    },
    "Identity & Access Management": {
        "weight": 0.12, "pillars": ["SEC"],
        "subcategories": {
            "Identity Federation": [
                {"id": "CT-IAM-001", "q": "Current identity provider for AWS?", "risk": "critical",
                 "opts": {"Local IAM": 1, "Some SAML": 2, "Identity Center": 3, "Full IdP": 4, "SCIM+JIT": 5}},
                {"id": "CT-IAM-002", "q": "IdP for IAM Identity Center?", "risk": "high",
                 "opts": {"Native": 1, "AD Connector": 2, "Azure AD": 3, "Okta": 4, "Multi-IdP": 5}},
                {"id": "CT-IAM-003", "q": "How is MFA enforced?", "risk": "critical",
                 "opts": {"No MFA": 1, "Encouraged": 2, "Console": 3, "All human": 4, "Hardware privileged": 5}},
            ],
            "Permission Management": [
                {"id": "CT-IAM-004", "q": "Permission sets management?", "risk": "high",
                 "opts": {"No Identity Center": 1, "AWS managed": 2, "Custom inline": 3, "Modular": 4, "ABAC dynamic": 5}},
                {"id": "CT-IAM-005", "q": "Least privilege implementation?", "risk": "high",
                 "opts": {"Broad": 1, "Manual review": 2, "Access Analyzer": 3, "Regular sizing": 4, "Automated": 5}},
                {"id": "CT-IAM-006", "q": "Privileged access management?", "risk": "critical",
                 "opts": {"No distinction": 1, "Separate accounts": 2, "JIT some": 3, "PAM solution": 4, "Zero-standing": 5}},
            ],
            "Workload Identity": [
                {"id": "CT-IAM-007", "q": "Machine/service identity management?", "risk": "high",
                 "opts": {"Long-lived keys": 1, "Roles some": 2, "Role chaining": 3, "Roles Anywhere": 4, "Short-lived": 5}},
                {"id": "CT-IAM-008", "q": "Cross-account roles management?", "risk": "high",
                 "opts": {"Manual": 1, "StackSets": 2, "Centralized IaC": 3, "Role vending": 4, "Automated trust": 5}},
            ]
        }
    },
    "Network Architecture": {
        "weight": 0.10, "pillars": ["SEC", "REL", "PERF"],
        "subcategories": {
            "Network Topology": [
                {"id": "CT-NET-001", "q": "Multi-account network architecture?", "risk": "high",
                 "opts": {"Independent VPCs": 1, "VPC peering": 2, "Transit Gateway": 3, "Hub-spoke": 4, "Advanced segmentation": 5}},
                {"id": "CT-NET-002", "q": "Network IPAM management?", "risk": "high",
                 "opts": {"No IPAM": 1, "Spreadsheet": 2, "VPC IPAM": 3, "Automated": 4, "Enterprise integration": 5}},
                {"id": "CT-NET-003", "q": "VPC design pattern?", "risk": "medium",
                 "opts": {"No standard": 1, "Basic": 2, "Multi-AZ": 3, "Standardized": 4, "Blueprints": 5}},
            ],
            "Hybrid & Security": [
                {"id": "CT-NET-004", "q": "On-premises connectivity?", "risk": "high",
                 "opts": {"None": 5, "Per account VPN": 2, "Centralized VPN": 3, "Direct Connect": 4, "Redundant DC": 5}},
                {"id": "CT-NET-005", "q": "Hybrid DNS resolution?", "risk": "medium",
                 "opts": {"No hybrid": 1, "Manual": 2, "R53 Resolver": 3, "Centralized": 4, "Bidirectional": 5}},
                {"id": "CT-NET-006", "q": "Network traffic inspection?", "risk": "high",
                 "opts": {"None": 1, "SG/NACLs": 2, "Firewall some": 3, "Centralized": 4, "IDS/IPS": 5}},
                {"id": "CT-NET-007", "q": "Egress traffic control?", "risk": "critical",
                 "opts": {"None": 1, "NAT only": 2, "Centralized logging": 3, "Proxy filtering": 4, "Zero-trust DLP": 5}},
            ]
        }
    },
    "Logging & Monitoring": {
        "weight": 0.10, "pillars": ["OPS", "SEC", "REL"],
        "subcategories": {
            "Centralized Logging": [
                {"id": "CT-LOG-001", "q": "CloudTrail configuration?", "risk": "critical",
                 "opts": {"Not all accounts": 1, "Account-level": 2, "Org trail": 3, "Data events": 4, "Insights+Lake": 5}},
                {"id": "CT-LOG-002", "q": "VPC Flow Logs management?", "risk": "high",
                 "opts": {"Not enabled": 1, "Some VPCs": 2, "All centralized": 3, "Traffic mirror": 4, "Real-time": 5}},
                {"id": "CT-LOG-003", "q": "Log retention strategy?", "risk": "medium",
                 "opts": {"No policy": 1, "Default": 2, "S3 lifecycle": 3, "Tiered Glacier": 4, "Compliance hold": 5}},
                {"id": "CT-LOG-004", "q": "Log analysis and correlation?", "risk": "high",
                 "opts": {"None": 1, "Manual": 2, "Insights": 3, "SIEM": 4, "ML anomaly": 5}},
            ],
            "Monitoring": [
                {"id": "CT-LOG-005", "q": "CloudWatch configuration?", "risk": "medium",
                 "opts": {"Default": 1, "Some custom": 2, "Cross-account": 3, "Dashboards": 4, "X-Ray ServiceLens": 5}},
                {"id": "CT-LOG-006", "q": "Alerting strategy?", "risk": "medium",
                 "opts": {"None": 1, "Email": 2, "SNS integration": 3, "Tiered severity": 4, "AIOps runbook": 5}},
            ]
        }
    },
    "Cost Management": {
        "weight": 0.08, "pillars": ["COST", "OPS"],
        "subcategories": {
            "Cost Visibility": [
                {"id": "CT-FIN-001", "q": "Cost visibility across accounts?", "risk": "medium",
                 "opts": {"Individual": 1, "Consolidated": 2, "Cost Explorer": 3, "CUR Athena": 4, "FinOps platform": 5}},
                {"id": "CT-FIN-002", "q": "Cost allocation to business units?", "risk": "medium",
                 "opts": {"No allocation": 1, "Account-based": 2, "Tags partial": 3, "Comprehensive": 4, "Advanced split": 5}},
                {"id": "CT-FIN-003", "q": "Budgets and forecasting?", "risk": "medium",
                 "opts": {"No budgets": 1, "Annual": 2, "Account alerts": 3, "Granular forecast": 4, "ML anomaly": 5}},
            ],
            "Optimization": [
                {"id": "CT-FIN-004", "q": "RI/Savings Plans management?", "risk": "medium",
                 "opts": {"None": 1, "Reactive": 2, "Coverage periodic": 3, "Optimized": 4, "Automated sharing": 5}},
                {"id": "CT-FIN-005", "q": "Optimization recommendations?", "risk": "low",
                 "opts": {"None": 1, "Ad-hoc": 2, "Trusted Advisor": 3, "Compute Optimizer": 4, "Automated": 5}},
            ]
        }
    },
    "Backup & DR": {
        "weight": 0.08, "pillars": ["REL", "SEC"],
        "subcategories": {
            "Backup": [
                {"id": "CT-BDR-001", "q": "Backup management across accounts?", "risk": "critical",
                 "opts": {"No strategy": 1, "Account-level": 2, "AWS Backup": 3, "Centralized": 4, "Org-wide cross": 5}},
                {"id": "CT-BDR-002", "q": "Backup policy enforcement?", "risk": "high",
                 "opts": {"None": 1, "Guidelines": 2, "Config rules": 3, "Mandatory": 4, "Preventive": 5}},
                {"id": "CT-BDR-003", "q": "Backup testing?", "risk": "high",
                 "opts": {"None": 1, "Ad-hoc": 2, "Periodic": 3, "Scheduled automated": 4, "Continuous drills": 5}},
            ],
            "Disaster Recovery": [
                {"id": "CT-BDR-004", "q": "Multi-region DR strategy?", "risk": "high",
                 "opts": {"None": 1, "Backup region": 2, "Pilot light": 3, "Warm standby": 4, "Active-active": 5}},
                {"id": "CT-BDR-005", "q": "Control Tower resilience?", "risk": "high",
                 "opts": {"No consideration": 1, "Documentation": 2, "IaC backup": 3, "Automated": 4, "Full DR tested": 5}},
            ]
        }
    },
    "Migration Readiness": {
        "weight": 0.08, "pillars": ["OPS", "REL"],
        "subcategories": {
            "Account Inventory": [
                {"id": "CT-MIG-001", "q": "Existing account inventory?", "risk": "high",
                 "opts": {"No inventory": 1, "Partial": 2, "Complete limited": 3, "With ownership": 4, "Dynamic automated": 5}},
                {"id": "CT-MIG-002", "q": "Account count and distribution?", "risk": "high",
                 "opts": {"Unknown": 1, "1-25": 5, "26-100": 4, "101-500": 3, "500+": 2}},
                {"id": "CT-MIG-003", "q": "Non-standard configurations?", "risk": "high",
                 "opts": {"Unknown": 1, "Many": 2, "Some identified": 3, "Few": 4, "All standard": 5}},
            ],
            "Enrollment": [
                {"id": "CT-MIG-004", "q": "Account readiness for enrollment?", "risk": "critical",
                 "opts": {"No assessment": 1, "Basic some": 2, "Issues identified": 3, "Most ready": 4, "All verified": 5}},
                {"id": "CT-MIG-005", "q": "Config/CloudTrail conflicts?", "risk": "critical",
                 "opts": {"Unknown": 1, "Many conflicts": 2, "Identified": 3, "Most resolved": 4, "All resolved": 5}},
                {"id": "CT-MIG-006", "q": "Accounts that cannot be enrolled?", "risk": "medium",
                 "opts": {"No approach": 1, "TBD": 2, "Identified": 3, "Legacy plan": 4, "Comprehensive": 5}},
            ]
        }
    },
    "Operational Readiness": {
        "weight": 0.08, "pillars": ["OPS"],
        "subcategories": {
            "Skills": [
                {"id": "CT-OPS-001", "q": "Team Control Tower experience?", "risk": "high",
                 "opts": {"None": 1, "Training": 2, "Sandbox": 3, "Production": 4, "Deep expertise": 5}},
                {"id": "CT-OPS-002", "q": "Training plan for CT operations?", "risk": "medium",
                 "opts": {"None": 1, "Self-paced": 2, "AWS training": 3, "Comprehensive": 4, "Certification+KT": 5}},
            ],
            "Runbooks": [
                {"id": "CT-OPS-003", "q": "Operational runbooks defined?", "risk": "medium",
                 "opts": {"None": 1, "During impl": 2, "Basic": 3, "Comprehensive": 4, "SSM automation": 5}},
                {"id": "CT-OPS-004", "q": "Incident response process?", "risk": "medium",
                 "opts": {"None": 1, "Ad-hoc": 2, "Escalation": 3, "Playbooks": 4, "Automated IR": 5}},
            ],
            "Change Management": [
                {"id": "CT-OPS-005", "q": "Control Tower change management?", "risk": "medium",
                 "opts": {"No process": 1, "Informal": 2, "Tickets": 3, "CAB review": 4, "GitOps": 5}},
                {"id": "CT-OPS-006", "q": "Control Tower upgrade approach?", "risk": "medium",
                 "opts": {"No strategy": 1, "When issues": 2, "Monitor periodic": 3, "Scheduled testing": 4, "Automated": 5}},
            ]
        }
    },
    "Data Protection": {
        "weight": 0.07, "pillars": ["SEC"],
        "subcategories": {
            "Encryption": [
                {"id": "CT-DAT-001", "q": "Encryption strategy at rest?", "risk": "critical",
                 "opts": {"No requirements": 1, "AWS SSE": 2, "KMS managed": 3, "Customer KMS": 4, "Centralized hierarchy": 5}},
                {"id": "CT-DAT-002", "q": "KMS management across accounts?", "risk": "high",
                 "opts": {"No strategy": 1, "Account-local": 2, "Cross-account": 3, "Centralized": 4, "Multi-region": 5}},
            ],
            "Classification": [
                {"id": "CT-DAT-003", "q": "Data classification framework?", "risk": "high",
                 "opts": {"None": 1, "Basic": 2, "With procedures": 3, "Technical controls": 4, "Automated DLP": 5}},
                {"id": "CT-DAT-004", "q": "Sensitive data discovery?", "risk": "high",
                 "opts": {"None": 1, "Manual": 2, "Macie S3": 3, "Custom identifiers": 4, "Comprehensive DLP": 5}},
            ]
        }
    }
}

# Golden Architecture Assessment Questions
GA_DOMAINS = {
    "Serverless Compute": {
        "weight": 0.15, "pillars": ["PERF", "COST", "OPS"],
        "subcategories": {
            "Lambda": [
                {"id": "GA-CMP-001", "q": "Lambda adoption maturity?", "risk": "medium",
                 "opts": {"No usage": 1, "Experimental": 2, "Production": 3, "Significant": 4, "Lambda-first": 5}},
                {"id": "GA-CMP-002", "q": "Lambda organization and management?", "risk": "medium",
                 "opts": {"Ad-hoc": 1, "Naming": 2, "Microservices": 3, "Domain-driven": 4, "Function mesh": 5}},
                {"id": "GA-CMP-003", "q": "Lambda runtime management?", "risk": "medium",
                 "opts": {"Default": 1, "Standard": 2, "Versioning": 3, "Automated": 4, "Custom container": 5}},
                {"id": "GA-CMP-004", "q": "Cold start handling?", "risk": "low",
                 "opts": {"None": 1, "Awareness": 2, "Basic": 3, "Provisioned": 4, "SnapStart+warming": 5}},
                {"id": "GA-CMP-005", "q": "Lambda layers strategy?", "risk": "low",
                 "opts": {"No layers": 1, "Some": 2, "Standard": 3, "Versioned": 4, "Automated CI/CD": 5}},
            ],
            "Containers": [
                {"id": "GA-CMP-006", "q": "Fargate adoption level?", "risk": "medium",
                 "opts": {"None": 1, "Experimental": 2, "Specific": 3, "Default": 4, "Comprehensive+Spot": 5}},
                {"id": "GA-CMP-007", "q": "Lambda vs Fargate decision framework?", "risk": "medium",
                 "opts": {"No framework": 1, "Ad-hoc": 2, "Guidelines": 3, "Decision tree": 4, "Cost modeling": 5}},
            ]
        }
    },
    "API & Integration": {
        "weight": 0.12, "pillars": ["PERF", "SEC", "REL"],
        "subcategories": {
            "API Gateway": [
                {"id": "GA-API-001", "q": "API Gateway type standard?", "risk": "medium",
                 "opts": {"No usage": 1, "REST all": 2, "HTTP default": 3, "Right-sized": 4, "Multi-type WAF": 5}},
                {"id": "GA-API-002", "q": "API versioning management?", "risk": "medium",
                 "opts": {"None": 1, "URL path": 2, "Stage": 3, "Header": 4, "Comprehensive": 5}},
                {"id": "GA-API-003", "q": "API documentation approach?", "risk": "low",
                 "opts": {"None": 1, "Manual": 2, "OpenAPI": 3, "Auto portal": 4, "Developer SDK": 5}},
                {"id": "GA-API-004", "q": "Rate limiting configuration?", "risk": "high",
                 "opts": {"None": 1, "Default": 2, "Custom": 3, "Usage plans": 4, "Dynamic quota": 5}},
            ],
            "Events": [
                {"id": "GA-API-005", "q": "EventBridge adoption?", "risk": "medium",
                 "opts": {"None": 1, "Basic": 2, "Custom+rules": 3, "Event-driven": 4, "Event mesh": 5}},
                {"id": "GA-API-006", "q": "Event schema management?", "risk": "medium",
                 "opts": {"None": 1, "Informal": 2, "Registry": 3, "Versioning": 4, "Governance": 5}},
                {"id": "GA-API-007", "q": "SQS/SNS patterns?", "risk": "medium",
                 "opts": {"None": 1, "Basic": 2, "Fan-out": 3, "DLQ+retry": 4, "FIFO exactly-once": 5}},
            ]
        }
    },
    "Orchestration": {
        "weight": 0.10, "pillars": ["REL", "OPS"],
        "subcategories": {
            "Step Functions": [
                {"id": "GA-WRK-001", "q": "Step Functions adoption?", "risk": "medium",
                 "opts": {"None": 1, "Experimental": 2, "Standard": 3, "Orchestration": 4, "Express+callbacks": 5}},
                {"id": "GA-WRK-002", "q": "Workflow error handling?", "risk": "high",
                 "opts": {"None": 1, "Try-catch": 2, "Retry": 3, "Fallbacks": 4, "Saga": 5}},
                {"id": "GA-WRK-003", "q": "Workflow patterns implemented?", "risk": "medium",
                 "opts": {"None": 1, "Sequential": 2, "Parallel+choice": 3, "Map dynamic": 4, "Human approval": 5}},
            ]
        }
    },
    "Data Layer": {
        "weight": 0.12, "pillars": ["PERF", "REL", "COST"],
        "subcategories": {
            "DynamoDB": [
                {"id": "GA-DAT-001", "q": "DynamoDB adoption level?", "risk": "medium",
                 "opts": {"None": 1, "Specific": 2, "Default": 3, "Advanced GSI": 4, "Single-table": 5}},
                {"id": "GA-DAT-002", "q": "DynamoDB capacity management?", "risk": "medium",
                 "opts": {"Not using": 1, "Provisioned": 2, "On-demand": 3, "Auto-scale": 4, "Optimized reserved": 5}},
                {"id": "GA-DAT-003", "q": "DynamoDB design patterns?", "risk": "medium",
                 "opts": {"N/A": 1, "Key-value": 2, "Multiple tables": 3, "Single-table": 4, "GSI overloading": 5}},
                {"id": "GA-DAT-004", "q": "DynamoDB caching?", "risk": "low",
                 "opts": {"None": 1, "Application": 2, "ElastiCache": 3, "DAX": 4, "Multi-layer": 5}},
            ],
            "Relational": [
                {"id": "GA-DAT-005", "q": "Aurora Serverless usage?", "risk": "medium",
                 "opts": {"None": 1, "Evaluating": 2, "Dev/test": 3, "Production": 4, "Data API": 5}},
                {"id": "GA-DAT-006", "q": "Database connections serverless?", "risk": "high",
                 "opts": {"Direct": 1, "Lambda pooling": 2, "RDS Proxy": 3, "Proxy+IAM": 4, "Data API": 5}},
            ],
            "Analytics": [
                {"id": "GA-DAT-007", "q": "Serverless analytics approach?", "risk": "low",
                 "opts": {"None": 1, "Traditional": 2, "Athena": 3, "Data lake": 4, "Comprehensive": 5}},
            ]
        }
    },
    "Serverless Security": {
        "weight": 0.15, "pillars": ["SEC"],
        "subcategories": {
            "Function Security": [
                {"id": "GA-SEC-001", "q": "Lambda execution roles?", "risk": "critical",
                 "opts": {"Single all": 1, "Broad app": 2, "Function-specific": 3, "Least-privilege": 4, "Automated": 5}},
                {"id": "GA-SEC-002", "q": "Code signing Lambda?", "risk": "high",
                 "opts": {"None": 1, "Evaluating": 2, "Some": 3, "Validation": 4, "Mandatory CI/CD": 5}},
                {"id": "GA-SEC-003", "q": "Lambda vulnerability management?", "risk": "high",
                 "opts": {"No scanning": 1, "Manual": 2, "CI/CD": 3, "Inspector": 4, "Continuous": 5}},
            ],
            "Secrets": [
                {"id": "GA-SEC-004", "q": "Secrets management?", "risk": "critical",
                 "opts": {"Env plaintext": 1, "Encrypted env": 2, "Parameter Store": 3, "Secrets Manager": 4, "Lambda extension": 5}},
                {"id": "GA-SEC-005", "q": "Secret rotation?", "risk": "high",
                 "opts": {"None": 1, "Manual": 2, "Scheduled": 3, "Automated some": 4, "Automated all": 5}},
            ],
            "API Security": [
                {"id": "GA-SEC-006", "q": "API authentication?", "risk": "critical",
                 "opts": {"None": 1, "API keys": 2, "Cognito": 3, "Lambda JWT": 4, "Multi-method": 5}},
                {"id": "GA-SEC-007", "q": "API traffic protection?", "risk": "high",
                 "opts": {"None": 1, "Throttling": 2, "WAF managed": 3, "WAF custom": 4, "WAF+Shield+bot": 5}},
                {"id": "GA-SEC-008", "q": "Input validation?", "risk": "high",
                 "opts": {"None": 1, "Basic": 2, "API Gateway": 3, "Schema": 4, "Comprehensive+WAF": 5}},
            ]
        }
    },
    "Observability": {
        "weight": 0.10, "pillars": ["OPS", "REL"],
        "subcategories": {
            "Logging": [
                {"id": "GA-OBS-001", "q": "Serverless logging structure?", "risk": "medium",
                 "opts": {"Console.log": 1, "Timestamps": 2, "JSON": 3, "Correlation IDs": 4, "Powertools": 5}},
                {"id": "GA-OBS-002", "q": "Log aggregation and analysis?", "risk": "medium",
                 "opts": {"Console": 1, "Insights": 2, "Centralized": 3, "Real-time": 4, "ML anomaly": 5}},
            ],
            "Tracing": [
                {"id": "GA-OBS-003", "q": "Distributed tracing approach?", "risk": "medium",
                 "opts": {"None": 1, "X-Ray some": 2, "X-Ray all": 3, "Custom segments": 4, "Service map": 5}},
            ],
            "Metrics": [
                {"id": "GA-OBS-004", "q": "Custom metrics captured?", "risk": "medium",
                 "opts": {"Default": 1, "Some": 2, "Business EMF": 3, "Comprehensive": 4, "Real-time": 5}},
                {"id": "GA-OBS-005", "q": "Serverless dashboards?", "risk": "low",
                 "opts": {"None": 1, "Basic": 2, "Application": 3, "Service SLIs": 4, "Comprehensive": 5}},
                {"id": "GA-OBS-006", "q": "SLOs/SLIs for serverless?", "risk": "medium",
                 "opts": {"None": 1, "Informal": 2, "Key SLIs": 3, "Error budgets": 4, "Automated": 5}},
            ]
        }
    },
    "CI/CD & DevOps": {
        "weight": 0.10, "pillars": ["OPS"],
        "subcategories": {
            "Deployment": [
                {"id": "GA-DEV-001", "q": "Serverless deployment approach?", "risk": "medium",
                 "opts": {"Manual": 1, "CLI": 2, "SAM/Serverless": 3, "CDK": 4, "GitOps": 5}},
                {"id": "GA-DEV-002", "q": "Infrastructure as Code?", "risk": "medium",
                 "opts": {"None": 1, "Partial": 2, "Full": 3, "Linting": 4, "Testing security": 5}},
                {"id": "GA-DEV-003", "q": "Deployment strategies?", "risk": "high",
                 "opts": {"All-at-once": 1, "Manual": 2, "Blue-green": 3, "Canary": 4, "Automated rollback": 5}},
                {"id": "GA-DEV-004", "q": "Rollback handling?", "risk": "high",
                 "opts": {"No capability": 1, "Manual": 2, "Automated": 3, "Version aliases": 4, "Blast radius": 5}},
            ],
            "Testing": [
                {"id": "GA-DEV-005", "q": "Serverless testing strategy?", "risk": "high",
                 "opts": {"None": 1, "Unit": 2, "Integration": 3, "Comprehensive": 4, "Full pyramid": 5}},
                {"id": "GA-DEV-006", "q": "Local development?", "risk": "low",
                 "opts": {"Deploy AWS": 1, "Limited": 2, "SAM Local": 3, "LocalStack": 4, "Comprehensive": 5}},
            ]
        }
    },
    "Cost Optimization": {
        "weight": 0.08, "pillars": ["COST"],
        "subcategories": {
            "Visibility": [
                {"id": "GA-CST-001", "q": "Serverless cost visibility?", "risk": "medium",
                 "opts": {"No tracking": 1, "Service": 2, "Function": 3, "Per-app": 4, "Per invocation": 5}},
                {"id": "GA-CST-002", "q": "Cost anomaly detection?", "risk": "medium",
                 "opts": {"None": 1, "Manual": 2, "AWS Anomaly": 3, "Custom": 4, "Auto-remediation": 5}},
            ],
            "Optimization": [
                {"id": "GA-CST-003", "q": "Lambda memory optimization?", "risk": "low",
                 "opts": {"Default": 1, "Manual": 2, "Power Tuning": 3, "Regular": 4, "Automated": 5}},
                {"id": "GA-CST-004", "q": "Unused resource cleanup?", "risk": "low",
                 "opts": {"None": 1, "Manual": 2, "Reporting": 3, "Scheduled": 4, "Automated": 5}},
                {"id": "GA-CST-005", "q": "Graviton utilization?", "risk": "low",
                 "opts": {"Not aware": 1, "Evaluating": 2, "Some": 3, "Default": 4, "Comprehensive": 5}},
            ]
        }
    },
    "Resilience": {
        "weight": 0.08, "pillars": ["REL"],
        "subcategories": {
            "Fault Tolerance": [
                {"id": "GA-REL-001", "q": "Retry and error handling?", "risk": "high",
                 "opts": {"None": 1, "Default": 2, "Backoff": 3, "Circuit breaker": 4, "Patterns+fallbacks": 5}},
                {"id": "GA-REL-002", "q": "Dead letter queue configuration?", "risk": "medium",
                 "opts": {"None": 1, "Some": 2, "All async": 3, "Monitoring": 4, "Auto-reprocessing": 5}},
                {"id": "GA-REL-003", "q": "Idempotency implementation?", "risk": "high",
                 "opts": {"None": 1, "Awareness": 2, "Critical": 3, "Tokens": 4, "Powertools": 5}},
            ],
            "Multi-Region": [
                {"id": "GA-REL-004", "q": "Multi-region strategy serverless?", "risk": "high",
                 "opts": {"Single": 1, "Replicated": 2, "Passive manual": 3, "Passive automated": 4, "Active-active": 5}},
                {"id": "GA-REL-005", "q": "Global data consistency?", "risk": "high",
                 "opts": {"N/A": 1, "Eventually": 2, "Global Tables": 3, "Defined": 4, "Comprehensive": 5}},
            ]
        }
    }
}


# =============================================================================
# APPLICATION FUNCTIONS
# =============================================================================

def init_state():
    defaults = {'ct_responses': {}, 'ga_responses': {}, 'ai_analysis': None,
                'org_name': '', 'assessor_name': '', 'industry': 'technology', 'report': None}
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def count_questions(domains):
    return sum(len(q) for d in domains.values() for q in d["subcategories"].values())

def calc_scores(responses, domains):
    domain_scores = {}
    for dname, ddata in domains.items():
        total, count = 0, 0
        for questions in ddata["subcategories"].values():
            for q in questions:
                if q["id"] in responses:
                    total += responses[q["id"]]
                    count += 1
        score = (total / (count * 5) * 100) if count > 0 else 0
        domain_scores[dname] = {"score": score, "answered": count,
                                "total": sum(len(qs) for qs in ddata["subcategories"].values()),
                                "weight": ddata["weight"]}
    weighted = sum(d["score"] * d["weight"] for d in domain_scores.values() if d["answered"] > 0)
    total_weight = sum(d["weight"] for d in domain_scores.values() if d["answered"] > 0)
    overall = weighted / total_weight if total_weight > 0 else 0
    return {"overall": overall, "domains": domain_scores}

def get_level(score):
    if score >= 80: return "Optimized", "success"
    if score >= 60: return "Managed", "warning"
    if score >= 40: return "Developing", "warning"
    return "Initial", "danger"

def find_gaps(responses, domains):
    gaps = []
    for dname, ddata in domains.items():
        for sname, questions in ddata["subcategories"].items():
            for q in questions:
                if q["id"] in responses and responses[q["id"]] <= 2:
                    gaps.append({"id": q["id"], "domain": dname, "subcat": sname,
                                "question": q["q"], "score": responses[q["id"]], "risk": q["risk"]})
    risk_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    return sorted(gaps, key=lambda x: risk_order.get(x["risk"], 3))

def call_ai(prompt):
    try:
        import anthropic
        key = os.environ.get("ANTHROPIC_API_KEY")
        if not key:
            return "⚠️ **API Key Required**: Add `ANTHROPIC_API_KEY` to Streamlit secrets."
        client = anthropic.Anthropic(api_key=key)
        resp = client.messages.create(
            model="claude-sonnet-4-20250514", max_tokens=8192,
            system="You are an expert AWS Solutions Architect. Provide detailed, actionable recommendations.",
            messages=[{"role": "user", "content": prompt}]
        )
        return resp.content[0].text
    except Exception as e:
        return f"⚠️ AI Error: {e}"

def render_metric(value, label, suffix="%"):
    level, level_class = get_level(value)
    colors = {"success": "#059669", "warning": "#d97706", "danger": "#dc2626"}
    badges = {"success": "badge-success", "warning": "badge-warning", "danger": "badge-danger"}
    color = colors.get(level_class, "#6b7280")
    badge = badges.get(level_class, "badge-neutral")
    st.markdown(f'''
    <div class="metric-card">
        <div class="metric-value color-{level_class}">{value:.0f}{suffix}</div>
        <div class="metric-label">{label}</div>
        <div class="metric-badge {badge}">{level}</div>
    </div>
    ''', unsafe_allow_html=True)

def render_assessment(domains, responses, prefix):
    for dname, ddata in domains.items():
        with st.expander(f"📁 {dname} — Weight: {ddata['weight']*100:.0f}%"):
            pillars = " ".join([f'<span class="pillar-tag pillar-{p}">{WA_PILLARS.get(p,p)}</span>' for p in ddata["pillars"]])
            st.markdown(f'<div class="pillar-container">Well-Architected: {pillars}</div>', unsafe_allow_html=True)
            for sname, questions in ddata["subcategories"].items():
                st.markdown(f'<div class="subcat-header">{sname}</div>', unsafe_allow_html=True)
                for q in questions:
                    st.markdown(f'''<div class="question-box">
                        <div class="question-header">
                            <div><span class="question-id">{q["id"]}</span></div>
                            <span class="risk-badge risk-{q["risk"]}">{q["risk"]}</span>
                        </div>
                        <div class="question-text">{q["q"]}</div>
                    </div>''', unsafe_allow_html=True)
                    opts = list(q["opts"].keys())
                    curr = 0
                    if q["id"] in responses:
                        for i, (opt, val) in enumerate(q["opts"].items()):
                            if val == responses[q["id"]]: curr = i; break
                    sel = st.radio(f"_{q['id']}", opts, index=curr, key=f"{prefix}_{q['id']}", label_visibility="collapsed")
                    responses[q["id"]] = q["opts"][sel]


# =============================================================================
# MAIN APPLICATION
# =============================================================================
def main():
    init_state()
    
    # Header
    st.markdown('''
    <div class="main-header">
        <h1>☁️ AWS Enterprise Assessment Platform <span class="aws-badge">ENTERPRISE</span></h1>
        <p>AI-Driven Control Tower Migration & Golden Architecture (Serverless) Assessment</p>
    </div>
    ''', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("### Configuration")
        st.session_state.org_name = st.text_input("Organization", st.session_state.org_name)
        st.session_state.assessor_name = st.text_input("Assessor", st.session_state.assessor_name)
        st.session_state.industry = st.selectbox("Industry", list(BENCHMARKS.keys()),
            format_func=lambda x: BENCHMARKS[x]["name"],
            index=list(BENCHMARKS.keys()).index(st.session_state.industry))
        
        st.markdown("### Progress")
        ct_total, ct_done = count_questions(CT_DOMAINS), len(st.session_state.ct_responses)
        ga_total, ga_done = count_questions(GA_DOMAINS), len(st.session_state.ga_responses)
        st.progress(ct_done/ct_total if ct_total else 0)
        st.caption(f"Control Tower: {ct_done}/{ct_total}")
        st.progress(ga_done/ga_total if ga_total else 0)
        st.caption(f"Golden Architecture: {ga_done}/{ga_total}")
        st.markdown("---")
        c1, c2 = st.columns(2)
        with c1: st.metric("Total", ct_total + ga_total)
        with c2: st.metric("Done", ct_done + ga_done)
    
    # Tabs
    tabs = st.tabs(["📊 Dashboard", "🎛️ Control Tower", "⚡ Golden Architecture", "🔍 Gaps", "🤖 AI Insights", "📄 Reports"])
    
    with tabs[0]:
        st.markdown('<div class="section-title">📊 Executive Dashboard</div>', unsafe_allow_html=True)
        ct_scores = calc_scores(st.session_state.ct_responses, CT_DOMAINS) if st.session_state.ct_responses else {"overall": 0}
        ga_scores = calc_scores(st.session_state.ga_responses, GA_DOMAINS) if st.session_state.ga_responses else {"overall": 0}
        combined = (ct_scores["overall"] + ga_scores["overall"]) / 2 if (ct_scores["overall"] or ga_scores["overall"]) else 0
        
        c1, c2, c3, c4 = st.columns(4)
        with c1: render_metric(ct_scores["overall"], "Control Tower")
        with c2: render_metric(ga_scores["overall"], "Golden Architecture")
        with c3: render_metric(combined, "Combined Score")
        with c4:
            bench = BENCHMARKS[st.session_state.industry]
            vs = combined - bench["avg"]
            color = "#059669" if vs >= 0 else "#dc2626"
            st.markdown(f'''<div class="metric-card">
                <div class="metric-value" style="color:{color}">{vs:+.0f}%</div>
                <div class="metric-label">vs {bench["name"]} Avg</div>
                <div class="metric-badge badge-neutral">Benchmark: {bench["avg"]}%</div>
            </div>''', unsafe_allow_html=True)
        
        st.markdown("---")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="section-subtitle">Control Tower Domains</div>', unsafe_allow_html=True)
            if "domains" in ct_scores:
                for dname, data in ct_scores["domains"].items():
                    level, lc = get_level(data["score"])
                    colors = {"success": "#059669", "warning": "#d97706", "danger": "#dc2626"}
                    st.markdown(f'''<div class="domain-card">
                        <div class="domain-header">
                            <span class="domain-name">{dname}</span>
                            <span class="domain-score" style="color:{colors.get(lc,'#6b7280')}">{data["score"]:.0f}% · {level}</span>
                        </div>
                    </div>''', unsafe_allow_html=True)
                    st.progress(data["score"]/100)
            else:
                st.info("Complete assessment to see domain scores")
        with c2:
            st.markdown('<div class="section-subtitle">Golden Architecture Domains</div>', unsafe_allow_html=True)
            if "domains" in ga_scores:
                for dname, data in ga_scores["domains"].items():
                    level, lc = get_level(data["score"])
                    colors = {"success": "#059669", "warning": "#d97706", "danger": "#dc2626"}
                    st.markdown(f'''<div class="domain-card">
                        <div class="domain-header">
                            <span class="domain-name">{dname}</span>
                            <span class="domain-score" style="color:{colors.get(lc,'#6b7280')}">{data["score"]:.0f}% · {level}</span>
                        </div>
                    </div>''', unsafe_allow_html=True)
                    st.progress(data["score"]/100)
            else:
                st.info("Complete assessment to see domain scores")
    
    with tabs[1]:
        st.markdown(f'<div class="section-title">🎛️ Control Tower Assessment</div>', unsafe_allow_html=True)
        st.markdown(f"**{len(CT_DOMAINS)} domains** · **{count_questions(CT_DOMAINS)} questions**")
        render_assessment(CT_DOMAINS, st.session_state.ct_responses, "ct")
    
    with tabs[2]:
        st.markdown(f'<div class="section-title">⚡ Golden Architecture Assessment</div>', unsafe_allow_html=True)
        st.markdown(f"**{len(GA_DOMAINS)} domains** · **{count_questions(GA_DOMAINS)} questions**")
        render_assessment(GA_DOMAINS, st.session_state.ga_responses, "ga")
    
    with tabs[3]:
        st.markdown('<div class="section-title">🔍 Gap Analysis</div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="section-subtitle">Control Tower Gaps</div>', unsafe_allow_html=True)
            ct_gaps = find_gaps(st.session_state.ct_responses, CT_DOMAINS)
            if ct_gaps:
                crit = len([g for g in ct_gaps if g["risk"]=="critical"])
                high = len([g for g in ct_gaps if g["risk"]=="high"])
                cc1, cc2, cc3 = st.columns(3)
                with cc1: st.metric("🔴 Critical", crit)
                with cc2: st.metric("🟠 High", high)
                with cc3: st.metric("🟡 Medium", len(ct_gaps)-crit-high)
                for g in ct_gaps[:8]:
                    cls = "" if g["risk"]=="critical" else " high" if g["risk"]=="high" else " medium"
                    st.markdown(f'''<div class="gap-card{cls}">
                        <strong>{g["id"]}</strong> · <span class="risk-badge risk-{g["risk"]}">{g["risk"]}</span><br/>
                        <span style="color:#475569;font-size:0.9rem">{g["question"]}</span><br/>
                        <small style="color:#94a3b8">Score: {g["score"]}/5 · {g["domain"]}</small>
                    </div>''', unsafe_allow_html=True)
            else:
                st.success("✅ No critical gaps")
        with c2:
            st.markdown('<div class="section-subtitle">Golden Architecture Gaps</div>', unsafe_allow_html=True)
            ga_gaps = find_gaps(st.session_state.ga_responses, GA_DOMAINS)
            if ga_gaps:
                crit = len([g for g in ga_gaps if g["risk"]=="critical"])
                high = len([g for g in ga_gaps if g["risk"]=="high"])
                cc1, cc2, cc3 = st.columns(3)
                with cc1: st.metric("🔴 Critical", crit)
                with cc2: st.metric("🟠 High", high)
                with cc3: st.metric("🟡 Medium", len(ga_gaps)-crit-high)
                for g in ga_gaps[:8]:
                    cls = "" if g["risk"]=="critical" else " high" if g["risk"]=="high" else " medium"
                    st.markdown(f'''<div class="gap-card{cls}">
                        <strong>{g["id"]}</strong> · <span class="risk-badge risk-{g["risk"]}">{g["risk"]}</span><br/>
                        <span style="color:#475569;font-size:0.9rem">{g["question"]}</span><br/>
                        <small style="color:#94a3b8">Score: {g["score"]}/5 · {g["domain"]}</small>
                    </div>''', unsafe_allow_html=True)
            else:
                st.success("✅ No critical gaps")
    
    with tabs[4]:
        st.markdown('<div class="section-title">🤖 AI-Powered Analysis</div>', unsafe_allow_html=True)
        analysis_type = st.selectbox("Analysis Type", ["🎯 Gap Analysis", "🗺️ Implementation Roadmap", "⚠️ Risk Assessment", "💰 Cost-Benefit", "🏗️ Architecture Recommendations"])
        context = st.text_area("Additional Context", placeholder="Add constraints, timeline, budget...", height=80)
        if st.button("🚀 Generate Analysis", type="primary"):
            if not st.session_state.ct_responses and not st.session_state.ga_responses:
                st.warning("Complete some questions first")
            else:
                with st.spinner("Generating..."):
                    ct_scores = calc_scores(st.session_state.ct_responses, CT_DOMAINS)
                    ga_scores = calc_scores(st.session_state.ga_responses, GA_DOMAINS)
                    ct_gaps = find_gaps(st.session_state.ct_responses, CT_DOMAINS)
                    ga_gaps = find_gaps(st.session_state.ga_responses, GA_DOMAINS)
                    prompt = f"""AWS Assessment - {analysis_type}
Organization: {st.session_state.org_name or 'N/A'}
Industry: {BENCHMARKS[st.session_state.industry]['name']}

Control Tower: {ct_scores['overall']:.0f}% ({get_level(ct_scores['overall'])[0]})
- Critical gaps: {len([g for g in ct_gaps if g['risk']=='critical'])}
- High gaps: {len([g for g in ct_gaps if g['risk']=='high'])}
- Top gaps: {json.dumps(ct_gaps[:5], indent=2)}

Golden Architecture: {ga_scores['overall']:.0f}% ({get_level(ga_scores['overall'])[0]})
- Critical gaps: {len([g for g in ga_gaps if g['risk']=='critical'])}
- High gaps: {len([g for g in ga_gaps if g['risk']=='high'])}
- Top gaps: {json.dumps(ga_gaps[:5], indent=2)}

Context: {context or 'None'}

Provide comprehensive, actionable recommendations with AWS services, effort estimates, and priorities."""
                    st.session_state.ai_analysis = call_ai(prompt)
        if st.session_state.ai_analysis:
            st.markdown("---")
            st.markdown('<div class="ai-response-box">', unsafe_allow_html=True)
            st.markdown(st.session_state.ai_analysis)
            st.markdown('</div>', unsafe_allow_html=True)
    
    with tabs[5]:
        st.markdown('<div class="section-title">📄 Reports & Export</div>', unsafe_allow_html=True)
        ct_scores = calc_scores(st.session_state.ct_responses, CT_DOMAINS) if st.session_state.ct_responses else {"overall": 0}
        ga_scores = calc_scores(st.session_state.ga_responses, GA_DOMAINS) if st.session_state.ga_responses else {"overall": 0}
        combined = (ct_scores["overall"] + ga_scores["overall"]) / 2
        
        c1, c2, c3, c4 = st.columns(4)
        with c1: render_metric(ct_scores["overall"], "Control Tower")
        with c2: render_metric(ga_scores["overall"], "Golden Arch")
        with c3: render_metric(combined, "Combined")
        with c4:
            done = len(st.session_state.ct_responses) + len(st.session_state.ga_responses)
            total = count_questions(CT_DOMAINS) + count_questions(GA_DOMAINS)
            render_metric(done/total*100 if total else 0, "Completion")
        
        st.markdown("---")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("📊 Generate Report", type="primary", use_container_width=True):
                ct_gaps = find_gaps(st.session_state.ct_responses, CT_DOMAINS)
                ga_gaps = find_gaps(st.session_state.ga_responses, GA_DOMAINS)
                st.session_state.report = f"""# AWS Enterprise Assessment Report

| Field | Value |
|-------|-------|
| Organization | {st.session_state.org_name or 'N/A'} |
| Assessor | {st.session_state.assessor_name or 'N/A'} |
| Date | {datetime.now().strftime('%Y-%m-%d')} |
| Industry | {BENCHMARKS[st.session_state.industry]['name']} |

## Scores

| Assessment | Score | Level |
|------------|-------|-------|
| Control Tower | {ct_scores['overall']:.0f}% | {get_level(ct_scores['overall'])[0]} |
| Golden Architecture | {ga_scores['overall']:.0f}% | {get_level(ga_scores['overall'])[0]} |
| Combined | {combined:.0f}% | {get_level(combined)[0]} |

## Gaps

**Control Tower**: {len([g for g in ct_gaps if g['risk']=='critical'])} critical, {len([g for g in ct_gaps if g['risk']=='high'])} high
**Golden Architecture**: {len([g for g in ga_gaps if g['risk']=='critical'])} critical, {len([g for g in ga_gaps if g['risk']=='high'])} high

## AI Analysis

{st.session_state.ai_analysis or 'Generate analysis in AI Insights tab.'}

---
*Generated by AWS Enterprise Assessment Platform v2.0*
"""
                st.success("✅ Report generated!")
        with c2:
            if st.session_state.report:
                st.download_button("⬇️ Download Report", st.session_state.report,
                    f"aws_assessment_{datetime.now().strftime('%Y%m%d')}.md", "text/markdown", use_container_width=True)
        
        export = {"metadata": {"date": datetime.now().isoformat(), "org": st.session_state.org_name},
                  "control_tower": {"responses": st.session_state.ct_responses, "scores": ct_scores},
                  "golden_architecture": {"responses": st.session_state.ga_responses, "scores": ga_scores}}
        st.download_button("📦 Export JSON", json.dumps(export, indent=2, default=str),
            f"aws_assessment_{datetime.now().strftime('%Y%m%d')}.json", "application/json")
        
        if st.session_state.report:
            with st.expander("Preview Report"):
                st.markdown(st.session_state.report)

if __name__ == "__main__":
    main()
