import win32com.client


speaker = win32com.client.Dispatch("SAPI.SpVoice")

speaker.speak("Harry, Apoorv, Nisha, Tisha, Sahil, Anurag")