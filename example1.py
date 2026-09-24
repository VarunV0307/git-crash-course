try:
    file = open("data.txt", "r")
    data = file.read()
    print(data)

except FileNotFoundError:
    print("Error: data.txt was not found.")

except PermissionError:
    print("Error: You don't have permission to read this file.")

finally:
    print("File operation completed.")


