# QInstaller

## Overview

QInstaller is a custom Windows installer application designed to speed up the installation process of any software and its dependencies. Built using PySide2 and Python, this installer provides a user-friendly interface for installing software with several important features.

![UI](1.mp4)
## Features

- **Graphical User Interface (GUI)**
  - Modern, clean design with multiple installation stages
  - Progress tracking during installation
  - Custom modal notifications
  - Installation path selection

- **Key Functionalities**
  - Automatic installation of software components
  - Multi-threaded file copying
  - Desktop shortcut creation
  - Optional application launch after installation

- **System Requirements**
  - Windows operating system
  - Administrator privileges
  - Approximately 3.19 - 5.10 GB of free disk space

## Installation Process

### Prerequisites

- Run the installer with administrator rights
- Ensure sufficient free disk space

### Steps

1. **Launch Installer**
   - The application automatically requests administrator privileges
   - Opens the main installation window

2. **Choose Installation Path**
   - Default path: `C:\Program Files\IVPN Auto Rotate`
   - Click "Browse" to select a different installation directory

3. **Installation Progress**
   - Copies software files
   - Extracts Python dependencies
   - Creates desktop shortcut
   - Displays real-time file installation progress

4. **Completion**
   - Option to launch the installed application
   - Desktop shortcut available for future use

## Technical Details

### Components Installed

- IVPN Auto Rotate application
- IVPN Client
- Python runtime and dependencies

### Installation Locations

- Main Application: `C:\Program Files\IVPN Auto Rotate`
- IVPN Client: `C:\Program Files\IVPN Client`
- Python Dependencies: `C:\Program Files\IVPN Auto Rotate\Dependenc`

### Technical Implementation

- **Language**: Python
- **GUI Framework**: PySide2
- **Key Libraries**:
  - `concurrent.futures` for multi-threaded file copying
  - `zipfile` for compressed file extraction
  - `winshell` and `win32com.client` for shortcut creation

## Troubleshooting

### Common Issues

1. **Insufficient Permissions**
   - Ensure you run the installer as an administrator
   - Temporarily disable antivirus software if it blocks installation

2. **Disk Space**
   - Free up at least 5.10 GB of disk space
   - Choose an installation drive with sufficient space

3. **Existing Installations**
   - Uninstall previous versions before reinstalling

## Security and Privacy

- Requires explicit user consent for installation
- Installs only pre-packaged, verified components
- Creates installation log for tracking

## Customization and Extension

Developers can modify the installer by:
- Updating source paths in the `Qinstaller` class
- Adjusting GUI styles in `style.json`
- Adding additional installation checks or features

## License and Support

Please refer to the software vendor's documentation for licensing and support information.

## Version Information

- Installer Version: 1.0
- Supported OS: Windows
- Last Updated: [15/12/2024]

## Changelog

### Version 1.0
- Initial release
- Basic installation functionality
- Multi-threaded file copying
- Desktop shortcut creation
