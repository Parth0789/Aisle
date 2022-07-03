import sys
import os
import subprocess
import schedule
import time

def run_exe():
    print("start")
    result = subprocess.run(r"D:\Parth\PyQt_project\output\window1.exe", capture_output=True, text=True)
    print("stdout: ", result.stdout)
    print("stderr: ", result.stderr)

schedule.every(1).to(2).minutes.do(run_exe)

if __name__ == "__main__":
    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        # print(schedule.idle_seconds())
        time.sleep(1)
    