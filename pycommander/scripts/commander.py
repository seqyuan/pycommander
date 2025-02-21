#!/Users/yuanzan/anaconda3/bin/python3
# -*- coding: utf-8 -*-
"""
    Auto bioinformatics workflow monitor system for SGE environment.
    Created at 20170815, Empowering enterprises for 7 years.
    Reconstitution as python package at 20250213.
"""

import click
#import yaml
import warnings
warnings.filterwarnings("ignore")
from pycommander.db import addproject, stat, dele
from pycommander.project import rerun, cron

@click.group()
def main():
    pass

# ------------------------------------------------------------------------------------
@main.command(name="addproject", short_help="Add a project to commander monitoring. \
              After adding a project to pycommander monitoring. \
              If detects that both info/info.xlsx and Filter/go.sign files exist \
              at the same time, the project analysis will be automatically started by pycommander")
@click.option('--projectid', '-p', default=None,
              help="project id, \
              eg.:\'XS05KF23080-21\'")
@click.option('--pipetype', '-t', default='scrna',
              help='pipeline type of the project')
@click.option('--workdir', '-d', 
              help='workdir, the dir should contain three dirs: info, Filter and Analysis')
def addproject_cli(projectid, pipetype, workdir):
    addproject(projectid, pipetype, workdir)

# ------------------------------------------------------------------------------------
@main.command(name="stat", short_help="Do crontab job")
@click.option('--projectid', '-p', default=None,
              help="show project stat (if not -p, will show you all the project stat, \
                if set -p will show the project's stdout and stderr.")
def stat_cli(projectid):
    stat(projectid)

# ------------------------------------------------------------------------------------
@main.command(name="rerun", short_help="re qsub an project (sh work_qsubsge.sh)")
@click.option('--projectid', '-p', 
              help="projectID")
def rerun_cli(projectid):
    rerun(projectid)

# ------------------------------------------------------------------------------------
@main.command(name="dele", short_help="Delete project(s) from pycommander database")
@click.option('--projectid', '-p', default=None,
              help="\"projectID1 projectID2 projectID3\"")
def dele_cli(projectid):
    dele(projectid)

# ------------------------------------------------------------------------------------
@main.command(name="cron", short_help="Do crontab job")
@click.option('--mode', '-m', default=1,
              help="Parameter can be 1 or 2. \
              1: check and update the AutoFlow database \
              2: clear the month ago finished or failed project")
def cron_cli(mode):
    cron(mode)



if __name__ == '__main__':
    main()

