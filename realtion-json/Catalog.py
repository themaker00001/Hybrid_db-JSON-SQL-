class Catalog:
    '''this is schema register which is checking the schema is good or not
    checking the table name and their columns definition'''
    def __init__(self):
        '''we are just making an empty dictonary which will have the Key as table name
        value as the rows inside the table(columns names and its definition)'''
        self.tables={}
    def create_table(self,name,columns):
        '''Adds a new table to the catalog.
        -> name as in the name of the table 
        columns like list  representing the schema'''
        self.tables[name]=columns
    def schema(self,name):
        '''
        reterive the schema of the table by the help of the table name 4
                catalog = Catalog()
                catalog.create_table("products", ["id", "name", "price"])
                print(catalog.get_schema("products"))
                # Output: ['id', 'name', 'price']
        '''
        self.tables.get(name)
    