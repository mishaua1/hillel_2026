import csv
import json
import logging
import os
import xml.etree.ElementTree as ET
SECOND_NAME = "shevchenko"

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_dir = os.path.join(current_dir, "ideas_for_test", "work_with_csv")
json_dir = os.path.join(current_dir, "ideas_for_test", "work_with_json")
xml_dir = os.path.join(current_dir, "ideas_for_test", "work_with_xml")


# Завдання 1
def remove_duplicates(first_file, second_file, output_file):
    header = None
    seen = []
    result_rows = []

    for file_path in [first_file, second_file]:
        with open(file_path, encoding="utf-8") as f:
            rows = list(csv.reader(f))

        if header is None:
            header = rows[0]

        for row in rows[1:]:
            if not any(row):
                continue
            if row not in seen:
                seen.append(row)
                result_rows.append(row)

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in result_rows:
            writer.writerow(row)

    return len(result_rows)


# Завдання 2
def validate_json_files(folder, log_file):
    logger = logging.getLogger("json_check")
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
    handler.setLevel(logging.ERROR)
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(handler)

    for name in os.listdir(folder):
        if not name.endswith(".json"):
            continue
        path = os.path.join(folder, name)
        try:
            with open(path, encoding="utf-8") as f:
                json.load(f)
            logger.info(f"{name} - valid json")
        except json.JSONDecodeError as error:
            logger.error(f"{name} is not valid json: {error}")


# Завдання 3
def find_incoming(xml_file, group_number):
    logger = logging.getLogger("xml_search")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        logger.addHandler(logging.StreamHandler())

    tree = ET.parse(xml_file)
    root = tree.getroot()

    for group in root.findall("group"):
        if group.find("number").text == str(group_number):
            timing = group.find("timingExbytes")
            if timing is not None and timing.find("incoming") is not None:
                value = timing.find("incoming").text
                logger.info(f"group {group_number}: incoming = {value}")
                return value

    logger.info(f"group {group_number} not found or has no incoming")
    return None


if __name__ == "__main__":
    result_path = os.path.join(csv_dir, f"result_{SECOND_NAME}.csv")
    total = remove_duplicates(
        os.path.join(csv_dir, "random-michaels.csv"),
        os.path.join(csv_dir, "r-m-c.csv"),
        result_path,
    )
    print(f"Записано рядків без дублікатів: {total}")

    log_path = os.path.join(json_dir, f"json__{SECOND_NAME}.log")
    validate_json_files(json_dir, log_path)

    find_incoming(os.path.join(xml_dir, "groups.xml"), 2)