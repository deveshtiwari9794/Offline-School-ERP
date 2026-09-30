import shutil
from db_path import database_path

shutil.copy(
    "school_erp.db",
    database_path
)

print("Old database copied successfully!")