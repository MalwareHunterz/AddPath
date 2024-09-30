# AddPath Script

## Overview
The **AddPath** script allows users to make files and folders executable globally from any terminal location on Linux systems. This script is developed by **MalwareHunterz** and comes with various features to enhance usability.

## Features
- **Make Executable**: Easily make any file or folder executable globally.
- **Install/Uninstall**: Install or uninstall the AddPath script effortlessly.
- **Status Check**: Verify if the AddPath script is installed on your system.
- **List Executables**: List all executable files in `/usr/local/bin`.
- **Copy Files**: Copy specified files to `/usr/local/bin` directly.

## Usage
To use the AddPath script, run the following commands:

### Install the Script
```bash
sudo ./Install.sh
```

### Make a File Executable
```bash
sudo AddPath -t <file_or_folder>
```
*Example:*
```bash
sudo AddPath -t File.py
```

### Uninstall the Script
```bash
sudo AddPath -u
```

### Check Installation Status
```bash
sudo AddPath -s
```

### List Executable Files
```bash
sudo AddPath -l
```

### Copy a File to Executable Directory
```bash
sudo AddPath -c <source>
```

## Disclaimer
Use this script at your own risk. Moving files can affect your system. **MalwareHunterz** is not responsible for any damage.

## License
This script is open-source and can be used freely under the terms of the MIT License.
