import asyncio
import difflib
import shlex
from typing import Tuple
import sys

async def chk_requirements(file1, file2):
    with open(file1) as f1:
        l1 = f1.readlines();l11 = [line.rstrip("\n") for line in l1]
    with open(file2) as f2:
        l2 = f2.readlines();l2 = [line.rstrip("\n") for line in l2]
    diff = difflib.unified_diff(
        l1, l2, fromfile=file1, tofile=file2, lineterm="", n=0
    )
    lns = list(diff)[2:];ifadd = [line[1:] for line in lns if line[0] == "+"];ifrm = [line[1:] for line in lns if line[0] == "-"];add = [i for i in ifadd if i not in ifrm];rm = [i for i in ifrm if i not in ifadd]
    return add, rm

async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd);process = await asyncio.create_subprocess_exec(*args,stdout=asyncio.subprocess.PIPE,stderr=asyncio.subprocess.PIPE);stdout, stderr = await process.communicate()
    return (stdout.decode("utf-8", "replace").strip(),stderr.decode("utf-8", "replace").strip(),process.returncode,process.pid,)


async def requirements(defrq , trq):
    a,r= await chk_requirements(defrq, trq)
    try:
        for i in a:
            await runcmd(f"pip install {i}")
            print(f"INFINIX: Succesfully installed {i}")
    except Exception as e:
        print(f"Error while installing requirments {str(e)}")

_inf = asyncio.get_event_loop();_inf.run_until_complete(requirements(sys.argv[1] , sys.argv[2]));_inf.close()
