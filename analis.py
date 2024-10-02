import pandas as pd

# Load the Excel file
file_path = '/path/to/your/dataKasus-1.xlsx'
xls = pd.ExcelFile(file_path)

# Load the sheet named '2022'
df = pd.read_excel(xls, sheet_name='2022')

# Filter data to identify those with and without hypertension
hipertensi_yes = df[df['RIW HIPERTENSI'] == 'Ya']
hipertensi_no = df[df['RIW HIPERTENSI'] == 'Tidak']

# Filter data to separate PE and Non-PE cases
pe_cases = df[df['PE/Non PE'] == 'PE']
non_pe_cases = df[df['PE/Non PE'] == 'Non PE']

# Summarize the counts of each group
summary = {
    'Hypertension Yes': len(hipertensi_yes),
    'Hypertension No': len(hipertensi_no),
    'PE Cases': len(pe_cases),
    'Non-PE Cases': len(non_pe_cases)
}

# Display the summary
print("Summary of Cases:")
print(summary)
