# Solar Challenge Week 1

## 🌞 Overview

This repository contains the code, notebooks, and configuration files for the Solar Challenge - Week 1. The project aims to analyze and compare solar energy data across three countries: Benin, Sierra Leone, and Togo. We cover repository setup, data profiling, EDA, and cross-country analysis.

---

## 🛠️ Task 1: Git & Environment Setup

### ✅ Objective

Establish version control and set up a standardized Python environment for all contributors.

### 📦 Repository Initialization

1. Create GitHub repo: `solar-challenge-week1`
2. Clone locally and set up Python virtual environment using `venv` or `conda`.

### 🌿 Branching Strategy

- Branch: `setup-task`
- Minimum 3 commits:
  - `init: add .gitignore`
  - `chore: venv setup`
  - `ci: add GitHub Actions workflow`

### 📁 File Checklist

- `.gitignore` (includes `data/`, `.csv`, `.ipynb_checkpoints/`)
- `requirements.txt` (with core packages)
- GitHub Actions workflow: `.github/workflows/ci.yml`

### ⚙️ Basic CI Workflow

Runs:

```bash
python --version
pip install -r requirements.txt

## 📊 Task 2: Data Profiling, Cleaning & Exploratory Data Analysis (EDA)

### 🎯 Objective

Profile, clean, and explore each country’s solar dataset end-to-end so it’s ready for comparison and region-ranking tasks.

---

### 🔀 Branch Naming Convention

- Create a branch for each country’s analysis:
  - `eda-benin`
  - `eda-sierra-leone`
  - `eda-togo`

---

### 📓 Notebook Structure

Create one notebook per country:
- `benin_eda.ipynb`
- `sierra_leone_eda.ipynb`
- `togo_eda.ipynb`

---

### 🧼 Data Profiling & Cleaning Checklist

#### 1. **Summary Statistics & Missing Values**
- Use:
  ```python
  df.describe()
  df.isna().sum()
