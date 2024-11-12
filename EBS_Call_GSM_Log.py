import subprocess
import tkinter as tk
from tkinter import scrolledtext
import threading

def run_adb_logcat():
    # adb logcat komutunu çalıştırıyoruz ve çıktıyı alıyoruz
    command = ["adb", "logcat"]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    while True:
        output = process.stdout.readline()  # adb'den gelen her satırı okur
        if output == '' and process.poll() is not None:
            break
        if "Telephony:" in output and not "OllieTelephony" in output:  # "Telephony:" içeriyor ve "OllieTelephony" içermiyor
            log_output.insert(tk.END, output)  # GUI'ye ekler
            log_output.yview(tk.END)  # Her yeni satırda kaydırma yapar

def start_logcat():
    # Bu fonksiyon logcat'i ayrı bir thread'de başlatır
    threading.Thread(target=run_adb_logcat, daemon=True).start()

# GUI oluşturma
root = tk.Tk()
root.title("ADB Logcat Viewer")

# ScrolledText widget'ı ile logları göstereceğiz
log_output = scrolledtext.ScrolledText(root, width=80, height=20)
log_output.pack(padx=10, pady=10)

# Başlat butonu
start_button = tk.Button(root, text="Başlat", command=start_logcat)
start_button.pack(pady=10)

# GUI'yi başlatıyoruz
root.mainloop()
