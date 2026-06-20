import os
import kagglehub
import traceback
import shutil
import subprocess

from numpy import True_

# Baixando arquivos
try:
    downloadpath = os.path.abspath("files")
    shutil.rmtree(downloadpath,ignore_errors=True)
    os.makedirs(downloadpath, exist_ok=True)

    path = kagglehub.dataset_download(
        "mominullptr/fifa-world-cup-2026-dataset",
        output_dir=downloadpath)
    print("Path to dataset files:", path)

    print(f"Arquivos instalados com sucesso na cominho {downloadpath}")
except:
    traceback.print_exc()
    print("[ERRO] ocorreu um erro no download dos aquivos")
finally:
    path_transform = os.path.abspath("Transform.py")
    subprocess.run(["python",path_transform], check=True)