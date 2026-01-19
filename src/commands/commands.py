from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class CommandInvoker:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        self.commands[name] = command

    def execute_command(self, name):
        if name in self.commands:
            self.commands[name].execute()
        else:
            print(f"⚠️ Commande '{name}' non reconnue.")
