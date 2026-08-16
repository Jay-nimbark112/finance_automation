import os

from pathlib import Path

from dotenv import load_dotenv


# ==========================================
# BASE DIRECTORY
# ==========================================

BASE_DIR = Path(
    __file__
).resolve().parent.parent


# ==========================================
# ENVIRONMENT
# ==========================================

ENV_FILE = BASE_DIR / ".env"

load_dotenv(
    ENV_FILE
)


# ==========================================
# FOLDERS
# ==========================================

INPUT_FOLDER = (
    BASE_DIR / "input"
)

OUTPUT_FOLDER = (
    BASE_DIR / "output"
)

LOG_FOLDER = (
    BASE_DIR / "logs"
)


# ==========================================
# REPORT FILES
# ==========================================

EXCEL_REPORT = (
    OUTPUT_FOLDER /
    "sales_report.xlsx"
)

PDF_REPORT = (
    OUTPUT_FOLDER /
    "sales_report.pdf"
)


# ==========================================
# EMAIL
# ==========================================

EMAIL_ADDRESS = os.getenv(
    "EMAIL_ADDRESS"
)

EMAIL_PASSWORD = os.getenv(
    "EMAIL_PASSWORD"
)

RECEIVER_EMAIL = os.getenv(
    "RECEIVER_EMAIL"
)


# ==========================================
# SMTP
# ==========================================

SMTP_SERVER = (
    "smtp.gmail.com"
)

SMTP_PORT = 587