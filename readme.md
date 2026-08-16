# Final Sales Automation Project

A Python-based business automation project that reads multiple Excel sales files, validates and processes the data, generates reports, and eventually sends the report to a client through email.

This project is being built step-by-step to simulate a real-world company automation workflow.

---

# Project Goal

The final automation workflow will be:

Excel Files
    ↓
Read Excel Data
    ↓
Validate & Clean Data
    ↓
Process Sales Data
    ↓
Generate Excel Report
    ↓
Generate PDF Report
    ↓
Send Report via Email
    ↓
Log Automation Result

---

# Technologies Used

- Python
- openpyxl
- pathlib
- smtplib
- email
- python-dotenv
- ReportLab
- logging

---

# Project Structure

```text
final_automation/
│
├── input/
│   ├── sales_january.xlsx
│   ├── sales_february.xlsx
│   └── sales_march.xlsx
│
├── output/
│
├── logs/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── excel_reader.py
│   └── data_processor.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md



After Part 3, the project works like this:

                  Excel Files
                       │
                       ▼
               excel_reader.py
                       │
                       ▼
                Raw Data
                       │
                       ▼
              data_processor.py
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
      Validation   Duplicates   Calculations
          │            │            │
          └────────────┼────────────┘
                       ▼
                Processed Data
                       │
                       ▼
                    main.py



                    