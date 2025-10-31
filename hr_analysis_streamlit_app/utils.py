# utils.py
from __future__ import annotations
import os
from typing import List
import pandas as pd

# Get the directory where this utils.py file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Go up one level and then into data folder
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "hr_dataset.csv")

EXPECTED_COLUMNS: List[str] = [
    "First Name", "Last Name", "Residence", "Age", "Department",
    "Seniority Level", "Workload", "Vacation Days Total",
    "Vacation Days Taken", "Hire Date"
]

def ensure_schema(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize column names/types so the app stays stable.
    - Enforce expected columns (add missing ones when possible)
    - Coerce types (Hire Date -> date, Workload -> int)
    """
    df = df.copy()

    # Ensure all expected columns exist
    for col in EXPECTED_COLUMNS:
        if col not in df.columns:
            # Create reasonable defaults if missing
            if col in ("Vacation Days Total", "Vacation Days Taken", "Age"):
                df[col] = pd.NA
            elif col == "Hire Date":
                df[col] = pd.NaT
            else:
                df[col] = ""

    # Reorder columns
    df = df[EXPECTED_COLUMNS]

    # Coerce Hire Date
    df["Hire Date"] = pd.to_datetime(df["Hire Date"], errors="coerce").dt.date

    # Coerce numeric
    for c in ["Age", "Vacation Days Total", "Vacation Days Taken"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    # Workload: accept "80%" or 80 -> store as int 80 in memory
    df["Workload"] = (
        df["Workload"]
        .astype(str)
        .str.replace("%", "", regex=False)
    )
    df["Workload"] = pd.to_numeric(df["Workload"], errors="coerce").fillna(0).astype(int)

    # Fill NA basics
    df["Residence"] = df["Residence"].fillna("")
    df["Department"] = df["Department"].fillna("")
    df["Seniority Level"] = df["Seniority Level"].fillna("")

    return df

def load_data() -> pd.DataFrame:
    if not os.path.exists(DATA_PATH):
        return pd.DataFrame(columns=EXPECTED_COLUMNS)
    df = pd.read_csv(DATA_PATH)
    return ensure_schema(df)

def save_data(df: pd.DataFrame) -> None:
    """Persist to CSV, formatting Workload as 'NN%' for readability."""
    df = ensure_schema(df)
    out = df.copy()
    out["Workload"] = out["Workload"].astype(int).astype(str) + "%"
    out.to_csv(DATA_PATH, index=False)

def append_row(new_row: pd.Series | dict) -> pd.DataFrame:
    base = load_data()
    new_df = pd.concat([base, pd.DataFrame([new_row])], ignore_index=True)
    new_df = ensure_schema(new_df)
    save_data(new_df)
    return new_df
