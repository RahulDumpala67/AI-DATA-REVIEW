import os
import sys
import requests
from analyzer import analyze_data_script

def post_comment(repo, pr_number, message, token):
    """Post a comment directly to the Pull Request on GitHub."""
    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json"
    }
    data = {"body": message}

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("💬 Comment posted successfully on the PR!")
    else:
        print(f"⚠️ Failed to post comment. Status: {response.status_code}")
        print(response.text)

def main():
    repo = sys.argv[1]
    pr_number = sys.argv[2]
    github_token = os.getenv("GITHUB_TOKEN")
    openai_key = os.getenv("OPENAI_API_KEY")

    print(f"🔍 Reviewing PR #{pr_number} in {repo}")
    print("Fetching changed files from GitHub...")

    # Analyze data script
    feedback = analyze_data_script("sample_data_analysis.py")

    message = f"🤖 **AI Data Review Bot** says:\n\n{feedback}"

    print("\n--- AI Data Review Report ---")
    print(feedback)
    print("-----------------------------")

    # Post feedback to PR as a comment
    if github_token:
        post_comment(repo, pr_number, message, github_token)
    else:
        print("⚠️ GitHub token not found. Cannot post comment.")

if __name__ == "__main__":
    main()
