#!/usr/bin/env python3

import yaml
import os
from pathlib import Path

class ViewCharacters:

    def __init__(self):
        self.file_path = 'characters/character_list.yaml'
        self.error = None
        self.exists()
        self.show_list()

    def exists(self):
        character_list = Path(self.file_path)
        self.file_exists = character_list.is_file()

    def show_list(self):
        if self.file_exists is True:
            self.add_header()
            self.load_list()
        else:
            self.error = "The list files doesn't exist"

    def load_list(self):
        with open(self.file_path, 'r') as character_yaml:
            try:
                self.characters = yaml.load(character_yaml)
            except ValueError as e:
                self.error['message'] = e
                self.error['action'] = None
            else:
                self.list()

    def list(self):
        for key, value in self.characters.items():
            print("{}) {}".format(key, value['name']))

    def add_header(self):
        os.system('cls' if  os.name == 'nt' else 'clear')
        print("CHARACTER LIST:")
        print("---------------")
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

