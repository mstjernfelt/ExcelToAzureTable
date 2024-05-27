# Azure Table Update Script

This script updates an Azure table with data from Excel files. 

## How it works

1. The script first reads settings from a `settings.json` file. If the file does not exist, it will prompt the user to enter the Azure storage account name, account key, and table name. These settings are then saved to `settings.json` for future use.

2. The script then iterates over all Excel files (`.xlsx`) in the `data` folder. For each file, it does the following:
    - Extracts the table name from the file name (minus the extension)
    - Creates an instance of the `ExcelToAzure` class with the account name, account key, and table name
    - Calls the `create_table` method to create the table in Azure
    - Calls the `update_table` method to update the table with the data from the Excel file

## Requirements

- Python 3
- pandas: Install with `pip3 install pandas`
- azure-cosmosdb-table: Install with `pip3 install azure-cosmosdb-table`
- openpyxl: Install with `pip3 install openpyxl`

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
settings = read_settings()

# Update the Azure table with data from each Excel file in the data folder
data_folder = 'data'
for file_name in os.listdir(data_folder):
    if file_name.endswith('.xlsx'):
        table_name = os.path.splitext(file_name)[0]
        excel_to_azure = ExcelToAzure(settings['account_name'], settings['account_key'], table_name)
        excel_to_azure.create_table()
        excel_to_azure.update_table(os.path.join(data_folder, file_name))
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
