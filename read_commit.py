import subprocess

commit_messages = subprocess.check_output(["git", "log", "--oneline"]).decode()
commit_lines = commit_messages.splitlines()
