# A few prompting techniques

This file documents practical AI prompt styles that can be used. Each style includes a sample prompt.

---

## Persona / role-based prompting

Prompt
```bash
You are a senior data engineer.
I’ve uploaded a CSV with HR data (first name, department, workload, vacation days, hire date). 
Help me build 3 useful Plotly visualizations for a Streamlit dashboard.
```
Use case:
tailors tone and suggestions to a specific expert role, encouraging more focused and relevant answers.

## Few-shot prompting

Prompt
```bash
Here are two visualizations I already used:  
- Bar chart: average vacation days per department  
- Histogram: age distribution of employees
Now suggest and code a third chart, following the same format,
ideally showing something about workload.
```
Use case: guides the AI by providing examples. Useful for expanding sets of similar tasks like visualizations or functions.

## Structured output prompting

Prompt
```bash
I want to add a new tab to my Streamlit HR app to track upcoming retirements.  
Please respond with:  
- Goal  
- Required Inputs  
- Data Filtering Logic  
- Streamlit Components Needed  
- Bonus Features if time allows
```
Use case: generates a clear development plan. Helps organize and scope tasks.

## Dialogue-based prompting

Prompt
```bash
I want to build a dashboard for HR managers with better filters and charts.  
Before giving code, ask me a few questions to better understand the target 
users and what data views they’d need.
```
Use case: promotes better alignment by encouraging the AI to clarify the goal before answering.

## Chain-of-thought prompting

Prompt
```bash
I want to add a feature that flags employees with low remaining vacation days.  
Walk through how to calculate that logic step-by-step before writing any code.
```
Use case: useful when logic or formulas are needed. The AI reasons step-by-step instead of jumping to code.

## Meta prompting

Prompt
```bash
Whenever I write a vague prompt like “help improve the HR dashboard,” 
suggest a clearer version before answering.
```
Example AI response: "A better prompt might be: Suggest 3 specific improvements to the HR dashboard, based on employee workload data."

Use case: helps users improve their prompting habits and results.

## Prompt debugging / interpretation

Prompt
```bash
I asked for a pie chart of workload distribution, but the chart looks wrong.  
Explain what assumptions you made from my prompt, and how I could phrase it better for accuracy.
```
Use case: useful when logic or formulas are needed. The AI reasons step-by-step instead of jumping to code.
