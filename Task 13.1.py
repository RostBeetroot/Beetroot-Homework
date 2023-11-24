def calculate_locals():
    car = "bmw"
    color = "red"
    gear = "manual"
    engine = "S54B32"
    local_symbols = locals()

    return len(local_symbols)


print(calculate_locals())
