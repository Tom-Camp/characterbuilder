#!/usr/bin/env python3

import os
import types
import main
import json
from pathlib import Path
from character import Character

class CreateCharacter:

    def __init__(self):
        self.character = {}
        self.assign_classes()
        self.assign_races()
        self.assign_fields()
        self.error = None
        self.build_character()


    def build_character(self):
        for field_name, value in self.fields.items():
            if value['type'] == 'text':
                self.input_text(field_name, value)
            elif value['type'] == 'list':
                self.input_list(field_name, value)
            else:
                self.input_integer(field_name, value)
        self.confirm()

    def confirm(self):
        self.add_header()
        try:
            self.accept = str(input("(A)ccept, (R)edo, (C)ancel: "))
        except TypeError as e:
            self.error = e
            self.confirm()
        else:
            if self.accept.upper() == 'A':
                self.create_character()
            elif self.accept.upper() == 'R':
                self.__init__()
            elif self.accept.upper() == 'C':
                main.main()
            else:
                self.error = "Illegal choice"
                self.confirm()


    def input_text(self, name, field):
        self.add_header()
        try:
            value = str(input("{}: ".format(name).capitalize()))
        except TypeError as e:
            self.error = e
            self.input_text(name, field)
        else:
            self.character[name] = value

    def input_list(self, name, field):
        self.add_header()
        print("Allowed {}".format(field['label']))
        print("----")
        for value in field['allowed_values']:
            print(value)
        print("\n")
        try:
            self.character[name] = str(input("{}: ".format(name).capitalize()))
        except TypeError as e:
            self.error = e
            self.input_list(name, field)
        else:
            if self.character[name] not in field['allowed_values']:
                del self.character[name]
                self.error = "Value not allowed"
                self.input_list(name, field)

    def input_integer(self, name, field):
        self.add_header()
        try:
            self.character[name] = int(input("{}: ".format(name).capitalize()))
        except TypeError as e:
            self.error = e
            self.input_integer(name, field)

    def add_header(self):
        os.system('cls' if  os.name == 'nt' else 'clear')
        if self.error is not None:
            print("Input error: {}".format(self.error))
            self.error = None
        self.print_character()

    def print_character(self):
        print("Character:")
        print("[")
        for key, value in self.character.items():
            print("  {}: {}".format(key.capitalize(), value))
        print("]\n")

    def create_character(self):
        list_file = Path('characters/character_list.json')
        if not list_file.is_file():
            is_new = True
        else:
            is_new = False

        if is_new == True:
            character_list = {}
            id = 1
        else:
            with open(list_file, 'r') as file:
                character_list = json.load(file)
                id = int(sorted(character_list.keys())[-1])
                id += 1
        character_list.update({id: {'id': id, 'name': self.character['name']}})
        self.character['id'] = id
        self.character['is_new'] = True
        with open(list_file, 'w+') as file:
            json.dump(character_list, file)
        with open('characters/character-' + str(id) + '.json', 'w+') as c:
            json.dump(self.character, c)
        Character(id)


    def assign_classes(self):
        self.class_types = [
            'Barbarian',
            'Bard',
            'Cleric',
            'Druid',
            'Fighter',
            'Monk',
            'Paladin',
            'Ranger',
            'Rogue',
            'Sorcerer',
            'Warlock',
            'Wizard',
        ]

    def assign_races(self):
        self.race_types = [
            'Dragonborn',
            'Dwarf',
            'Eladrin',
            'Elf',
            'Gnome',
            'Half-elf',
            'Half-orc',
            'Halfling',
            'Human',
            'Tiefling',
        ]

    def assign_fields(self):
        self.fields = {
            'name': {
                'type': 'text',
                'default': None,
                'required': True,
            },
            'race': {
                'type': 'list',
                'allowed_values': self.race_types,
                'required': True,
                'label': 'Races',
            },
            'class': {
                'type': 'list',
                'allowed_values': self.class_types,
                'required': True,
                'label': 'Classes',
            },
            'level': {
                'type': 'int',
                'default': 1,
                'required': True,
            },
        }