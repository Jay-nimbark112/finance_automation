import streamlit as st
from pathlib import Path
import sys
import shutil


# ==========================================
# PROJECT PATH
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

SRC_DIR = BASE_DIR / "src"

INPUT_FOLDER = BASE_DIR / "input"


sys.path.append(
    str(SRC_DIR)
)


# ==========================================
# IMPORT AUTOMATION
# ==========================================

from main import main


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Finance Automation",
    page_icon="💰",
    layout="wide"
)


# ==========================================
# HEADER
# ==========================================

st.title(
    "💰 Finance Automation Dashboard"
)

st.write(
    "Upload sales files and run the complete "
    "finance reporting automation."
)


st.divider()


# ==========================================
# FILE UPLOAD
# ==========================================

st.subheader(
    "📁 Upload Sales Files"
)

uploaded_files = st.file_uploader(
    "Select Excel files",
    type=["xlsx", "xlsm"],
    accept_multiple_files=True
)


# ==========================================
# SHOW FILES
# ==========================================

if uploaded_files:

    st.success(
        f"{len(uploaded_files)} file(s) selected"
    )

    for file in uploaded_files:

        st.write(
            f"📄 {file.name}"
        )


st.divider()


# ==========================================
# RUN AUTOMATION
# ==========================================

st.subheader(
    "⚙️ Automation"
)


run_button = st.button(
    "🚀 Run Automation",
    type="primary",
    use_container_width=True
)


if run_button:

    if not uploaded_files:

        st.error(
            "Please upload at least one Excel file."
        )

    else:

        try:

            # ==================================
            # SAVE UPLOADED FILES
            # ==================================

            INPUT_FOLDER.mkdir(
                exist_ok=True
            )

            for file in uploaded_files:

                file_path = (
                    INPUT_FOLDER /
                    file.name
                )

                with open(
                    file_path,
                    "wb"
                ) as output:

                    output.write(
                        file.getbuffer()
                    )


            # ==================================
            # RUN AUTOMATION
            # ==================================

            with st.spinner(
                "Running finance automation..."
            ):

                result = main()


            # ==================================
            # SUCCESS
            # ==================================

            if result["success"]:

                st.success(
                    "✅ Automation completed successfully!"
                )


                # ==============================
                # SUMMARY
                # ==============================

                summary = result["summary"]


                st.subheader(
                    "📊 Automation Summary"
                )


                col1, col2, col3, col4 = st.columns(4)


                col1.metric(
                    "Total Records",
                    summary.get(
                        "total_records",
                        0
                    )
                )


                col2.metric(
                    "Total Quantity",
                    summary.get(
                        "total_quantity",
                        0
                    )
                )


                col3.metric(
                    "Total Revenue",
                    f"₹{summary.get('total_revenue', 0):,.2f}"
                )


                col4.metric(
                    "Employees",
                    summary.get(
                        "number_of_employees",
                        0
                    )
                )


                st.divider()


                # ==============================
                # REPORTS
                # ==============================

                st.subheader(
                    "📥 Generated Reports"
                )


                excel_file = Path(
                    result["excel_file"]
                )

                pdf_file = Path(
                    result["pdf_file"]
                )


                col1, col2 = st.columns(2)


                with col1:

                    if excel_file.exists():

                        with open(
                            excel_file,
                            "rb"
                        ) as file:

                            st.download_button(
                                label="📊 Download Excel Report",
                                data=file,
                                file_name=excel_file.name,
                                mime=(
                                    "application/"
                                    "vnd.openxmlformats-officedocument"
                                    ".spreadsheetml.sheet"
                                ),
                                use_container_width=True
                            )


                with col2:

                    if pdf_file.exists():

                        with open(
                            pdf_file,
                            "rb"
                        ) as file:

                            st.download_button(
                                label="📄 Download PDF Report",
                                data=file,
                                file_name=pdf_file.name,
                                mime="application/pdf",
                                use_container_width=True
                            )


                # ==============================
                # EMPLOYEE SUMMARY
                # ==============================

                st.subheader(
                    "👨‍💼 Employee Summary"
                )


                employees = result[
                    "employees"
                ]


                for employee, values in employees.items():

                    st.write(
                        f"**{employee}**"
                    )

                    st.write(
                        f"Sales: ₹{values['total_sales']:,.2f} | "
                        f"Quantity: {values['total_quantity']} | "
                        f"Orders: {values['number_of_orders']}"
                    )


            # ==================================
            # FAILURE
            # ==================================

            else:

                st.error(
                    "❌ Automation failed"
                )

                st.error(
                    result.get(
                        "error",
                        "Unknown error"
                    )
                )


        except Exception as e:

            st.error(
                "❌ Dashboard error"
            )

            st.exception(e)