
# Desktop and Downloads Cleaner

A simple Python script that cleans files from your Desktop and Downloads folders. This project includes an executable created with PyInstaller, allowing you to run the script without needing a Python environment.

## Features

- Cleans specified file types from your Desktop and Downloads folders
- Easy-to-use executable for quick cleanup

## Getting Started

### Prerequisites

To run the script directly from the source code, you need to have Python installed on your machine. If you prefer to use the executable, you don't need any prerequisites.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mwangihub/python-file-cleaner.git
   cd python-file-cleaner
   ```

2. **Using the Executable:**

   - Download the executable file from the [releases page](https://github.com/mwangihub/python-file-cleaner/releases).
   - Optionally, add the executable to your PATH for easier access:
     - **Windows:**
       1. Move the `cleaner.exe` file to a directory of your choice (e.g., `C:\Program Files\Cleaner`).
       2. Open the Start Search, type in "env", and select "Edit the system environment variables."
       3. In the System Properties window, click on the "Environment Variables..." button.
       4. In the Environment Variables window, find the "Path" variable in the "System variables" section and select it. Click on "Edit...".
       5. Click "New" and add the directory where you moved `cleaner.exe` (e.g., `C:\Program Files\Cleaner`).
       6. Click "OK" to close all the windows.
     - **MacOS/Linux:**
       1. Move the `cleaner` file to a directory of your choice (e.g., `/usr/local/bin`).
       2. Open a terminal and add the directory to your PATH:
          ```bash
          export PATH=$PATH:/path/to/directory
          ```
       3. To make this change permanent, add the above line to your shell's startup file (e.g., `~/.bashrc`, `~/.zshrc`).

   - Run the executable to clean your Desktop and Downloads folders.

3. **Running from Source:**

   - Run the script:

     ```bash
     python cleaner.py
     ```

### Usage

By default, the script cleans specific file types. You can modify the script to specify different file types or directories.

### Creating the Executable

If you want to create the executable yourself, you can use PyInstaller. Install PyInstaller:

```bash
pip install pyinstaller
```

Then run the following command in the project directory:

```bash
pyinstaller --onefile cleaner.py
```

This will generate a `dist` folder containing the `cleaner.exe` file.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the need to keep the Desktop and Downloads folders organized.

---
