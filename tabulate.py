import pandas as pd

input_path = "D:\CFTR\clinvar_result_final.txt"
output_path = "D:\CFTR\clinvar_result_final_tabulated.xlsx"

# Read as tab-separated, keep everything as string to avoid any implicit conversions
df = pd.read_csv(input_path, sep="\t", dtype=str, keep_default_na=False)

# Write to Excel
df.to_excel(output_path, index=False)

output_path