# 💰 AI Financial Copilot

> AI-Powered Personal Finance Management Platform

An intelligent personal finance management platform built using **FastAPI**, **Streamlit**, **SQLite**, **JWT Authentication**, and **Google Gemini AI**. The application enables users to manage accounts, track income & expenses, create budgets, analyze financial health, interact with an AI financial advisor, and generate downloadable AI-powered financial reports.

---

# 👨‍💻 Project Information

**Project Name**

AI Financial Copilot

**Developed By**

**Kalyana Sundar**

**AI Engineer**

---

# 📖 Project Overview

AI Financial Copilot is a full-stack AI-powered finance management application that helps users organize their personal finances from a single dashboard.

The system combines traditional financial management with Artificial Intelligence to provide:

- Smart financial insights
- Personalized financial recommendations
- AI-powered financial chatbot
- Automatic financial report generation
- PDF report download

The project demonstrates the integration of FastAPI REST APIs, JWT Authentication, Streamlit UI, SQLAlchemy ORM, SQLite Database, and Google Gemini AI.

---

# 🚀 Key Features

## Authentication

- Secure JWT Login
- Password Hashing
- Token Authentication

---

## Account Management

- Create Accounts
- View Accounts
- Multiple Account Types
- Balance Tracking

---

## Transaction Management

- Add Income
- Add Expenses
- Category Wise Transactions
- Transaction History

---

## Budget Management

- Create Monthly Budgets
- Category Based Budgets
- Budget Tracking

---

## Financial Analytics

- Income Summary
- Expense Summary
- Net Balance
- Financial Health Score
- Expense Category Analysis

---

## AI Financial Copilot

Powered by **Google Gemini AI**

Ask questions like:

- How can I save money?
- Where am I spending too much?
- Investment advice
- Retirement planning
- Budget suggestions
- Emergency fund planning

---

## AI Financial Report

Generate a professional financial report including:

- Executive Summary
- Financial Health
- Income vs Expense
- Savings Analysis
- Budget Analysis
- Investment Recommendations
- Risk Analysis
- Emergency Fund
- Retirement Planning
- Final Recommendations

---

## PDF Report

Download the generated report as PDF.

---

# 🏗 System Architecture

```
                Streamlit Frontend
                        │
                        │
                REST API Requests
                        │
                 FastAPI Backend
                        │
      ┌─────────────────┼─────────────────┐
      │                 │                 │
 SQLite Database   Google Gemini AI   Report Generator
      │                 │                 │
 SQLAlchemy ORM     AI Insights      PDF Reports
```

---

# 🛠 Technology Stack

## Frontend

- Streamlit

## Backend

- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic

## Database

- SQLite

## Authentication

- JWT
- Passlib

## Artificial Intelligence

- Google Gemini AI

## PDF

- ReportLab

## Language

- Python 3.12+

---

# 📂 Project Structure

```
AI_Financial_Copilot/

backend/
    app/
        api/
        auth/
        models/
        routers/
        schemas/
        services/

frontend/
    pages/
    app.py

reports/

requirements.txt

README.md
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone <repository-url>

cd AI_Financial_Copilot
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

Example:

```env
GOOGLE_API_KEY=YOUR_GOOGLE_GEMINI_API_KEY

SECRET_KEY=YOUR_SECRET_KEY

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60

DATABASE_URL=sqlite:///financial.db
```

---

# ▶ Running Backend

```bash
uvicorn backend.app.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger API

```
http://127.0.0.1:8000/docs
```

---

# ▶ Running Frontend

```bash
streamlit run frontend/app.py
```

Frontend

```
http://localhost:8501
```

---

# 🔐 Demo Login

Email

```
sundar@example.com
```

Password

```
Password123
```

---

# 📚 API Endpoints

## Authentication

```
POST /api/v1/auth/register

POST /api/v1/auth/login

GET /api/v1/auth/me
```

---

## Accounts

```
GET /api/v1/accounts

POST /api/v1/accounts
```

---

## Categories

```
GET /api/v1/categories

POST /api/v1/categories
```

---

## Transactions

```
GET /api/v1/transactions

POST /api/v1/transactions
```

---

## Budgets

```
GET /api/v1/budgets

POST /api/v1/budgets
```

---

## Analytics

```
GET /api/v1/analytics/spending

GET /api/v1/analytics/financial-health
```

---

## AI Copilot

```
POST /api/v1/copilot/chat
```

---

## AI Report

```
GET /api/v1/report/generate

GET /api/v1/report/download
```

---

## Investment

```
GET /api/v1/investment/recommendation
```

---

## AI Insights

```
GET /api/v1/insights
```

---

# 📋 How To Use

### Step 1

Login using the demo account.

### Step 2

Create a financial account.

### Step 3

Add income and expense transactions.

### Step 4

Create monthly budgets.

### Step 5

View analytics and financial health.

### Step 6

Ask financial questions using the AI Copilot.

### Step 7

Generate an AI Financial Report.

### Step 8

Download the report as a PDF.

---

# 🌟 Project Highlights

- Secure Authentication
- RESTful APIs
- AI Financial Assistant
- Financial Health Analysis
- Smart Recommendations
- PDF Report Generation
- Clean Streamlit Dashboard
- Recruiter-Friendly Full Stack AI Project

---

# 🔮 Future Enhancements

- PostgreSQL/MySQL Support
- Email Reports
- Expense Charts
- OCR Bill Scanner
- Voice AI Assistant
- Multi-user Dashboard
- Cloud Deployment
- Docker Support

---

# 👨‍💻 Developer

**Kalyana Sundar**

**AI Engineer**

GitHub:
https://github.com/sundar66kalyan

LinkedIn:
(Add your LinkedIn URL)

---

# ⭐ If you found this project useful, please consider giving it a Star.