# Example of while true
from time import sleep
while True:
    try:
        print("Poolin.")
        # Poll some resource
        sleep(1)
    except KeyboardInterrupt:
        break