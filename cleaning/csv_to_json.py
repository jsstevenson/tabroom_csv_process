import csv
import json
import sys
from pathlib import Path


def get_data(infile, outfile):
    reader = csv.reader(infile)
    if outfile:
        data = json.load(outfile)
    else:
        data = {}
    for line in reader:
        yr = line[0]
        tourn = line[1]
        rd = line[2]
        div = line[3]
        debate = {}
        debate["aff"] = line[4]
        debate["aff_1"] = line[5]
        debate["aff_2"] = line[6]
        debate["neg"] = line[7]
        debate["neg_1"] = line[8]
        debate["neg_2"] = line[9]
        if line[10] == "BYE":
            decisions = ["BYE"]
        else:
            decisions = {}
            decs_list = line[10:]
            for i in range(int(len(decs_list)/6)):
                judge = decs_list[6 * i]
                decision = {}
                decision["winner"] = decs_list[1 + 6 * i]
                decision["aff_1_pts"] = decs_list[2 + 6 * i]
                decision["aff_2_pts"] = decs_list[3 + 6 * i]
                decision["neg_1_pts"] = decs_list[4 + 6 * i]
                decision["neg_2_pts"] = decs_list[5 + 6 * i]
                decisions[judge] = decision
        debate["decisions"] = decisions
        if yr not in data:
            data[yr] = {}
        if tourn not in data[yr]:
            data[yr][tourn] = {}
        if div not in data[yr][tourn]:
            data[yr][tourn][div] = {}
        if rd not in data[yr][tourn][div]:
            data[yr][tourn][div][rd] = []
        data[yr][tourn][div][rd].append(debate)
    return data


def main():
    infilename = sys.argv[1]
    infile = open(infilename, 'r')
    outfilename = infilename[:-4] + '.json'
    outfile_path = Path(outfilename)
    if outfile_path.is_file():
        outfile = open(outfile_path, 'r')
        data = get_data(infile, outfile)
    else:
        data = get_data(infile, None)
    outfile = open(outfilename, 'w+')
    outfile.seek(0)
    json.dump(data, outfile)
    outfile.truncate()
    infile.close()


if __name__ == '__main__':
    main()
