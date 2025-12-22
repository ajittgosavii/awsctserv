"""
AWS Enterprise Assessment Platform v2.0
Control Tower Migration & Golden Architecture (Serverless) Assessment
AI-Driven Enterprise Grade Assessment Application

Features:
- 80+ Assessment Questions across 12 domains
- AWS Well-Architected Framework Alignment  
- Industry Benchmarking
- AI-Powered Analysis with Claude
- Comprehensive Reporting
"""

import streamlit as st
import json
import os
from datetime import datetime
from typing import Dict, List, Tuple

st.set_page_config(
    page_title="AWS Enterprise Assessment Platform",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono&display=swap');
:root {
    --primary: #0f1419; --secondary: #1a2634; --accent: #ff9500;
    --success: #00d4aa; --warning: #ff9500; --danger: #ff6b6b;
}
.stApp { background: linear-gradient(135deg, #0f1419 0%, #1a2634 50%, #0f1419 100%); }
.main-header {
    background: linear-gradient(90deg, #1a2634, #2d3e50);
    padding: 2rem; border-radius: 16px; margin-bottom: 2rem;
    border: 1px solid #2d3e50;
}
.main-header h1 {
    font-family: 'IBM Plex Sans', sans-serif; font-weight: 700; font-size: 2rem;
    background: linear-gradient(90deg, #ff9500, #00d4aa);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.metric-card {
    background: linear-gradient(145deg, #243447, #1a2634);
    padding: 1.5rem; border-radius: 12px; text-align: center;
    border: 1px solid #2d3e50; margin-bottom: 1rem;
}
.metric-value { font-family: 'IBM Plex Mono'; font-size: 2.5rem; font-weight: 700; }
.metric-label { font-size: 0.85rem; color: #8899a6; text-transform: uppercase; }
.score-high { background: rgba(0,212,170,0.2); color: #00d4aa; }
.score-medium { background: rgba(255,149,0,0.2); color: #ff9500; }
.score-low { background: rgba(255,107,107,0.2); color: #ff6b6b; }
.domain-header { color: #ff9500; font-weight: 600; border-bottom: 2px solid #2d3e50; padding-bottom: 0.5rem; }
.subcat-header { color: #00d4aa; font-weight: 500; border-left: 3px solid #00d4aa; padding-left: 0.5rem; }
.question-card { background: rgba(26,38,52,0.5); padding: 1rem; border-radius: 8px; margin: 0.5rem 0; border: 1px solid #2d3e50; }
.risk-critical { background: #ff6b6b; color: white; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.75rem; }
.risk-high { background: #ff9500; color: white; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.75rem; }
.risk-medium { background: #ffd43b; color: #1a2634; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.75rem; }
.pillar-tag { display: inline-block; padding: 0.15rem 0.4rem; border-radius: 4px; font-size: 0.7rem; margin-right: 0.25rem; }
.pillar-SEC { background: rgba(239,68,68,0.2); color: #ef4444; }
.pillar-REL { background: rgba(59,130,246,0.2); color: #3b82f6; }
.pillar-PERF { background: rgba(168,85,247,0.2); color: #a855f7; }
.pillar-COST { background: rgba(34,197,94,0.2); color: #22c55e; }
.pillar-OPS { background: rgba(249,115,22,0.2); color: #f97316; }
.stButton > button { background: linear-gradient(90deg, #ff9500, #ff7b00); color: white; font-weight: 600; }
hr { border-color: #2d3e50; }
</style>
""", unsafe_allow_html=True)

# Well-Architected Pillars
WA_PILLARS = {
    "SEC": "Security", "REL": "Reliability", "PERF": "Performance",
    "COST": "Cost Optimization", "OPS": "Operational Excellence"
}

# Industry Benchmarks
BENCHMARKS = {
    "financial": {"name": "Financial Services", "avg": 72, "top": 85},
    "healthcare": {"name": "Healthcare", "avg": 65, "top": 80},
    "technology": {"name": "Technology", "avg": 78, "top": 90},
    "retail": {"name": "Retail", "avg": 60, "top": 75},
    "government": {"name": "Government", "avg": 58, "top": 72}
}

# =============================================================================
# CONTROL TOWER ASSESSMENT - COMPREHENSIVE (80+ Questions)
# =============================================================================
CT_DOMAINS = {
    "Organizational Strategy": {
        "weight": 0.12, "pillars": ["OPS", "SEC"],
        "subcategories": {
            "Multi-Account Strategy": [
                {"id": "CT-ORG-001", "q": "What is your AWS multi-account strategy maturity?", "risk": "high",
                 "opts": {"No strategy": 1, "Basic dev/prod separation": 2, "Defined OU structure": 3, "Comprehensive with workload isolation": 4, "Mature with automated lifecycle": 5}},
                {"id": "CT-ORG-002", "q": "How are Organizational Units structured?", "risk": "high",
                 "opts": {"No OU structure": 1, "Basic OUs": 2, "SDLC-aligned OUs": 3, "Nested OUs with separation": 4, "Comprehensive hierarchy with policy inheritance": 5}},
                {"id": "CT-ORG-003", "q": "What is your account naming and metadata approach?", "risk": "medium",
                 "opts": {"No convention": 1, "Informal guidelines": 2, "Documented partially followed": 3, "Enforced with validation": 4, "Automated with metadata enrichment": 5}},
                {"id": "CT-ORG-004", "q": "How is account ownership managed?", "risk": "medium",
                 "opts": {"No ownership model": 1, "Informal assignments": 2, "Documented manual tracking": 3, "CMDB/ServiceNow tracked": 4, "Automated with HR integration": 5}},
            ],
            "Governance Framework": [
                {"id": "CT-ORG-005", "q": "What governance bodies oversee cloud operations?", "risk": "high",
                 "opts": {"No governance": 1, "Ad-hoc IT decisions": 2, "CCoE established": 3, "CCoE with RACI": 4, "Mature federated governance": 5}},
                {"id": "CT-ORG-006", "q": "How are cloud policies documented?", "risk": "medium",
                 "opts": {"No policies": 1, "Informal wikis": 2, "Formal with review": 3, "Integrated with compliance tools": 4, "Policy-as-Code automated": 5}},
                {"id": "CT-ORG-007", "q": "What is your exception management process?", "risk": "medium",
                 "opts": {"No process": 1, "Ad-hoc approvals": 2, "Documented request process": 3, "Workflow with time-bound": 4, "Automated with risk scoring": 5}},
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
                 "opts": {"2+ weeks": 1, "1-2 weeks": 2, "3-5 days": 3, "1-2 days": 4, "<4 hours automated": 5}},
            ],
            "Baseline Configuration": [
                {"id": "CT-ACC-004", "q": "What baseline configurations are applied?", "risk": "critical",
                 "opts": {"No baselines": 1, "Basic IAM/logging": 2, "Security baseline": 3, "Comprehensive with networking": 4, "Full with compliance controls": 5}},
                {"id": "CT-ACC-005", "q": "How is baseline drift detected?", "risk": "high",
                 "opts": {"No detection": 1, "Manual audits": 2, "Config rules alerting": 3, "Automated detection": 4, "Auto-remediation": 5}},
                {"id": "CT-ACC-006", "q": "What IaC approach for baselines?", "risk": "medium",
                 "opts": {"No IaC": 1, "Partial IaC": 2, "CloudFormation StackSets": 3, "Terraform managed": 4, "GitOps automated": 5}},
            ]
        }
    },
    "Guardrails & Controls": {
        "weight": 0.15, "pillars": ["SEC", "OPS"],
        "subcategories": {
            "Service Control Policies": [
                {"id": "CT-GRD-001", "q": "What is your SCP implementation maturity?", "risk": "critical",
                 "opts": {"No SCPs": 1, "Basic deny policies": 2, "Security guardrails": 3, "Comprehensive OU-specific": 4, "Layered with inheritance": 5}},
                {"id": "CT-GRD-002", "q": "How are SCPs tested before deployment?", "risk": "high",
                 "opts": {"No testing": 1, "Manual review": 2, "Sandbox OU testing": 3, "Policy Simulator": 4, "CI/CD with validation": 5}},
                {"id": "CT-GRD-003", "q": "What SCP categories are enforced?", "risk": "high",
                 "opts": {"None": 1, "Region/service only": 2, "Security controls": 3, "Security + compliance + cost": 4, "Full coverage + data residency": 5}},
                {"id": "CT-GRD-004", "q": "How is SCP versioning managed?", "risk": "medium",
                 "opts": {"No version control": 1, "Manual documentation": 2, "Git-based": 3, "With change history": 4, "GitOps with rollback": 5}},
            ],
            "Control Tower Guardrails": [
                {"id": "CT-GRD-005", "q": "Which guardrail categories will you enable?", "risk": "high",
                 "opts": {"Mandatory only": 1, "Some strongly recommended": 2, "All strongly recommended": 3, "Selective elective": 4, "Comprehensive + custom": 5}},
                {"id": "CT-GRD-006", "q": "How will guardrail violations be handled?", "risk": "high",
                 "opts": {"No process": 1, "Manual review": 2, "Automated alerting": 3, "Escalation workflow": 4, "Auto-remediation": 5}},
                {"id": "CT-GRD-007", "q": "Approach to custom Control Tower controls?", "risk": "medium",
                 "opts": {"No custom controls": 1, "Evaluate later": 2, "Identified not implemented": 3, "Key compliance requirements": 4, "Comprehensive with CI/CD": 5}},
            ]
        }
    },
    "Detective Controls & Compliance": {
        "weight": 0.12, "pillars": ["SEC", "OPS"],
        "subcategories": {
            "AWS Config": [
                {"id": "CT-DET-001", "q": "AWS Config deployment status?", "risk": "critical",
                 "opts": {"Not enabled": 1, "Some accounts": 2, "Organization-wide": 3, "With aggregator + custom": 4, "Conformance packs + auto-remediation": 5}},
                {"id": "CT-DET-002", "q": "How many Config rules deployed?", "risk": "high",
                 "opts": {"None": 1, "1-20": 2, "21-50": 3, "51-100 + conformance": 4, "100+ with custom": 5}},
                {"id": "CT-DET-003", "q": "How is Config data aggregated?", "risk": "medium",
                 "opts": {"No aggregation": 1, "Manual collection": 2, "Aggregator in mgmt": 3, "Delegated admin": 4, "Advanced analytics": 5}},
            ],
            "Security Hub": [
                {"id": "CT-DET-004", "q": "Security Hub deployment status?", "risk": "critical",
                 "opts": {"Not enabled": 1, "Some accounts": 2, "Org-wide delegated": 3, "Multiple standards": 4, "Custom insights + integrations": 5}},
                {"id": "CT-DET-005", "q": "Security Hub standards enabled?", "risk": "high",
                 "opts": {"None": 1, "AWS Foundational only": 2, "CIS Benchmark": 3, "Multiple (CIS, PCI, NIST)": 4, "All + custom controls": 5}},
                {"id": "CT-DET-006", "q": "How are findings triaged?", "risk": "high",
                 "opts": {"No triage": 1, "Periodic manual": 2, "Automated alerting critical": 3, "Ticketing integration": 4, "Auto-remediation + exceptions": 5}},
            ],
            "Compliance": [
                {"id": "CT-DET-007", "q": "Compliance frameworks required?", "risk": "critical",
                 "opts": {"None": 1, "Internal policies": 2, "Single framework": 3, "Multiple (SOC2, PCI, HIPAA)": 4, "Complex multi-framework": 5}},
                {"id": "CT-DET-008", "q": "How is compliance evidence collected?", "risk": "high",
                 "opts": {"No collection": 1, "Manual screenshots": 2, "Periodic exports": 3, "Audit Manager": 4, "GRC platform integration": 5}},
            ]
        }
    },
    "Identity & Access Management": {
        "weight": 0.12, "pillars": ["SEC"],
        "subcategories": {
            "Identity Federation": [
                {"id": "CT-IAM-001", "q": "Current identity provider for AWS?", "risk": "critical",
                 "opts": {"Local IAM users": 1, "Some federated SAML": 2, "AWS SSO/Identity Center": 3, "Full IdP integration": 4, "SCIM + JIT provisioning": 5}},
                {"id": "CT-IAM-002", "q": "IdP for IAM Identity Center?", "risk": "high",
                 "opts": {"Native directory": 1, "AD Connector": 2, "Azure AD/Entra": 3, "Okta/enterprise IdP": 4, "Multi-IdP routing": 5}},
                {"id": "CT-IAM-003", "q": "How is MFA enforced?", "risk": "critical",
                 "opts": {"No MFA": 1, "Encouraged not enforced": 2, "Console access": 3, "All human access": 4, "Hardware for privileged": 5}},
            ],
            "Permission Management": [
                {"id": "CT-IAM-004", "q": "Permission sets management?", "risk": "high",
                 "opts": {"Not using Identity Center": 1, "AWS managed only": 2, "Custom inline": 3, "Modular managed": 4, "ABAC-enabled dynamic": 5}},
                {"id": "CT-IAM-005", "q": "Least privilege implementation?", "risk": "high",
                 "opts": {"Broad permissions": 1, "Manual review": 2, "Access Analyzer": 3, "Regular right-sizing": 4, "Automated continuous": 5}},
                {"id": "CT-IAM-006", "q": "Privileged access management?", "risk": "critical",
                 "opts": {"No distinction": 1, "Separate accounts": 2, "JIT for some": 3, "PAM solution": 4, "Zero-standing + recording": 5}},
            ],
            "Workload Identity": [
                {"id": "CT-IAM-007", "q": "Machine/service identity management?", "risk": "high",
                 "opts": {"Long-lived keys": 1, "IAM roles some": 2, "Role chaining": 3, "Roles Anywhere": 4, "Short-lived comprehensive": 5}},
                {"id": "CT-IAM-008", "q": "Cross-account roles management?", "risk": "high",
                 "opts": {"Manual per account": 1, "StackSets": 2, "Centralized IaC": 3, "Role vending": 4, "Automated trust controls": 5}},
            ]
        }
    },
    "Network Architecture": {
        "weight": 0.10, "pillars": ["SEC", "REL", "PERF"],
        "subcategories": {
            "Network Topology": [
                {"id": "CT-NET-001", "q": "Multi-account network architecture?", "risk": "high",
                 "opts": {"Independent VPCs": 1, "VPC peering select": 2, "Transit Gateway": 3, "Hub-spoke centralized": 4, "Advanced segmentation": 5}},
                {"id": "CT-NET-002", "q": "Network IPAM management?", "risk": "high",
                 "opts": {"No IPAM": 1, "Spreadsheet": 2, "VPC IPAM basic": 3, "Automated allocation": 4, "Enterprise IPAM integration": 5}},
                {"id": "CT-NET-003", "q": "VPC design pattern?", "risk": "medium",
                 "opts": {"No standard": 1, "Basic public/private": 2, "Multi-AZ NAT": 3, "Standardized automated": 4, "Customizable blueprints": 5}},
            ],
            "Hybrid & Security": [
                {"id": "CT-NET-004", "q": "On-premises connectivity?", "risk": "high",
                 "opts": {"None": 5, "Site-to-site per account": 2, "Centralized VPN": 3, "Direct Connect + VPN": 4, "Redundant DC engineering": 5}},
                {"id": "CT-NET-005", "q": "Hybrid DNS resolution?", "risk": "medium",
                 "opts": {"No hybrid DNS": 1, "Manual config": 2, "R53 Resolver forwarding": 3, "Centralized endpoints": 4, "Full bidirectional": 5}},
                {"id": "CT-NET-006", "q": "Network traffic inspection?", "risk": "high",
                 "opts": {"No inspection": 1, "SG/NACLs only": 2, "Network Firewall some": 3, "Centralized inspection": 4, "IDS/IPS + threat intel": 5}},
                {"id": "CT-NET-007", "q": "Egress traffic control?", "risk": "critical",
                 "opts": {"No controls": 1, "NAT no filtering": 2, "Centralized logging": 3, "Proxy URL filtering": 4, "Zero-trust + DLP": 5}},
            ]
        }
    },
    "Logging & Monitoring": {
        "weight": 0.10, "pillars": ["OPS", "SEC", "REL"],
        "subcategories": {
            "Centralized Logging": [
                {"id": "CT-LOG-001", "q": "CloudTrail configuration?", "risk": "critical",
                 "opts": {"Not all accounts": 1, "Account-level local": 2, "Organization trail": 3, "With data events": 4, "Insights + Lake": 5}},
                {"id": "CT-LOG-002", "q": "VPC Flow Logs management?", "risk": "high",
                 "opts": {"Not enabled": 1, "Some VPCs": 2, "All centralized": 3, "Traffic mirroring": 4, "Real-time analysis": 5}},
                {"id": "CT-LOG-003", "q": "Log retention strategy?", "risk": "medium",
                 "opts": {"No policy": 1, "Default": 2, "S3 lifecycle": 3, "Tiered Glacier": 4, "Compliance legal hold": 5}},
                {"id": "CT-LOG-004", "q": "Log analysis and correlation?", "risk": "high",
                 "opts": {"None": 1, "Manual when needed": 2, "CloudWatch Insights": 3, "SIEM integration": 4, "ML anomaly detection": 5}},
            ],
            "Monitoring": [
                {"id": "CT-LOG-005", "q": "CloudWatch configuration?", "risk": "medium",
                 "opts": {"Default only": 1, "Some custom metrics": 2, "Cross-account access": 3, "Centralized dashboards": 4, "X-Ray ServiceLens": 5}},
                {"id": "CT-LOG-006", "q": "Alerting strategy?", "risk": "medium",
                 "opts": {"No alerting": 1, "Email some": 2, "SNS PagerDuty/Slack": 3, "Tiered severity": 4, "AIOps runbook automation": 5}},
            ]
        }
    },
    "Cost Management": {
        "weight": 0.08, "pillars": ["COST", "OPS"],
        "subcategories": {
            "Cost Visibility": [
                {"id": "CT-FIN-001", "q": "Cost visibility across accounts?", "risk": "medium",
                 "opts": {"Individual billing": 1, "Consolidated limited": 2, "Cost Explorer basic": 3, "CUR Athena": 4, "FinOps platform": 5}},
                {"id": "CT-FIN-002", "q": "Cost allocation to business units?", "risk": "medium",
                 "opts": {"No allocation": 1, "Account-based": 2, "Tags partial": 3, "Comprehensive enforced": 4, "Advanced split amortization": 5}},
                {"id": "CT-FIN-003", "q": "Budgets and forecasting?", "risk": "medium",
                 "opts": {"No budgets": 1, "Annual org level": 2, "Account-level alerts": 3, "Granular forecasting": 4, "ML anomaly detection": 5}},
            ],
            "Optimization": [
                {"id": "CT-FIN-004", "q": "RI/Savings Plans management?", "risk": "medium",
                 "opts": {"None": 1, "Reactive RIs": 2, "Coverage periodic": 3, "Optimized central": 4, "Automated sharing": 5}},
                {"id": "CT-FIN-005", "q": "Optimization recommendations?", "risk": "low",
                 "opts": {"None": 1, "Ad-hoc": 2, "Trusted Advisor": 3, "Compute Optimizer": 4, "Automated governance": 5}},
            ]
        }
    },
    "Backup & DR": {
        "weight": 0.08, "pillars": ["REL", "SEC"],
        "subcategories": {
            "Backup": [
                {"id": "CT-BDR-001", "q": "Backup management across accounts?", "risk": "critical",
                 "opts": {"No strategy": 1, "Account-level": 2, "AWS Backup each": 3, "Centralized policies": 4, "Org-wide cross-account": 5}},
                {"id": "CT-BDR-002", "q": "Backup policy enforcement?", "risk": "high",
                 "opts": {"No enforcement": 1, "Guidelines": 2, "Config rules": 3, "Mandatory opt-in": 4, "Preventive controls": 5}},
                {"id": "CT-BDR-003", "q": "Backup testing?", "risk": "high",
                 "opts": {"None": 1, "Ad-hoc": 2, "Periodic manual": 3, "Scheduled automated": 4, "Continuous DR drills": 5}},
            ],
            "Disaster Recovery": [
                {"id": "CT-BDR-004", "q": "Multi-region DR strategy?", "risk": "high",
                 "opts": {"None": 1, "Backup to region": 2, "Pilot light": 3, "Warm standby": 4, "Active-active": 5}},
                {"id": "CT-BDR-005", "q": "Control Tower resilience?", "risk": "high",
                 "opts": {"No consideration": 1, "Documentation": 2, "IaC backup": 3, "Automated backup": 4, "Full DR tested": 5}},
            ]
        }
    },
    "Migration Readiness": {
        "weight": 0.08, "pillars": ["OPS", "REL"],
        "subcategories": {
            "Account Inventory": [
                {"id": "CT-MIG-001", "q": "Existing account inventory?", "risk": "high",
                 "opts": {"No inventory": 1, "Partial": 2, "Complete limited meta": 3, "With ownership/purpose": 4, "Dynamic automated": 5}},
                {"id": "CT-MIG-002", "q": "Account count and distribution?", "risk": "high",
                 "opts": {"Unknown": 1, "1-25": 5, "26-100": 4, "101-500": 3, "500+": 2}},
                {"id": "CT-MIG-003", "q": "Non-standard configurations?", "risk": "high",
                 "opts": {"Unknown": 1, "Many non-standard": 2, "Some identified": 3, "Few non-standard": 4, "All follow standards": 5}},
            ],
            "Enrollment": [
                {"id": "CT-MIG-004", "q": "Account readiness for enrollment?", "risk": "critical",
                 "opts": {"No assessment": 1, "Basic some": 2, "Pre-flight issues identified": 3, "Most ready remediation plan": 4, "All verified": 5}},
                {"id": "CT-MIG-005", "q": "Config/CloudTrail conflicts?", "risk": "critical",
                 "opts": {"Unknown": 1, "Many conflicts": 2, "Identified planned": 3, "Most resolved": 4, "None or all resolved": 5}},
                {"id": "CT-MIG-006", "q": "Accounts that cannot be enrolled?", "risk": "medium",
                 "opts": {"No approach": 1, "Determine during": 2, "Identified no solution": 3, "Legacy handling plan": 4, "Comprehensive parity": 5}},
            ]
        }
    },
    "Operational Readiness": {
        "weight": 0.08, "pillars": ["OPS"],
        "subcategories": {
            "Skills": [
                {"id": "CT-OPS-001", "q": "Team Control Tower experience?", "risk": "high",
                 "opts": {"None": 1, "Training awareness": 2, "Sandbox hands-on": 3, "Production experience": 4, "Deep expertise": 5}},
                {"id": "CT-OPS-002", "q": "Training plan for CT operations?", "risk": "medium",
                 "opts": {"None": 1, "Self-paced": 2, "AWS training identified": 3, "Comprehensive program": 4, "Certification + KT": 5}},
            ],
            "Runbooks": [
                {"id": "CT-OPS-003", "q": "Operational runbooks defined?", "risk": "medium",
                 "opts": {"None": 1, "During implementation": 2, "Basic planned": 3, "Comprehensive automated": 4, "Full SSM automation": 5}},
                {"id": "CT-OPS-004", "q": "Incident response process?", "risk": "medium",
                 "opts": {"None": 1, "Ad-hoc": 2, "Escalation path": 3, "IR playbooks": 4, "Automated IR": 5}},
            ],
            "Change Management": [
                {"id": "CT-OPS-005", "q": "Control Tower change management?", "risk": "medium",
                 "opts": {"No process": 1, "Informal": 2, "Tickets + approval": 3, "CAB review": 4, "GitOps validation": 5}},
                {"id": "CT-OPS-006", "q": "Control Tower upgrade approach?", "risk": "medium",
                 "opts": {"No strategy": 1, "When issues": 2, "Monitor + periodic": 3, "Scheduled + testing": 4, "Automated rollback": 5}},
            ]
        }
    },
    "Data Protection": {
        "weight": 0.07, "pillars": ["SEC"],
        "subcategories": {
            "Encryption": [
                {"id": "CT-DAT-001", "q": "Encryption strategy at rest?", "risk": "critical",
                 "opts": {"No requirements": 1, "AWS managed SSE": 2, "KMS AWS managed": 3, "Customer managed KMS": 4, "Centralized hierarchy rotation": 5}},
                {"id": "CT-DAT-002", "q": "KMS management across accounts?", "risk": "high",
                 "opts": {"No strategy": 1, "Account-local": 2, "Shared cross-account": 3, "Centralized key mgmt": 4, "Multi-region automated": 5}},
            ],
            "Classification": [
                {"id": "CT-DAT-003", "q": "Data classification framework?", "risk": "high",
                 "opts": {"None": 1, "Basic public/internal/confidential": 2, "With handling procedures": 3, "Technical controls mapping": 4, "Automated DLP": 5}},
                {"id": "CT-DAT-004", "q": "Sensitive data discovery?", "risk": "high",
                 "opts": {"None": 1, "Manual inventory": 2, "Macie for S3": 3, "Custom identifiers": 4, "Comprehensive DLP": 5}},
            ]
        }
    }
}

# =============================================================================
# GOLDEN ARCHITECTURE (SERVERLESS) ASSESSMENT
# =============================================================================
GA_DOMAINS = {
    "Serverless Compute": {
        "weight": 0.15, "pillars": ["PERF", "COST", "OPS"],
        "subcategories": {
            "Lambda": [
                {"id": "GA-CMP-001", "q": "Lambda adoption maturity?", "risk": "medium",
                 "opts": {"No usage": 1, "Experimental": 2, "Production specific": 3, "Significant standards": 4, "Lambda-first strategy": 5}},
                {"id": "GA-CMP-002", "q": "Lambda organization and management?", "risk": "medium",
                 "opts": {"Ad-hoc": 1, "Naming conventions": 2, "Microservices-aligned": 3, "Domain-driven": 4, "Function mesh discovery": 5}},
                {"id": "GA-CMP-003", "q": "Lambda runtime management?", "risk": "medium",
                 "opts": {"Default no mgmt": 1, "Standard selection": 2, "Versioning + upgrade": 3, "Automated updates": 4, "Custom container": 5}},
                {"id": "GA-CMP-004", "q": "Cold start handling?", "risk": "low",
                 "opts": {"No consideration": 1, "Awareness only": 2, "Basic optimization": 3, "Provisioned concurrency": 4, "SnapStart + warming": 5}},
                {"id": "GA-CMP-005", "q": "Lambda layers strategy?", "risk": "low",
                 "opts": {"No layers": 1, "Some shared": 2, "Standard libraries": 3, "Versioned dependencies": 4, "Automated CI/CD": 5}},
            ],
            "Containers": [
                {"id": "GA-CMP-006", "q": "Fargate adoption level?", "risk": "medium",
                 "opts": {"None": 1, "Experimental": 2, "Specific workloads": 3, "Default containerized": 4, "Comprehensive + Spot": 5}},
                {"id": "GA-CMP-007", "q": "Lambda vs Fargate decision framework?", "risk": "medium",
                 "opts": {"No framework": 1, "Ad-hoc": 2, "Basic guidelines": 3, "Decision tree": 4, "Automated cost modeling": 5}},
            ]
        }
    },
    "API & Integration": {
        "weight": 0.12, "pillars": ["PERF", "SEC", "REL"],
        "subcategories": {
            "API Gateway": [
                {"id": "GA-API-001", "q": "API Gateway type standard?", "risk": "medium",
                 "opts": {"No usage": 1, "REST all": 2, "HTTP default": 3, "Right-sized selection": 4, "Multi-type domains WAF": 5}},
                {"id": "GA-API-002", "q": "API versioning management?", "risk": "medium",
                 "opts": {"No versioning": 1, "URL path": 2, "Stage-based": 3, "Header routing": 4, "Comprehensive deprecation": 5}},
                {"id": "GA-API-003", "q": "API documentation approach?", "risk": "low",
                 "opts": {"None": 1, "Manual": 2, "OpenAPI specs": 3, "Auto-generated portal": 4, "Developer portal SDK": 5}},
                {"id": "GA-API-004", "q": "Rate limiting configuration?", "risk": "high",
                 "opts": {"None": 1, "Default limits": 2, "Custom per stage": 3, "Usage plans + keys": 4, "Dynamic quota mgmt": 5}},
            ],
            "Events": [
                {"id": "GA-API-005", "q": "EventBridge adoption?", "risk": "medium",
                 "opts": {"None": 1, "Basic buses": 2, "Custom + rules": 3, "Event-driven patterns": 4, "Event mesh + registry": 5}},
                {"id": "GA-API-006", "q": "Event schema management?", "risk": "medium",
                 "opts": {"None": 1, "Informal docs": 2, "Registry discovery": 3, "Versioning validation": 4, "Governance breaking change": 5}},
                {"id": "GA-API-007", "q": "SQS/SNS patterns?", "risk": "medium",
                 "opts": {"None": 1, "Basic queue": 2, "Fan-out SNS→SQS": 3, "DLQ + retry": 4, "FIFO exactly-once": 5}},
            ]
        }
    },
    "Orchestration": {
        "weight": 0.10, "pillars": ["REL", "OPS"],
        "subcategories": {
            "Step Functions": [
                {"id": "GA-WRK-001", "q": "Step Functions adoption?", "risk": "medium",
                 "opts": {"None": 1, "Experimental": 2, "Standard some": 3, "Orchestration standard": 4, "Express + callbacks": 5}},
                {"id": "GA-WRK-002", "q": "Workflow error handling?", "risk": "high",
                 "opts": {"None": 1, "Basic try-catch": 2, "Retry policies": 3, "Comprehensive fallbacks": 4, "Saga compensation": 5}},
                {"id": "GA-WRK-003", "q": "Workflow patterns implemented?", "risk": "medium",
                 "opts": {"None": 1, "Sequential only": 2, "Parallel + choice": 3, "Map dynamic": 4, "Callback human approval": 5}},
            ]
        }
    },
    "Data Layer": {
        "weight": 0.12, "pillars": ["PERF", "REL", "COST"],
        "subcategories": {
            "DynamoDB": [
                {"id": "GA-DAT-001", "q": "DynamoDB adoption level?", "risk": "medium",
                 "opts": {"None": 1, "Specific cases": 2, "Default NoSQL": 3, "Advanced GSI transactions": 4, "Single-table patterns": 5}},
                {"id": "GA-DAT-002", "q": "DynamoDB capacity management?", "risk": "medium",
                 "opts": {"Not using": 1, "Provisioned manual": 2, "On-demand all": 3, "Right-sized auto-scale": 4, "Optimized reserved": 5}},
                {"id": "GA-DAT-003", "q": "DynamoDB design patterns?", "risk": "medium",
                 "opts": {"N/A": 1, "Simple key-value": 2, "Multiple tables": 3, "Single-table basic": 4, "GSI overloading": 5}},
                {"id": "GA-DAT-004", "q": "DynamoDB caching?", "risk": "low",
                 "opts": {"None": 1, "Application-level": 2, "ElastiCache front": 3, "DAX read-heavy": 4, "Multi-layer strategy": 5}},
            ],
            "Relational": [
                {"id": "GA-DAT-005", "q": "Aurora Serverless usage?", "risk": "medium",
                 "opts": {"None": 1, "Evaluating v2": 2, "Dev/test": 3, "Production": 4, "With Data API": 5}},
                {"id": "GA-DAT-006", "q": "Database connections serverless?", "risk": "high",
                 "opts": {"Direct connections": 1, "Lambda pooling": 2, "RDS Proxy": 3, "Proxy + IAM": 4, "Data API connectionless": 5}},
            ],
            "Analytics": [
                {"id": "GA-DAT-007", "q": "Serverless analytics approach?", "risk": "low",
                 "opts": {"None": 1, "Traditional": 2, "Athena ad-hoc": 3, "Data lake Glue": 4, "Comprehensive platform": 5}},
            ]
        }
    },
    "Serverless Security": {
        "weight": 0.15, "pillars": ["SEC"],
        "subcategories": {
            "Function Security": [
                {"id": "GA-SEC-001", "q": "Lambda execution roles?", "risk": "critical",
                 "opts": {"Single role all": 1, "Broad per app": 2, "Function-specific": 3, "Least-privilege reviewed": 4, "Automated boundaries": 5}},
                {"id": "GA-SEC-002", "q": "Code signing Lambda?", "risk": "high",
                 "opts": {"None": 1, "Evaluating": 2, "Some functions": 3, "Validation policy": 4, "Mandatory CI/CD": 5}},
                {"id": "GA-SEC-003", "q": "Lambda vulnerability management?", "risk": "high",
                 "opts": {"No scanning": 1, "Manual review": 2, "CI/CD scanning": 3, "Inspector": 4, "Continuous auto-remediation": 5}},
            ],
            "Secrets": [
                {"id": "GA-SEC-004", "q": "Secrets management?", "risk": "critical",
                 "opts": {"Env vars plaintext": 1, "Encrypted env": 2, "Parameter Store": 3, "Secrets Manager rotation": 4, "Lambda extension caching": 5}},
                {"id": "GA-SEC-005", "q": "Secret rotation?", "risk": "high",
                 "opts": {"None": 1, "Manual when needed": 2, "Scheduled manual": 3, "Automated some": 4, "Automated all": 5}},
            ],
            "API Security": [
                {"id": "GA-SEC-006", "q": "API authentication?", "risk": "critical",
                 "opts": {"None": 1, "API keys only": 2, "Cognito User Pools": 3, "Lambda authorizers JWT": 4, "Multi-method fine-grained": 5}},
                {"id": "GA-SEC-007", "q": "API traffic protection?", "risk": "high",
                 "opts": {"None": 1, "Basic throttling": 2, "WAF managed rules": 3, "WAF custom": 4, "WAF + Shield + bot": 5}},
                {"id": "GA-SEC-008", "q": "Input validation?", "risk": "high",
                 "opts": {"None": 1, "Basic in code": 2, "API Gateway validation": 3, "Schema + sanitization": 4, "Comprehensive + WAF": 5}},
            ]
        }
    },
    "Observability": {
        "weight": 0.10, "pillars": ["OPS", "REL"],
        "subcategories": {
            "Logging": [
                {"id": "GA-OBS-001", "q": "Serverless logging structure?", "risk": "medium",
                 "opts": {"Console.log": 1, "Basic timestamps": 2, "Structured JSON": 3, "Correlation IDs": 4, "Powertools comprehensive": 5}},
                {"id": "GA-OBS-002", "q": "Log aggregation and analysis?", "risk": "medium",
                 "opts": {"Console only": 1, "Logs Insights": 2, "Centralized S3/OpenSearch": 3, "Real-time analysis": 4, "ML anomaly": 5}},
            ],
            "Tracing": [
                {"id": "GA-OBS-003", "q": "Distributed tracing approach?", "risk": "medium",
                 "opts": {"None": 1, "X-Ray some": 2, "X-Ray all serverless": 3, "Custom segments annotations": 4, "Comprehensive service map": 5}},
            ],
            "Metrics": [
                {"id": "GA-OBS-004", "q": "Custom metrics captured?", "risk": "medium",
                 "opts": {"Default only": 1, "Some custom": 2, "Business EMF": 3, "Comprehensive dimensions": 4, "Real-time embedded": 5}},
                {"id": "GA-OBS-005", "q": "Serverless dashboards?", "risk": "low",
                 "opts": {"None": 1, "Basic function": 2, "Application-level": 3, "Service-level SLIs": 4, "Comprehensive drill-down": 5}},
                {"id": "GA-OBS-006", "q": "SLOs/SLIs for serverless?", "risk": "medium",
                 "opts": {"None": 1, "Informal targets": 2, "Key function SLIs": 3, "SLOs error budgets": 4, "Comprehensive automation": 5}},
            ]
        }
    },
    "CI/CD & DevOps": {
        "weight": 0.10, "pillars": ["OPS"],
        "subcategories": {
            "Deployment": [
                {"id": "GA-DEV-001", "q": "Serverless deployment approach?", "risk": "medium",
                 "opts": {"Manual console": 1, "CLI-based": 2, "SAM/Serverless Framework": 3, "CDK multi-env": 4, "GitOps automated": 5}},
                {"id": "GA-DEV-002", "q": "Infrastructure as Code?", "risk": "medium",
                 "opts": {"None": 1, "Partial": 2, "Full SAM/CDK": 3, "Linting validation": 4, "Automated testing security": 5}},
                {"id": "GA-DEV-003", "q": "Deployment strategies?", "risk": "high",
                 "opts": {"All-at-once": 1, "Manual staged": 2, "Blue-green": 3, "Canary + metrics": 4, "Automated canary rollback": 5}},
                {"id": "GA-DEV-004", "q": "Rollback handling?", "risk": "high",
                 "opts": {"No capability": 1, "Manual redeploy": 2, "Automated on failure": 3, "Version aliases": 4, "Automated blast radius": 5}},
            ],
            "Testing": [
                {"id": "GA-DEV-005", "q": "Serverless testing strategy?", "risk": "high",
                 "opts": {"None": 1, "Unit only": 2, "Unit + integration": 3, "Comprehensive local": 4, "Full pyramid contracts": 5}},
                {"id": "GA-DEV-006", "q": "Local development?", "risk": "low",
                 "opts": {"Deploy to AWS": 1, "Limited local": 2, "SAM Local": 3, "LocalStack full": 4, "Comprehensive mocking": 5}},
            ]
        }
    },
    "Cost Optimization": {
        "weight": 0.08, "pillars": ["COST"],
        "subcategories": {
            "Visibility": [
                {"id": "GA-CST-001", "q": "Serverless cost visibility?", "risk": "medium",
                 "opts": {"No tracking": 1, "Service-level": 2, "Function-level": 3, "Tagging per-app": 4, "Real-time per invocation": 5}},
                {"id": "GA-CST-002", "q": "Cost anomaly detection?", "risk": "medium",
                 "opts": {"None": 1, "Manual review": 2, "AWS Anomaly Detection": 3, "Custom alerting": 4, "Real-time auto-remediation": 5}},
            ],
            "Optimization": [
                {"id": "GA-CST-003", "q": "Lambda memory optimization?", "risk": "low",
                 "opts": {"Default": 1, "Manual testing": 2, "Power Tuning": 3, "Regular cycles": 4, "Automated monitoring": 5}},
                {"id": "GA-CST-004", "q": "Unused resource cleanup?", "risk": "low",
                 "opts": {"None": 1, "Manual periodic": 2, "Automated reporting": 3, "Scheduled approval": 4, "Automated lifecycle": 5}},
                {"id": "GA-CST-005", "q": "Graviton utilization?", "risk": "low",
                 "opts": {"Not aware": 1, "Evaluating": 2, "Some functions": 3, "Default compatible": 4, "Comprehensive strategy": 5}},
            ]
        }
    },
    "Resilience": {
        "weight": 0.08, "pillars": ["REL"],
        "subcategories": {
            "Fault Tolerance": [
                {"id": "GA-REL-001", "q": "Retry and error handling?", "risk": "high",
                 "opts": {"None": 1, "Default Lambda": 2, "Custom backoff": 3, "Circuit breaker": 4, "Patterns + fallbacks": 5}},
                {"id": "GA-REL-002", "q": "Dead letter queue configuration?", "risk": "medium",
                 "opts": {"None": 1, "Some functions": 2, "All async": 3, "Monitoring alerting": 4, "Automated reprocessing": 5}},
                {"id": "GA-REL-003", "q": "Idempotency implementation?", "risk": "high",
                 "opts": {"None": 1, "Awareness only": 2, "Critical operations": 3, "Comprehensive tokens": 4, "Powertools all": 5}},
            ],
            "Multi-Region": [
                {"id": "GA-REL-004", "q": "Multi-region strategy serverless?", "risk": "high",
                 "opts": {"Single region": 1, "Data replicated DR": 2, "Active-passive manual": 3, "Active-passive automated": 4, "Active-active": 5}},
                {"id": "GA-REL-005", "q": "Global data consistency?", "risk": "high",
                 "opts": {"N/A single": 1, "Eventually consistent": 2, "Global Tables": 3, "Multi-region defined": 4, "Comprehensive patterns": 5}},
            ]
        }
    }
}

# =============================================================================
# APPLICATION LOGIC
# =============================================================================

def init_state():
    defaults = {
        'ct_responses': {}, 'ga_responses': {}, 'ai_analysis': None,
        'org_name': '', 'assessor_name': '', 'industry': 'technology', 'report': None
    }
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
    if score >= 80: return "Optimized", "score-high"
    if score >= 60: return "Managed", "score-medium"
    if score >= 40: return "Developing", "score-medium"
    return "Initial", "score-low"

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
            return "⚠️ Set ANTHROPIC_API_KEY in Streamlit secrets for AI analysis."
        client = anthropic.Anthropic(api_key=key)
        resp = client.messages.create(
            model="claude-sonnet-4-20250514", max_tokens=8192,
            system="You are an expert AWS Solutions Architect specializing in Control Tower and serverless architectures. Provide detailed, actionable enterprise recommendations.",
            messages=[{"role": "user", "content": prompt}]
        )
        return resp.content[0].text
    except Exception as e:
        return f"⚠️ AI Error: {e}"

def render_metric(value, label, suffix="%"):
    color = "#00d4aa" if value >= 60 else "#ff9500" if value >= 40 else "#ff6b6b"
    level, _ = get_level(value)
    st.markdown(f'''<div class="metric-card">
        <div class="metric-value" style="color:{color}">{value:.0f}{suffix}</div>
        <div class="metric-label">{label}</div>
        <div style="margin-top:0.5rem;color:{color}">{level}</div>
    </div>''', unsafe_allow_html=True)

def render_assessment(domains, responses, prefix):
    for dname, ddata in domains.items():
        with st.expander(f"📁 {dname} (Weight: {ddata['weight']*100:.0f}%)"):
            st.markdown(f'<div class="domain-header">{dname}</div>', unsafe_allow_html=True)
            pillars = " ".join([f'<span class="pillar-tag pillar-{p}">{WA_PILLARS.get(p,p)}</span>' for p in ddata["pillars"]])
            st.markdown(f"**Well-Architected:** {pillars}", unsafe_allow_html=True)
            
            for sname, questions in ddata["subcategories"].items():
                st.markdown(f'<div class="subcat-header">{sname}</div>', unsafe_allow_html=True)
                for q in questions:
                    with st.container():
                        st.markdown(f'<div class="question-card">', unsafe_allow_html=True)
                        col1, col2 = st.columns([4, 1])
                        with col1:
                            st.markdown(f"**{q['id']}**: {q['q']}")
                        with col2:
                            st.markdown(f'<span class="risk-{q["risk"]}">{q["risk"].upper()}</span>', unsafe_allow_html=True)
                        
                        opts = list(q["opts"].keys())
                        curr = 0
                        if q["id"] in responses:
                            curr_val = responses[q["id"]]
                            for i, (opt, val) in enumerate(q["opts"].items()):
                                if val == curr_val: curr = i; break
                        
                        sel = st.radio(f"_{q['id']}", opts, index=curr, 
                                      key=f"{prefix}_{q['id']}", label_visibility="collapsed")
                        responses[q["id"]] = q["opts"][sel]
                        st.markdown('</div>', unsafe_allow_html=True)

# =============================================================================
# MAIN APPLICATION
# =============================================================================
def main():
    init_state()
    
    # Header
    st.markdown('''<div class="main-header">
        <h1>🏗️ AWS Enterprise Assessment Platform</h1>
        <p>AI-Driven Control Tower & Golden Architecture Assessment | Enterprise Edition v2.0</p>
    </div>''', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("### 📋 Configuration")
        st.session_state.org_name = st.text_input("Organization", st.session_state.org_name)
        st.session_state.assessor_name = st.text_input("Assessor", st.session_state.assessor_name)
        st.session_state.industry = st.selectbox("Industry", list(BENCHMARKS.keys()),
            format_func=lambda x: BENCHMARKS[x]["name"],
            index=list(BENCHMARKS.keys()).index(st.session_state.industry))
        
        st.markdown("---")
        st.markdown("### 📊 Progress")
        ct_total = count_questions(CT_DOMAINS)
        ct_done = len(st.session_state.ct_responses)
        st.progress(ct_done/ct_total if ct_total else 0)
        st.caption(f"Control Tower: {ct_done}/{ct_total}")
        
        ga_total = count_questions(GA_DOMAINS)
        ga_done = len(st.session_state.ga_responses)
        st.progress(ga_done/ga_total if ga_total else 0)
        st.caption(f"Golden Arch: {ga_done}/{ga_total}")
        
        st.markdown("---")
        st.metric("Total Questions", ct_total + ga_total)
        st.metric("Answered", ct_done + ga_done)
    
    # Main Tabs
    tabs = st.tabs(["📊 Dashboard", "🎛️ Control Tower", "⚡ Golden Architecture", 
                    "🔍 Gaps", "🤖 AI Insights", "📄 Reports"])
    
    # Dashboard
    with tabs[0]:
        st.markdown("## 📊 Executive Dashboard")
        ct_scores = calc_scores(st.session_state.ct_responses, CT_DOMAINS) if st.session_state.ct_responses else {"overall": 0}
        ga_scores = calc_scores(st.session_state.ga_responses, GA_DOMAINS) if st.session_state.ga_responses else {"overall": 0}
        
        col1, col2, col3, col4 = st.columns(4)
        with col1: render_metric(ct_scores["overall"], "Control Tower")
        with col2: render_metric(ga_scores["overall"], "Golden Architecture")
        with col3: render_metric((ct_scores["overall"]+ga_scores["overall"])/2, "Combined")
        with col4:
            bench = BENCHMARKS[st.session_state.industry]
            combined = (ct_scores["overall"]+ga_scores["overall"])/2
            vs_avg = combined - bench["avg"]
            st.markdown(f'''<div class="metric-card">
                <div class="metric-value" style="color:{"#00d4aa" if vs_avg>=0 else "#ff6b6b"}">{vs_avg:+.0f}%</div>
                <div class="metric-label">vs {bench["name"]} Avg</div>
            </div>''', unsafe_allow_html=True)
        
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Control Tower Domains")
            if "domains" in ct_scores:
                for dname, data in ct_scores["domains"].items():
                    level, _ = get_level(data["score"])
                    st.markdown(f"**{dname}**: {data['score']:.0f}% ({level})")
                    st.progress(data["score"]/100)
        with col2:
            st.markdown("### Golden Architecture Domains")
            if "domains" in ga_scores:
                for dname, data in ga_scores["domains"].items():
                    level, _ = get_level(data["score"])
                    st.markdown(f"**{dname}**: {data['score']:.0f}% ({level})")
                    st.progress(data["score"]/100)
    
    # Control Tower Assessment
    with tabs[1]:
        st.markdown(f"## 🎛️ Control Tower Assessment ({count_questions(CT_DOMAINS)} questions)")
        render_assessment(CT_DOMAINS, st.session_state.ct_responses, "ct")
    
    # Golden Architecture Assessment
    with tabs[2]:
        st.markdown(f"## ⚡ Golden Architecture Assessment ({count_questions(GA_DOMAINS)} questions)")
        render_assessment(GA_DOMAINS, st.session_state.ga_responses, "ga")
    
    # Gaps
    with tabs[3]:
        st.markdown("## 🔍 Gap Analysis")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Control Tower Gaps")
            ct_gaps = find_gaps(st.session_state.ct_responses, CT_DOMAINS)
            if ct_gaps:
                critical = len([g for g in ct_gaps if g["risk"]=="critical"])
                high = len([g for g in ct_gaps if g["risk"]=="high"])
                st.error(f"🔴 Critical: {critical} | 🟠 High: {high}")
                for g in ct_gaps[:10]:
                    with st.expander(f"{g['id']} - {g['domain'][:25]}..."):
                        st.markdown(f"**{g['question']}**")
                        st.markdown(f"Score: {g['score']}/5 | Risk: **{g['risk'].upper()}**")
            else:
                st.success("No critical gaps identified")
        
        with col2:
            st.markdown("### Golden Architecture Gaps")
            ga_gaps = find_gaps(st.session_state.ga_responses, GA_DOMAINS)
            if ga_gaps:
                critical = len([g for g in ga_gaps if g["risk"]=="critical"])
                high = len([g for g in ga_gaps if g["risk"]=="high"])
                st.error(f"🔴 Critical: {critical} | 🟠 High: {high}")
                for g in ga_gaps[:10]:
                    with st.expander(f"{g['id']} - {g['domain'][:25]}..."):
                        st.markdown(f"**{g['question']}**")
                        st.markdown(f"Score: {g['score']}/5 | Risk: **{g['risk'].upper()}**")
            else:
                st.success("No critical gaps identified")
    
    # AI Insights
    with tabs[4]:
        st.markdown("## 🤖 AI-Driven Analysis")
        
        analysis_type = st.selectbox("Analysis Type", [
            "🎯 Gap Analysis & Prioritization",
            "🗺️ Implementation Roadmap",
            "⚠️ Risk Assessment",
            "💰 Cost-Benefit Analysis",
            "🏗️ Architecture Recommendations"
        ])
        
        context = st.text_area("Additional Context", placeholder="Add specific constraints, timeline, or requirements...")
        
        if st.button("🚀 Generate AI Analysis", type="primary"):
            if not st.session_state.ct_responses and not st.session_state.ga_responses:
                st.warning("Complete some assessment questions first.")
            else:
                with st.spinner("Generating analysis..."):
                    ct_scores = calc_scores(st.session_state.ct_responses, CT_DOMAINS)
                    ga_scores = calc_scores(st.session_state.ga_responses, GA_DOMAINS)
                    ct_gaps = find_gaps(st.session_state.ct_responses, CT_DOMAINS)
                    ga_gaps = find_gaps(st.session_state.ga_responses, GA_DOMAINS)
                    
                    prompt = f"""
AWS Enterprise Assessment Analysis Request: {analysis_type}

CONTROL TOWER SCORES:
- Overall: {ct_scores['overall']:.1f}%
- Domains: {json.dumps({k: v['score'] for k,v in ct_scores.get('domains',{}).items()}, indent=2)}

GOLDEN ARCHITECTURE SCORES:
- Overall: {ga_scores['overall']:.1f}%  
- Domains: {json.dumps({k: v['score'] for k,v in ga_scores.get('domains',{}).items()}, indent=2)}

CRITICAL GAPS:
Control Tower: {len([g for g in ct_gaps if g['risk']=='critical'])} critical, {len([g for g in ct_gaps if g['risk']=='high'])} high
{json.dumps(ct_gaps[:5], indent=2)}

Golden Architecture: {len([g for g in ga_gaps if g['risk']=='critical'])} critical, {len([g for g in ga_gaps if g['risk']=='high'])} high
{json.dumps(ga_gaps[:5], indent=2)}

Organization: {st.session_state.org_name or 'Not specified'}
Industry: {BENCHMARKS[st.session_state.industry]['name']}
Additional Context: {context or 'None'}

Provide comprehensive, actionable enterprise-grade recommendations with specific AWS services, timelines, and effort estimates.
"""
                    st.session_state.ai_analysis = call_ai(prompt)
        
        if st.session_state.ai_analysis:
            st.markdown("---")
            st.markdown("### 📋 AI Analysis Results")
            st.markdown(st.session_state.ai_analysis)
    
    # Reports
    with tabs[5]:
        st.markdown("## 📄 Assessment Reports")
        
        ct_scores = calc_scores(st.session_state.ct_responses, CT_DOMAINS) if st.session_state.ct_responses else {"overall": 0}
        ga_scores = calc_scores(st.session_state.ga_responses, GA_DOMAINS) if st.session_state.ga_responses else {"overall": 0}
        
        col1, col2, col3, col4 = st.columns(4)
        with col1: render_metric(ct_scores["overall"], "Control Tower")
        with col2: render_metric(ga_scores["overall"], "Golden Arch")
        with col3: render_metric((ct_scores["overall"]+ga_scores["overall"])/2, "Combined")
        with col4:
            total = len(st.session_state.ct_responses) + len(st.session_state.ga_responses)
            max_q = count_questions(CT_DOMAINS) + count_questions(GA_DOMAINS)
            render_metric(total/max_q*100 if max_q else 0, "Completion")
        
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📊 Generate Report", type="primary", use_container_width=True):
                ct_gaps = find_gaps(st.session_state.ct_responses, CT_DOMAINS)
                ga_gaps = find_gaps(st.session_state.ga_responses, GA_DOMAINS)
                
                report = f"""# AWS Enterprise Assessment Report

**Organization:** {st.session_state.org_name or 'N/A'}
**Assessor:** {st.session_state.assessor_name or 'N/A'}
**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Industry:** {BENCHMARKS[st.session_state.industry]['name']}

---

## Executive Summary

| Assessment | Score | Level |
|------------|-------|-------|
| Control Tower | {ct_scores['overall']:.1f}% | {get_level(ct_scores['overall'])[0]} |
| Golden Architecture | {ga_scores['overall']:.1f}% | {get_level(ga_scores['overall'])[0]} |
| **Combined** | **{(ct_scores['overall']+ga_scores['overall'])/2:.1f}%** | **{get_level((ct_scores['overall']+ga_scores['overall'])/2)[0]}** |

---

## Gap Summary

### Control Tower
- Critical Gaps: {len([g for g in ct_gaps if g['risk']=='critical'])}
- High Priority: {len([g for g in ct_gaps if g['risk']=='high'])}
- Medium Priority: {len([g for g in ct_gaps if g['risk']=='medium'])}

### Golden Architecture
- Critical Gaps: {len([g for g in ga_gaps if g['risk']=='critical'])}
- High Priority: {len([g for g in ga_gaps if g['risk']=='high'])}
- Medium Priority: {len([g for g in ga_gaps if g['risk']=='medium'])}

---

## AI Analysis

{st.session_state.ai_analysis or 'Generate AI analysis in the AI Insights tab.'}

---

*Generated by AWS Enterprise Assessment Platform v2.0*
"""
                st.session_state.report = report
                st.success("Report generated!")
        
        with col2:
            if st.session_state.report:
                st.download_button("⬇️ Download Report", st.session_state.report,
                    f"aws_assessment_{datetime.now().strftime('%Y%m%d')}.md", "text/markdown",
                    use_container_width=True)
            
            export_data = {
                "metadata": {"date": datetime.now().isoformat(), "org": st.session_state.org_name},
                "control_tower": {"responses": st.session_state.ct_responses, "scores": ct_scores},
                "golden_architecture": {"responses": st.session_state.ga_responses, "scores": ga_scores}
            }
            st.download_button("⬇️ Export JSON", json.dumps(export_data, indent=2, default=str),
                f"aws_assessment_{datetime.now().strftime('%Y%m%d')}.json", "application/json",
                use_container_width=True)
        
        if st.session_state.report:
            st.markdown("---")
            with st.expander("📋 Report Preview"):
                st.markdown(st.session_state.report)

if __name__ == "__main__":
    main()
