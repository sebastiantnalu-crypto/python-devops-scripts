error_count = 0

with open("server.log", "r") as file:
    for line in file:
        if "ERROR" in line:
            print("[ERROR FOUND]", line.strip())
            error_count += 1

print(f"\nTotal Errors: {error_count}")
