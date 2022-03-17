from piku.core import config
from piku.commands.add import add


def install_command(args):
    dependencies = config.get('dependencies')
    for package in dependencies:
        constraint = dependencies[package]
        add(package, constraint)
