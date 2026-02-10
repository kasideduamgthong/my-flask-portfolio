import os
import subprocess
from datetime import datetime, timedelta


def run_command(command):
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    out, err = process.communicate()
    return out.decode("utf-8", errors="ignore")


def generate_git_history():
    print("--- Starting Git Generation (50 Commits / 10 Days) ---")

    # 1. Init Git if needed
    if not os.path.exists(".git"):
        run_command("git init")

    run_command("git checkout -b main")
    run_command('git config user.name "Kasided Uamgthong"')
    run_command('git config user.email "kasided@example.com"')

    # 2. Make sure README exists
    readme_text = "# Flask Portfolio Project\n\nDeveloped with Flask and Tailwind CSS."
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_text)

    # 3. Commits Loop
    start_date = datetime.now() - timedelta(days=10)

    for i in range(50):
        # Calc time (distribute 50 commits over 10 days)
        # Roughly 5 commits per day, spaced out
        commit_date = start_date + timedelta(hours=i * 4.8)
        iso_date = commit_date.strftime("%Y-%m-%dT%H:%M:%S")

        # Modify a log file
        with open("work_log.txt", "a") as f:
            f.write(f"Commit {i+1} completed at {iso_date}\n")

        run_command("git add .")

        # Windows-specific date setting for Git
        msg = f"Improvement phase {i+1}: Feature update"
        env_setup = (
            f"set GIT_AUTHOR_DATE={iso_date}&& set GIT_COMMITTER_DATE={iso_date}&& "
        )
        run_command(f'{env_setup}git commit -m "{msg}"')

        if i % 10 == 0:
            print(f"Progress: {i}/50 commits created...")

    print("--- SUCCESS: 50 Commits Created! ---")
    print("Next: git push -u origin main")


if __name__ == "__main__":
    generate_git_history()
