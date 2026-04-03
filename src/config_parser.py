import os


def config_parser(filename: str) -> None:

    k_required = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"]

    if not os.path.exists(filename):
        raise FileNotFoundError(f"Fichier introuvable : {filename}")

    with open(filename, "r") as f:
        line = f.read()
        for key in k_required:
            if key not in line:
                raise KeyError(f"Error {key} key not found in {filename}")
        else:
            print("All good")


def main() -> None:
    config_parser("config.txt")


if __name__ == "__main__":
    main()
