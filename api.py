import os
def runapi():
  print("Api is running!")

runapi()

key = os.environ['APIkey']

print(f"Api is running as {key}")
