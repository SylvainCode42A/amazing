def parse_config(filename: str) -> dict:

    dict_file = {}

    try:
        with open(filename, "r") as f:
            for line in f:
                if line.strip() == "" or line.strip().startswith("#"):
                    continue
                key, value = line.split("=", 1)
                dict_file[key] = value.strip()
    except FileNotFoundError:
        raise FileNotFoundError("Sorry, config.txt not found")

    return dict_file


def verify_dict(dict_file: dict) -> bool:

    required = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"]

    for word in required:
        if word not in dict_file:
            raise ValueError(f"Missing required attribute: '{word}'")
        if not dict_file[word].strip():
            raise ValueError(f"Attribute '{word}' is empty.")

    return True
