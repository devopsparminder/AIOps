import subprocess

def get_commits():
    commit_messages = subprocess.check_output(["git", "log", "--format=%H%x1f%an%x1f%ad%x1f%s", "--date=iso-strict"]).decode()
    commit_lines = commit_messages.splitlines()
    commits = []

    for commit_line in commit_lines:
        commit_hash, author, date, message = commit_line.split("\x1f")
        commit = {
            "hash": commit_hash,
            "author": author,
            "date": date,
            "message": message,
        }
        commits.append(commit)

    return commits

commits = get_commits()

def find_commits(commits, keyword):
    matches = []

    for commit in commits:
        if keyword in commit["message"].lower():
            matches.append(commit)

    return matches

keyword = "fix"
fix_commits = find_commits(commits, keyword)

if len(fix_commits) == 0:
    print("No fix commits found")
elif len(fix_commits) <= 2:
    print("Small number of fix commits")
else:
    print("Many fix commits found")

print(len(fix_commits))

for commit in fix_commits:
    if "fix" in commit["message"].lower():
        print(f"Fix commit detected: {commit['message']}")
    print(f"{commit['hash']} | {commit['author']} | {commit['date']} | {commit['message']}")
