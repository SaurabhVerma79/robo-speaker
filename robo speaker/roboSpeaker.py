import os

if __name__=='__main__':
    print("welcome to RoboSpeaker 1.1. created my saurabh")
    while True:
        x=input("Enter what you want me to speak : ")
        if x=='q':
            os.system("PowerShell -Command Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('bye bye friend');")
            break
        command=f"PowerShell -Command Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}');"
        os.system(command)