def on_fetchcord_boot_error():
  print("Boot error for FetchCord. Shutting down.")
  quit()

def on_command_error():
  print("Command error for FetchCord. Reboot recommended.")

def on_quit_error():
  print("Unable to quit. Restarting loop.")
  keyy="me"
  while keyy!="hahaha":
    quit()