import os
import subprocess


def install_requirements():
    subprocess.check_call(["pip", "install", "-r", "requirements.txt"])


def main():
    install_requirements()
    print("Installation complete. You can now run the json_split script.")


if __name__ == "__main__":
    main()