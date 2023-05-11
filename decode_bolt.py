def decode_bolt(part_number):
    # Extract the relevant digits from the part number
    standardization = int(part_number[0])
    manufacturer_prefix = int(part_number[1])
    bolt_type = int(part_number[2])
    material = int(part_number[3:5])
    dimension = int(part_number[5:7])
    length = int(part_number[7:9])
    suffix = int(part_number[9:])

    # Determine the dimension units (metric or imperial)
    if dimension in [1, 31, 51, 61]:
        dimension_units = "inch"
    else:
        dimension_units = "mm"

    # Determine the dimension size
    if dimension_units == "inch":
        dimension_size = {
            7: "1/4",
            10: "3/8",
            13: "1/2",
            16: "5/8",
            19: "3/4",
            22: "7/8",
            26: "1",
            28: "1-1/8",
            32: "1-1/4",
            35: "1-3/8",
            38: "1-1/2",
            41: "1-5/8",
            44: "1-3/4",
            48: "1-7/8",
            51: "2",
            54: "2-1/8",
            57: "2-1/4",
            64: "2-1/2",
            70: "2-3/4",
            76: "3"
        }.get(dimension)
    else:
        dimension_size = str(dimension)

    # Determine the material type
    material_type = {
        11: "Zinc cadmium coated",
        22: "Chrome coated",
        33: "Copper coated",
        44: "Phosphoric acid coated",
        55: "Brass",
        66: "Copper"
    }.get(material)

    # Determine the bolt type
    bolt_type_name = {
        1: "Hexagon bolt",
        7: "Carriage bolt"
    }.get(bolt_type)

    # Determine the suffix meaning
    suffix_meaning = {
        0: "Surface not processed",
        1: "Cotter pin hole",
        11: "Zinc cadmium coated with cotter pin hole",
        22: "Chrome coated with cotter pin hole",
        33: "Copper coated with cotter pin hole",
        44: "Phosphoric acid coated with cotter pin hole",
        55: "Brass with cotter pin hole",
        66: "Copper with cotter pin hole",
        110: "Surface not processed with cotter pin hole",
        211: "Zinc cadmium coated with cotter pin hole",
        321: "Chrome coated with cotter pin hole",
        431: "Copper coated with cotter pin hole",
        541: "Phosphoric acid coated with cotter pin hole",
        651: "Brass with cotter pin hole",
        761: "Copper with cotter pin hole"
    }.get(suffix)

    # Construct the decoded bolt information string
    decoded_bolt = f"{dimension_size} {dimension_units} {material_type} {bolt_type_name} {length}mm {suffix_meaning}"

    return decoded_bolt

part_number = input("Enter the part number: ")
decoded_bolt = decode_bolt(part_number)
print(decoded_bolt)
