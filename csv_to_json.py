# This is the code used to dump the csv to json
# you will need to download the csv from https://simplemaps.com/data/us-zips in order to run this script

import csv
import json
import unicodedata

def main():
    export_json = []

    with open('uszips.csv', newline='', encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            # skip header row
            if row[0] == "zip":
                continue
            export_json.append({
                "zip": row[0],
                "longitude": row[1],
                "latitude": row[2],
                "city": strip_accents(row[3]),
                "stateAbbreviation": row[4],
                "state": row[5],
                "county": strip_accents(row[11])
            })


    print(export_json)
    with open("geolocation.json","w") as f:
        json.dump(export_json, f, indent=5)


def strip_accents(text):
    return ''.join(char for char in
                   unicodedata.normalize('NFKD', text)
                   if unicodedata.category(char) != 'Mn')


if __name__ == "__main__":
    main()
        
