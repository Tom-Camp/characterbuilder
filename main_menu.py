#!/usr/bin/env python3

import os
import sys
import create
import list

class MainMenu:
    _options = [
        'Create character',
        'List all characters',
        'Quit'
    ]

    def __init__(self):
        self.error = None
        self.main_menu()

    def main_menu(self):
        os.system('cls' if  os.name == 'nt' else 'clear')
        if self.error is not None:
            print("*** Illegal choise: {} ***".format(self.error))
        del self.error
        for key, value in enumerate(self._options, start=1):
            print("{}) {}".format(key, value))
        print("------------------------")
        try:
            self.choice = int(input("Choose an option: "))
        except ValueError as e:
            self.error = e
            self.main_menu()
        else:
            self.handle_choice()

    def handle_choice(self):
        if self.choice == 1:
            create.CreateCharacter()
        elif self.choice == 2:
            list.ViewCharacters()
        elif self.choice == 3:
            sys.exit(0)
        else:
            self.error = self.choice
            self.main_menu()
