from pathlib import Path

# Main term folder
term = Path("26W")

# Course folders (Homeroom excluded)
courses = [
    "26W_GIS2203_100_Geospatial_Analytical_Methods",
    "26W_GIS2202_100_Cartographic_Elements_and_Design",
    "26W_ENL2019T_100_Technical_Communication",
    "26W_GIS2206_100_Geodatabase_Design",
    "26W_GIS2205_100_Landscape_Geography",
    "26W_GIS2200_100_Statistics_for_Geomatics",
    "26W_GIS2103_100_Remote_Sensing_I"
]

# Standard subfolders for each course
subfolders = [
    "Notes",
    "Assignments",
    "Slides",
    "Labs",
    "Projects",
    "Data",
    "Readings",
    "Exams",
    "Software"
]

# Create folders
term.mkdir(exist_ok=True)

for course in courses:
    course_path = term / course
    course_path.mkdir(exist_ok=True)

    for sub in subfolders:
        (course_path / sub).mkdir(exist_ok=True)

print("✅ 26W folder structure created successfully.")
