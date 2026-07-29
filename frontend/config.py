import os

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://127.0.0.1:8000"
)

LOGIN_URL = f"{BACKEND_URL}/api/v1/auth/login"
REGISTER_URL = f"{BACKEND_URL}/api/v1/auth/register"

ACCOUNT_URL = f"{BACKEND_URL}/api/v1/accounts"
CATEGORY_URL = f"{BACKEND_URL}/api/v1/categories"
TRANSACTION_URL = f"{BACKEND_URL}/api/v1/transactions"
BUDGET_URL = f"{BACKEND_URL}/api/v1/budgets"

SPENDING_URL = f"{BACKEND_URL}/api/v1/analytics/spending"
HEALTH_URL = f"{BACKEND_URL}/api/v1/analytics/financial-health"

COPILOT_URL = f"{BACKEND_URL}/api/v1/copilot/chat"

INVESTMENT_URL = f"{BACKEND_URL}/api/v1/investment/recommendation"

REPORT_URL = f"{BACKEND_URL}/api/v1/report/generate"
DOWNLOAD_REPORT_URL = f"{BACKEND_URL}/api/v1/report/download"