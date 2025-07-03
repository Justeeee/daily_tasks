def convert_length(value, from_unit, to_unit):
    units = {
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "mi": 1609.34
    }
    if from_unit not in units or to_unit not in units:
        return None
    return value * units[from_unit] / units[to_unit]


def convert_weight(value, from_unit, to_unit):
    units = {
        "g": 0.001,
        "kg": 1,
        "lb": 0.453592
    }
    if from_unit not in units or to_unit not in units:
        return None
    return value * units[from_unit] / units[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "C":
        return value * 9 / 5 + 32 if to_unit == "F" else value + 273.15
    if from_unit == "F":
        return (value - 32) * 5 / 9 if to_unit == "C" else (value - 32) * 5 / 9 + 273.15
    if from_unit == "K":
        return value - 273.15 if to_unit == "C" else (value - 273.15) * 9 / 5 + 32
    return None


def main():
    while True:
        print("=== 🚀 WooMann's Unit Converter ===")
        print("1. Length\n2. Weight\n3. Temperature\n4. Exit")
        category = input("Choose category (1-4): ").strip()

        if category == "4":
            print("👋 Bye, WooMann!")
            break

        try:
            value = float(input("Enter value to convert: "))
        except ValueError:
            print("⚠️ Invalid number. Try again.\n")
            continue

        if category == "1":
            print("Available units: cm, m, km, in, ft, mi")
            from_unit = input("Convert from: ").strip().lower()
            to_unit = input("Convert to: ").strip().lower()
            result = convert_length(value, from_unit, to_unit)

        elif category == "2":
            print("Available units: g, kg, lb")
            from_unit = input("Convert from: ").strip().lower()
            to_unit = input("Convert to: ").strip().lower()
            result = convert_weight(value, from_unit, to_unit)

        elif category == "3":
            print("Available units: C, F, K")
            from_unit = input("Convert from (C/F/K): ").strip().upper()
            to_unit = input("Convert to (C/F/K): ").strip().upper()
            result = convert_temperature(value, from_unit, to_unit)

        else:
            print("⚠️ Invalid choice.\n")
            continue

        if result is None:
            print("❌ Conversion failed. Check your units.\n")
        else:
            print(f"✅ Result: {value} {from_unit} = {round(result, 6)} {to_unit}\n")


if __name__ == "__main__":
    main()
