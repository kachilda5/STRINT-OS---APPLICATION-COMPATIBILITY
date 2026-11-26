import json
import os
import subprocess

REGISTRY = os.path.join(os.path.dirname(__file__), "applications.json")


def load_applications():
    with open(REGISTRY, "r") as file:
        return json.load(file)["applications"]


def save_applications(applications):
    with open(REGISTRY, "w") as file:
        json.dump({"applications": applications}, file, indent=4)


def list_applications():
    applications = load_applications()

    print("\nInstalled Windows Applications")
    print("------------------------------")

    if not applications:
        print("No applications registered.")
        return

    for number, app in enumerate(applications, start=1):
        print(f"{number}. {app['name']}")
        print(f"   Architecture: {app['architecture']}")
        print(f"   Status: {app['status']}")


def register_application():
    applications = load_applications()

    name = input("Application name: ").strip()
    executable = input("Executable path inside Wine drive_c: ").strip()
    architecture = input("Architecture (32-bit/64-bit): ").strip()

    if not name or not executable:
        print("Application name and executable path are required.")
        return

    prefix = os.path.expanduser("~/.wine")
    full_path = os.path.join(prefix, "drive_c", executable)

    if not os.path.isfile(full_path):
        print("Executable not found. Application was not registered.")
        return

    applications.append({
        "name": name,
        "executable": executable,
        "wine_prefix": "~/.wine",
        "architecture": architecture,
        "status": "installed"
    })

    save_applications(applications)
    print(f"{name} registered successfully.")


def launch_application():
    applications = load_applications()

    if not applications:
        print("No applications registered.")
        return

    list_applications()

    try:
        choice = int(input("\nEnter application number to launch: "))

        if choice < 1 or choice > len(applications):
            print("Invalid application selection.")
            return

        app = applications[choice - 1]
        prefix = os.path.expanduser(app["wine_prefix"])

        executable = os.path.join(
            prefix, "drive_c", app["executable"]
        )

        if not os.path.isfile(executable):
            print("Application executable not found.")
            return

        environment = os.environ.copy()
        environment["WINEPREFIX"] = prefix

        subprocess.Popen(["wine", executable], env=environment)
        print(f"Launching {app['name']}...")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\nWindows Application Manager")
        print("1. List applications")
        print("2. Launch application")
        print("3. Register application")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            list_applications()
        elif choice == "2":
            launch_application()
        elif choice == "3":
            register_application()
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()

