# Running Log Backend

A simple Python command-line app to log workouts, track overall mileage, and save data so you don't lose your progress.

## What it Does

- Logs runs with date, distance, duration, and notes.
- Automatically calculates your mile pace (time / distance).
- Saves all entries to a JSON file (`running_log.json`) and exports a readable text file (`log.txt`).
- Shows a quick dashboard with total runs and cumulative miles.
- Prevents crashes from accidental 0-distance inputs or missing files.

## How Pace & Totals Are Calculated

- **Pace:** Time divided by distance (e.g., 30 minutes / 4 miles = 7.5 min/mile). If distance is 0, pace defaults to 0 to prevent division errors.
- **Total Miles:** Adds up the distance field across all saved entries in the log.

## How to Run It

1. Download or clone this repository.
2. Open your terminal and navigate to the project folder.
3. Run the script:
   ```bash
   python3 runner.py
