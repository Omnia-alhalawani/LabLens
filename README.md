# 🔬 LabLens  
> Serverless AI ecosystem for clinical lab report interpretation — powered by AWS & Google Gemini

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Online-brightgreen)](http://lablens-final-app.s3-website.eu-north-1.amazonaws.com/)
![AWS](https://img.shields.io/badge/AWS-Lambda%20%7C%20S3%20%7C%20API%20Gateway-orange)
![AI](https://img.shields.io/badge/AI-Gemini%202.5%20Flash-blue)
![Language](https://img.shields.io/badge/Language-Arabic%20NLP-lightgrey)

---
##  Overview

**LabLens** is a fully serverless, multi-cloud AI web application that interprets clinical laboratory reports. Users upload a photo or PDF of their lab results and receive a simplified Arabic explanation with clear 🟢 Normal / 🔴 Abnormal indicators — no medical background required.

---

## Features

-  Upload lab reports as **JPG, PNG, or PDF**
-  AI-powered analysis via **Google Gemini 2.5 Flash** (multimodal vision)
-  Results explained in **simple Arabic**
-  **Serverless architecture** — zero idle cost
-  **Secure** — API keys stored in environment variables, never in code

---

##  Architecture

```
User (Browser)
     │
     ▼
Amazon S3  ──────────────────────────────►  Static Frontend (index.html)
     │
     ▼
AWS API Gateway  (REST API)
     │
     ▼
AWS Lambda  (Python 3.12)
     │
     ▼
Google Gemini 2.5 Flash API  ──►  Arabic Medical Analysis
```

---

##  Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5 |
| Hosting | Amazon S3 (Static Website) |
| API Layer | AWS API Gateway (REST) |
| Backend | AWS Lambda (Python 3.12) |
| AI Model | Google Gemini 2.5 Flash |
| Region | eu-north-1 (Stockholm) |



---

##  Deployment Guide

### Prerequisites
- AWS Account
- Google AI Studio account (for Gemini API key)

### 1. Deploy the Frontend (S3)
1. Go to **AWS S3** → Create bucket → Enable **Static Website Hosting**
2. Upload `frontend/index.html`
3. Set bucket policy to **public read**

### 2. Deploy the Backend (Lambda)
1. Go to **AWS Lambda** → Create function → Runtime: **Python 3.12**
2. Upload `backend/lambda_function.py`
3. Add **Environment Variable**:
   - Key: `GEMINI_API_KEY`
   - Value: *(your Google Gemini API key)*

### 3. Create the API (API Gateway)
1. Go to **AWS API Gateway** → Create REST API
2. Add resource `/analyze` → Method: **POST**
3. Connect to your Lambda function
4. Enable **CORS**
5. Deploy to a stage (e.g., `prod`)
6. Copy the Invoke URL → paste into `INVOKE_URL` in `index.html`

---

##  Security Notes

-  API key stored in **Lambda Environment Variables** — never in source code
-  IAM role uses **least privilege** (only required permissions)
-  All traffic encrypted via **TLS 1.3**
-  This app is for **educational purposes only** — not a medical device

---

##  Cost Estimate

| Architecture | Monthly Cost (1,000 users) |
|-------------|---------------------------|
| Traditional (EC2) | ~$72.00 |
| LabLens (Serverless) | ~$0.20 |

> **99.7% cost reduction** using pay-per-use serverless model.

---

##  Roadmap

- [ ] Amazon Textract — better extraction from handwritten reports
- [ ] AWS Secrets Manager — automated API key rotation
- [ ] Amazon CloudFront — global CDN for lower latency
- [ ] CloudWatch Dashboards — real-time monitoring
- [ ] Support for more file types

---

##  Disclaimer

LabLens is for **educational and informational purposes only**. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider.

---

##  Author

**Omnia Mohamed Elhalawani**

---


