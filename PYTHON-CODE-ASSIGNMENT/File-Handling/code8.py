import datetime

def write_log(message, log_file="example.txt"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, 'a') as file:
        file.write(f"[{timestamp}] {message}\n")
    with open(log_file, 'r') as file:
        print("Current log content: ")
        for line in file:
            print(line.strip())

write_log("Program started.")
