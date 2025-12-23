# AWS Enterprise Assessment Platform v3.0

A comprehensive, enterprise-grade assessment tool for AWS Control Tower migration and serverless architecture readiness.

## 📊 Assessment Coverage

| Category | Questions | Domains |
|----------|-----------|---------|
| **Control Tower** | 72 | 12 |
| **Golden Architecture (Serverless)** | 60 | 10 |
| **Total** | **132** | **22** |

## 🚀 Quick Deploy to Streamlit Cloud

### Step 1: Upload to GitHub
Create a new repository and upload these files:
```
aws-assessment-platform/
├── streamlit_app.py           # Main application
├── requirements.txt           # Dependencies
├── .streamlit/config.toml     # Theme configuration
└── README.md                  # This file
```

### Step 2: Deploy
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Connect your GitHub repository
4. Select `streamlit_app.py` as the main file
5. Click "Deploy"

### Step 3: Enable AI Features (Optional)
1. Go to your app's Settings → Secrets
2. Add your Anthropic API key:
```toml
ANTHROPIC_API_KEY = "sk-ant-your-key-here"
```

---

## ✨ Enterprise Features

### Professional UI
- Clean, modern light theme
- Responsive design for presentations
- Color-coded risk indicators
- Progress tracking
- Industry benchmarking

### Comprehensive Assessment
- **132 detailed questions** with context explanations
- **22 domains** covering all aspects of Control Tower and serverless
- **Risk-weighted scoring** (Critical, High, Medium, Low)
- **Well-Architected Framework alignment**

### AI-Powered Analysis
- Claude integration for intelligent recommendations
- Multiple analysis types:
  - Gap Analysis & Prioritization
  - 12-Month Implementation Roadmap
  - Risk Assessment Matrix
  - Cost-Benefit Analysis
  - Architecture Recommendations
  - Executive Summary

### Export & Reporting
- Executive reports in Markdown
- JSON data export for integration
- Professional formatting for stakeholder presentations

---

## 🎛️ Control Tower Domains (12)

1. Organizational Strategy & Governance
2. Account Factory & Provisioning
3. Guardrails & Service Control Policies
4. Detective Controls & Compliance
5. Identity & Access Management
6. Network Architecture
7. Logging & Security Operations
8. Cost Management & FinOps
9. Backup & Disaster Recovery
10. Migration Readiness
11. Operational Readiness
12. Data Protection

## ⚡ Golden Architecture Domains (10)

1. Serverless Compute Strategy
2. API & Integration Layer
3. Workflow Orchestration
4. Serverless Data Layer
5. Serverless Security
6. Observability & Monitoring
7. CI/CD & DevOps
8. Cost Optimization
9. Resilience & Reliability
10. Event-Driven Architecture

---

## 🐛 Bug Fixes in v3.0

✅ **Fixed**: Questions now properly default to "Not yet assessed"
- Progress only counts questions you've explicitly answered
- Selecting one question no longer marks all as answered

✅ **Removed**: Unnecessary Docker/shell files
- Only essential files for Streamlit Cloud deployment

✅ **Enhanced**: Comprehensive question context
- Each question includes detailed rationale
- Explains AWS best practices and recommendations

---

## 💻 Local Development

```bash
# Clone the repository
git clone <your-repo-url>
cd aws-assessment-platform

# Install dependencies
pip install -r requirements.txt

# Optional: Set API key for AI features
export ANTHROPIC_API_KEY="your-key"

# Run the application
streamlit run streamlit_app.py
```

---

## 📄 License

Enterprise use. Contact for licensing details.

---

*Built with Streamlit and Claude AI*
