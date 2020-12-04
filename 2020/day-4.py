import re

mandatory_fields = {
    "byr": [
        {
            "type": "boundary",
            "regex": r"^(\d{4})$",
            "min": 1920,
            "max": 2002
        }
    ],
    "iyr": [
        {
            "type": "boundary",
            "regex": r"^(\d{4})$",
            "min": 2010,
            "max": 2020
        }

    ],
    "eyr": [
        {
            "type": "boundary",
            "regex": r"^(\d{4})$",
            "min": 2020,
            "max": 2030
        }
    ],
    "hgt": [
        {
            "type": "boundary",
            "regex": r"^(\d+)cm$",
            "min": 150,
            "max": 193
        },
        {
            "type": "boundary",
            "regex": r"^(\d+)in$",
            "min": 59,
            "max": 76
        }
    ],
    "hcl": [
        {
            "type": "matches",
            "regex": r"^#(?:[0-9]|[a-f]){6}$"
        }
    ],
    "ecl": [
        {
            "type": "value",
            "values": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        }
    ],
    "pid": [
        {
            "type": "matches",
            "regex": r"^\d{9}$"
        }
    ]
    }

def input_to_passport_data(raw_input):
    passports_data = []
    passport = []
    for line in raw_input:
        if line == "\n":
            passports_data.append(passport)
            passport = []
            continue
        passport += line.replace("\n", "").split(" ")
    return passports_data

def passport_processing(passports_input, validate_fields=False):
    valid_count = 0
    for passport_input in passports_input:
        valid_fields = 0
        for field in passport_input:
            field_name, field_value = field.split(":")
            if field_name in mandatory_fields and (not validate_fields or (validate_fields and is_field_valid(field_name, field_value))):
                valid_fields += 1
            elif field_name != "cid":
                break
        if valid_fields == 7:
            valid_count += 1
    print(valid_count)


def is_field_valid(field_name, field_value):
    for validation_rule in mandatory_fields[field_name]:
        if validation_rule["type"] == "value":
            if field_value in validation_rule["values"]:
                return True
        elif validation_rule["type"] == "matches":
            regex_match = re.match(validation_rule["regex"], field_value)
            if regex_match is not None:
                return True
        elif validation_rule["type"] == "boundary":
            regex_match = re.match(validation_rule["regex"], field_value)
            if regex_match is not None and validation_rule["min"] <= int(regex_match.groups()[0]) <= validation_rule["max"]:
                    return True
    return False


with open(r"2020/Input/day-4-puzzle.txt") as input_data_file:
    input_data = input_data_file.readlines()


passport_data = input_to_passport_data(input_data)
passport_processing(passport_data)
passport_processing(passport_data, True)
