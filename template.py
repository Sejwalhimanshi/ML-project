import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name="mlproject"

list_of_file=[
    ".github/workflows/.gitkeep",
    f"src/mlproject/__init__.py",
    f"src/mlproject/components/__init__.py",
    f"src/mlproject/components/data_ingestion.py",
    f"src/mlproject/components/data_transformation.py",
    f"src/mlproject/components/model_tranier.py",
    f"src/mlproject/components/model_monitering.py",
    f"src/mlproject/pipelines/__init__.py",
    f"src/mlproject/components/training_pipeline.py",
    f"src/mlproject/components/prediction_pipeline.py",
    f"src/mlproject/exception.py",
    f"src/mlproject/logger.py",
    f"src/mlproject/utlis.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    ]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info("Creating directory:{filedir} for the file {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")



        
