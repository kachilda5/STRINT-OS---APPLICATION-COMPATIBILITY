# Wine Compatibility Testing

## 1. Objective
To investigate how Wine can be used to run selected Windows desktop applications in a Linux environment as part of the STRINT OS application compatibility work.

## 2. Testing Environment

- Operating System: Kali Linux 2026.3
- Environment: WSL2
- Processor Architecture: x86_64
- Wine Version: 10.0
- Windows Prefix Architecture: win64

Note: These practical tests were conducted on x86_64, not ARM64.

## 3. Wine Installation and Configuration

Wine was installed successfully using the Kali package manager.

The following components were installed:

- Wine
- Wine 32-bit loader
- Wine 64-bit loader
- 32-bit Wine libraries
- 64-bit Wine libraries
- Wine Common
- Winetricks

The Wine configuration tool (winecfg) opened successfully and created the default Wine prefix.

## 4. Application Testing

### Windows Notepad
- Launched through Wine.
- Result: Successful.

### Notepad++
- Windows installer executed through Wine.
- Application installed successfully.
- Application launched successfully.
- Application relaunched after closing.
- Text file creation and saving tested successfully.
- Saved file reopened successfully.
- Application appeared in Wine's installed applications list.
- Uninstallation tested successfully.
- Application reinstalled and launched successfully.

### Application Architecture
The Notepad++ executable was examined using the Linux `file` command.

Result:
PE32 executable, Intel i386.

This identifies it as a 32-bit Windows application.

## 5. Dependency Configuration

Winetricks was installed and its version verified.

Wine 32-bit and 64-bit components were confirmed installed.

## 6. ARM64 Compatibility Investigation

The current testing environment uses x86_64 architecture.

ARM64 Wine compatibility remains under investigation. The current practical results do not establish that these applications will run on ARM64.

Additional testing on ARM64 hardware or a suitable ARM64 virtual environment is required.

## 7. Summary

Wine was successfully installed and configured in the Kali Linux testing environment.

Notepad and Notepad++ were used to test Windows application execution. Notepad++ also passed installation, relaunch, file handling, application detection and removal tests.

These results provide preliminary evidence of Windows application compatibility through Wine on x86_64 Linux.
