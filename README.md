# AWS Enterprise Assessment Platform v3.0

## 🚀 Deploy to Streamlit Cloud (Recommended)

### Files Included
```
aws-assessment-platform/
├── streamlit_app.py      # Main application (1,760 lines)
├── requirements.txt      # Python dependencies
├── .streamlit/
│   └── config.toml      # Theme configuration
└── README.md            # This file
```

**No Docker or shell scripts needed!** Streamlit Cloud handles everything.

### Deployment Steps

1. **Upload to GitHub**
   - Create a new GitHub repository
   - Upload all files maintaining the folder structure

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Connect your GitHub repo
   - Select `streamlit_app.py` as main file
   - Click "Deploy"

3. **Enable AI Features (Optional)**
   - In Streamlit Cloud, go to app Settings → Secrets
   - Add your API key:
   ```toml
   ANTHROPIC_API_KEY = "sk-ant-your-key-here"
   ```

---

## 📊 Assessment Coverage

### Control Tower Assessment (42 Questions)
| Domain | Questions | Weight |
|--------|-----------|--------|
| Organizational Strategy | 4 | 12% |
| Account Factory & Provisioning | 4 | 10% |
| Guardrails & Preventive Controls | 4 | 15% |
| Detective Controls & Compliance | 4 | 12% |
| Identity & Access Management | 4 | 12% |
| Network Architecture | 4 | 10% |
| Logging & Monitoring | 3 | 10% |
| Cost Management | 3 | 8% |
| Backup & Disaster Recovery | 3 | 8% |
| Migration Readiness | 3 | 8% |
| Operational Readiness | 2 | 5% |

### Golden Architecture Assessment (22 Questions)
| Domain | Questions | Weight |
|--------|-----------|--------|
| Serverless Compute Strategy | 4 | 18% |
| API & Integration Layer | 4 | 15% |
| Serverless Security | 5 | 18% |
| Observability & Monitoring | 4 | 12% |
| CI/CD & DevOps | 3 | 12% |
| Cost Optimization | 2 | 10% |
| Resilience & Reliability | 3 | 15% |

---

## ✅ Bug Fixes in v3.0

1. **Fixed**: Questions now properly default to "Not Assessed"
   - Progress only counts questions you've actually answered
   - Selecting a question no longer marks all as answered

2. **Removed**: Unnecessary Docker/shell files
   - Only essential files for Streamlit Cloud deployment

3. **Enhanced**: Comprehensive question context
   - Each question includes detailed rationale
   - Explains why the question matters for enterprise readiness

---

## 🎨 Features

- **Professional Light Theme**: Clean enterprise design
- **64 Comprehensive Questions**: With detailed context for each
- **Well-Architected Alignment**: Questions mapped to AWS pillars
- **Industry Benchmarking**: Compare against 6 industry verticals
- **Gap Analysis**: Automatic prioritization by risk level
- **AI Analysis**: Claude-powered recommendations
- **Export Options**: Markdown reports and JSON data

---

## 💻 Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Optional: Set API key for AI features
export ANTHROPIC_API_KEY="your-key"

# Run locally
streamlit run streamlit_app.py
```

---

## 📝 License

Enterprise use. Contact for licensing details.
