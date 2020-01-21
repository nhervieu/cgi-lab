#!/usr/bin/env python3

import os
import cgi
import cgitb
from templates import login_page, secret_page, after_login_incorrect
import secret
from http.cookies import SimpleCookie
cgitb.enable()


#remember that the format of the header is important

#get username and password
s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

print("Content-Type: text/html") #note: had to delete a new line here or it just printed it at the top instead of updating cookies
form_ok = username==secret.username and password==secret.password

#get username and password from cookies if there
c = SimpleCookie(os.environ["HTTP_COOKIE"])
c_username = None
c_password = None
if c.get("username"):
	c_username = c.get("username").value
if c.get("password"):
	c_password = c.get("password").value

#you can manually reset cookies in console in browser with document.cookie = "username = test" or you can just do it the storage tab

if form_ok:
	#prints to the server
	print("Set-Cookie:username=", username)
	print("Set-Cookie:password=", password)
print()
#print(login_page())  #show login page

if not username and not password:
	print(login_page())
elif username==secret.username and password==secret.password:
	print(secret_page(username,password))
else:
	print(after_login_incorrect())

cookie_ok = c_username==secret.username and c_password==secret.password
if cookie_ok:
	username = c_username
	password = c_password


#remember to set this file to executable or you will get an error code
#on firefox go to network to see params
