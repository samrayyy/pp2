import time
import math

def square_root_after_delay(number, milliseconds):
    time.sleep(milliseconds / 1000)  # Convert milliseconds to seconds
    result = math.sqrt(number)
    return result
