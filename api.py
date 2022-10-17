import os
def runapi():
  print("Api is running!")

runapi()

my_secret = os.environ['APIkey']

print(f"Api is running as {my_secret}")
