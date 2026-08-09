from horizons_api import data
import csv


def extract_csv(text: str):
    """Return only the content between SOE and EOE markers as CSV text."""
    # if not text:
    #     return ""

    if isinstance(text, dict):
        text = text.get("result", "")

    normalized = text.replace("\r\n", "\n").replace("\r", "\n")

    tables = []
    start = 0

    While True: 

    # start = None
    # for marker in ("$$SOE", "SOE"):
    #     idx = normalized.find(marker)
    #     if idx != -1:
    #         start = idx + len(marker)
    #         break

    # if start is None:
    #     raise ValueError("SOE marker not found")

    # end = None
    # for marker in ("$$EOE", "EOE"):
    #     idx = normalized.find(marker, start)
    #     if idx != -1:
    #         end = idx
    #         break

    # if end is None:
    #     raise ValueError("EOE marker not found")

    lines = [line.strip() for line in normalized[start:end].splitlines() if line.strip()]
    return "\n".join(lines) + "\n"


planet_data = extract_csv(data)
print(planet_data)



#converting to CSV:
def to_csv:
    with open("output.csv")