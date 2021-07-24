import os
import sys
import webbrowser
def main():
    try:
    
        os.chdir(r"C:\Users\Pranav Katlana\Desktop\Ease-My-Shopping")
        webbrowser.open_new("http://127.0.0.1:8000/")
        os.system(r'manage.py runserver')
        
        # webbrowser.get("C:\Program Files\Google\Chrome\Application\chrome.exe %s").open("http://google.com")
        # # os.chdir(r"C:\Program Files\Google\Chrome\Application")
        # os.system("chrome http://127.0.0.1:8000/")
        # print("Everything is good")
        # input("")
    except:
        print("Everytning is bad")
        webbrowser.open_new("http://127.0.0.1:8000/")

main()
