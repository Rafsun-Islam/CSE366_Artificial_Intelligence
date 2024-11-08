import random

def read_student_ids(filename):
    """
    Reads student IDs from a file and returns them as a list.
    Handles the case where the file might not exist or could be empty.

    Parameters:
        filename (str): The name of the file containing student IDs.

    Returns:
        list: A list of student IDs, or an empty list if there was an error.
    """
    try:
        with open(filename, 'r') as file:
            # Read each line, strip whitespace, and add to the list if it's not empty
            student_ids = [line.strip() for line in file if line.strip()]
            if not student_ids:
                print("The file is empty or has no valid IDs.")
            return student_ids
    except FileNotFoundError:
        # Handle the case where the file doesn't exist
        print(f"Error: The file '{filename}' was not found.")
        return []

def select_students_for_viva(student_ids):
    """
    Randomly selects students for viva and logs each selection with a viva count.
    Prints each selection to the console and logs it in 'viva_selection_log.txt'.

    Parameters:
        student_ids (list): List of student IDs to select from.

    Returns:
        list: An empty list indicating all students have been selected.
    """
    if not student_ids:
        print("No student IDs available for selection.")
        return []

    viva_count = 1  # Counter for each viva selection

    # Create or clear the log file at the beginning
    with open("viva_selection_log.txt", "w") as log_file:
        log_file.write("Viva Selection Log\n")
        log_file.write("------------------\n")

    # Loop until all students have been selected
    while student_ids:
        # Randomly select a student from the list
        selected_student = random.choice(student_ids)
        print(f"Viva #{viva_count}: {selected_student}")

        # Append the selection to the log file with viva count
        with open("viva_selection_log.txt", "a") as log_file:
            log_file.write(f"Viva #{viva_count}: {selected_student}\n")
        
        # Remove the selected student from the list to avoid re-selection
        student_ids.remove(selected_student)
        viva_count += 1

    print("\nAll students have been selected.")
    return student_ids  # Return an empty list to indicate all students have been selected

def main():
    """
    Main function to control the flow of the viva selection process.
    Reads student IDs from a file, selects students for viva, and logs the process.
    """
    filename = "student_ids.txt"  # The file containing student IDs
    student_ids = read_student_ids(filename)  # Read student IDs from the file

    # Proceed with viva selection if there are students in the list
    if student_ids:
        student_ids = select_students_for_viva(student_ids)  # Run the selection process
        if not student_ids:
            # Confirm when all students have been selected
            print("The viva selection is complete, and all students have been selected once.")

# Run the main function only if the script is executed directly
if __name__ == "__main__":
    main()
