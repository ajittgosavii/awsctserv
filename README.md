# 🏗️ AWS Enterprise Assessment Platform

> **AI-Driven Control Tower Migration & Golden Architecture (Serverless) Assessment Tool**

An enterprise-grade Streamlit application designed to assess organizational readiness for AWS Control Tower migration and Golden Architecture (Serverless) adoption. The platform leverages AI-powered analysis using Claude API to provide actionable insights, gap analysis, and implementation roadmaps.

![Platform Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.9+-green)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red)
![License](https://img.shields.io/badge/license-MIT-yellow)

---

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Assessment Domains](#-assessment-domains)
- [AI Capabilities](#-ai-capabilities)
- [Export Options](#-export-options)
- [Deployment](#-deployment)
- [Security Considerations](#-security-considerations)
- [Contributing](#-contributing)

---

## ✨ Features

### Multi-Modal Assessment
- **Questionnaire-Based Assessment**: Comprehensive domain-specific questionnaires with weighted scoring
- **Document Analysis**: Upload and analyze existing documentation (PDF, DOCX, PPTX)
- **Hybrid Assessment**: Combine questionnaire responses with document analysis

### AI-Driven Intelligence
- **Gap Analysis & Prioritization**: Identify critical gaps with remediation recommendations
- **Implementation Roadmap**: Phased approach with timelines and milestones
- **Risk Assessment**: Technical, operational, security, and financial risk evaluation
- **Cost-Benefit Analysis**: ROI calculation framework and TCO comparison
- **Architecture Recommendations**: Reference patterns and best practices
- **Compliance Mapping**: SOC 2, PCI DSS, HIPAA, GDPR alignment

### Enterprise Features
- **Weighted Scoring Model**: Domain-specific weights for accurate maturity assessment
- **Maturity Level Classification**: Ad-hoc, Initial, Developing, Managed, Optimized
- **Real-time Score Calculation**: Instant feedback as assessments progress
- **Comprehensive Reporting**: Executive summaries and detailed breakdowns
- **Export Capabilities**: JSON, Markdown, and structured reports

---

## 🏛️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    AWS Assessment Platform                       │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │ Streamlit   │  │ Assessment  │  │ Document    │             │
│  │ Frontend    │──│ Engine      │──│ Processor   │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│         │                │                │                      │
│         └────────────────┼────────────────┘                      │
│                          │                                       │
│                  ┌───────┴───────┐                              │
│                  │ Claude API    │                              │
│                  │ Integration   │                              │
│                  └───────────────┘                              │
│                          │                                       │
│         ┌────────────────┼────────────────┐                      │
│         │                │                │                      │
│  ┌──────┴──────┐  ┌──────┴──────┐  ┌──────┴──────┐             │
│  │ Control     │  │ Golden      │  │ Reporting   │             │
│  │ Tower       │  │ Architecture│  │ Engine      │             │
│  │ Assessment  │  │ Assessment  │  │             │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Installation

### Prerequisites

- Python 3.9 or higher
- pip package manager
- Anthropic API key (for AI features)

### Local Installation

```bash
# Clone or download the application
cd aws-assessment-platform

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export ANTHROPIC_API_KEY="your-api-key-here"

# Run the application
streamlit run streamlit_app.py
```

### Docker Installation

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

```bash
# Build and run
docker build -t aws-assessment-platform .
docker run -p 8501:8501 -e ANTHROPIC_API_KEY=your-key aws-assessment-platform
```

---

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `ANTHROPIC_API_KEY` | Claude API authentication key | Yes (for AI features) |
| `STREAMLIT_SERVER_PORT` | Application port (default: 8501) | No |
| `LOG_LEVEL` | Logging verbosity | No |

### Configuration File

Edit `config.yaml` to customize:

```yaml
assessment:
  control_tower:
    enabled: true
  golden_architecture:
    enabled: true

ai:
  model: "claude-sonnet-4-20250514"
  max_tokens: 4096
```

---

## 📖 Usage

### 1. Start Assessment

1. Launch the application
2. Enter organization details in the sidebar
3. Select assessment mode (Questionnaire, Document, or Hybrid)

### 2. Complete Questionnaires

Navigate through domain-specific questions for:
- **Control Tower**: Landing Zone, Governance, Security, Networking, Operations
- **Golden Architecture**: Compute, API, Data, Security, Observability

### 3. Upload Documents (Optional)

Upload existing documentation for AI analysis:
- Architecture diagrams (PDF)
- Design documents (DOCX)
- Presentations (PPTX)
- Configuration files (JSON, TXT)

### 4. Generate AI Insights

Select analysis type:
- Gap Analysis & Prioritization
- Implementation Roadmap
- Risk Assessment
- Cost-Benefit Analysis
- Architecture Recommendations
- Compliance Mapping

### 5. Export Results

Download comprehensive reports in:
- Markdown format
- JSON (raw data)
- PDF (coming soon)

---

## 📊 Assessment Domains

### Control Tower Migration Assessment

| Domain | Weight | Focus Areas |
|--------|--------|-------------|
| Landing Zone Architecture | 20% | Multi-account strategy, Account Factory, Baseline configuration |
| Governance & Guardrails | 25% | SCPs, Config rules, Compliance, Tagging |
| Security & Identity | 20% | IAM Identity Center, Cross-account access, Security baseline |
| Networking & Connectivity | 15% | VPC design, Transit Gateway, Hybrid connectivity |
| Operations & Monitoring | 20% | Centralized logging, Cost management, Automation |

### Golden Architecture (Serverless) Assessment

| Domain | Weight | Focus Areas |
|--------|--------|-------------|
| Compute & Runtime | 25% | Lambda adoption, Deployment patterns, Fargate |
| API & Integration | 20% | API Gateway, EventBridge, Step Functions |
| Data & Storage | 20% | DynamoDB, Aurora Serverless, Data lake |
| Security & Compliance | 20% | IAM, Secrets management, API security |
| Observability & DevOps | 15% | Monitoring, CI/CD, Testing |

---

## 🤖 AI Capabilities

### Powered by Claude API

The platform integrates with Anthropic's Claude API to provide:

1. **Document Analysis**: Extract insights from uploaded documentation
2. **Gap Identification**: Compare current state against best practices
3. **Recommendation Generation**: Actionable, prioritized recommendations
4. **Roadmap Creation**: Phased implementation plans
5. **Risk Evaluation**: Comprehensive risk assessment with mitigation strategies

### Analysis Types

| Analysis | Description |
|----------|-------------|
| Gap Analysis | Identifies gaps by severity with remediation steps |
| Implementation Roadmap | 12-month phased plan with milestones |
| Risk Assessment | Technical, operational, security, financial risks |
| Cost-Benefit Analysis | ROI framework and TCO comparison |
| Architecture Recommendations | Reference patterns and service selection |
| Compliance Mapping | SOC 2, PCI DSS, HIPAA, GDPR alignment |

---

## 📥 Export Options

### JSON Export
```json
{
  "metadata": {
    "generated_at": "2025-01-15T10:30:00",
    "organization": "Acme Corp"
  },
  "control_tower": {
    "responses": {...},
    "scores": {...}
  },
  "golden_architecture": {
    "responses": {...},
    "scores": {...}
  },
  "ai_analysis": "..."
}
```

### Markdown Report
- Executive Summary
- Domain Scores
- Maturity Levels
- AI-Generated Recommendations
- Implementation Roadmap

---

## 🌐 Deployment

### AWS Deployment Options

#### ECS Fargate
```bash
# Build and push to ECR
aws ecr create-repository --repository-name aws-assessment-platform
docker tag aws-assessment-platform:latest <account>.dkr.ecr.<region>.amazonaws.com/aws-assessment-platform:latest
docker push <account>.dkr.ecr.<region>.amazonaws.com/aws-assessment-platform:latest

# Deploy with ECS
# Use provided CloudFormation template or CDK stack
```

#### EC2 with Application Load Balancer
- Deploy behind ALB with SSL termination
- Use Secrets Manager for API keys
- Enable CloudWatch logging

#### Streamlit Community Cloud
1. Push code to GitHub repository
2. Connect to Streamlit Community Cloud
3. Configure secrets in Streamlit dashboard

---

## 🔒 Security Considerations

### Best Practices

1. **API Key Management**: Use AWS Secrets Manager or environment variables
2. **Access Control**: Implement authentication for production deployments
3. **Data Encryption**: Enable encryption at rest and in transit
4. **Audit Logging**: Enable CloudTrail and application logging
5. **Network Security**: Deploy in private subnet with NAT Gateway

### Compliance

- No PII stored in application state
- All AI analysis performed in real-time (no data retention)
- Export data encrypted in transit

---

## 🛠️ Development

### Project Structure

```
aws-assessment-platform/
├── streamlit_app.py       # Main Streamlit application
├── requirements.txt       # Python dependencies
├── config.yaml           # Application configuration
├── README.md             # Documentation
├── Dockerfile            # Container configuration
└── .streamlit/
    └── config.toml       # Streamlit configuration
```

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest tests/ --cov=app
```

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- AI powered by [Anthropic Claude](https://www.anthropic.com/)
- Inspired by AWS Well-Architected Framework

---

## 📞 Support

For questions or support:
- Create an issue in the repository
- Contact the Cloud Architecture team

---

**Built with ❤️ for Enterprise Cloud Transformation**
