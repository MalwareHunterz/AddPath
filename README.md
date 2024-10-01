```markdown
# AddPath Script - by MalwareHunterz

## Overview
**AddPath** is a utility designed to streamline the process of adding scripts or executables to your system's `$PATH`. Once added, you can execute those scripts from any terminal location without having to type the full path each time. This tool also allows you to cleanly remove entries from `$PATH` when they're no longer needed.

Feel free to use this script personally or commercially, and if you want to contribute, improvements are always welcome on the GitHub project!

## Features
- **Add any executable to `$PATH`**: Simply specify the file, and this script will ensure it’s copied to `/usr/local/bin`, making it executable from anywhere.
- **Remove executables from `$PATH`**: List all files in `/usr/local/bin` and remove any you no longer need, with special highlighting for files added by the script.
- **Track changes**: The script keeps a log of all files added to `/usr/local/bin` via the script, so you can easily manage them later.
- **Automatic Permissions**: If the file you're adding isn't executable, the script will automatically make it executable with `chmod +x` before adding it to `$PATH`.
- **Safe and Efficient**: Built for simplicity and performance, ensuring only necessary changes are made.

## Installation

To install **AddPath** itself as a globally executable command, run:

```bash
sudo AddPath -i
```

This will copy the script into `/usr/local/bin` and allow you to call `AddPath` from any terminal session.

## Usage

### Adding a File to PATH

To add a file (for example, `myscript.sh`) to your system's `$PATH`, use:

```bash
AddPath -t /path/to/myscript.sh
```

The script will ensure the file is executable and copy it to `/usr/local/bin`. Afterward, you'll be able to run `myscript.sh` from any terminal session.

### Listing and Removing Files from PATH

To list all files in `/usr/local/bin` and highlight those added by **AddPath**, run:

```bash
AddPath -r
```

You'll be presented with a numbered list of files, and you can select one for removal by typing the corresponding number.

### Uninstalling AddPath

To remove **AddPath** itself from your system, run:

```bash
AddPath -u
```

This will delete the script from `/usr/local/bin` and remove any logs.

### Help Menu

For a quick reference guide, you can use the help flag:

```bash
AddPath -h
```

## Important Notes on Permissions

**AddPath** manipulates files in `/usr/local/bin`, which typically requires root privileges. If you encounter any permission errors when running this script, make sure to run it with `sudo`. Without root access, the script will be unable to make necessary changes to your system's `$PATH`.

```bash
sudo AddPath -t /path/to/your_script.sh
```

## Contributing

Contributions are welcome! If you have improvements, bug fixes, or new features you'd like to suggest, feel free to submit a pull request or open an issue on the GitHub repository. This tool is open-source, and I encourage both personal and commercial usage.

---

### Author: MalwareHunterz
```
