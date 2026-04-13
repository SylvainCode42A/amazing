def parse_config(filename: str) -> dict[str, str]:
    """Parse a KEY=VALUE configuration file.

    Lines starting with '#' and blank lines are ignored.
    Lines without '=' are skipped. Keys and values are stripped
    of surrounding whitespace.

    Args:
        filename: Path to the configuration file.

    Returns:
        A dict mapping configuration keys to their string values.

    Raises:
        FileNotFoundError: If the file does not exist.
    """

    dict_file: dict[str, str] = {}

    try:
        with open(filename, "r") as f:
            for line in f:
                if line.strip() == "" or line.strip().startswith("#"):
                    continue
                if "=" not in line:
                    continue
                key, value = line.split("=", 1)
                dict_file[key.strip()] = value.strip()
    except FileNotFoundError:
        raise FileNotFoundError("Sorry, config.txt not found")

    return dict_file


def verify_dict(dict_file: dict[str, str]) -> bool:
    """Verify that all required keys are present and non-empty.

    Args:
        dict_file: Dict of configuration keys and values.

    Returns:
        True if all required keys are present and non-empty.

    Raises:
        ValueError: If a required key is missing or empty.
    """

    required = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"]

    for word in required:
        if word not in dict_file:
            raise ValueError(f"Missing required attribute: '{word}'")
        if not dict_file[word].strip():
            raise ValueError(f"Attribute '{word}' is empty.")

    return True
