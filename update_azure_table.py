import time
import unicodedata
import pandas as pd
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity

import json

class ExcelToAzure:
    """
    A class that handles updating an Azure table with data from an Excel file.
    """

    def __init__(self, account_name, account_key, table_name):
        """
        Initializes an instance of the ExcelToAzure class.

        Args:
            account_name (str): The name of the Azure storage account.
            account_key (str): The access key for the Azure storage account.
            table_name (str): The name of the Azure table.
        """
        self.table_service = TableService(account_name, account_key)
        self.table_name = table_name

    def create_table(self):
        """
        Creates a new Azure table or deletes all entities in an existing table.
        """
        if self.table_service.exists(self.table_name):
            self.delete_all_entities()
        else:
            self.table_service.create_table(self.table_name)

    def delete_all_entities(self):
        """
        Deletes all entities in the Azure table.
        """
        entities = self.table_service.query_entities(self.table_name)
        for entity in entities:
            self.table_service.delete_entity(self.table_name, entity['PartitionKey'], entity['RowKey'])

    def sanitize_column_name(self, column_name):
        """
        Sanitizes a column name by removing control characters, prepending an underscore if the first character is numeric, and truncating to 255 characters.

        Args:
            column_name (str): The column name to sanitize.

        Returns:
            str: The sanitized column name.
        """
        # Remove control characters
        column_name = ''.join(ch for ch in column_name if unicodedata.category(ch)[0]!="C")
        # If the first character is numeric, prepend an underscore
        if column_name[0].isdigit():
            column_name = '_' + column_name
        # Truncate to 255 characters
        column_name = column_name[:255]
        return column_name

    def update_table(self, excel_file):
        """
        Updates the Azure table with data from an Excel file.

        Args:
            excel_file (str): The path to the Excel file.
        """
        df = pd.read_excel(excel_file)
        for i, row in df.iterrows():
            entity = Entity()
            entity.PartitionKey = str(i)
            entity.RowKey = str(i)
            
            for column in df.columns[0:]:
                sanitized_column_name = self.sanitize_column_name(column)
                value = row[column]
                if pd.api.types.is_integer_dtype(df[column]):
                    value = int(value)
                entity[sanitized_column_name] = value
            
            self.table_service.insert_or_replace_entity(self.table_name, entity)

def read_settings():
    try:
        with open('settings.json') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Settings.json file not found. Creating new settings...")
        data = {}
        data['account_name'] = input("Enter the Azure storage account name: ")
        data['account_key'] = input("Enter the Azure storage account key: ")
        data['table_name'] = input("Enter the Azure table name: ")
        
        with open('settings.json', 'w') as f:
            json.dump(data, f)

    return data

settings = read_settings()

excel_to_azure = ExcelToAzure(settings['account_name'], settings['account_key'], settings['table_name'])

excel_to_azure.create_table()

excel_to_azure.update_table('data.xlsx')