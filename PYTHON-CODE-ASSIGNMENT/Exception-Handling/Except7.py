def log_exceptions():
    try:
        x = 10 / 0
    except Exception as e:
        with open("log.txt", "a") as file:
            file.write(f"Exception occurred: {e}\n")
            print("Log file created with exception details.")

log_exceptions()
