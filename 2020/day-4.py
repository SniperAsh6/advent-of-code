mandatory_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

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

def passport_processing(passports_input):
    valid_count = 0
    for passport_input in passports_input:
        valid_fields = 0
        for field in passport_input:
            field_name = field.split(":")[0]
            if field_name in mandatory_fields:
                valid_fields += 1
        if valid_fields == 7:
            valid_count += 1
    print(valid_count)


with open(r"2020/Input/day-4-puzzle.txt") as input_data_file:
    input_data = input_data_file.readlines()


passport_data = input_to_passport_data(input_data)
passport_processing(passport_data)
