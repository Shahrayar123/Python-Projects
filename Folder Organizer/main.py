import os
import sys

# No need for a specific root on all OS
DIRNAME_PATTERN = 'Folders'


def mkdir(name):
    # Use os.makedirs to create directory and its parents if they don't exist
    if not os.path.exists(name):
        os.makedirs(name)


def move(old, new):
    os.rename(old, new)


def validate_path(path):
    # Check if the path exists and is a directory
    if not os.path.isdir(path):
        print('Error: The provided folder does not exist. Please provide the full path of the folder.')
        return False

    return True


def main():
    if len(sys.argv) < 2:
        print('Error: Please provide a path')
        return

    path = sys.argv[1]

    # Validate the provided path
    if not validate_path(path):
        return

    try:
        os.chdir(path)
        mkdir(os.path.join(path, DIRNAME_PATTERN))

        print('Cleaning has been started !!')

        for file in os.listdir():
            file_path = os.path.join(path, file)

            if os.path.isdir(file_path):
                # Move subdirectories to the specified directory pattern
                if not file.startswith('.') and file != DIRNAME_PATTERN:
                    move(file_path, os.path.join(path, DIRNAME_PATTERN, file))

            else:
                _, ext = os.path.splitext(file)
                # Create directories based on file extensions
                mkdir(os.path.join(path, ext))
                move(file_path, os.path.join(path, ext, file))

        print('Cleaning is done !!')

    # Handle FileNotFoundError specifically
    except FileNotFoundError as e:
        print(f'Error: {e.filename} not found')

    # Handle PermissionError specifically
    except PermissionError as e:
        print(f'Error: Permission issue. Unable to perform the operation on {e.filename}')

    # Handle other unexpected exceptions
    except Exception as e:
        print(f'Error: An unexpected error occurred - {e}')


if __name__ == "__main__":
    main()
