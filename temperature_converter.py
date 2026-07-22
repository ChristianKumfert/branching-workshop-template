def celsius_to_fahrenheit(celsius: float) -> float:
    """Konvertiert eine Temperatur von Celsius in Fahrenheit."""
    return (celsius * 9 / 5) + 32


# Zum schnellen Testen (optional):
if __name__ == "__main__":
    test_temp = 25.0
    print(f"{test_temp}°C sind {celsius_to_fahrenheit(test_temp)}°F")