#!/usr/bin/env python3

import yaml
import os
from pathlib import Path

class Character:

    def __init__(self, id):
        self.id = id
        self.error = None
        self.file_path = 'characters/character-' + str(id) + '.yaml'
        self.exists()
        self.load()

    def exists(self):
        file = Path(self.file_path)
        self.character_exists = file.is_file()

    def load(self):
        if self.character_exists == True:
            with open(self.file_path, 'r') as character_yaml:
                try:
                    self.character = yaml.load(character_yaml)
                except ValueError as e:
                    self.error = e
                    self.show_error()

    def show_error(self):
        if self.error is not None:
            error_length = len(self.error)
            line = '*'
            for _ in range(error_length + 3):
                line += '*'
            line += '\n'
            print(line)
            print("* {} *".format(self.error))
            print(line)
