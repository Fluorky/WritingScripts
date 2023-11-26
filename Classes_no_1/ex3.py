import os
import datetime
import psutil  # You may need to install the psutil library if not already installed

def main():
    # 1. Create the "Reports" directory
    reports_dir = "Reports"
    os.makedirs(reports_dir, exist_ok=True)

    # 2. Generate 5 text files in "Reports" with current date, time, and CPU usage from the last 5 seconds
    for i in range(1, 6):
        report_filename = f"raport{i}.txt"
        report_path = os.path.join(reports_dir, report_filename)

        # Get current date and time
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Get CPU usage from the last 5 seconds
        cpu_usage = psutil.cpu_percent(interval=5)

        # Write information to the report file
        with open(report_path, 'w') as report_file:
            report_file.write(f"File: {report_filename}\n")
            report_file.write(f"Date and Time: {current_datetime}\n")
            report_file.write(f"CPU Usage (last 5 seconds): {cpu_usage}%\n")

    # 3. Create the "summary.txt" file with combined information from the report files
    summary_filename = "summary.txt"
    summary_path = os.path.join(reports_dir, summary_filename)

    with open(summary_path, 'w') as summary_file:
        summary_file.write("Summary of Reports:\n")

        # List the contents of the "Reports" directory
        report_files = os.listdir(reports_dir)
        for report_file in report_files:
            report_path = os.path.join(reports_dir, report_file)

            # Read information from each report file
            with open(report_path, 'r') as report_content:
                content = report_content.read()

            # Write information to the summary file
            summary_file.write(f"\n{content}\n")

    # 4. Create a new directory named "Trash" and move the report files there
    trash_dir = "Trash"
    os.makedirs(trash_dir, exist_ok=True)

    for i in range(1, 6):
        report_filename = f"raport{i}.txt"
        report_path = os.path.join(reports_dir, report_filename)
        trash_path = os.path.join(trash_dir, report_filename)

        # Move the report file to the "Trash" directory
        os.rename(report_path, trash_path)

    print("Process completed successfully.")


if __name__ == '__main__':
    main()