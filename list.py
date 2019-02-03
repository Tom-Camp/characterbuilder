#!/usr/bin/env python3

import json
from pathlib import Path

class ViewCharacter:

    def __init__(self):
        self.file_path = 'character/character_list.json'
        self.error = {}
        self.exists()
        self.show_list()

    def exists(self):
        self.file_exists = Path(self.file_path)

    def show_list(self):
        if self.file_exists is True:
            self.load_list()
            self.add_header()
        else:
            self.error['message'] = "The list files doesn't exist"
            self.error['action'] = [
                'create',
                'main',
            ]

    def load_list(self):
        with open(self.file_path, 'r') as character_json:
            try:
                self.character = json.loads(character_json)
            except ValueError as e:
                self.error['message'] = e
                self.error['action'] = None

    def list(self):
        pass

    def add_header(self):
        pass

    def show_error(self):
        if 'message' in self.error.keys():
            error_length = len(self.error['message'])
            line = '*'
            for _ in range(error_length + 3):
                line += '*'
            line += '\n'
            print(line)
            print("* {} *".format(self.error['message']))
            print(line)
        if 'action' in self.error.keys():
            self.error_actions()

    def error_actions(self):
        pass