import os
import kagglehub

# Baixando arquivos
downloadpath = os.path.abspath("files")
os.makedirs(downloadpath, exist_ok=True)
path = kagglehub.dataset_download(
    "mominullptr/fifa-world-cup-2026-dataset",
    output_dir=downloadpath)
print("Path to dataset files:", path)