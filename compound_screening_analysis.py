import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
if not os.path.exists("plots"):   #create a plots folder if it doesnt exist
    os.makedirs("plots")


df = pd.read_csv("compound_data.csv", sep=";")
df.head()  # Display the first 5 rows of the dataframe just to get an idea of the data

df = df[df["Standard Type"] == "IC50"] #renaming

df["Standard Value"] = pd.to_numeric(df["Standard Value"], errors="coerce") #removes non-numeric unusuable IC50 values
df = df.dropna(subset=["Standard Value"])

df["pIC50"] = -np.log10(df["Standard Value"] * 1e-9)  # Convert IC50 from nM to M and calculate pIC50 to make plots and interpretation easier
df = df.dropna(subset=["pIC50"])   #drop any rows where pIC50 could not be calculated
#higher pIC50 means more potent

# I researched that below 1000 nM is considered an active kinase inhibitor and above that is weak or non-kinase inhibitor,so im using 1000 nM as cutoff
df["compound_class"] = np.where(
    df["Standard Value"] <= 1000,
    "Kinase inhibitors (high potency)",
    "Non-kinase / weak inhibitors"
)

#df["Standard Value"] <= 1000 compares each IC50 value to 1000nM and returns a true/false value
#np.where(condition, value_if_true, value_if_false)
#If true, assigns "Kinase inhibitors (high potency)" to compound_class column, else assigns "Non-kinase / weak inhibitors"
#so now, [compound_class] column has two categories based on potency (kinase inhibitors and non-kinase/weak inhibitors)

grouped = df.groupby("compound_class")["pIC50"].mean()


plt.figure(figsize=(6,4))   #creates an empty figure canvas 6 inches wide(width) and 4 inches tall(height)
plt.bar(grouped.index, grouped.values)
plt.ylabel("Mean pIC50")
plt.title("Potency Comparison by Compound Class")
plt.xticks(rotation=15) #rotate x-axis labels by 15 degrees for better readability
plt.tight_layout() #removes any extra white spacing around the plot
plt.savefig("plots/potency_barplot.png")
plt.show()

df.boxplot(column="pIC50", by="compound_class")
plt.title("Distribution of Potency by Compound Class")
plt.suptitle("")  # removes automatic title which is pIC50 by compound_class since we added our own title
plt.ylabel("pIC50")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("plots/potency_boxplot.png")
plt.show()

le_means = df.groupby("compound_class")["Ligand Efficiency LE"].mean()
print(le_means)

plt.figure(figsize=(6,4))
plt.bar(le_means.index, le_means.values)
plt.ylabel("Mean Ligand Efficiency (LE)")
plt.title("Average Ligand Efficiency by Compound Class")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("plots/ligand_efficiency_barplot.png")
plt.show()

# Create a cleaned dataframe with selected columns for sharing or further analysis
clean_df = df.copy()
clean_df = clean_df[
    [
        "Molecule ChEMBL ID",
        "Molecule Name",
        "Smiles",
        "Standard Value",
        "Standard Units",
        "pIC50",
        "compound_class",
        "Target Name"
    ]
]
clean_df.columns
clean_df.to_csv(
    "cleaned_kinase_activity.csv",
    index=False
)
