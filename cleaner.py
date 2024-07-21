# Provides functions for interacting with the operating system
import os  
# Provides functions for high-level file operations such as copying and moving
import shutil  
# Provides a way to configure and use logging in Python
import logging  
# Provides classes for manipulating dates and times
from datetime import datetime  
# Provides functions to generate random numbers
import random  

# DEFINE SOURCE AND DESTINATION DIRECTORIES
#  --------------------------------------------------------------------------------------------
# Get the user's home directory dynamically
BASE_DIR = os.path.expanduser('~') 
source_dirs = [
    os.path.join(BASE_DIR, 'Desktop'),
    os.path.join(BASE_DIR, 'Downloads')
]

# DESTINATION DIRECTORIES FOR DIFFERENT FILE TYPES
#  --------------------------------------------------------------------------------------------
dest_dirs = {
    'pictures': os.path.join(BASE_DIR, 'Pictures'),
    'videos': os.path.join(BASE_DIR, 'Videos'),
    'documents': os.path.join(BASE_DIR, 'Documents'),
    # 'zip': 'D:\COMPRESSED'
    # For files with extensions not specified in `extensions`
    'unknown': os.path.join(BASE_DIR, 'Documents', 'UnknownFiles')  
}

# DEFINE FILE EXTENSIONS FOR EACH CATEGORY
#  --------------------------------------------------------------------------------------------
extensions = {
    'pictures': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'videos': ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.mpeg'],
    'documents': ['.doc', '.docx', '.pdf', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', '.csv'],
    # 'zip': ['.zip', '.tar']
}

# ENSURE THE UnknownFiles DIRECTORY EXISTS
#  --------------------------------------------------------------------------------------------
if not os.path.exists(dest_dirs['unknown']):
    # Create the UnknownFiles directory if it doesn't exist
    os.makedirs(dest_dirs['unknown'])  

# SET UP LOGGING CONFIGURATION
#  --------------------------------------------------------------------------------------------

# Get the current date in the format 'day-month-year'
current_date = datetime.now().strftime('%d-%m-%Y')  
# Define the log file name with the current date
log_filename = f'D:\\{current_date}.txt'  
logging.basicConfig(
    # Set the filename for the log
    filename=log_filename,  
    # Set the logging level to INFO
    level=logging.INFO,  
    # Define the format for log messages
    format='%(message)s'  
)

# SET UP LOGGING TO THE CONSOLE
#  --------------------------------------------------------------------------------------------
# Create a handler for logging to the console
console_handler = logging.StreamHandler()  
# Set the console logging level to INFO
console_handler.setLevel(logging.INFO)  
 # Define the format for console log messages
formatter = logging.Formatter('%(message)s') 
# Set the formatter for the console handler
console_handler.setFormatter(formatter)  
# Add the console handler to the root logger
logging.getLogger().addHandler(console_handler)  



def move_file_with_handling(file_path, destination):
    """
    Move a file to the specified destination, handling name conflicts by renaming.
    """
    try:
        # Attempt to move the file
        shutil.move(file_path, destination)  
        # Return the destination if move is successful
        return destination  
        # Catch errors related to the move operation
    except shutil.Error as e:  
        if "already exists" in str(e):
            base, ext = os.path.splitext(destination)
            new_destination = f"{base}_{random.randint(1000, 9999)}{ext}"
            try:
                # Attempt to move the file with a new name
                shutil.move(file_path, new_destination)  
                # Return the new destination if move is successful
                return new_destination  
            except Exception as e2:
                # Remove the file if renaming also fails
                os.remove(file_path)  
                logging.error(f"Failed to move file {file_path}. Error: {e2}. File deleted.")
        else:
            logging.error(f"Failed to move file {file_path}. Error: {e}. File unmodified!")

def move_files(src, dest):
    """
    Function to move files from source to destination based on their extensions.
    """
    # Recursively walk the directory tree
    for root, dirs, files in os.walk(src, topdown=False):  
        # Iterate over all files in the current directory
        for file in files:  
            # Get the full path of the file
            file_path = os.path.join(root, file)  
            # Get the file extension and convert to lowercase
            file_ext = os.path.splitext(file)[1].lower()  
            # Flag to check if the file has been moved
            moved = False  
            # Iterate over each category and its extensions
            for category, exts in extensions.items():  
                # Check if the file extension matches the current category
                if file_ext in exts:  
                    destination = os.path.join(dest_dirs[category], file)
                    final_destination = move_file_with_handling(file_path, destination)
                    log_message = f'{current_date} File: {file_path} \t MOVED TO \n{final_destination}\n'
                    # Log the file move operation
                    logging.info(log_message)  
                    # Set the moved flag to True
                    moved = True  
                    break
            # If the file was not moved to any category
            if not moved:  
                destination = os.path.join(dest_dirs['unknown'], file)
                final_destination = move_file_with_handling(file_path, destination)
                log_message = f'{current_date} File: {file_path} \t MOVED TO \n{final_destination}\n'
                # Log the file move operation
                logging.info(log_message)  
        # Remove empty directories after processing files
        for dir in dirs:
            # Get the full path of the directory
            dir_path = os.path.join(root, dir)  
             # Check if the directory is empty
            if not os.listdir(dir_path): 
                 # Remove the empty directory
                try: 
                    os.rmdir(dir_path) 
                except Exception as e:
                    logging.error(f"Failed to Remove directory {dir_path}. Error: {e}. Folder unmodified!")


if __name__ == '__main__':
    # Execute the script for each source directory
    for source in source_dirs:
        # Call the move_files function for the current source directory
        move_files(source, dest_dirs)  
     # Print a completion message to the console
    print("Cleaning and organizing complete!") 
