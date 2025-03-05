import os
import glob
from colorama import Fore, Back, Style
import yaml

def generate_shell(shell, content, finish_string="Live_long_and_prosper"):
        shell = str(shell)
        print(shell,content)
        for file in glob.glob(shell + '.*'):
                os.remove(file)
        f=open(shell,'w')
        f.write('#!/bin/bash\n')
        f.write('echo ==========start at : `date -d today +"%Y-%m-%d %H:%M:%S"` ==========\n')
        f.write(content + ' && ' + '\\\n')
        f.write('echo -e \"\\n\"==========end at : `date -d today +"%Y-%m-%d %H:%M:%S"` ========== && \\\n')
        f.write('echo -e \"\\n\"' + finish_string + ' 1>&2 && \\\n')
        f.write('echo ' + finish_string + ' > ' + shell + '.sign\n')
        f.write('sleep 10s')
        f.close()

def decorate_shell(shell, finish_string="Live_long_and_prosper"):
        shell = str(shell)
        for file in glob.glob(shell + '.*'):
                os.remove(file)
        cmd = 'cat ' + shell
        content = os.popen(cmd).read().rstrip()
        f=open(shell,'w')
        f.write('#!/bin/bash\n')
        f.write('echo ==========start at : `date -d today +"%Y-%m-%d %H:%M:%S"` ==========\n')
        f.write(content + ' && ' + '\\\n')
        f.write('echo -e \"\\n\"==========end at : `date -d today +"%Y-%m-%d %H:%M:%S"` ========== && \\\n')
        f.write('echo -e \"\\n\"' + finish_string + ' 1>&2 && \\\n')
        f.write('echo ' + finish_string + ' > ' + shell + '.sign\n')
        f.write('sleep 10s')
        f.close()


def _get_yaml_data(yaml_file):
    file = open(yaml_file, "r", encoding="utf-8")
    file_data = file.read()
    file.close()

    data = yaml.safe_load(file_data)
    return data

def yes_green_err_red(astring,gg,rr,yy):
    if astring == gg:
        astring = f'{Back.GREEN}{astring}{Style.RESET_ALL}'
    elif astring == rr:
        astring = f'{Back.RED}{astring}{Style.RESET_ALL}'
    elif astring == yy:
        astring = f'{Back.YELLOW}{astring}{Style.RESET_ALL}'
    else:
        pass
    return astring

def same_len(strings,lens):
    strings = str(strings)
    if len(strings) <= lens:
        strings += str(' ' * (lens-len(strings)))
    else:
        strings = strings[:lens]

    return strings

