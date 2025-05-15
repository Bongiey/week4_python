def read_and_modify_file():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, "r") as file:
            content = file.read()
            print("✅ File read successfully.")

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write modified content to a new file
        with open("modified_output.txt", "w") as new_file:
            new_file.write(modified_content)
            print("✍️ Modified content written to 'modified_output.txt'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except IOError:
        print("❌ Error: Could not read the file.")


# Run the program
read_and_modify_file()
