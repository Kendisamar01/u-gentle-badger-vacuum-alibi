from pathlib import Path


def main():
    print(Path(__file__).with_name("entry.txt").read_text().strip())


if __name__ == "__main__":
    main()
