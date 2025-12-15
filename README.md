# Leverage AI coding assistants to create a Streamlit app 

![alternative text](img/readme_image.jpg)

#### -- Project Status: [Completed]

## Objective

The HR Tool Demo is a small web-application (built with Streamlit) for HR-data analysis and simple employee management. The idea is to demonstrate how modern AI-assisted coding tools can accelerate software development. The project uses a synthetic Swiss HR dataset and showcases interactive visualisations and form-based data entry developed with minimal manual coding.

### Features

* Data generation & exploration: use ChatGPT to create a synthetic Swiss HR dataset and explore it in Colab with Gemini AI through descriptive statistics and Plotly visualizations
* Visualization & insights: build interactive Plotly charts to analyze workload, vacation usage, and seniority patterns across departments
* Streamlit app development: develop a modular Streamlit app (app.py, utils.py, plots.py) in GitHub Codespaces with ChatGPT, adding filtering and data management features
* Deployment & troubleshooting: set up the environment, install dependencies, and learn how to resolve common path and API issues as part of a full AI-assisted workflow
* AI-assisted development: leverage AI coding assistants (ChatGPT, GitHub Copilot, etc.) throughout the entire development process to accelerate prototyping and improve code quality

### Project structure

```bash
AI_assisted_programming/
│
├── data/
│   └── hr_dataset.csv
│
├── hr_analysis_streamlit_app/
│   ├── app.py
│   ├── plots.py
│   ├── utils.py
│   └── requirements.txt
│
├── .gitignore
├── hrtool_prompting_walkthrough.ipynb
├── prompting_types.md
└── README.md

```

### Technologies and packages

- ChatGPT
- Google Colab and Gemini
- GitHub Codespaces
- Python
- Pandas
- Plotly
- Streamlit
- Additional dependencies listed in `requirements.txt`

### Sources

- Inspired by the AI-Assisted Programming Workshop at [Constructor Nexademy](https://nexademy.org/)
