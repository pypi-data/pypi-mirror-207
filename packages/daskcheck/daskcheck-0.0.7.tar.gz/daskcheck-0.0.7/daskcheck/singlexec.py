#!/usr/bin/env python3
# v1945
from fire import Fire
import time
import platform
import datetime as dt
import os
import tempfile
from console import fg,bg
import subprocess as sp
import glob

import sys

def main( order, param):
    """
    test to RUN BASH  on remote. Must exist 1st

    It creates a file in ~/dask_sendbox - the name changes with param. Try
with ./daskcheck.py dask temod.py 1,3

    :param order: just the number returned back
    :param param: list or number, only first element taken
    """
    #time.sleep(1)
    #print("i... param===", param)
    if type(param) is list:
        pp = param[0]
    elif type(param) is tuple:
        pp = param[0]
    else:
        pp = param

    #pi = pislow(pp*1000000)
    ###print(f" {fg.yellow} {tempfile.gettempdir()} {fg.default}")
    ###cwd = tempfile.gettempdir()


    # ENTER SANDBOX

    SANDBOX = os.path.expanduser("~/dask_sandbox")
    if not os.path.exists(SANDBOX):
        os.mkdir(SANDBOX)
    cwd = os.getcwd()
    os.chdir( SANDBOX )
    nwd = os.getcwd()


    # CHECK EXISTENCE OF RUNME

    CODENAME = "./runme"

    print(f"i... SE: checking #{CODENAME}# presence ", end="")
    if not os.path.exists( f"{nwd}/{CODENAME}" ):
        print(f" {fg.red} ... [MISSING]{fg.default}")
        print(f"X... {fg.red}SE: ... prg to run  doesnt exist ...      EXIT{fg.default}")
        sys.exit(1)
    else:
        print(f" {fg.green}  .... [OK] {fg.default}")

    # RUN AND GLOB THE RESULTS

    sp.run(["./runme"])
    res = glob.glob("bashed_*") # rusults are files in FOLDER
    #print(res)

    #with open(f"aaaa{pp}","w") as f:
    #    f.write(" ")

    print(f"{bg.green} ... I created the file {pp} in sandbox ... {bg.default}")


    name, platf,   =  platform.node(), platform.machine()
    return order,[name, param,  nwd, res , dt.datetime.now().strftime("%H:%M:%S")]

if __name__=="__main__":
    Fire(main)
