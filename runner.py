import json
import os

running_log = []

script_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(script_dir, "running_log.json")
txt_file_path = os.path.join(script_dir, "log.txt")


def load_data(filename=json_file_path):
    """Loads existing log entries from JSON on application start."""
    global running_log

    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                running_log = json.load(file)
            print(f"📁 Loaded {len(running_log)} run(s) from past logs.")
        except json.JSONDecodeError:
            print("⚠️ Warning: Saved JSON log is corrupted or empty. Starting fresh.")
            running_log = []
        except Exception as e:
            print(f"⚠️ Error reading file: {e}. Starting fresh.")
            running_log = []
    else:
        print("📁 No existing log found. Starting a fresh running log.")


def save_data_json(filename=json_file_path):
    """Saves current runs to structured JSON format."""
    try:
        with open(filename, "w") as file:
            json.dump(running_log, file, indent=4)
        print("💾 JSON log updated.")
    except Exception as e:
        print(f"❌ Failed to save JSON log: {e}")


def save_data_txt(filename=txt_file_path):
    """Exports current runs into a formatted plain-text log."""
    try:
        with open(filename, "w") as file:
            file.write("=== RUNNING LOG ===\n\n")
            for run in running_log:
                run_string = (
                    f"Date: {run['date']} | "
                    f"Distance: {run['distance']} miles | "
                    f"Time: {run['time']} mins | "
                    f"Pace: {run['pace']} min/mile | "
                    f"Notes: {run['notes']}\n"
                )
                file.write(run_string)
        print("💾 Text log updated.")
    except Exception as e:
        print(f"❌ Failed to save text log: {e}")


def add_new_run(date, distance, time, notes):
    """Calculates mile pace and appends a new run to the log."""
    pace = round(time / distance, 2) if distance > 0 else 0

    new_run = {
        "date": date,
        "distance": distance,
        "time": time,
        "pace": pace,
        "notes": notes,
    }
    running_log.append(new_run)
    print(f"\n🏃 Run successfully added for {date}!")


def display_dashboard():
    """Displays calculated stats and all recorded logs."""
    total_miles = sum(run["distance"] for run in running_log)

    print("\n================ RUNNING DASHBOARD ================")
    print(f"Total Runs Logged  : {len(running_log)}")
    print(f"Total Cumulative   : {total_miles:.2f} miles")
    print("--------------------------------------------------")

    if not running_log:
        print("No runs recorded yet.")
    else:
        for index, run in enumerate(running_log, start=1):
            print(
                f"{index}. [{run['date']}] {run['distance']} mi in {run['time']} min "
                f"({run['pace']} min/mi) - Notes: {run['notes']}"
            )
    print("==================================================\n")


def main():
    """Main terminal loop."""
    load_data()

    # The continuous loop for the menu
    while True:
        print("\n--- MENU ---")
        print("1. Log a Run")
        print("2. View Stats")
        print("3. Exit Program")

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            print("\n--- Log a New Run ---")
            date = input("Enter date (YYYY-MM-DD): ").strip()

            try:
                distance = float(input("Enter distance (miles): "))
                time = float(input("Enter time (minutes): "))
            except ValueError:
                print("❌ Invalid input! Distance and time must be numbers.")
                continue

            notes = input("Enter notes: ").strip()

            add_new_run(date, distance, time, notes)
            save_data_json()
            save_data_txt()

        elif choice == "2":
            display_dashboard()

        elif choice == "3":
            save_data_json()
            save_data_txt()
            print("👋 Exiting program. All data saved!")
            break

        else:
            print("❌ Invalid choice. Please type 1, 2, or 3.")


if __name__ == "__main__":
    main()
