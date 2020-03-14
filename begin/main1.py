# -*- coding: utf-8 -*-

from __future__ import print_function

import inspect
import sys

from commands import (
    ListCommand,
    NewCommand,
    ExitCommand,
    DoneCommand, 
    UndoneCommand,
    UserExitException,
)
from models import (
    Storage,
)
from utils import get_input_function



def get_routes():
    """`Эта функция содержит словарь возможных команд.
    Возвращает словарь возможных команд в формате:` name -> class`
    """
    return {
        ListCommand.label(): ListCommand,
        NewCommand.label(): NewCommand,
        DoneCommand.label(): DoneCommand,
        UndoneCommand.label(): UndoneCommand,
        ExitCommand.label(): ExitCommand,
    }


def perform_command(command):
    """
    Выполняет команду по имени.
    Сохраняет результат в `Storage ()`.
    : param command: имя команды, выбранное пользователем.
    """
    command = command.lower()
    routes = get_routes()

    try:
        command_class = routes[command]
        command_inst = command_class()

        storage = Storage()
        command_inst.perform(storage.items)
    except KeyError:
        print('Bad command, try again.')
    except UserExitException as ex:
        print(ex)
        raise


def parse_user_input():
    """
    Получает пользовательский ввод.
    Возвращает: строку с пользовательским вводом.
    """
    input_function = input

    message = 'Input your command: (%s): ' % '|'.join(
        {
            ListCommand.label(): ListCommand,
            NewCommand.label(): NewCommand,
            DoneCommand.label(): DoneCommand,
            UndoneCommand.label(): UndoneCommand,
            ExitCommand.label(): ExitCommand,
        }.keys()
    )
    return input_function(message)


def main():
    """
    Основной метод, работает бесконечно, пока пользователь не запустит команду `exit`.
    Или нажмите Ctrl + C в консоли.
    """
    while True:
        try:
            command = parse_user_input()
            perform_command(command)
        except UserExitException:
            break
        except Exception as e:
            print('You have done something wrong!', e)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Shutting down, bye!')
