import random
import tkinter as tk

def challenge(challenge_num, secret):
    return (challenge_num + secret) % 10

def authenticate():
    # Get the input from the user
    code = code_entry.get()
    
    # Convert the input to binary
    code_bin = bin(int(code))[2:]
    
    # Send the code to Node B
    code_label.config(text=f"Node A sends code: {code_bin}")
    
    # Generate a random number and send it to Node A
    random_num = random.randint(1, 100)
    random_num_bin = bin(random_num)[2:]
    random_num_label.config(text=f"Node B sends random number: {random_num_bin}")
    
    # Perform the challenge and send the result to Node B
    challenge_result = challenge(int(random_num_bin, 2), int(code_bin, 2))
    challenge_result_bin = bin(challenge_result)[2:]
    challenge_label.config(text=f"Node A sends challenge result: {challenge_result_bin}")
    
    # Perform the same challenge and compare the results
    challenge_result_b = challenge(random_num, int(code_bin, 2))
    challenge_result_bin_b = bin(challenge_result_b)[2:]
    if challenge_result_bin == challenge_result_bin_b:
        result_label.config(text="Authentication successful!")
    else:
        result_label.config(text="Access denied!")

# Create the GUI
root = tk.Tk()
root.title("CHAP Simulation")

def validate_code(new_value):
    # Ensure that the value entered is an integer
    try:
        int(new_value)
        return True
    except ValueError:
        return False

code_label = tk.Label(root, text="Node A sends code: ")
code_label.pack()

code_entry = tk.Entry(root, validate="key", validatecommand=(root.register(validate_code), '%P'))
code_entry.pack()

secret_label = tk.Label(root, text="Secret code: ")
secret_label.pack()

secret_entry = tk.Entry(root)
secret_entry.pack()

random_num_label = tk.Label(root, text="Node B sends random number: ")
random_num_label.pack()

challenge_label = tk.Label(root, text="Node A sends challenge result: ")
challenge_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

button = tk.Button(root, text="Authenticate", command=authenticate)
button.pack()

root.mainloop()
