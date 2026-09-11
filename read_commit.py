import subprocess

commit_messages = subprocess.check_output(["git", "log", "--oneline"]).decode()
print(commit_messages)
