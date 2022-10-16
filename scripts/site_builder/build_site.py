#!/usr/bin/env python3

import glob
import os

from datetime import datetime
from pprint import pprint

script_dir = os.path.dirname(os.path.realpath(__file__))
source_dir = os.path.join('..', '..', 'site', 'material-images')

class Builder():
    def __init__(self):
        self.materials = []

    def get_materials(self):
        tmp_dirs = [
            file for file in glob.glob(f"{source_dir}/*")
            if os.path.isdir(file)
        ]
        for tmp_dir in tmp_dirs:
            self.materials.append( {
                "dir": tmp_dir
            })

    def prep_materials(self):
        for material in self.materials:
            dir_name = material['dir'].split('/')[-1]
            name_parts = dir_name.split('--')
            material['id'] = int(name_parts[0])
            material['date'] = datetime.strptime(name_parts[1], "%Y-%m-%d")
        self.materials.sort(key=lambda x: x['id'])

    def get_files(self):
        for material in self.materials:
            material['files'] = [
                file for file in glob.glob(f"{material['dir']}/*")
                if os.path.isfile(file)
            ]
            material['files'].sort()

if __name__ == '__main__':
    b = Builder()
    b.get_materials()
    b.prep_materials()
    b.get_files()
    pprint(b.materials)


