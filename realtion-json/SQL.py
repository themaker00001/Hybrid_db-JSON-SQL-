import sqlparse
from Storage import Storage
from Catalog import Catalog
import json 
def parse_values(values_str):
    # remove outer parentheses
        values_str = values_str.strip().lstrip("(").rstrip(")")
        parts = []
        for v in values_str.split(","):
            v = v.strip()
            if v.startswith("'") and v.endswith("'"):   # quoted string
                parts.append(v.strip("'"))
            elif v.startswith("{") and v.endswith("}"): # JSON literal
                parts.append(json.loads(v))
            else:  # number or other literal
                try:
                    parts.append(int(v))
                except ValueError:
                    parts.append(v)
        return parts
class SQLEngine:
    def __init__(self):
        self.catalog=Catalog()
        self.storage=Storage()
    
    def execute(self,query):
        stmt=sqlparse.parse(query)[0] # taking in the first line of the query 
        tokens=[t.value for t in stmt.tokens if not t.is_whitespace] # just gettting the value from the tokens without the whitespace 
        
        #creating the table statement -> CREATE TABLE sample (id,name,email)
        if tokens[0].upper()=="CREATE":
            table=tokens[2] ## we are making a assumption that every 3 token is the name of the table
            cols=tokens[3].strip("()").split(",") # getting the col name  removing the parathesis ,  and breaking the columns name into list 
            cols=[c.strip().split()[0] for c in cols] # removing the whitespace and just grabbing the column name  id INT -> id 
            self.catalog.create_table(table,cols) # registering the table and column in catalog 
            print(f"Table {table} created  with columns {cols}")
        elif tokens[0].upper()=="INSERT":
            table=tokens[2]
            values=query.split("VALUES")[1]
            row=parse_values(values)
            #this just look complex start reading it from the back 
            # we are just spliting on , into individual piece and ilterate 
            #just changed the code over here got the parse_value function which is handling the pasring of the value 
            self.storage.insert(table,row)
            print(f"inserted the row{row} into the table:{table}")
        elif tokens[0].upper()=="SELECT":
            table= tokens[-1]
            rows = self.storage.scan(table)
            return rows  
          
        