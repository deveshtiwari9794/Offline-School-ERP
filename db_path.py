import os

data_folder = os.path.join(
    os.path.expanduser("~"),
    "SchoolERP"
)

os.makedirs(data_folder, exist_ok=True)

database_path = os.path.join(
    data_folder,
    "school_erp.db"
)
print(data_folder)
print(database_path)