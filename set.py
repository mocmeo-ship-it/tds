import os
Pin = input("pin: ")
CRP = input("crd: ")
username = input("username muốn set: ")
class CRD:
    def __init__(self):
        self.finish()
        def finish():
            print("Finalizing")
            os.system(f"adduser {username} chrome-remote-desktop")
            command = f"{CRP} --pin={Pin}"
            os.system(f"su - {username} -c '{command}'")
            os.system("service chrome-remote-desktop start")
            print("Finished Succesfully")
