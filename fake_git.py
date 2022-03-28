import argparse
import subprocess


def simulate_master_activity(trigram: str):
    subprocess.run(["git", "checkout", f"master-{trigram}"])
    subprocess.run(["cp", "templates/main.py", "src/main.py"])
    subprocess.run(["git", "add", "src/main.py"])
    subprocess.run(["git", "commit", "-m", "'pretty print'"])
    subprocess.run(["git", "push", "origin", f"master-{trigram}"])
    subprocess.run(["git", "checkout", f"dev-{trigram}"])


def clean(trigram: str):
    subprocess.run(["git", "checkout", "master"])
    subprocess.run(["git", "push", "origin", "--delete", f"master-{trigram}"])
    subprocess.run(["git", "push", "origin", "--delete", f"dev-{trigram}"])
    subprocess.run(["git", "branch", "-d", f"dev-{trigram}"])
    subprocess.run(["git", "branch", "-d", f"master-{trigram}"])


def main():
    parser = argparse.ArgumentParser(description="Fake git activity")
    parser.add_argument("command", type=str, choices=["master_activity", "clean"])
    parser.add_argument("trigram", type=str)
    args = parser.parse_args()

    command = {"master_activity": simulate_master_activity, "clean": clean}[
        args.command
    ]
    command(args.trigram)


if __name__ == "__main__":
    main()
