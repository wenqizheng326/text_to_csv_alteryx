# from ayx import Alteryx
import re 
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

text_file = os.getenv('INPUT_FILE')
csv_file = os.getenv('OUTPUT_FILE')

with open(text_file, 'r') as file:
    lines = file.readlines()
    
table_lines = []

for line in lines:
    line = line.strip()
    if "\t" in line:
        line = re.sub(r"[ ]{2,}", "\t", line)
        line = re.sub(r"\t", ",", line)
    if re.search(r"[ ]{2,}", line):
        line = re.sub(r"[ ]{2,}", ",", line)
    table_lines.append(line)
    
# print(table_lines)

header = table_lines[0].split(",")
data_rows = [row.split(",") for row in table_lines[:]]
df = pd.DataFrame(data_rows)
# df.to_csv(csv_file)
# Alteryx.write(df,1)