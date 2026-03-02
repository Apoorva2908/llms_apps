'''This file is used to read tables and store the table in dictionary format
-Apoorva S Shekhawat
'''

import camelot

def extract_tables(pdf_path):
    tables = camelot.read_pdf(pdf_path, pages = "all")
    table_dict = {}

    for i, table in enumerate(tables):
        table_dict[f"table_{i}"] = table.df.to_dict()
    
    return table_dict