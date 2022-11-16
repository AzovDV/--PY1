import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str, delimiter: str = ',', new_line: str = "\n") -> list[dict]:
    with open(filename, "rt", encoding="utf-8") as file:
        raw_lines = file.read().split(new_line)
        headers = raw_lines[0].split(delimiter)
        data = [raw_lines[i].split(delimiter) for i in range(1, len(raw_lines))]

        return [{headers[i]: row[i] for i in range(len(headers))} for row in data]


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
