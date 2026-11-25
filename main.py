import os

LINE = (
    "Our team building exercise was trust falls, which is ironic, "
    "because the only thing I trust in this office is that the Wi-Fi "
    "will fail right in the middle of the demo."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
