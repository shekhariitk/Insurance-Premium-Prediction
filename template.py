import os
from pathlib import Path

project_name = "src"

list_of_files = [

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py", 
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/piplines/__init__.py",
    f"{project_name}/piplines/training_pipeline.py",
    f"{project_name}/piplines/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "main.py",
    "setup.py",
    "config/schema.yaml",
    "config/params.yaml",
    "config.yaml",
    ".gitignore",
    "README.md",
    "LICENSE",
    "notebooks/data",
    "notebooks/eda.ipynb",
    "notebooks/model.ipynb",
    "notebooks/trails.ipynb",
    "templates/index.html",
    "templates/base.html",
    "templates/about.html",
    "templates/result.html",
    "static/css/style.css",
    "static/js/script.js",
    "static/images/logo.png",
    "dvc.yaml",
    "Dockerfile",
    ".dockerignore",
    "config/config.yaml",
    "config/params.yaml",
    "config.py"

]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")