"""Constant representing the expected bake time in minutes."""
EXPECTED_BAKE_TIME=40
print(EXPECTED_BAKE_TIME)


def bake_time_remaining(elapsed_bake_time):
    """Return the remaining bake time in minutes."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    

def preparation_time_in_minutes(number_of_layers):
    """Return the preparation time in minutes based on the number of layers."""
    preparation_time =  number_of_layers * 2
    return (preparation_time)
    

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Return the total elapsed cooking time in minutes."""
    total_time = (number_of_layers*2) + elapsed_bake_time;
    return total_time
    
    
