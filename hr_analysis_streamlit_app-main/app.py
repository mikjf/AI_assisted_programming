# app.py
from __future__ import annotations
import pandas as pd
import streamlit as st
import os

from utils import load_data, save_data, append_row, ensure_schema, EXPECTED_COLUMNS
from plots import headcount_by_department, age_distribution, vacation_taken_by_department

st.set_page_config(page_title="HR Tool", layout="wide")
st.title("HR Tool")

tab1, tab2, tab3 = st.tabs(["📂 Data", "📊 Visualizations", "🤖 Chatbot (coming soon)"])

# ----------------------
# Tab 1: Data management
# ----------------------
with tab1:
    st.header("Upload or Manage Data")

    uploaded = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded is not None:
        df_up = pd.read_csv(uploaded)
        missing = set(EXPECTED_COLUMNS) - set(df_up.columns)
        if missing:
            st.warning(f"Uploaded file missing columns: {sorted(list(missing))}")
        df_up = ensure_schema(df_up)
        save_data(df_up)
        st.success("File uploaded and saved to data/hr_dataset.csv")

    df = load_data()

    if not df.empty:
        st.subheader("Current Data Preview")

        # ✅ Toggle between preview and full dataset
        show_all = st.checkbox("Show all rows", value=False)
        if show_all:
            st.dataframe(df, use_container_width=True)
        else:
            st.dataframe(df.head(20), use_container_width=True)

        st.caption(f"Rows: {len(df)}")

    st.subheader("➕ Add New Employee")
    with st.form("add_employee_form", clear_on_submit=True):
        c1, c2, c3 = st.columns(3)
        with c1:
            first_name = st.text_input("First Name")
            last_name  = st.text_input("Last Name")
            residence  = st.text_input("Residence (Canton)", value="Ticino")
            department = st.selectbox("Department", ["HR", "Production", "IT", "Finance", "Sales"])
        with c2:
            seniority  = st.selectbox("Seniority Level", ["Mid", "Senior"])
            age        = st.number_input("Age", min_value=18, max_value=70, value=35)
            workload   = st.selectbox("Workload (%)", [60, 70, 80, 90, 100])
            vac_total  = int(round(25 * (workload / 100)))
        with c3:
            hire_date  = st.date_input("Hire Date")
            vac_taken  = st.slider("Vacation Days Taken", 0, vac_total, 0)
            st.caption(f"Vacation entitlement at {workload}%: {vac_total} days")

        submitted = st.form_submit_button("Add Employee")
        if submitted:
            if not first_name or not last_name:
                st.error("First Name and Last Name are required.")
            else:
                new_row = {
                    "First Name": first_name,
                    "Last Name": last_name,
                    "Residence": residence,
                    "Age": int(age),
                    "Department": department,
                    "Seniority Level": seniority,
                    "Workload": int(workload),
                    "Vacation Days Total": int(vac_total),
                    "Vacation Days Taken": int(vac_taken),
                    "Hire Date": hire_date
                }
                df_out = append_row(new_row)
                st.success(f"Employee {first_name} {last_name} added. Total rows: {len(df_out)}")

# ----------------------
# Tab 2: Visualizations
# ----------------------
with tab2:
    st.header("HR Visualizations")
    df = load_data()

    if df.empty:
        st.warning("No data available. Upload or add employees in the Data tab.")
    else:
        # ✅ Sidebar filters with checkboxes
        st.sidebar.header("Filters")

        # Department filter
        dept_options = sorted(df["Department"].dropna().unique())
        selected_depts = []
        st.sidebar.subheader("Department")
        for dept in dept_options:
            if st.sidebar.checkbox(dept, value=True, key=f"dept_{dept}"):
                selected_depts.append(dept)

        # Seniority filter
        seniority_options = sorted(df["Seniority Level"].dropna().unique())
        selected_seniority = []
        st.sidebar.subheader("Seniority")
        for s in seniority_options:
            if st.sidebar.checkbox(s, value=True, key=f"seniority_{s}"):
                selected_seniority.append(s)

        # Apply filters
        dff = df.copy()
        if selected_depts:
            dff = dff[dff["Department"].isin(selected_depts)]
        if selected_seniority:
            dff = dff[dff["Seniority Level"].isin(selected_seniority)]

        # KPIs
        k1, k2, k3, k4 = st.columns(4)
        with k1:
            st.metric("Headcount", len(dff))
        with k2:
            st.metric("Avg Age", f"{dff['Age'].mean():.1f}" if len(dff) else "–")
        with k3:
            st.metric("Avg Vacation Taken", f"{dff['Vacation Days Taken'].mean():.1f}" if len(dff) else "–")
        with k4:
            st.metric("Avg Workload", f"{pd.to_numeric(dff['Workload'], errors='coerce').mean():.0f}%" if len(dff) else "–")

        # Charts
        st.subheader("Headcount by Department")
        st.plotly_chart(headcount_by_department(dff), use_container_width=True)

        st.subheader("Age Distribution")
        st.plotly_chart(age_distribution(dff), use_container_width=True)

        st.subheader("Vacation Days Taken by Department")
        st.plotly_chart(vacation_taken_by_department(dff), use_container_width=True)

# ----------------------
# ----------------------
def hr_assistant_tab():
    st.header("HR Assistant (RAG - Mock)")

    st.subheader("Step 1: Upload a PDF")
    uploaded_file = st.file_uploader("Choose a PDF file to analyze", type=["pdf"], key="rag_pdf")

    if uploaded_file:
        st.success(f"📄 Uploaded: {uploaded_file.name}")
        st.info("✅ PDF uploaded successfully. Text extraction and indexing will happen here later.")

        st.subheader("Step 2: (Mock) Ask a question")
        user_query = st.text_input("Type your question about the document")

        if st.button("Ask"):
            st.write("🤖 Mock Answer: This is where the chatbot will respond once OpenAI is connected.")
    else:
        st.warning("Please upload a PDF to continue.")

with tab3:
    hr_assistant_tab()
