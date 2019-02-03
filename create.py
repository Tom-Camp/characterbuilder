#!/usr/bin/env python3

import os
import types

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
            if self.accept.upper == 'A':
                print("accept")
            elif self.accept.upper == 'R':
                print('redo')
            elif self.accept.upper == 'C':
                print('cancel')
            else:
                pass


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
        print('Creating')

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