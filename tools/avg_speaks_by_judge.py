import json
from pathlib import Path
import sys


def main():
    filepath = Path(sys.argv[1])
    file = open(filepath, 'r')
    data = json.load(file)
    for i in data:
        yr = data[i]
        for j in yr:
            tourney = yr[j]
            for # TODO


if __name__ == '__main__':
    main()
