import os


def config_parser(filename: str):

    required = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"]

    if not os.path.exists(filename):
        raise FileNotFoundError(f"Fichier config introuvable : {filename}")
    
    with open(filename, "r") as file:
        file.read("WIDTH")
