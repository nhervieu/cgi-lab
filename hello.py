#!/usr/bin/env python3

import os
import json
import cgi
import cgitb
cgitb.enable()

#TODO: make it print nicely
env_s = json.dumps(dict(os.environ))
env_j = json.loads(env_s)

print("Content-Type: text/html\n")
print()
#print("<!doctype html><title>Hello</title><h2>Hello World</h2>")

#show environment variables
print(json.dumps(dict(os.environ),indent = 2))

#Q2: can add query like http://localhost:8080/hello.py?hello=1