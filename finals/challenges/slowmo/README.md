Slowmo
---------

Turing machine simulator that allows out of bounds write to an array.
Incrementing the function pointer to the helper shell function will give a
shell.

# Question Text

```
What is in this mysterious package?

nc ctf.pwn.sg 4005
```

*Creator -  amon (@nn_amon)*

# Setup Guide

0. Install docker on the hosting system
1. Replace the flag in distribute/flag
2. Build the docker image with: `sh dockerbuild.sh`
3. Replace the port with your desired port in dockerrun.sh
4. Start the docker image: `sh dockerrun.sh`
5. Test the connectivity with netcat.

# Exploit Details

Annotated working exploit is in src/exploit.py
