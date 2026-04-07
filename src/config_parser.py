def parse_config(filename: str) -> dict: 
    dict_file = {}

    with open(filename, "r") as f:
        for line in f:
            if line.strip() == "":
                continue
            key, value = line.split("=")
            dict_file[key] = value.strip()
    return dict_file

def verify_dict(dict_file: dict) -> bool:
    required = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"]

    for word in required:
        if not word in dict_file.keys():
            return False
        if not dict_file[word]:
            return False
    return True
