#!/usr/bin/env python3

import json
import os
from pathlib import Path

class Character:

    def __init__(self, id):
        self.id = id
        self.error = None
        self.file_path = 'character/character-' + id + '.json'
        self.exists()
        self.load()

    def exists(self):
        self.character_exists = Path(self.file_path)

    def load(self):
        if self.character_exists == True:
            with open(self.file_path, 'r') as character_json:
                try:
                    self.character = json.loads(character_json)
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
