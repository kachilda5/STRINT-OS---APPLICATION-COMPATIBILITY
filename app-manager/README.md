# STRINT OS – Application Manager Prototype

## 1. Overview
The Application Manager is a Python-based prototype developed to manage selected Windows applications in a Linux testing environment using Wine.

Its purpose is to provide a simple way to register, view and launch Windows applications.

## 2. Architecture

The prototype consists of four main components:

- **User Interface:** Displays the application manager menu and receives user selections.
- **Application Registry:** Stores application details in a JSON file.
- **Application Manager:** Processes registration, listing and launching requests.
- **Wine Compatibility Layer:** Runs the selected Windows executable in the Linux environment.

## 3. How It Works

1. The user opens the Application Manager.
2. The manager reads registered applications from `applications.json`.
3. The user selects an operation.
4. The manager either lists an application, registers a new one or launches an existing one.
5. Wine handles the execution of the selected Windows application.

## 4. Implemented Features

- List registered Windows applications.
- Register applications and save their details.
- Launch registered applications through Wine.
- Exit the application manager.

## 5. Testing Results

The prototype was tested in Kali Linux running on an x86_64 environment.

| Test | Result |
|---|---|
| List registered applications | Passed |
| Launch Notepad++ | Passed |
| Register Windows Notepad | Passed |
| Save application details | Passed |
| Exit application manager | Passed |

## 6. Current Limitations

This is an initial prototype tested on x86_64 Linux. ARM64 compatibility has not yet been tested.

Additional integration work will be required before this prototype can become part of the STRINT OS mobile operating system.
