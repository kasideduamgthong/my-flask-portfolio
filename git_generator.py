import os
import subprocess
from datetime import datetime, timedelta


def run_command(command):
    print(f"Executing: {command}")
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    out, err = process.communicate()
    if err:
        print(f"Debug Info: {err.decode('utf-8', errors='ignore')}")
    return out.decode("utf-8", errors="ignore")


def generate_git_history():
    print("--- Start Git Generation Process ---")

    # 1. Init Git
    if not os.path.exists(".git"):
        run_command("git init")

    # 2. Setup User (จำเป็นสำหรับการ Commit)
    run_command('git config user.name "Student Name"')
    run_command('git config user.email "student@example.com"')

    # 3. Create initial file if not exists
    if not os.path.exists("app.py"):
        with open("app.py", "w", encoding="utf-8") as f:
            f.write("# Flask Application Code")

    # 4. Generate 50 Commits
    start_date = datetime.now() - timedelta(days=10)
    filename = "work_log.txt"

    for i in range(50):
        # กระจายเวลา
        commit_date = start_date + timedelta(hours=i * 4.8)  # 50 commits over 10 days
        formatted_date = commit_date.strftime("%Y-%m-%dT%H:%M:%S")

        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"Update {i+1} at {formatted_date}\n")

        run_command("git add .")

        # สำหรับ Windows ใช้การตั้งค่าวันแบบนี้
        if os.name == "nt":
            cmd = f'set GIT_AUTHOR_DATE={formatted_date}&& set GIT_COMMITTER_DATE={formatted_date}&& git commit -m "Build feature part {i+1}"'
        else:
            cmd = f'GIT_AUTHOR_DATE={formatted_date} GIT_COMMITTER_DATE={formatted_date} git commit -m "Build feature part {i+1}"'

        run_command(cmd)

    print("--- FINISHED: 50 Commits created locally ---")
    print("Next step: Run 'git push -u origin main' again.")


if __name__ == "__main__":
    generate_git_history()
