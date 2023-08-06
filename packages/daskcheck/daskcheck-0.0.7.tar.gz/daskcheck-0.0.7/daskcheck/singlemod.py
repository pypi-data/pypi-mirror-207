#!/usr/bin/env python3
# v1945
from fire import Fire
import time
import platform
import datetime as dt
import os
import tempfile
from console import fg,bg


#-----------------------------------
def pislow(size):
    """
    calculate PI
    """
    pi = 0
    accuracy = size
    for i in range(0, accuracy):
        pi += ((4.0 * (-1)**i) / (2*i + 1))
    return float(pi)



def main( order, param):
    """
    test to write to a directory on remote

    It creates a file in ~/dask_sendbox - the name changes with param. Try
with ./daskcheck.py dask temod.py 1,3

    :param order: just the number returned back
    :param param: list or number, only first element taken
    """
    #time.sleep(1)
    print("i... param===", param)
    if type(param) is list:
        pp = param[0]
    elif type(param) is tuple:
        pp = param[0]
    else:
        pp = param

    pi = pislow(pp*1000000)
    #print(f" {fg.yellow} {tempfile.gettempdir()} {fg.default}")
    #cwd = tempfile.gettempdir()

    SANDBOX = os.path.expanduser("~/dask_sandbox")
    if not os.path.exists(SANDBOX):
        os.mkdir(SANDBOX)
    os.chdir( SANDBOX )
    cwd = os.getcwd()

    with open(f"aaaa{pp}","w") as f:
        f.write(" ")

    print(f"{bg.green} ... I created the file {pp} in sandbox ... {bg.default}")

    name, platf,   =  platform.node(), platform.machine()
    return order,[name, param, pi, cwd, pp*0.999, dt.datetime.now().strftime("%H:%M:%S")]

if __name__=="__main__":
    Fire(main)
