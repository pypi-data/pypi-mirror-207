from  pitv import pitv
import os
import sys
import redis
import time
import subprocess
import json
import argparse
import requests

def runme(command):
  commandlist = command.split(" ")
  result = subprocess.run(commandlist, capture_output=True)
  payload = {"returncode": result.returncode, "stdout": result.stdout.decode(), "stderr": result.stderr }
  return payload

def main():
    parser = argparse.ArgumentParser(description="Pictures In The Vaut", usage="pitv <action> \n\n \
               \
               version : 0.1.2 BETA \n                                              \
               actions:\n                                                      \
               save         save picture in the vault \n  \
               \
               2023 Knowit Miracle\
               ")
    parser.add_argument('action', metavar='<action>', type=str, nargs='+', help='setup netbox')
    args = parser.parse_args()
    ready = False
    print("check if we are ready to go")

    if args.action[0] == "save":
        pitv.pitv()