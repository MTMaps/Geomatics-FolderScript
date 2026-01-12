import os

# -------------------------------
# Project setup
# -------------------------------
project_name = "ProjectName"  # Change for each new project
task_orders = ["TaskOrder_0001", "TaskOrder_0002"]  # Add as needed

# -------------------------------
# Top-level folders
# -------------------------------
top_folders = [
    "00_Metadata",
    "01_Geodatabases",
    "02_Raw_Data",
    "03_Processed_Data",
    "04_Imagery",
    "05_Projects",
    "06_Maps",
    "07_Docs",
    "08_Scripts",
    "09_Backups",
    "10_Delivery"
]

# -------------------------------
# Subfolders by purpose
# -------------------------------

# Metadata types
metadata_folders = ["Vector", "Raster", "Imagery", "LiDAR", "Tabular"]

# Raw data types
raw_data_folders = ["CAD", "GNSS", "LiDAR", "Raster", "Vector", "Tabular"]

# Processed data types
processed_data_folders = ["Vector", "Raster", "LiDAR", "Tabular"]

# Imagery types
imagery_folders = ["Aerial", "Satellite", "Orthophoto", "Mosaics"]

# Project subfolders
project_subfolders = [
    "GIS",           # ArcGIS Pro projects
    "GEODATABASE",   # Project-specific geodatabase
    "STYLE",         # Symbology (.lyrx)
    "1_IMG",         # Project images
    "2_TABULAR",     # Project tables
    "3_SCRIPTS",     # Project-specific scripts
    "4_REPORTS",     # Reports, PDFs
    "5_DELIVERABLES" # Shareable outputs
]

# Geodatabases placeholders
gdb_list = ["BaseGDB.gdb", "ProjectGDB_YYYYMMDD.gdb", "TerrainGDB.gdb"]

# -------------------------------
# Function to create folders
# -------------------------------
def make_folders():
    os.makedirs(project_name, exist_ok=True)

    # Create top-level folders
    for top in top_folders:
        top_path = os.path.join(project_name, top)
        os.makedirs(top_path, exist_ok=True)

        # Add metadata subfolders
        if top == "00_Metadata":
            for sub in metadata_folders:
                os.makedirs(os.path.join(top_path, sub), exist_ok=True)

        # Add geodatabases
        elif top == "01_Geodatabases":
            for gdb in gdb_list:
                os.makedirs(os.path.join(top_path, gdb), exist_ok=True)

        # Add raw data subfolders
        elif top == "02_Raw_Data":
            for sub in raw_data_folders:
                os.makedirs(os.path.join(top_path, sub), exist_ok=True)

        # Add processed data subfolders
        elif top == "03_Processed_Data":
            for sub in processed_data_folders:
                os.makedirs(os.path.join(top_path, sub), exist_ok=True)

        # Add imagery subfolders
        elif top == "04_Imagery":
            for sub in imagery_folders:
                os.makedirs(os.path.join(top_path, sub), exist_ok=True)

        # Add project folders and task orders
        elif top == "05_Projects":
            for task in task_orders:
                task_path = os.path.join(top_path, task)
                os.makedirs(task_path, exist_ok=True)
                for sub in project_subfolders:
                    os.makedirs(os.path.join(task_path, sub), exist_ok=True)

        # Add backup placeholder
        elif top == "09_Backups":
            os.makedirs(os.path.join(top_path, "YYYYMMDD"), exist_ok=True)

    print(f"Folder structure for project '{project_name}' created successfully!")

# -------------------------------
# Run the script
# -------------------------------
if __name__ == "__main__":
    make_folders()
