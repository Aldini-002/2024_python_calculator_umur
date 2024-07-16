import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def hitung_umur():
    try:
        tanggal_lahir = entry_tanggal.get()
        bulan_lahir = entry_bulan.get()
        tahun_lahir = entry_tahun.get()
        
        tanggal_lahir = datetime.strptime(f"{tanggal_lahir}-{bulan_lahir}-{tahun_lahir}", "%d-%m-%Y")
        hari_ini = datetime.today()
        umur = hari_ini.year - tanggal_lahir.year - ((hari_ini.month, hari_ini.day) < (tanggal_lahir.month, tanggal_lahir.day))
        
        label_hasil.config(text=f"Umur Anda: {umur} tahun")
        
    except ValueError:
        messagebox.showerror("Error", "Masukkan tanggal, bulan, dan tahun yang valid")

# Inisialisasi GUI
root = tk.Tk()
root.title("Kalkulator Umur")

# Label dan Entry untuk tanggal lahir
label_tanggal = tk.Label(root, text="Tanggal lahir (DD):")
label_tanggal.grid(column=0, row=0, padx=10, pady=10)

entry_tanggal = tk.Entry(root)
entry_tanggal.grid(column=1, row=0, padx=10, pady=10)

# Label dan Entry untuk bulan lahir
label_bulan = tk.Label(root, text="Bulan lahir (MM):")
label_bulan.grid(column=0, row=1, padx=10, pady=10)

entry_bulan = tk.Entry(root)
entry_bulan.grid(column=1, row=1, padx=10, pady=10)

# Label dan Entry untuk tahun lahir
label_tahun = tk.Label(root, text="Tahun lahir (YYYY):")
label_tahun.grid(column=0, row=2, padx=10, pady=10)

entry_tahun = tk.Entry(root)
entry_tahun.grid(column=1, row=2, padx=10, pady=10)

# Tombol hitung
button_hitung = tk.Button(root, text="Hitung Umur", command=hitung_umur)
button_hitung.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# Label hasil
label_hasil = tk.Label(root, text="Umur Anda: ")
label_hasil.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Menjalankan GUI
root.mainloop()
