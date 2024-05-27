# Excel to Azure Table Updater

This project contains a Python script that updates an Azure table with data from an Excel file.

## Dependencies

The script uses the following Python libraries:

- pandas
- azure.cosmosdb.table.tableservice
- azure.cosmosdb.table.models

## Class: ExcelToAzure

This class handles updating an Azure table with data from an Excel file.

### Methods

- `__init__(self, account_name, account_key, table_name)`: Initializes an instance of the ExcelToAzure class.
- `create_table(self)`: Creates a new Azure table or deletes all entities in an existing table.
- `delete_all_entities(self)`: Deletes all entities in the Azure table.
- `sanitize_column_name(self, column_name)`: Sanitizes a column name by removing control characters, prepending an underscore if the first character is numeric, and truncating to 255 characters.
- `update_table(self, excel_file)`: Updates the Azure table with data from an Excel file.

## Usage

To use this script, you need to create an instance of the `ExcelToAzure` class with your Azure storage account name, access key, and the name of the Azure table. Then, you can call the `update_table` method with the path to your Excel file.

```python
from update_azure_table import ExcelToAzure
from settings import read_local_settings

settings = read_local_settings()

azure_updater = ExcelToAzure(settings['account_name'], settings['account_key'], settings['table_name'])
azure_updater.update_table('path_to_my_excel_file.xlsx')
```

## Local settings file

Create a file named `settings.json` in the root folder of this project. The file should contain the below information.

```json
{
    "account_name": "your_account_name",
    "account_key": "your_account_key",
    "table_name": "your_table_name"
} 
```
