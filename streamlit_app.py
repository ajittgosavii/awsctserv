"""
AWS Enterprise Assessment Platform v3.0
Enterprise-Grade Control Tower & Golden Architecture Assessment
With AI-Powered Analysis

Deploy to Streamlit Cloud:
1. Push to GitHub
2. Connect repo on share.streamlit.io
3. Add ANTHROPIC_API_KEY to Secrets
"""

import streamlit as st
import json
import os
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="AWS Enterprise Assessment",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# PROFESSIONAL LIGHT THEME CSS
# =============================================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@400;600;700&family=Fira+Code:wght@400;500&display=swap');

:root {
    --primary: #2563eb;
    --success: #059669;
    --warning: #d97706;
    --danger: #dc2626;
    --bg-primary: #f8fafc;
    --bg-card: #ffffff;
    --border: #e2e8f0;
    --text-primary: #0f172a;
    --text-secondary: #64748b;
}

.stApp { background: var(--bg-primary) !important; }
[data-testid="stSidebar"] { background: var(--bg-card) !important; border-right: 1px solid var(--border) !important; }

/* Main Header */
.main-header {
    background: linear-gradient(135deg, #1e3a5f 0%, #0f172a 100%);
    padding: 2rem;
    border-radius: 16px;
    margin-bottom: 1.5rem;
    box-shadow: 0 10px 40px rgba(0,0,0,0.12);
}
.main-header h1 {
    font-family: 'Source Sans Pro', sans-serif;
    font-weight: 700;
    font-size: 1.75rem;
    color: #ffffff;
    margin: 0;
}
.main-header p {
    color: rgba(255,255,255,0.7);
    margin: 0.5rem 0 0 0;
    font-size: 0.95rem;
}
.aws-badge {
    background: #ff9900;
    color: #0f172a;
    padding: 0.25rem 0.6rem;
    border-radius: 4px;
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.5px;
    margin-left: 0.75rem;
}

/* Metric Cards */
.metric-card {
    background: var(--bg-card);
    padding: 1.5rem;
    border-radius: 12px;
    text-align: center;
    border: 1px solid var(--border);
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}
.metric-value {
    font-family: 'Fira Code', monospace;
    font-size: 2.5rem;
    font-weight: 700;
    line-height: 1;
}
.metric-label {
    font-size: 0.75rem;
    font-weight: 600;
    color: var(--text-secondary);
    text-transform: uppercase;
    letter-spacing: 0.5px;
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
.badge-success { background: #d1fae5; color: #065f46; }
.badge-warning { background: #fef3c7; color: #92400e; }
.badge-danger { background: #fee2e2; color: #991b1b; }
.badge-neutral { background: #f1f5f9; color: #64748b; }

/* Question Styling */
.question-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1.25rem;
    margin: 1rem 0;
}
.question-card.answered {
    border-left: 4px solid var(--success);
    background: #f0fdf4;
}
.question-card.unanswered {
    border-left: 4px solid #e2e8f0;
}
.question-id {
    font-family: 'Fira Code', monospace;
    font-size: 0.7rem;
    color: var(--primary);
    background: #eff6ff;
    padding: 0.15rem 0.4rem;
    border-radius: 4px;
}
.question-text {
    font-size: 0.95rem;
    font-weight: 600;
    color: var(--text-primary);
    margin: 0.5rem 0;
    line-height: 1.5;
}
.question-context {
    font-size: 0.85rem;
    color: var(--text-secondary);
    background: #f8fafc;
    padding: 0.75rem;
    border-radius: 6px;
    margin-top: 0.5rem;
    border-left: 3px solid #cbd5e1;
}

/* Risk Badges */
.risk-badge {
    display: inline-block;
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    font-size: 0.6rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.risk-critical { background: #fef2f2; color: #dc2626; }
.risk-high { background: #fff7ed; color: #ea580c; }
.risk-medium { background: #fefce8; color: #ca8a04; }
.risk-low { background: #f0fdf4; color: #16a34a; }

/* Pillar Tags */
.pillar-tag {
    display: inline-block;
    padding: 0.15rem 0.4rem;
    border-radius: 4px;
    font-size: 0.6rem;
    font-weight: 600;
    margin-right: 0.25rem;
}
.pillar-SEC { background: #fef2f2; color: #dc2626; }
.pillar-REL { background: #eff6ff; color: #2563eb; }
.pillar-PERF { background: #faf5ff; color: #9333ea; }
.pillar-COST { background: #f0fdf4; color: #16a34a; }
.pillar-OPS { background: #fff7ed; color: #ea580c; }

/* Section Headers */
.section-title {
    font-family: 'Source Sans Pro', sans-serif;
    font-size: 1.4rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 3px solid var(--primary);
    display: inline-block;
}

/* Domain Cards */
.domain-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 0.75rem 1rem;
    margin-bottom: 0.5rem;
}

/* Gap Cards */
.gap-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-left: 4px solid var(--danger);
    border-radius: 0 8px 8px 0;
    padding: 1rem;
    margin: 0.5rem 0;
}
.gap-card.high { border-left-color: #ea580c; }
.gap-card.medium { border-left-color: #ca8a04; }

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: var(--bg-card);
    padding: 0.4rem;
    border-radius: 10px;
    border: 1px solid var(--border);
    gap: 0.25rem;
}
.stTabs [data-baseweb="tab"] {
    font-weight: 600;
    font-size: 0.85rem;
    color: var(--text-secondary);
    border-radius: 8px;
    padding: 0.5rem 1rem;
}
.stTabs [aria-selected="true"] {
    background: var(--primary) !important;
    color: white !important;
}

/* Buttons */
.stButton > button {
    font-weight: 600;
    background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(37,99,235,0.25);
}
.stDownloadButton > button {
    background: linear-gradient(135deg, #059669, #047857) !important;
}

/* Expanders */
div[data-testid="stExpander"] {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    margin-bottom: 0.5rem;
}

/* Progress */
.stProgress > div > div > div { background: linear-gradient(90deg, #2563eb, #3b82f6) !important; }
.stProgress > div > div { background: #e2e8f0 !important; }

/* AI Response */
.ai-response {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.5rem;
    margin-top: 1rem;
}
.ai-response h2 { color: var(--text-primary); font-size: 1.2rem; border-bottom: 1px solid var(--border); padding-bottom: 0.5rem; margin-top: 1.5rem; }
.ai-response h3 { color: var(--primary); font-size: 1rem; }

/* Hide Streamlit defaults */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# CONSTANTS
# =============================================================================
WA_PILLARS = {"SEC": "Security", "REL": "Reliability", "PERF": "Performance", "COST": "Cost Optimization", "OPS": "Operations"}

BENCHMARKS = {
    "financial": {"name": "Financial Services", "avg": 72},
    "healthcare": {"name": "Healthcare", "avg": 65},
    "technology": {"name": "Technology", "avg": 78},
    "retail": {"name": "Retail/E-Commerce", "avg": 60},
    "government": {"name": "Government", "avg": 58},
    "manufacturing": {"name": "Manufacturing", "avg": 55}
}

# Placeholder for "not answered" - this is the KEY to the bug fix
NOT_ANSWERED = "-- Select an option --"

# =============================================================================
# CONTROL TOWER ASSESSMENT - COMPREHENSIVE QUESTIONS
# Each question has detailed context explaining why it matters
# =============================================================================
CT_QUESTIONS = {
    "Organizational Strategy": {
        "weight": 0.12, "pillars": ["OPS", "SEC"],
        "description": "Evaluates multi-account strategy, governance frameworks, and organizational readiness.",
        "questions": [
            {
                "id": "CT-ORG-001",
                "question": "What is your current AWS multi-account strategy maturity level?",
                "context": "A well-defined multi-account strategy is fundamental for Control Tower success. AWS recommends separating workloads by function, compliance requirements, and SDLC stages. Organizations without clear strategy face significant refactoring during Control Tower implementation. The strategy should address account lifecycle, ownership, and purpose classification.",
                "risk": "critical",
                "options": [
                    "No Strategy: Single account or ad-hoc account creation without documented rationale",
                    "Basic Separation: Simple dev/prod split, but no formal OU design or account lifecycle management",
                    "Defined Structure: Documented OU hierarchy aligned with AWS best practices (Security, Infrastructure, Workloads OUs)",
                    "Comprehensive Design: Full workload isolation, environment separation, dedicated accounts for shared services, logging, and security",
                    "Mature & Automated: Complete account lifecycle automation, self-service provisioning, automated tagging, CMDB integration"
                ]
            },
            {
                "id": "CT-ORG-002",
                "question": "How well-documented and enforced is your Organizational Unit (OU) structure?",
                "context": "Control Tower relies heavily on OU structure for policy inheritance and guardrail application. A poorly designed OU structure leads to security gaps, compliance issues, and operational complexity. AWS recommends nested OUs with Security OU at top, followed by Infrastructure, Sandbox, Workloads (with nested Prod/NonProd), and Suspended OUs.",
                "risk": "high",
                "options": [
                    "No OU Structure: All accounts at organization root or single flat OU",
                    "Basic OUs: Simple grouping (Production, Non-Production) without clear inheritance strategy",
                    "SDLC-Aligned: OUs structured by environment (Dev, Test, Staging, Prod) with basic policy differentiation",
                    "Nested Hierarchy: Multi-level OU structure with Security, Infrastructure, Sandbox, Workloads, and Suspended OUs",
                    "Enterprise Architecture: Comprehensive OU design with business unit separation, workload classification, policy inheritance documentation"
                ]
            },
            {
                "id": "CT-ORG-003",
                "question": "What cloud governance bodies and decision-making frameworks exist?",
                "context": "Effective Control Tower adoption requires clear governance structures for policy decisions, exception handling, and cross-functional coordination. A Cloud Center of Excellence (CCoE) with representation from Security, Finance, Architecture, and Operations is recommended for organizations with significant AWS footprints.",
                "risk": "high",
                "options": [
                    "No Governance: No formal cloud governance; decisions made ad-hoc by individual teams",
                    "IT-Led Decisions: Central IT makes cloud decisions without formal framework or stakeholder input",
                    "Emerging CCoE: Cloud Center of Excellence established with representatives from key teams; meeting regularly",
                    "Mature CCoE: CCoE with documented RACI matrix, decision rights, escalation paths, multi-team representation",
                    "Federated Governance: Mature CCoE with federated decision-making, self-service for approved patterns, executive sponsorship"
                ]
            },
            {
                "id": "CT-ORG-004",
                "question": "What is your process for managing policy exceptions and temporary guardrail deviations?",
                "context": "Even with strong guardrails, legitimate business needs may require temporary exceptions. Without a formal process, exceptions become permanent security debt. Time-bound exceptions with compensating controls, documented business justification, and automatic expiration are essential.",
                "risk": "medium",
                "options": [
                    "No Process: Exceptions not tracked; guardrails bypassed without approval",
                    "Ad-hoc Approval: Exceptions approved via email/Slack by individual managers; no central tracking",
                    "Documented Process: Formal exception request form; approval workflow; tracking spreadsheet; manual expiration monitoring",
                    "Workflow Automation: Ticketing system with approval chains; automatic reminders; compensating controls documented",
                    "Risk-Based Automation: Automated risk scoring; self-service for low-risk exceptions; automatic expiration; security tool integration"
                ]
            }
        ]
    },
    "Account Factory & Provisioning": {
        "weight": 0.10, "pillars": ["OPS", "SEC", "REL"],
        "description": "Evaluates account provisioning automation, baseline configurations, and Infrastructure as Code maturity.",
        "questions": [
            {
                "id": "CT-ACC-001",
                "question": "How are new AWS accounts currently provisioned in your organization?",
                "context": "Control Tower Account Factory provides automated, governed account provisioning. Organizations with manual processes will benefit most but need change management. Account Factory for Terraform (AFT) enables GitOps-based account vending with customizations applied automatically.",
                "risk": "high",
                "options": [
                    "Manual Console: Accounts created manually through AWS Console; no automation or templates",
                    "CLI/Scripts: Basic CLI scripts for account creation; manual baseline configuration afterward",
                    "Semi-Automated IaC: CloudFormation/Terraform for some baseline resources; manual steps required",
                    "Service Catalog: AWS Service Catalog products for account provisioning with approval workflows",
                    "Account Factory for Terraform (AFT): Fully automated provisioning with GitOps workflow; automatic customizations"
                ]
            },
            {
                "id": "CT-ACC-002",
                "question": "What is your average time from account request to fully provisioned, production-ready account?",
                "context": "Account provisioning speed directly impacts developer productivity and time-to-market. Control Tower with AFT can reduce this to under 4 hours. Long provisioning times often indicate manual processes, approval bottlenecks, and lack of automation.",
                "risk": "medium",
                "options": [
                    "2+ Weeks: Manual process with multiple approval chains and handoffs",
                    "1-2 Weeks: Some automation but significant manual configuration and validation",
                    "3-5 Business Days: Automated provisioning with manual security review and baseline validation",
                    "1-2 Business Days: Mostly automated with minimal manual approval gates",
                    "Less than 4 Hours: Fully automated end-to-end with pre-approved patterns and self-service"
                ]
            },
            {
                "id": "CT-ACC-003",
                "question": "What baseline security configurations are automatically applied to new accounts?",
                "context": "Account baselines are critical for security posture. Control Tower applies foundational baselines (CloudTrail, Config, GuardDuty enablement), but organizations typically need additional customizations: VPC configuration, IAM permission boundaries, security tool agents, cost controls, and compliance-specific settings.",
                "risk": "critical",
                "options": [
                    "No Baselines: Accounts created without standard configurations; teams configure independently",
                    "Basic Security: Password policy, root MFA reminder, basic IAM roles; manual application",
                    "Security Baseline: Automated CloudTrail, Config, GuardDuty, Security Hub enablement",
                    "Comprehensive Baseline: Security baseline + networking (VPC, endpoints), logging, IAM permission boundaries, cost controls",
                    "Full Enterprise Baseline: Complete baseline including security tool integration, compliance controls, monitoring, backup policies"
                ]
            },
            {
                "id": "CT-ACC-004",
                "question": "How is configuration drift from baselines detected and remediated?",
                "context": "Without automated detection, baseline configurations degrade as teams make changes. AWS Config rules detect drift; auto-remediation reduces operational burden. SCPs can prevent certain drift types entirely. Continuous compliance monitoring is essential for regulated industries.",
                "risk": "high",
                "options": [
                    "No Detection: Drift not monitored; discovered only during audits or incidents",
                    "Manual Audits: Periodic manual reviews; no continuous monitoring",
                    "Config Rules Alerting: AWS Config rules detect drift; alerts sent to security team for manual remediation",
                    "Automated Detection: Continuous drift detection with dashboards; prioritized remediation queue; SLA tracking",
                    "Auto-Remediation: Automated remediation for approved baseline components; preventive SCPs where possible"
                ]
            }
        ]
    },
    "Guardrails & Preventive Controls": {
        "weight": 0.15, "pillars": ["SEC", "OPS"],
        "description": "Evaluates SCP maturity, Control Tower guardrail strategy, and preventive control implementation.",
        "questions": [
            {
                "id": "CT-GRD-001",
                "question": "What is your current Service Control Policy (SCP) implementation maturity?",
                "context": "SCPs are the primary mechanism for implementing preventive guardrails. Control Tower deploys mandatory SCPs, but organizations need custom SCPs for: region restriction, service denials, encryption requirements, network controls. SCP design requires careful planning to avoid breaking legitimate workloads.",
                "risk": "critical",
                "options": [
                    "No SCPs: Not using AWS Organizations or no SCPs beyond default FullAWSAccess",
                    "Basic Deny Policies: Simple deny SCPs for high-risk actions (deny root usage, deny leaving organization)",
                    "Security Guardrails: SCPs covering region restriction, critical service protection, security service enforcement",
                    "Comprehensive OU-Specific: Layered SCPs with OU-specific policies; workload-appropriate restrictions; documented exceptions",
                    "Enterprise SCP Framework: Modular SCP architecture with inheritance design; version control; automated testing; impact analysis"
                ]
            },
            {
                "id": "CT-GRD-002",
                "question": "How are SCPs tested and validated before production deployment?",
                "context": "SCP mistakes can cause widespread outages across your entire organization. Testing in isolated sandbox OUs, using AWS IAM Policy Simulator, and implementing gradual rollouts with monitoring are essential. CI/CD pipelines can automate validation and catch syntax errors.",
                "risk": "high",
                "options": [
                    "No Testing: SCPs deployed directly to production without testing",
                    "Manual Review: Peer review of SCP syntax and logic; no isolated testing",
                    "Sandbox OU Testing: SCPs tested in dedicated sandbox OU before broader deployment",
                    "Policy Simulator + Sandbox: IAM Policy Simulator validation plus sandbox OU testing; documented test cases",
                    "CI/CD Pipeline: Automated SCP validation in CI/CD; syntax checking, policy simulation, sandbox deployment, gradual rollout"
                ]
            },
            {
                "id": "CT-GRD-003",
                "question": "What is your strategy for enabling Control Tower guardrails?",
                "context": "Control Tower provides mandatory, strongly recommended, and elective guardrails. Mandatory guardrails cannot be disabled. The appropriate mix of strongly recommended and elective guardrails depends on risk tolerance and compliance requirements. Over-restrictive guardrails impede legitimate work; under-restrictive creates risk.",
                "risk": "high",
                "options": [
                    "Mandatory Only: Plan to enable only mandatory guardrails to minimize restrictions",
                    "Some Strongly Recommended: Mandatory plus select strongly recommended guardrails based on obvious needs",
                    "All Strongly Recommended: Enable all mandatory and strongly recommended guardrails across all OUs",
                    "Selective Elective: All strongly recommended plus carefully selected elective guardrails based on risk assessment",
                    "Comprehensive + Custom: Full guardrail enablement plus custom controls for organization-specific requirements"
                ]
            },
            {
                "id": "CT-GRD-004",
                "question": "How will guardrail violations be detected, reported, and remediated?",
                "context": "Detective guardrails identify non-compliant resources but don't prevent creation. Organizations need processes to handle violations: automated alerting, severity-based routing, remediation SLAs, exception handling. Integration with ITSM and security operations enables tracking and accountability.",
                "risk": "high",
                "options": [
                    "No Process: Violations not actively monitored; discovered only during audits",
                    "Manual Review: Security team periodically reviews Control Tower dashboard; manual ticket creation",
                    "Automated Alerting: Violations trigger automated alerts to security team; prioritization based on severity",
                    "Escalation Workflow: Automated ticketing with SLAs; escalation paths; management dashboards; compliance reporting",
                    "Auto-Remediation: Automated remediation for approved violation types; exception workflow; continuous compliance posture"
                ]
            }
        ]
    },
    "Detective Controls & Compliance": {
        "weight": 0.12, "pillars": ["SEC", "OPS"],
        "description": "Evaluates AWS Config, Security Hub, compliance framework alignment, and evidence collection.",
        "questions": [
            {
                "id": "CT-DET-001",
                "question": "What is your current AWS Config deployment and rule coverage?",
                "context": "AWS Config is foundational for Control Tower detective controls. Config records resource configurations and changes, enabling compliance assessment and drift detection. Organization-wide deployment with aggregation provides centralized visibility. Conformance packs bundle related rules.",
                "risk": "critical",
                "options": [
                    "Not Enabled: AWS Config not enabled or enabled in very few accounts",
                    "Partial Deployment: Config enabled in some accounts; inconsistent rules; no aggregation",
                    "Organization-Wide: Config enabled across all accounts via Control Tower; basic aggregator",
                    "Aggregator + Custom Rules: Organization-wide Config with delegated administrator; custom rules for organizational requirements",
                    "Conformance Packs + Remediation: Comprehensive Config with conformance packs; auto-remediation for critical rules"
                ]
            },
            {
                "id": "CT-DET-002",
                "question": "What is your AWS Security Hub deployment and standards enablement status?",
                "context": "Security Hub aggregates findings from AWS services (GuardDuty, Inspector, Macie) and third-party tools. Control Tower can automatically enable Security Hub with delegated administrator. Multiple security standards (AWS Foundational, CIS, PCI-DSS, NIST) provide compliance baselines.",
                "risk": "critical",
                "options": [
                    "Not Enabled: Security Hub not deployed or enabled in very few accounts",
                    "Partial Deployment: Security Hub in some accounts; no central aggregation; limited standards",
                    "Organization-Wide: Security Hub enabled organization-wide with delegated administrator; AWS Foundational Security Best Practices",
                    "Multiple Standards: Organization-wide Security Hub with multiple standards (FSBP, CIS, PCI-DSS) based on compliance requirements",
                    "Custom Insights + Integrations: Comprehensive Security Hub with all relevant standards; custom insights; third-party integrations"
                ]
            },
            {
                "id": "CT-DET-003",
                "question": "What compliance frameworks and regulatory requirements apply to your AWS environment?",
                "context": "Compliance requirements drive guardrail selection, evidence collection needs, and audit processes. Different frameworks (SOC 2, PCI-DSS, HIPAA, FedRAMP, GDPR) have overlapping but distinct requirements. AWS Audit Manager helps map controls to frameworks and collect evidence.",
                "risk": "critical",
                "options": [
                    "None Identified: No specific compliance frameworks apply; internal policies only",
                    "Internal Policies: Internal security policies but no external compliance certifications required",
                    "Single Framework: One primary compliance framework (e.g., SOC 2 Type II) drives requirements",
                    "Multiple Frameworks: Multiple compliance requirements (e.g., SOC 2 + PCI-DSS + HIPAA) with mapped controls",
                    "Complex Multi-Framework: Complex compliance landscape with multiple overlapping frameworks; automated control mapping"
                ]
            },
            {
                "id": "CT-DET-004",
                "question": "How is compliance evidence collected and maintained for audits?",
                "context": "Auditors require evidence of control effectiveness. Manual evidence collection is time-consuming and error-prone. AWS Audit Manager automates evidence collection from Config, CloudTrail, and Security Hub. GRC platforms provide continuous compliance monitoring and auditor portals.",
                "risk": "high",
                "options": [
                    "No Collection: Evidence gathered ad-hoc during audits; significant manual effort required",
                    "Manual Screenshots: Security team manually captures evidence; stored in shared drives; no organization system",
                    "Periodic Exports: Regular exports from AWS services; organized evidence repository; manual collection",
                    "AWS Audit Manager: Automated evidence collection via Audit Manager; assessment reports; some manual supplements",
                    "GRC Platform: Comprehensive GRC platform (Drata, Vanta, ServiceNow GRC) with automated evidence; continuous monitoring"
                ]
            }
        ]
    },
    "Identity & Access Management": {
        "weight": 0.12, "pillars": ["SEC"],
        "description": "Evaluates identity federation, IAM Identity Center readiness, permission management, and privileged access.",
        "questions": [
            {
                "id": "CT-IAM-001",
                "question": "What is your current identity management approach for AWS access?",
                "context": "Control Tower strongly recommends IAM Identity Center (formerly AWS SSO) for centralized identity. Organizations using local IAM users or legacy SAML federation need migration planning. Identity Center supports external IdPs (Azure AD, Okta, Active Directory) with SCIM for automated user provisioning.",
                "risk": "critical",
                "options": [
                    "Local IAM Users: AWS access via IAM users in each account; no centralized identity management",
                    "Partial Federation: Some accounts federated via SAML; others use local IAM users; inconsistent approach",
                    "AWS IAM Identity Center: Centralized access via Identity Center; single identity source; basic permission sets",
                    "Full IdP Integration: Identity Center with enterprise IdP (Okta, Azure AD); automated provisioning; comprehensive permission sets",
                    "SCIM + JIT Provisioning: Full IdP integration with SCIM for automated user lifecycle; just-in-time access; ABAC"
                ]
            },
            {
                "id": "CT-IAM-002",
                "question": "How is multi-factor authentication (MFA) enforced across your AWS environment?",
                "context": "MFA is critical for preventing unauthorized access from compromised credentials. Control Tower requires MFA for management account root user. Enterprise best practice extends MFA to all human access (console and CLI), with hardware tokens (YubiKey) for privileged accounts and phishing-resistant MFA.",
                "risk": "critical",
                "options": [
                    "No MFA: MFA not required or inconsistently enabled across accounts",
                    "Encouraged Only: MFA recommended but not enforced; actual compliance unknown",
                    "Console Access MFA: MFA required for AWS Console access; CLI may not require MFA",
                    "All Human Access: MFA required for all human access (console and CLI) via Identity Center or IdP",
                    "Hardware MFA for Privileged: All access requires MFA; hardware tokens for privileged accounts and root users"
                ]
            },
            {
                "id": "CT-IAM-003",
                "question": "How is least privilege enforced and maintained over time?",
                "context": "Permissions tend to accumulate over time as teams request access for various tasks. Without active enforcement, users end up with far more permissions than needed, increasing blast radius of compromised credentials. IAM Access Analyzer identifies unused permissions; regular reviews and automated right-sizing maintain least privilege.",
                "risk": "high",
                "options": [
                    "No Enforcement: Broad permissions granted based on requests; no review or right-sizing",
                    "Manual Review: Annual access reviews; manual analysis of permissions; reactive approach",
                    "Access Analyzer: IAM Access Analyzer used to identify unused permissions; findings reviewed manually",
                    "Regular Right-Sizing: Quarterly permission reviews; automated unused access identification; documented reduction process",
                    "Continuous Enforcement: Automated continuous permission analysis; proactive right-sizing; permission boundaries enforced"
                ]
            },
            {
                "id": "CT-IAM-004",
                "question": "How is privileged access to AWS managed and controlled?",
                "context": "Privileged access (administrative permissions, production changes) requires additional controls beyond standard access. Zero standing privilege models require users to request elevated access for specific tasks and time windows, reducing blast radius. Session recording provides audit trail.",
                "risk": "critical",
                "options": [
                    "No Distinction: All users have similar access levels; no privileged access tier defined",
                    "Separate Accounts: Privileged users use separate accounts; same broad permissions always available",
                    "JIT for Some: Just-in-time access for some privileged operations; manual approval process",
                    "PAM Solution: Dedicated Privileged Access Management solution; session recording; approval workflows",
                    "Zero Standing Privilege: No standing privileged access; all elevated access via JIT; full session recording"
                ]
            }
        ]
    },
    "Network Architecture": {
        "weight": 0.10, "pillars": ["SEC", "REL", "PERF"],
        "description": "Evaluates multi-account network topology, connectivity, security controls, and hybrid architecture.",
        "questions": [
            {
                "id": "CT-NET-001",
                "question": "What is your current or planned multi-account network architecture?",
                "context": "Network architecture significantly impacts Control Tower implementation. Hub-spoke with AWS Transit Gateway is recommended for most enterprises, providing centralized connectivity, shared services access, and network inspection capabilities. Existing VPC peering or independent VPCs may require re-architecture.",
                "risk": "high",
                "options": [
                    "Independent VPCs: Each account has isolated VPCs; no inter-account connectivity strategy",
                    "VPC Peering: Selected accounts connected via VPC peering; manual peering management; limited scale",
                    "Transit Gateway Basic: Transit Gateway for connectivity; basic routing; per-account attachments",
                    "Hub-Spoke Centralized: Central network account with Transit Gateway; shared services VPC; centralized egress",
                    "Advanced Segmentation: Multi-TGW design with route domains; Network Firewall inspection; automated VPC provisioning"
                ]
            },
            {
                "id": "CT-NET-002",
                "question": "How is IP address management (IPAM) handled across AWS accounts?",
                "context": "IP address conflicts can prevent VPC connectivity and cause significant rework. AWS VPC IPAM provides centralized IP management with pools and automatic allocation. Enterprise integration with existing IPAM solutions (Infoblox, BlueCat) ensures consistency across hybrid environments.",
                "risk": "high",
                "options": [
                    "No IPAM: IP ranges assigned ad-hoc; frequent conflicts; no central tracking or planning",
                    "Spreadsheet Tracking: IP allocations tracked in spreadsheet; manual coordination; occasional conflicts",
                    "AWS VPC IPAM Basic: VPC IPAM deployed; pools defined; manual allocation requests",
                    "Automated VPC IPAM: VPC IPAM with automated allocation; integration with account provisioning",
                    "Enterprise IPAM Integration: AWS IPAM integrated with enterprise IPAM solution; bi-directional sync; automated allocation"
                ]
            },
            {
                "id": "CT-NET-003",
                "question": "How is egress (outbound internet) traffic controlled and monitored?",
                "context": "Uncontrolled egress is a significant security risk for data exfiltration and command-and-control traffic. Centralized egress through proxy or AWS Network Firewall enables URL filtering, logging, malware scanning, and DLP integration. Zero-trust approaches minimize allowed destinations.",
                "risk": "critical",
                "options": [
                    "No Controls: NAT Gateways in each VPC; no filtering or logging of outbound traffic",
                    "Centralized NAT Only: Centralized NAT Gateway; VPC Flow Logs enabled; no content inspection",
                    "Basic Proxy: Forward proxy for HTTP/HTTPS; basic URL categorization; logging enabled",
                    "Full Proxy + Firewall: Enterprise proxy with URL filtering and malware scanning; Network Firewall for non-HTTP",
                    "Zero Trust Egress: Full proxy inspection with DLP; certificate inspection; minimal allowed destinations"
                ]
            },
            {
                "id": "CT-NET-004",
                "question": "What is your on-premises to AWS connectivity architecture?",
                "context": "Hybrid connectivity is essential for most enterprises during cloud migration. AWS Direct Connect provides consistent, low-latency connectivity; VPN provides encrypted backup. Redundant connections with diverse paths ensure availability. Transit Gateway integration enables scalable hybrid architecture.",
                "risk": "high",
                "options": [
                    "No Connectivity: Cloud-only architecture; no on-premises connectivity required",
                    "Per-Account VPN: Site-to-site VPN connections per account; manual management; limited bandwidth",
                    "Centralized VPN: VPN terminates at central Transit Gateway; shared across accounts",
                    "Direct Connect + VPN Backup: Direct Connect for primary traffic; VPN for backup; Transit Gateway integration",
                    "Redundant Direct Connect: Dual Direct Connect with diverse paths; automated failover; VPN backup"
                ]
            }
        ]
    },
    "Logging & Monitoring": {
        "weight": 0.10, "pillars": ["OPS", "SEC", "REL"],
        "description": "Evaluates centralized logging architecture, monitoring capabilities, and security operations.",
        "questions": [
            {
                "id": "CT-LOG-001",
                "question": "What is your CloudTrail configuration across the organization?",
                "context": "CloudTrail is foundational for security investigation and compliance. Control Tower creates an organization trail automatically. Advanced configurations include data events for S3 and Lambda (additional cost), CloudTrail Insights for anomaly detection, and CloudTrail Lake for SQL-based log analysis.",
                "risk": "critical",
                "options": [
                    "Incomplete Coverage: CloudTrail not enabled in all accounts or regions; significant visibility gaps",
                    "Account-Level Trails: Individual account trails; logs stored locally; no organization-wide view",
                    "Organization Trail: Organization trail via Control Tower; centralized S3 bucket; management events only",
                    "Organization Trail + Data Events: Organization trail with S3/Lambda data events for critical resources",
                    "CloudTrail Lake + Insights: Full organization trail; CloudTrail Lake for SQL queries; Insights for anomaly detection"
                ]
            },
            {
                "id": "CT-LOG-002",
                "question": "How are logs from multiple sources correlated and analyzed?",
                "context": "Security investigations require correlation across CloudTrail, VPC Flow Logs, application logs, and AWS service logs. SIEM integration enables automated analysis, threat detection, and incident response. Machine learning can identify anomalies that rule-based detection misses.",
                "risk": "high",
                "options": [
                    "No Correlation: Logs reviewed in isolation; manual investigation across multiple consoles when needed",
                    "Manual Analysis: Security team manually correlates logs during investigations; no automated analysis",
                    "CloudWatch Insights: CloudWatch Logs Insights for basic correlation; manual query building",
                    "SIEM Integration: Logs forwarded to SIEM (Splunk, Elastic, etc.); automated correlation rules; alerting",
                    "Advanced Security Analytics: Comprehensive SIEM with ML-based threat detection; automated response playbooks"
                ]
            },
            {
                "id": "CT-LOG-003",
                "question": "What is your alerting and incident response strategy for AWS events?",
                "context": "Effective alerting requires proper threshold tuning to reduce noise while catching real issues. Tiered severity with different response SLAs prevents alert fatigue. Integration with incident management tools (PagerDuty, ServiceNow) enables automated routing and escalation.",
                "risk": "medium",
                "options": [
                    "No Alerting: No automated alerting; issues discovered reactively when users report problems",
                    "Basic Email Alerts: CloudWatch alarms send email; high noise; no prioritization or routing",
                    "SNS to Operations Tools: Alerts routed to Slack/PagerDuty; basic routing rules; some noise reduction",
                    "Tiered Alerting: Severity-based routing; SLA-driven escalation; runbook links; noise reduction tuning",
                    "AIOps + Automation: ML-based anomaly alerting; automated remediation for known issues; continuous optimization"
                ]
            }
        ]
    },
    "Cost Management": {
        "weight": 0.08, "pillars": ["COST", "OPS"],
        "description": "Evaluates cost visibility, allocation, optimization, and FinOps maturity.",
        "questions": [
            {
                "id": "CT-FIN-001",
                "question": "What is your current level of cost visibility across AWS accounts?",
                "context": "Multi-account environments require consolidated cost visibility for budgeting, forecasting, and optimization. Cost Explorer provides basic visualization; Cost and Usage Reports with Athena enable detailed analysis. FinOps platforms (CloudHealth, Spot, Apptio) provide advanced capabilities and recommendations.",
                "risk": "medium",
                "options": [
                    "Per-Account Billing: Individual account billing; no consolidated view; limited organizational visibility",
                    "Consolidated Billing Only: AWS Organizations consolidated billing; basic Cost Explorer usage",
                    "Cost Explorer Advanced: Cost Explorer with saved reports; basic cost anomaly detection; manual analysis",
                    "CUR + Athena: Cost and Usage Reports in S3; Athena queries; custom dashboards; detailed analysis",
                    "FinOps Platform: Third-party FinOps platform with automated recommendations; executive reporting; optimization tracking"
                ]
            },
            {
                "id": "CT-FIN-002",
                "question": "How are AWS costs allocated to business units, projects, and teams?",
                "context": "Cost allocation enables accountability and optimization. Tagging is the primary mechanism, but requires enforcement. AWS Cost Categories can group costs without tags. Advanced scenarios need cost allocation rules for shared services and split amortization of commitments.",
                "risk": "medium",
                "options": [
                    "No Allocation: Costs not allocated to business units; central IT budget absorbs all cloud costs",
                    "Account-Based: Costs allocated by account; assumes one team per account; limited granularity",
                    "Partial Tagging: Cost allocation tags defined; partial compliance; manual gap-filling for reporting",
                    "Comprehensive Tagging: Enforced cost allocation tags; automated compliance checking; shared cost rules",
                    "Full FinOps: Complete cost allocation with split amortization; showback/chargeback automation; unit economics"
                ]
            },
            {
                "id": "CT-FIN-003",
                "question": "How are Reserved Instances and Savings Plans managed?",
                "context": "Commitment-based discounts (Reserved Instances, Savings Plans) can reduce costs by 30-72%. Centralized management in management/billing account enables organizational benefit sharing. Right-sizing analysis should precede commitment purchases to optimize savings.",
                "risk": "medium",
                "options": [
                    "No Commitments: No Reserved Instances or Savings Plans; all on-demand pricing",
                    "Reactive Purchasing: Occasional RI/SP purchases based on obvious steady-state; limited coverage",
                    "Periodic Review: Quarterly review of commitment coverage; manual purchase decisions",
                    "Optimized Coverage: Target coverage levels defined; regular optimization; benefit sharing across accounts",
                    "Automated Management: Automated commitment recommendations; continuous optimization; hybrid commitment strategy"
                ]
            }
        ]
    },
    "Backup & Disaster Recovery": {
        "weight": 0.08, "pillars": ["REL", "SEC"],
        "description": "Evaluates backup strategy, policy enforcement, testing, and disaster recovery readiness.",
        "questions": [
            {
                "id": "CT-BDR-001",
                "question": "How is data backup managed across your AWS accounts?",
                "context": "AWS Backup enables centralized backup management with organization-wide policies. Cross-account backup vaults provide protection against account compromise and ransomware. Backup policies should be enforced as part of account baseline configuration.",
                "risk": "critical",
                "options": [
                    "No Strategy: Backups not consistently implemented; team-dependent; significant gaps likely",
                    "Per-Account Management: Each account manages backups independently; inconsistent policies and retention",
                    "AWS Backup Per-Account: AWS Backup used in each account; policies defined but not centralized",
                    "Centralized Policies: AWS Backup Policies via Organizations; consistent protection; central vault",
                    "Organization-Wide with Cross-Account: Centralized policies; cross-account vault for ransomware protection; compliance checking"
                ]
            },
            {
                "id": "CT-BDR-002",
                "question": "How frequently are backup restores tested and validated?",
                "context": "Backups are useless if they can't be restored when needed. Regular restore testing validates backup integrity and recovery procedures, identifies issues before emergencies. AWS Backup provides restore testing capabilities. DR drills should include realistic scenarios.",
                "risk": "high",
                "options": [
                    "No Testing: Restore capability never tested; assumed functional; high risk of failure during incident",
                    "Ad-hoc Testing: Tested only when issues arise or during incidents; no scheduled validation",
                    "Annual Testing: Yearly restore test for critical systems; manual process; limited coverage",
                    "Quarterly Automated: Quarterly restore tests; automated validation; documented results; coverage tracking",
                    "Continuous Validation: Automated restore testing; integrity validation; recovery time measurement; DR drills"
                ]
            },
            {
                "id": "CT-BDR-003",
                "question": "What is your multi-region disaster recovery strategy?",
                "context": "DR strategy depends on RTO/RPO requirements and cost tolerance. Backup-only approaches have long RTO. Pilot light maintains minimal resources in DR region. Warm standby keeps scaled-down environment running. Active-active provides near-zero RTO but highest cost and complexity.",
                "risk": "high",
                "options": [
                    "No DR Strategy: Single region deployment; no cross-region backup or recovery capability",
                    "Backup to Secondary Region: Data backed up to another region; no compute preparation; long RTO",
                    "Pilot Light: Minimal resources in DR region (DB replicas); manual scaling during failover",
                    "Warm Standby: Scaled-down but functional environment in DR region; automated failover capability",
                    "Active-Active: Full active deployment in multiple regions; automatic traffic routing; near-zero RPO"
                ]
            }
        ]
    },
    "Migration Readiness": {
        "weight": 0.08, "pillars": ["OPS", "REL"],
        "description": "Evaluates existing account inventory, enrollment prerequisites, and migration planning.",
        "questions": [
            {
                "id": "CT-MIG-001",
                "question": "How complete and accurate is your existing AWS account inventory?",
                "context": "Control Tower enrollment requires understanding of existing accounts. Shadow IT may have created unknown accounts. Comprehensive inventory includes account ID, owner, purpose, criticality, current configurations, and dependencies. Dynamic inventory enables ongoing governance.",
                "risk": "high",
                "options": [
                    "No Inventory: Unknown how many AWS accounts exist; possible shadow IT; no tracking",
                    "Partial List: Some accounts known; no comprehensive inventory; ownership and purpose gaps",
                    "Complete List: All accounts identified; limited metadata (owner, purpose unclear for some)",
                    "Detailed Inventory: All accounts with ownership, purpose, criticality, dependencies documented",
                    "Dynamic Inventory: Automated inventory with real-time updates; CMDB integration; complete metadata"
                ]
            },
            {
                "id": "CT-MIG-002",
                "question": "Have existing accounts been assessed for Control Tower enrollment prerequisites?",
                "context": "Control Tower has specific prerequisites: no existing Config Recorder, specific CloudTrail configurations, no conflicting SCPs, clean root email addresses. Pre-flight assessment identifies blockers before enrollment. Remediation planning enables phased migration.",
                "risk": "critical",
                "options": [
                    "No Assessment: Enrollment prerequisites not evaluated; blockers unknown",
                    "Partial Assessment: Some accounts checked; many not evaluated; scope unclear",
                    "Full Assessment Done: All accounts assessed; blockers identified; remediation scope known",
                    "Most Ready: Most accounts meet prerequisites; remediation in progress for remaining accounts",
                    "All Verified Ready: All accounts verified ready for enrollment; pre-flight checks passed"
                ]
            },
            {
                "id": "CT-MIG-003",
                "question": "Are there existing AWS Config Recorders or organization CloudTrail trails that conflict with Control Tower?",
                "context": "Control Tower creates its own Config Recorder and organization trail in each account. Existing configurations must be removed or consolidated before enrollment. This is one of the most common enrollment blockers and requires careful planning to avoid losing historical data.",
                "risk": "critical",
                "options": [
                    "Unknown: Existing Config/CloudTrail status not assessed across accounts",
                    "Many Conflicts: Most accounts have conflicting Config Recorders or CloudTrail trails",
                    "Conflicts Identified: Conflicts documented across accounts; remediation plan in development",
                    "Most Resolved: Most conflicts resolved; few remaining accounts in progress",
                    "All Clear: No conflicts exist; all accounts ready for Control Tower Config/CloudTrail"
                ]
            }
        ]
    },
    "Operational Readiness": {
        "weight": 0.05, "pillars": ["OPS"],
        "description": "Evaluates team skills, operational processes, and change management readiness.",
        "questions": [
            {
                "id": "CT-OPS-001",
                "question": "What is your team's current experience level with AWS Control Tower?",
                "context": "Control Tower operations require specific knowledge different from general AWS skills. Teams without experience need hands-on training before go-live. Sandbox experimentation is different from production operations. Deep expertise enables troubleshooting and customization.",
                "risk": "high",
                "options": [
                    "No Experience: Team has not worked with Control Tower; learning from documentation only",
                    "Awareness Only: Team has read documentation or attended presentations; no hands-on experience",
                    "Sandbox Experience: Team has deployed Control Tower in sandbox; basic hands-on operations",
                    "Production Experience: Team member(s) have operated Control Tower in production elsewhere",
                    "Deep Expertise: Team has extensive Control Tower experience; can handle advanced scenarios and troubleshooting"
                ]
            },
            {
                "id": "CT-OPS-002",
                "question": "How will changes to Control Tower configuration be managed?",
                "context": "Control Tower changes (guardrails, OUs, SCPs, Account Factory settings) have organization-wide impact. Change management ensures proper review, testing, and approval. GitOps approaches provide audit trail and enable rollback. Emergency change processes handle urgent situations.",
                "risk": "medium",
                "options": [
                    "No Process: Changes made directly by team members without approval or documentation",
                    "Informal Approval: Changes discussed in team but no formal process or tracking",
                    "Ticket-Based: Changes require ticket with description; basic approval; manual implementation",
                    "CAB Review: Change Advisory Board reviews significant changes; documented rollback plans",
                    "GitOps + Automated Validation: Changes via pull request; automated validation; staged rollout; audit trail"
                ]
            }
        ]
    }
}

# =============================================================================
# GOLDEN ARCHITECTURE (SERVERLESS) ASSESSMENT
# =============================================================================
GA_QUESTIONS = {
    "Serverless Compute Strategy": {
        "weight": 0.18, "pillars": ["PERF", "COST", "OPS"],
        "description": "Evaluates Lambda adoption, runtime management, Fargate usage, and compute decision frameworks.",
        "questions": [
            {
                "id": "GA-CMP-001",
                "question": "What is your Lambda adoption and standardization maturity?",
                "context": "Lambda-first strategies prioritize serverless for new workloads. Standardization includes runtime selection policies, layer management for shared code, and deployment patterns. Mature organizations have Lambda as default compute choice with clear decision criteria for alternatives.",
                "risk": "medium",
                "options": [
                    "No Lambda: No Lambda usage; traditional EC2/container-based architecture only",
                    "Experimental: Lambda for specific experiments or POCs; no organizational standards",
                    "Production Specific: Lambda in production for specific use cases; basic standards emerging",
                    "Significant Usage: Lambda for significant workload portion; comprehensive standards; Lambda-default policy",
                    "Lambda-First Strategy: Lambda as primary compute; comprehensive patterns library; continuous optimization"
                ]
            },
            {
                "id": "GA-CMP-002",
                "question": "How are Lambda cold starts managed for latency-sensitive workloads?",
                "context": "Cold starts impact user experience for synchronous API calls. Mitigation strategies include: optimal package size, runtime selection (Python/Node faster than Java), Provisioned Concurrency for predictable traffic, SnapStart for Java. Architecture patterns (async, warming) can reduce impact.",
                "risk": "medium",
                "options": [
                    "Not Considered: Cold starts not analyzed; latency issues discovered in production",
                    "Awareness Only: Team aware of cold start impact; no systematic mitigation implemented",
                    "Basic Optimizations: Package size optimization; appropriate runtime selection; lazy loading",
                    "Provisioned Concurrency: Critical functions use Provisioned Concurrency; cold start monitoring dashboards",
                    "Comprehensive Strategy: SnapStart for Java; Provisioned Concurrency; architecture patterns; continuous optimization"
                ]
            },
            {
                "id": "GA-CMP-003",
                "question": "What is your Fargate adoption level for containerized serverless workloads?",
                "context": "Fargate provides serverless containers without cluster management. Appropriate for: workloads exceeding Lambda limits (15 min timeout, 10GB memory), existing containerized applications, specific tooling requirements. Fargate Spot provides 70% savings for fault-tolerant workloads.",
                "risk": "medium",
                "options": [
                    "No Fargate: EC2-based containers or no container workloads; not using serverless containers",
                    "Experimental: Fargate for experiments or non-production; evaluating fit",
                    "Specific Workloads: Fargate in production for specific workloads; basic configuration",
                    "Default for Containers: Fargate as default for containerized workloads; Spot integration for batch",
                    "Full Serverless Container Strategy: ECS/EKS on Fargate; cost-optimized configurations; automated scaling"
                ]
            },
            {
                "id": "GA-CMP-004",
                "question": "Do you have a decision framework for choosing Lambda vs Fargate vs EC2?",
                "context": "Each compute option has trade-offs. Lambda: best for event-driven, short-duration (<15min), variable traffic. Fargate: containers, longer processes, consistent traffic. EC2: maximum control, GPU, specific OS needs. Clear decision frameworks ensure optimal choices and prevent inappropriate usage.",
                "risk": "medium",
                "options": [
                    "No Framework: Compute decisions made ad-hoc by individual teams; inconsistent choices",
                    "Informal Guidelines: Basic guidance exists but inconsistently applied",
                    "Documented Decision Tree: Formal decision tree with criteria; applied during design reviews",
                    "Comprehensive Framework: Decision framework including cost modeling; mandatory architecture review",
                    "Automated Recommendations: Workload analysis tools; cost-performance optimization; continuous right-sizing"
                ]
            }
        ]
    },
    "API & Integration Layer": {
        "weight": 0.15, "pillars": ["PERF", "SEC", "REL"],
        "description": "Evaluates API Gateway patterns, EventBridge adoption, and asynchronous messaging architecture.",
        "questions": [
            {
                "id": "GA-API-001",
                "question": "What is your API Gateway architecture and type selection approach?",
                "context": "API Gateway offers: REST APIs (full features, higher cost), HTTP APIs (lower cost, simpler features), WebSocket APIs (real-time). Type selection significantly impacts cost - HTTP APIs are ~70% cheaper than REST APIs. Custom domains, stages, and WAF integration provide enterprise capabilities.",
                "risk": "medium",
                "options": [
                    "No API Gateway: APIs exposed directly from compute or using third-party gateway",
                    "REST API Everywhere: REST API used for all workloads; no type optimization for cost",
                    "HTTP APIs Adopted: HTTP APIs for cost optimization where features sufficient",
                    "Right-Sized Selection: Deliberate type selection based on requirements; multi-stage deployments",
                    "Comprehensive API Strategy: Optimized type selection; custom domains; WAF integration; usage plans; developer portal"
                ]
            },
            {
                "id": "GA-API-002",
                "question": "How is API rate limiting and throttling configured?",
                "context": "Rate limiting protects backends from overload and abuse. Usage plans enable API monetization and partner quota management. Without proper limits, a single client can impact all users. Adaptive rate limiting adjusts based on backend health.",
                "risk": "high",
                "options": [
                    "No Rate Limiting: Default AWS service limits only; no API-level throttling configured",
                    "Basic Throttling: API-level throttling; no per-client or per-key limits",
                    "Custom Throttling: Custom throttling per stage and method; burst handling configured",
                    "Usage Plans: API keys with usage plans; per-client quotas and rate limits; monitoring",
                    "Dynamic Quota Management: Usage plans with automated quota management; adaptive rate limiting; abuse detection"
                ]
            },
            {
                "id": "GA-API-003",
                "question": "What is your EventBridge adoption for event-driven architecture?",
                "context": "EventBridge enables loosely-coupled architectures through event buses and routing rules. Event schema registry provides discovery and validation. Cross-account event delivery enables organizational event mesh. Event replay supports debugging and reprocessing.",
                "risk": "medium",
                "options": [
                    "No EventBridge: Point-to-point integrations; no event bus architecture",
                    "Basic Usage: Default event bus; simple CloudWatch Events patterns",
                    "Custom Buses: Custom event buses for applications; event rules for routing",
                    "Event-Driven Patterns: EventBridge as integration backbone; schema registry; event replay",
                    "Full Event Mesh: Cross-account events; schema governance; event versioning; event-first design"
                ]
            },
            {
                "id": "GA-API-004",
                "question": "How are asynchronous messaging patterns implemented?",
                "context": "SQS provides reliable queuing with at-least-once delivery. SNS enables pub/sub fan-out. Combined SNS→SQS provides scalable fan-out with per-subscriber queues. FIFO queues guarantee ordering and exactly-once processing. Dead-letter queues capture failures for analysis.",
                "risk": "medium",
                "options": [
                    "No Async Messaging: Synchronous communication only; no SQS/SNS usage",
                    "Basic Queue Usage: Simple SQS queues; synchronous where async would be better",
                    "Fan-out Patterns: SNS to SQS fan-out; basic retry configuration",
                    "Comprehensive Patterns: Dead-letter queues everywhere; visibility timeout tuning; batch processing",
                    "Advanced Messaging: FIFO where needed; exactly-once processing; message deduplication; advanced patterns"
                ]
            }
        ]
    },
    "Serverless Security": {
        "weight": 0.18, "pillars": ["SEC"],
        "description": "Evaluates Lambda security, secrets management, and API protection mechanisms.",
        "questions": [
            {
                "id": "GA-SEC-001",
                "question": "How are Lambda execution roles designed and managed?",
                "context": "Each Lambda function should have a unique IAM execution role with minimal permissions (least privilege). Shared roles across functions result in excessive permissions. IAM Access Analyzer identifies unused permissions. Permission boundaries provide guardrails preventing privilege escalation.",
                "risk": "critical",
                "options": [
                    "Single Shared Role: One role shared across all Lambda functions; broad permissions",
                    "Per-Application Roles: Broad roles per application; same role for multiple functions",
                    "Function-Specific Roles: Each function has dedicated role; manually managed; often overly permissive",
                    "Least-Privilege Roles: Function-specific roles with minimal permissions; Access Analyzer for optimization",
                    "Automated IAM Management: Automated role creation; permission boundaries; continuous permission analysis"
                ]
            },
            {
                "id": "GA-SEC-002",
                "question": "How is secrets management implemented for serverless applications?",
                "context": "Secrets (API keys, database credentials) must never be in code or plaintext environment variables. AWS Secrets Manager provides secure storage with automatic rotation. Parameter Store offers hierarchical configuration. Lambda extensions enable cached secret retrieval without cold start penalty.",
                "risk": "critical",
                "options": [
                    "Environment Variables Plaintext: Secrets stored as plaintext Lambda environment variables",
                    "Encrypted Environment Variables: Secrets in encrypted environment variables; manual rotation",
                    "Parameter Store: AWS Systems Manager Parameter Store for configuration and secrets",
                    "Secrets Manager with Rotation: Secrets Manager for credentials; automatic rotation configured",
                    "Secrets Manager + Lambda Extension: Secrets Manager with rotation; Lambda extension for caching; no env var secrets"
                ]
            },
            {
                "id": "GA-SEC-003",
                "question": "How is API authentication and authorization implemented?",
                "context": "APIs require authentication to identify callers and authorization to control access. Cognito User Pools handle user identity. Lambda authorizers enable custom JWT validation and claims-based access. IAM authorization suits service-to-service. Fine-grained authorization controls resource-level access.",
                "risk": "critical",
                "options": [
                    "No Authentication: APIs publicly accessible without authentication",
                    "API Keys Only: API keys for access control (not true authentication; easily shared)",
                    "Cognito User Pools: Cognito for user authentication; basic authorization",
                    "Lambda Authorizers: Custom Lambda authorizers with JWT validation; role-based access control",
                    "Multi-Method Fine-Grained: Multiple auth methods; OAuth/OIDC; fine-grained authorization; machine-to-machine auth"
                ]
            },
            {
                "id": "GA-SEC-004",
                "question": "How is API traffic protected from attacks and abuse?",
                "context": "APIs are attack targets for injection, DDoS, and credential stuffing. AWS WAF protects against OWASP Top 10 attacks. Shield provides DDoS protection. Bot Control identifies automated threats. Rate limiting combined with WAF provides defense in depth.",
                "risk": "high",
                "options": [
                    "No Protection: No WAF; only basic API Gateway throttling",
                    "Basic Throttling: API Gateway throttling; no WAF or additional protection",
                    "WAF Managed Rules: AWS WAF with AWS managed rule sets (common attacks)",
                    "WAF Custom Rules: WAF with custom rules; Shield Standard; logging and monitoring",
                    "Comprehensive Protection: WAF custom rules; Shield Advanced; Bot Control; real-time threat analysis"
                ]
            },
            {
                "id": "GA-SEC-005",
                "question": "How are Lambda function vulnerabilities detected and remediated?",
                "context": "Lambda functions can have vulnerabilities in dependencies and custom code. CI/CD scanning catches issues before deployment. Amazon Inspector scans Lambda functions for vulnerabilities. Software composition analysis (SCA) tracks dependency vulnerabilities. Automated remediation speeds response.",
                "risk": "high",
                "options": [
                    "No Scanning: No vulnerability scanning for Lambda functions",
                    "Manual Review: Manual code review; no automated scanning",
                    "CI/CD Scanning: Dependency scanning in CI/CD pipeline; critical vulnerability blocking",
                    "Inspector Scanning: Amazon Inspector for Lambda; prioritized findings; remediation tracking",
                    "Continuous Security: Inspector + CI/CD scanning; automated remediation; runtime protection"
                ]
            }
        ]
    },
    "Observability & Monitoring": {
        "weight": 0.12, "pillars": ["OPS", "REL"],
        "description": "Evaluates logging, distributed tracing, metrics, and operational visibility for serverless.",
        "questions": [
            {
                "id": "GA-OBS-001",
                "question": "How is logging structured and standardized across serverless applications?",
                "context": "Structured logging (JSON format) enables querying and analysis in CloudWatch Logs Insights. Correlation IDs enable request tracing across functions. AWS Lambda Powertools provides standardized logging with automatic correlation. Centralized aggregation enables cross-function analysis and security investigation.",
                "risk": "medium",
                "options": [
                    "Unstructured Logging: console.log/print statements; no standard format; difficult to query",
                    "Basic Structure: Some structured logging; inconsistent format across functions",
                    "JSON Logging: Consistent JSON logging with timestamps and standard fields",
                    "Correlation IDs: Structured logging with correlation IDs; Lambda Powertools adoption",
                    "Comprehensive Logging: Powertools; correlation; log sampling; centralized aggregation; security integration"
                ]
            },
            {
                "id": "GA-OBS-002",
                "question": "How is distributed tracing implemented across serverless components?",
                "context": "AWS X-Ray provides distributed tracing showing request flow across Lambda, API Gateway, SQS, DynamoDB, and other services. Custom segments add business context. Service maps visualize dependencies. Trace analysis identifies latency bottlenecks and errors.",
                "risk": "medium",
                "options": [
                    "No Tracing: No distributed tracing; debugging requires log correlation",
                    "Partial X-Ray: X-Ray enabled for some functions; limited visibility",
                    "X-Ray All Serverless: X-Ray enabled for all Lambda and API Gateway; basic service map",
                    "Custom Segments: X-Ray with custom segments and annotations; external call subsegments",
                    "Comprehensive Tracing: X-Ray + OpenTelemetry; custom instrumentation; business correlation"
                ]
            },
            {
                "id": "GA-OBS-003",
                "question": "How are custom metrics captured and used for serverless applications?",
                "context": "AWS provides default Lambda metrics (invocations, duration, errors). Custom metrics capture business KPIs and application-specific data. Embedded Metric Format (EMF) enables efficient metric publishing from Lambda. Anomaly detection identifies deviations from expected patterns.",
                "risk": "medium",
                "options": [
                    "Default Metrics Only: Only using AWS-provided Lambda metrics; no custom metrics",
                    "Some Custom Metrics: Custom metrics for specific needs; manual CloudWatch PutMetric calls",
                    "EMF for Business Metrics: Business metrics via Embedded Metric Format; standard dimensions",
                    "Comprehensive Metrics: Full custom metrics; per-application dashboards; alerting configured",
                    "Full Observability: EMF metrics; anomaly detection; SLI/SLO tracking; real-time dashboards"
                ]
            },
            {
                "id": "GA-OBS-004",
                "question": "Are SLOs (Service Level Objectives) defined and tracked for serverless workloads?",
                "context": "SLOs define reliability targets (e.g., 99.9% availability, p99 latency <500ms). SLIs (Service Level Indicators) measure actual performance. Error budgets quantify acceptable unreliability. SLO tracking enables data-driven reliability decisions and appropriate investment.",
                "risk": "medium",
                "options": [
                    "No SLOs: No formal reliability targets defined; reactive incident response",
                    "Informal Targets: Implicit availability expectations; not formally tracked",
                    "Key Function SLIs: SLIs tracked for critical functions; basic dashboards",
                    "SLOs with Error Budgets: Formal SLOs; error budget tracking; alerting on budget burn",
                    "Comprehensive SLO Program: SLOs for all services; automated tracking; error budget policies; continuous improvement"
                ]
            }
        ]
    },
    "CI/CD & DevOps": {
        "weight": 0.12, "pillars": ["OPS"],
        "description": "Evaluates deployment automation, testing strategies, and DevOps practices for serverless.",
        "questions": [
            {
                "id": "GA-DEV-001",
                "question": "What is your serverless deployment approach and tooling?",
                "context": "SAM and Serverless Framework simplify Lambda deployment with infrastructure-as-code. CDK enables infrastructure definition using programming languages with type safety. GitOps workflows provide automated, auditable deployments triggered by code commits.",
                "risk": "medium",
                "options": [
                    "Manual Console: Lambda deployed through AWS Console; no automation",
                    "CLI-Based: AWS CLI or framework CLI for deployments; manual execution",
                    "SAM/Serverless Framework: SAM or Serverless Framework; basic CI/CD pipeline",
                    "CDK Multi-Environment: AWS CDK with multiple environments; automated testing before deployment",
                    "Full GitOps: PR-based deployments; automated testing; multiple environments; comprehensive IaC"
                ]
            },
            {
                "id": "GA-DEV-002",
                "question": "How are safe deployments implemented for serverless applications?",
                "context": "All-at-once deployments risk widespread outages from bugs. Canary deployments route small traffic percentage to new version while monitoring. Linear deployments gradually shift traffic. CodeDeploy integrates with Lambda for automated traffic shifting and rollback.",
                "risk": "high",
                "options": [
                    "All-at-Once: New versions deployed to all traffic immediately; no gradual rollout",
                    "Manual Staged: Manual deployment to environments; human monitoring for issues",
                    "Blue-Green: Blue-green deployment with manual traffic shift; rollback capability",
                    "Canary with Alarms: Canary deployment with CloudWatch alarms; automated rollback on errors",
                    "Progressive Deployment: Canary + linear deployment; comprehensive monitoring; automatic rollback; feature flags"
                ]
            },
            {
                "id": "GA-DEV-003",
                "question": "How comprehensive is your serverless testing strategy?",
                "context": "Serverless testing requires different approaches: unit tests for business logic, integration tests for AWS service interactions, contract tests for API compatibility. Local testing with SAM Local or LocalStack simulates AWS environment. Chaos engineering validates resilience.",
                "risk": "high",
                "options": [
                    "No Automated Testing: Manual validation only; tests not automated",
                    "Unit Tests Only: Unit tests for business logic; limited coverage; no integration tests",
                    "Unit + Integration: Unit tests plus integration tests; some AWS service mocking",
                    "Comprehensive Local Testing: Unit, integration, and E2E tests; SAM Local or LocalStack for AWS simulation",
                    "Full Test Pyramid: Comprehensive testing; contract tests; chaos engineering; automated in CI/CD"
                ]
            }
        ]
    },
    "Cost Optimization": {
        "weight": 0.10, "pillars": ["COST"],
        "description": "Evaluates serverless cost visibility, optimization practices, and efficiency.",
        "questions": [
            {
                "id": "GA-CST-001",
                "question": "What is your visibility into serverless costs?",
                "context": "Serverless costs can be difficult to attribute without proper tagging. Function-level cost analysis identifies optimization opportunities. Per-invocation cost understanding enables architectural decisions. Anomaly detection catches unexpected cost spikes before budget impact.",
                "risk": "medium",
                "options": [
                    "No Tracking: Serverless costs not specifically tracked; aggregate AWS bill only",
                    "Service-Level Costs: Lambda costs visible at service level; no function-level breakdown",
                    "Function-Level Tagging: Cost allocation tags on functions; manual analysis possible",
                    "Per-Application Dashboards: Comprehensive tagging; automated cost dashboards; anomaly alerts",
                    "Real-Time Cost Visibility: Per-invocation cost analysis; automated optimization recommendations"
                ]
            },
            {
                "id": "GA-CST-002",
                "question": "How is Lambda memory/CPU optimization performed?",
                "context": "Lambda pricing depends on memory allocation (which also controls CPU) and duration. Higher memory can reduce duration enough to lower cost. AWS Lambda Power Tuning automates finding optimal configuration. Graviton2 (ARM) provides better price-performance for many workloads.",
                "risk": "low",
                "options": [
                    "Default Settings: Default 128MB-512MB memory; no optimization analysis",
                    "Manual Testing: One-time manual testing for some functions; no ongoing optimization",
                    "Power Tuning Tool: AWS Lambda Power Tuning for critical functions; periodic optimization",
                    "Systematic Optimization: Regular optimization cycles; Graviton2 adoption; cost-performance tracking",
                    "Automated Continuous: Automated optimization integrated with CI/CD; continuous right-sizing; FinOps integration"
                ]
            }
        ]
    },
    "Resilience & Reliability": {
        "weight": 0.15, "pillars": ["REL"],
        "description": "Evaluates fault tolerance patterns, retry logic, and multi-region strategies for serverless.",
        "questions": [
            {
                "id": "GA-REL-001",
                "question": "How is error handling and retry logic implemented?",
                "context": "Serverless applications must handle transient failures gracefully. Exponential backoff prevents thundering herd problems. Circuit breakers prevent cascade failures. Dead-letter queues capture failed events for analysis and reprocessing. Proper timeout configuration prevents hung invocations.",
                "risk": "high",
                "options": [
                    "No Error Handling: Basic try-catch; failures cause data loss; no retry logic",
                    "Default Lambda Retries: Relying on Lambda's built-in retry behavior only",
                    "Custom Retry Logic: Custom retry with exponential backoff; basic error categorization",
                    "Comprehensive Patterns: Circuit breakers; dead-letter queues for all async; retry with jitter",
                    "Full Resilience: All patterns implemented; bulkhead isolation; fallback responses; chaos testing"
                ]
            },
            {
                "id": "GA-REL-002",
                "question": "How is idempotency implemented for serverless functions?",
                "context": "Serverless platforms may invoke functions multiple times (at-least-once delivery). Idempotency ensures repeated invocations produce the same result without side effects. Implementation approaches: idempotency keys, database constraints, conditional writes. Lambda Powertools provides utilities.",
                "risk": "high",
                "options": [
                    "Not Implemented: Idempotency not considered; duplicate processing possible",
                    "Awareness Only: Team aware of need; not systematically implemented",
                    "Critical Operations: Idempotency for payment/critical operations; ad-hoc implementation",
                    "Comprehensive Tokens: Idempotency tokens for all state-changing operations; database constraints",
                    "Powertools Idempotency: Lambda Powertools idempotency utility; comprehensive coverage; automatic deduplication"
                ]
            },
            {
                "id": "GA-REL-003",
                "question": "What is your multi-region strategy for serverless applications?",
                "context": "Multi-region provides resilience against regional failures and lower latency for global users. DynamoDB Global Tables provide multi-region data. API Gateway regional deployments with Route 53 health checks enable failover. Active-active requires careful conflict handling.",
                "risk": "high",
                "options": [
                    "Single Region: All serverless workloads in single region; no multi-region capability",
                    "Data Backup Only: Data replicated to secondary region; no compute failover",
                    "Active-Passive Manual: Secondary region deployable; manual failover procedure",
                    "Active-Passive Automated: Automated failover with Route 53; DynamoDB Global Tables",
                    "Active-Active: Traffic served from multiple regions; automatic routing; conflict resolution"
                ]
            }
        ]
    }
}

# =============================================================================
# APPLICATION LOGIC - WITH PROPER BUG FIX
# =============================================================================

def init_state():
    """Initialize session state"""
    if 'initialized' not in st.session_state:
        st.session_state.initialized = True
        st.session_state.ct_responses = {}  # Stores {qid: score} only for answered questions
        st.session_state.ga_responses = {}
        st.session_state.touched_questions = set()  # Tracks which questions user has interacted with
        st.session_state.ai_analysis = None
        st.session_state.org_name = ''
        st.session_state.assessor_name = ''
        st.session_state.industry = 'technology'
        st.session_state.report = None

def count_questions(domains: dict) -> int:
    """Count total questions"""
    return sum(len(d["questions"]) for d in domains.values())

def count_answered(responses: dict) -> int:
    """Count actually answered questions"""
    return len(responses)

def calc_scores(responses: dict, domains: dict) -> dict:
    """Calculate weighted scores"""
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
    """Get maturity level, class, and description"""
    if score >= 80: return "Optimized", "success", "Continuous improvement with automation"
    if score >= 60: return "Managed", "warning", "Proactive management with defined processes"
    if score >= 40: return "Developing", "warning", "Emerging standards and reactive approach"
    if score >= 20: return "Initial", "danger", "Ad-hoc processes with limited consistency"
    return "Not Assessed", "neutral", "Assessment not complete"

def find_gaps(responses: dict, domains: dict) -> list:
    """Find gaps prioritized by risk"""
    gaps = []
    for dname, ddata in domains.items():
        for q in ddata["questions"]:
            if q["id"] in responses and responses[q["id"]] <= 2:
                gaps.append({
                    "id": q["id"], "domain": dname,
                    "question": q["question"],
                    "context": q.get("context", ""),
                    "score": responses[q["id"]],
                    "risk": q["risk"]
                })
    
    risk_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    return sorted(gaps, key=lambda x: (risk_order.get(x["risk"], 3), -x["score"]))

def on_question_change(qid: str, responses: dict, options: list):
    """Callback when user changes a question - THIS IS THE KEY BUG FIX"""
    key = f"q_{qid}"
    if key in st.session_state:
        selected = st.session_state[key]
        st.session_state.touched_questions.add(qid)
        
        if selected == NOT_ANSWERED:
            # User explicitly selected "not answered" - remove from responses
            if qid in responses:
                del responses[qid]
        else:
            # Find the score for this option (1-5)
            option_index = options.index(selected)
            responses[qid] = option_index  # 0 = not answered, 1-5 = scores

def render_metric(value: float, label: str, suffix: str = "%"):
    """Render metric card"""
    level, level_class, _ = get_maturity(value)
    colors = {"success": "#059669", "warning": "#d97706", "danger": "#dc2626", "neutral": "#6b7280"}
    badges = {"success": "badge-success", "warning": "badge-warning", "danger": "badge-danger", "neutral": "badge-neutral"}
    
    st.markdown(f'''
    <div class="metric-card">
        <div class="metric-value" style="color:{colors.get(level_class, '#6b7280')}">{value:.0f}{suffix}</div>
        <div class="metric-label">{label}</div>
        <div class="metric-badge {badges.get(level_class, 'badge-neutral')}">{level}</div>
    </div>
    ''', unsafe_allow_html=True)

def render_questions(domains: dict, responses: dict, prefix: str):
    """Render assessment questions with proper state handling"""
    for dname, ddata in domains.items():
        answered = sum(1 for q in ddata["questions"] if q["id"] in responses)
        total = len(ddata["questions"])
        
        pillars_html = " ".join([f'<span class="pillar-tag pillar-{p}">{WA_PILLARS.get(p, p)}</span>' for p in ddata["pillars"]])
        
        with st.expander(f"📁 {dname} — {answered}/{total} answered ({ddata['weight']*100:.0f}% weight)"):
            st.markdown(f"**{ddata.get('description', '')}**")
            st.markdown(f"Well-Architected Pillars: {pillars_html}", unsafe_allow_html=True)
            st.markdown("---")
            
            for q in ddata["questions"]:
                qid = q["id"]
                is_answered = qid in responses
                card_class = "answered" if is_answered else "unanswered"
                
                st.markdown(f'''
                <div class="question-card {card_class}">
                    <div style="display:flex;justify-content:space-between;align-items:center">
                        <span class="question-id">{qid}</span>
                        <span class="risk-badge risk-{q["risk"]}">{q["risk"]}</span>
                    </div>
                    <div class="question-text">{q["question"]}</div>
                </div>
                ''', unsafe_allow_html=True)
                
                # Show context
                if q.get("context"):
                    with st.expander("ℹ️ Why this matters", expanded=False):
                        st.markdown(f'<div class="question-context">{q["context"]}</div>', unsafe_allow_html=True)
                
                # Build options with NOT_ANSWERED as first option
                options = [NOT_ANSWERED] + q["options"]
                
                # Determine current index
                current_idx = 0
                if qid in responses:
                    current_idx = responses[qid]  # 1-5 maps to index 1-5
                
                # Use selectbox with on_change callback
                st.selectbox(
                    f"Response for {qid}",
                    options=options,
                    index=current_idx,
                    key=f"q_{qid}",
                    label_visibility="collapsed",
                    on_change=on_question_change,
                    args=(qid, responses, options)
                )
                
                st.markdown("")  # Spacing

def call_claude(prompt: str) -> str:
    """Call Claude API"""
    try:
        import anthropic
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            return "⚠️ **API Key Required**\n\nTo enable AI analysis:\n1. Go to Streamlit Cloud app settings\n2. Click 'Secrets'\n3. Add: `ANTHROPIC_API_KEY = \"your-key\"`"
        
        client = anthropic.Anthropic(api_key=api_key)
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=8192,
            system="You are an expert AWS Solutions Architect specializing in Control Tower and serverless architecture. Provide detailed, actionable recommendations.",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text
    except Exception as e:
        return f"⚠️ **Error**: {str(e)}"

# =============================================================================
# MAIN APPLICATION
# =============================================================================
def main():
    init_state()
    
    # Header
    st.markdown('''
    <div class="main-header">
        <h1>☁️ AWS Enterprise Assessment Platform <span class="aws-badge">v3.0</span></h1>
        <p>AI-Powered Control Tower Migration & Serverless Architecture Assessment</p>
    </div>
    ''', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("### ⚙️ Configuration")
        st.session_state.org_name = st.text_input("Organization", st.session_state.org_name)
        st.session_state.assessor_name = st.text_input("Assessor", st.session_state.assessor_name)
        st.session_state.industry = st.selectbox(
            "Industry",
            options=list(BENCHMARKS.keys()),
            format_func=lambda x: BENCHMARKS[x]["name"],
            index=list(BENCHMARKS.keys()).index(st.session_state.industry)
        )
        
        st.markdown("### 📊 Progress")
        ct_total = count_questions(CT_QUESTIONS)
        ct_answered = count_answered(st.session_state.ct_responses)
        ga_total = count_questions(GA_QUESTIONS)
        ga_answered = count_answered(st.session_state.ga_responses)
        
        st.markdown(f"**Control Tower**: {ct_answered}/{ct_total}")
        st.progress(ct_answered/ct_total if ct_total else 0)
        
        st.markdown(f"**Golden Architecture**: {ga_answered}/{ga_total}")
        st.progress(ga_answered/ga_total if ga_total else 0)
        
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total", ct_total + ga_total)
        with col2:
            st.metric("Done", ct_answered + ga_answered)
        
        if st.button("🔄 Reset All", type="secondary"):
            st.session_state.ct_responses = {}
            st.session_state.ga_responses = {}
            st.session_state.touched_questions = set()
            st.session_state.ai_analysis = None
            st.session_state.report = None
            st.rerun()
    
    # Tabs
    tabs = st.tabs(["📊 Dashboard", "🎛️ Control Tower", "⚡ Golden Architecture", "🔍 Gaps", "🤖 AI Analysis", "📄 Reports"])
    
    # Dashboard
    with tabs[0]:
        st.markdown('<div class="section-title">📊 Executive Dashboard</div>', unsafe_allow_html=True)
        
        ct_scores = calc_scores(st.session_state.ct_responses, CT_QUESTIONS)
        ga_scores = calc_scores(st.session_state.ga_responses, GA_QUESTIONS)
        combined = (ct_scores["overall"] + ga_scores["overall"]) / 2 if (ct_scores["overall"] > 0 or ga_scores["overall"] > 0) else 0
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            render_metric(ct_scores["overall"], "Control Tower")
        with col2:
            render_metric(ga_scores["overall"], "Golden Architecture")
        with col3:
            render_metric(combined, "Combined Score")
        with col4:
            bench = BENCHMARKS[st.session_state.industry]
            vs_avg = combined - bench["avg"]
            color = "#059669" if vs_avg >= 0 else "#dc2626"
            st.markdown(f'''
            <div class="metric-card">
                <div class="metric-value" style="color:{color}">{vs_avg:+.0f}%</div>
                <div class="metric-label">vs {bench["name"]} Avg</div>
                <div class="metric-badge badge-neutral">Benchmark: {bench["avg"]}%</div>
            </div>
            ''', unsafe_allow_html=True)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Control Tower Domains")
            if ct_scores["total_answered"] > 0:
                for dname, data in ct_scores["domains"].items():
                    if data["answered"] > 0:
                        level, lclass, _ = get_maturity(data["score"])
                        colors = {"success": "#059669", "warning": "#d97706", "danger": "#dc2626", "neutral": "#6b7280"}
                        st.markdown(f'''
                        <div class="domain-card">
                            <div style="display:flex;justify-content:space-between">
                                <span style="font-weight:600">{dname}</span>
                                <span style="font-family:'Fira Code';color:{colors.get(lclass,'#6b7280')}">{data["score"]:.0f}%</span>
                            </div>
                            <div style="font-size:0.8rem;color:#64748b">{level} • {data["answered"]}/{data["total"]}</div>
                        </div>
                        ''', unsafe_allow_html=True)
                        st.progress(data["score"]/100)
            else:
                st.info("Answer Control Tower questions to see domain scores")
        
        with col2:
            st.markdown("#### Golden Architecture Domains")
            if ga_scores["total_answered"] > 0:
                for dname, data in ga_scores["domains"].items():
                    if data["answered"] > 0:
                        level, lclass, _ = get_maturity(data["score"])
                        colors = {"success": "#059669", "warning": "#d97706", "danger": "#dc2626", "neutral": "#6b7280"}
                        st.markdown(f'''
                        <div class="domain-card">
                            <div style="display:flex;justify-content:space-between">
                                <span style="font-weight:600">{dname}</span>
                                <span style="font-family:'Fira Code';color:{colors.get(lclass,'#6b7280')}">{data["score"]:.0f}%</span>
                            </div>
                            <div style="font-size:0.8rem;color:#64748b">{level} • {data["answered"]}/{data["total"]}</div>
                        </div>
                        ''', unsafe_allow_html=True)
                        st.progress(data["score"]/100)
            else:
                st.info("Answer Golden Architecture questions to see domain scores")
    
    # Control Tower Assessment
    with tabs[1]:
        st.markdown('<div class="section-title">🎛️ Control Tower Assessment</div>', unsafe_allow_html=True)
        ct_total = count_questions(CT_QUESTIONS)
        ct_answered = count_answered(st.session_state.ct_responses)
        
        col1, col2, col3 = st.columns(3)
        with col1: st.metric("Total Questions", ct_total)
        with col2: st.metric("Answered", ct_answered)
        with col3: st.metric("Completion", f"{(ct_answered/ct_total*100):.0f}%" if ct_total else "0%")
        
        st.info("💡 **Tip**: Select an option to answer each question. Questions default to 'Not Assessed' until you make a selection.")
        st.markdown("---")
        render_questions(CT_QUESTIONS, st.session_state.ct_responses, "ct")
    
    # Golden Architecture Assessment
    with tabs[2]:
        st.markdown('<div class="section-title">⚡ Golden Architecture Assessment</div>', unsafe_allow_html=True)
        ga_total = count_questions(GA_QUESTIONS)
        ga_answered = count_answered(st.session_state.ga_responses)
        
        col1, col2, col3 = st.columns(3)
        with col1: st.metric("Total Questions", ga_total)
        with col2: st.metric("Answered", ga_answered)
        with col3: st.metric("Completion", f"{(ga_answered/ga_total*100):.0f}%" if ga_total else "0%")
        
        st.info("💡 **Tip**: Select an option to answer each question. Questions default to 'Not Assessed' until you make a selection.")
        st.markdown("---")
        render_questions(GA_QUESTIONS, st.session_state.ga_responses, "ga")
    
    # Gap Analysis
    with tabs[3]:
        st.markdown('<div class="section-title">🔍 Gap Analysis</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Control Tower Gaps")
            ct_gaps = find_gaps(st.session_state.ct_responses, CT_QUESTIONS)
            if ct_gaps:
                crit = len([g for g in ct_gaps if g["risk"] == "critical"])
                high = len([g for g in ct_gaps if g["risk"] == "high"])
                c1, c2, c3 = st.columns(3)
                with c1: st.metric("🔴 Critical", crit)
                with c2: st.metric("🟠 High", high)
                with c3: st.metric("🟡 Medium", len(ct_gaps) - crit - high)
                
                for g in ct_gaps[:8]:
                    cls = "" if g["risk"]=="critical" else " high" if g["risk"]=="high" else " medium"
                    st.markdown(f'''
                    <div class="gap-card{cls}">
                        <strong>{g["id"]}</strong> · <span class="risk-badge risk-{g["risk"]}">{g["risk"]}</span><br/>
                        <span style="color:#374151">{g["question"][:100]}...</span><br/>
                        <small style="color:#64748b">Score: {g["score"]}/5 · {g["domain"]}</small>
                    </div>
                    ''', unsafe_allow_html=True)
            else:
                if count_answered(st.session_state.ct_responses) > 0:
                    st.success("✅ No critical gaps found!")
                else:
                    st.info("Complete assessment to see gaps")
        
        with col2:
            st.markdown("#### Golden Architecture Gaps")
            ga_gaps = find_gaps(st.session_state.ga_responses, GA_QUESTIONS)
            if ga_gaps:
                crit = len([g for g in ga_gaps if g["risk"] == "critical"])
                high = len([g for g in ga_gaps if g["risk"] == "high"])
                c1, c2, c3 = st.columns(3)
                with c1: st.metric("🔴 Critical", crit)
                with c2: st.metric("🟠 High", high)
                with c3: st.metric("🟡 Medium", len(ga_gaps) - crit - high)
                
                for g in ga_gaps[:8]:
                    cls = "" if g["risk"]=="critical" else " high" if g["risk"]=="high" else " medium"
                    st.markdown(f'''
                    <div class="gap-card{cls}">
                        <strong>{g["id"]}</strong> · <span class="risk-badge risk-{g["risk"]}">{g["risk"]}</span><br/>
                        <span style="color:#374151">{g["question"][:100]}...</span><br/>
                        <small style="color:#64748b">Score: {g["score"]}/5 · {g["domain"]}</small>
                    </div>
                    ''', unsafe_allow_html=True)
            else:
                if count_answered(st.session_state.ga_responses) > 0:
                    st.success("✅ No critical gaps found!")
                else:
                    st.info("Complete assessment to see gaps")
    
    # AI Analysis
    with tabs[4]:
        st.markdown('<div class="section-title">🤖 AI-Powered Analysis</div>', unsafe_allow_html=True)
        
        analysis_type = st.selectbox("Analysis Type", [
            "🎯 Gap Analysis & Prioritization",
            "🗺️ 12-Month Implementation Roadmap",
            "⚠️ Risk Assessment",
            "💰 Cost-Benefit Analysis",
            "🏗️ Architecture Recommendations"
        ])
        
        context = st.text_area("Additional Context", placeholder="Budget, timeline, team size, constraints...", height=80)
        
        if st.button("🚀 Generate Analysis", type="primary"):
            total = count_answered(st.session_state.ct_responses) + count_answered(st.session_state.ga_responses)
            if total < 3:
                st.warning("Answer at least 3 questions first")
            else:
                with st.spinner("Generating analysis..."):
                    ct_scores = calc_scores(st.session_state.ct_responses, CT_QUESTIONS)
                    ga_scores = calc_scores(st.session_state.ga_responses, GA_QUESTIONS)
                    ct_gaps = find_gaps(st.session_state.ct_responses, CT_QUESTIONS)
                    ga_gaps = find_gaps(st.session_state.ga_responses, GA_QUESTIONS)
                    
                    prompt = f"""AWS Assessment - {analysis_type}

Organization: {st.session_state.org_name or 'Not specified'}
Industry: {BENCHMARKS[st.session_state.industry]['name']}

CONTROL TOWER: {ct_scores['overall']:.0f}% ({get_maturity(ct_scores['overall'])[0]})
- Critical gaps: {len([g for g in ct_gaps if g['risk']=='critical'])}
- High gaps: {len([g for g in ct_gaps if g['risk']=='high'])}
- Top gaps: {json.dumps([{'id': g['id'], 'q': g['question'][:60], 'risk': g['risk']} for g in ct_gaps[:5]], indent=2)}

GOLDEN ARCHITECTURE: {ga_scores['overall']:.0f}% ({get_maturity(ga_scores['overall'])[0]})
- Critical gaps: {len([g for g in ga_gaps if g['risk']=='critical'])}
- High gaps: {len([g for g in ga_gaps if g['risk']=='high'])}
- Top gaps: {json.dumps([{'id': g['id'], 'q': g['question'][:60], 'risk': g['risk']} for g in ga_gaps[:5]], indent=2)}

Context: {context or 'None'}

Provide detailed analysis with:
1. Executive summary
2. Prioritized recommendations with AWS services
3. Effort estimates (person-weeks)
4. Dependencies and sequencing
5. Success metrics"""
                    
                    st.session_state.ai_analysis = call_claude(prompt)
        
        if st.session_state.ai_analysis:
            st.markdown("---")
            st.markdown('<div class="ai-response">', unsafe_allow_html=True)
            st.markdown(st.session_state.ai_analysis)
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Reports
    with tabs[5]:
        st.markdown('<div class="section-title">📄 Reports & Export</div>', unsafe_allow_html=True)
        
        ct_scores = calc_scores(st.session_state.ct_responses, CT_QUESTIONS)
        ga_scores = calc_scores(st.session_state.ga_responses, GA_QUESTIONS)
        combined = (ct_scores["overall"] + ga_scores["overall"]) / 2 if (ct_scores["overall"] > 0 or ga_scores["overall"] > 0) else 0
        
        col1, col2, col3, col4 = st.columns(4)
        with col1: render_metric(ct_scores["overall"], "Control Tower")
        with col2: render_metric(ga_scores["overall"], "Golden Arch")
        with col3: render_metric(combined, "Combined")
        with col4:
            total_ans = count_answered(st.session_state.ct_responses) + count_answered(st.session_state.ga_responses)
            total_q = count_questions(CT_QUESTIONS) + count_questions(GA_QUESTIONS)
            render_metric(total_ans/total_q*100 if total_q else 0, "Completion")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📊 Generate Report", type="primary", use_container_width=True):
                ct_gaps = find_gaps(st.session_state.ct_responses, CT_QUESTIONS)
                ga_gaps = find_gaps(st.session_state.ga_responses, GA_QUESTIONS)
                
                st.session_state.report = f"""# AWS Enterprise Assessment Report

## Summary
| Field | Value |
|-------|-------|
| Organization | {st.session_state.org_name or 'N/A'} |
| Assessor | {st.session_state.assessor_name or 'N/A'} |
| Date | {datetime.now().strftime('%Y-%m-%d')} |
| Industry | {BENCHMARKS[st.session_state.industry]['name']} |

## Scores
| Assessment | Score | Level |
|------------|-------|-------|
| Control Tower | {ct_scores['overall']:.0f}% | {get_maturity(ct_scores['overall'])[0]} |
| Golden Architecture | {ga_scores['overall']:.0f}% | {get_maturity(ga_scores['overall'])[0]} |
| Combined | {combined:.0f}% | {get_maturity(combined)[0]} |

## Gap Summary
- **Control Tower**: {len([g for g in ct_gaps if g['risk']=='critical'])} critical, {len([g for g in ct_gaps if g['risk']=='high'])} high
- **Golden Architecture**: {len([g for g in ga_gaps if g['risk']=='critical'])} critical, {len([g for g in ga_gaps if g['risk']=='high'])} high

## AI Analysis
{st.session_state.ai_analysis or 'Generate AI analysis for recommendations.'}

---
*AWS Enterprise Assessment Platform v3.0*
"""
                st.success("✅ Report generated!")
        
        with col2:
            if st.session_state.report:
                st.download_button("⬇️ Download Report", st.session_state.report, 
                    f"aws_assessment_{datetime.now().strftime('%Y%m%d')}.md", "text/markdown", use_container_width=True)
        
        # JSON Export
        export = {
            "metadata": {"date": datetime.now().isoformat(), "org": st.session_state.org_name, "industry": st.session_state.industry},
            "control_tower": {"responses": st.session_state.ct_responses, "scores": ct_scores},
            "golden_architecture": {"responses": st.session_state.ga_responses, "scores": ga_scores}
        }
        st.download_button("📦 Export JSON", json.dumps(export, indent=2, default=str),
            f"aws_data_{datetime.now().strftime('%Y%m%d')}.json", "application/json")

if __name__ == "__main__":
    main()
