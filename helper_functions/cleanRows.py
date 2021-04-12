
def clean_rows(row):
    row = row.lower().strip("[")
    row = row.strip("]")
    #row = row.strip('"')
    row = row.split(',')
    return row