"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json
from pathlib import Path

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path: Path) -> list[NearEarthObject]:
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos = []
    with open(neo_csv_path) as neo_csv:
        reader = csv.DictReader(neo_csv)
        for row in reader:
            info = {
                'designation': row['pdes'] if row['pdes'] else None,
                'name': row['name'] if row['name'] else None,
                'diameter': float(row['diameter']) if row['diameter'] else float('nan'),
                'hazardous': row['pha'] == 'Y'
            }
            neo = NearEarthObject(**info)
            neos.append(neo)
    return neos


def load_approaches(cad_json_path: Path) -> list[CloseApproach]:
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    approaches = []
    with open(cad_json_path) as cad_json:
        reader = json.load(cad_json)['data']
        for value in reader:
            info = {
                'designation': value[0],
                'time': value[3],
                'distance': float(value[4]),
                'velocity': float(value[7]),
            }
            approach = CloseApproach(**info)
            approaches.append(approach)
    return approaches


if __name__ == '__main__':
    main_neos = load_neos('data/neos.csv')
    main_approaches = load_approaches('data/cad.json')
