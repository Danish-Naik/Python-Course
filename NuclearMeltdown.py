"""Functions to prevent a nuclear meltdown."""
def is_criticality_balanced(temperature, neutrons_emitted):
    if (temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000):
        return True;
    else: 
        return False;
def reactor_efficiency(voltage, current, theoretical_max_power):
    percentage_value = (voltage * current / theoretical_max_power) * 100
    if percentage_value < 30:
        return "black"
    elif percentage_value < 60:
        return "red"
    elif percentage_value < 80:
        return "orange"
    else:
        return "green"
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    value = temperature * neutrons_produced_per_second
    if value < 0.9 * threshold:
        return "LOW"
    elif value <= 1.1 * threshold:
        return "NORMAL"
    else:
        return "DANGER"
