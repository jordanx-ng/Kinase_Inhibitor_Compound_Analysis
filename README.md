# Compound Screening Insights – Kinase Target Analysis

## Overview
This project analyzes bioactivity data from ChEMBL to compare
high-potency kinase inhibitors against weaker or non-kinase compounds.
It demonstrates how early-stage compound screening data can be used
to derive pharmacologically relevant insights.

## Dataset
- Source: ChEMBL (via Kaggle)
- Target Type: Single Protein Kinase
- Activity Measure: IC50 (nM)

## Methods
- Data cleaning and filtering using pandas
- IC50 → pIC50 conversion
- Classification of compounds based on pharmacological thresholds
- Visualizing potency trends using seaborn and matplotlib

## Key Findings
- High-potency kinase inhibitors (IC50 ≤ 1 µM) show stronger activity
  than weak or non-kinase compounds
- Potent inhibitors also exhibit higher ligand efficiency, indicating
  favorable binding properties

## Relevance to Pharma
This workflow mimics early-stage decision-making in drug discovery,
helping to prioritize compounds for further development.

## Tools
- Python, pandas, seaborn, matplotlib

## How to Use
1. Clone the repository
2. Load `kinase.csv` into Jupyter Notebook
3. Run the analysis cells to reproduce plots and interpretations
