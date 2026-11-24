import tkinter as tk  # Mengimpor modul utama Tkinter untuk membuat antarmuka grafis (GUI)
from tkinter import messagebox  # Mengimpor messagebox untuk menampilkan jendela pop-up peringatan/error


class KalkulatorGUI:  # Mendefinisikan class untuk aplikasi kalkulator berbasis Tkinter
    def __init__(self, root: tk.Tk):  # Konstruktor yang dijalankan saat objek KalkulatorGUI dibuat
        self.root = root  # Menyimpan referensi jendela utama (root window)
        self.root.title("Kalkulator Sederhana")  # Mengatur judul pada title bar jendela
        self.root.geometry("300x400")  # Mengatur ukuran awal jendela (lebar 300px, tinggi 400px)
        self.root.resizable(False, False)  # Menonaktifkan fitur ubah ukuran jendela secara manual

        self.ekspresi = ""  # Menyimpan teks ekspresi matematika yang sedang diketik/diklik
        self.var_layar = tk.StringVar(value="0")  # Variabel reaktif Tkinter untuk teks layar, diawali "0"

        self._bangun_ui()  # Memanggil method internal untuk menyusun komponen antarmuka

    def _bangun_ui(self) -> None:  # Method untuk membangun tampilan layar dan tombol kalkulator
        layar = tk.Entry(  # Membuat widget Entry sebagai layar tampilan angka
            self.root,  # Menempatkan widget di dalam jendela utama
            textvariable=self.var_layar,  # Menghubungkan isi layar dengan variabel self.var_layar
            font=("Segoe UI", 22, "bold"),  # Mengatur jenis, ukuran, dan ketebalan huruf layar
            justify="right",  # Meratakan teks angka ke sisi kanan layar seperti kalkulator asli
            bd=10,  # Mengatur ketebalan border/bingkai layar
            state="readonly",  # Membuat layar hanya baca agar tidak diketik manual sembarangan
        )
        layar.pack(fill=tk.X, padx=10, pady=12)  # Menempatkan layar secara penuh horizontal dengan margin

        frame_tombol = tk.Frame(self.root)  # Membuat container Frame untuk menampung grid tombol
        frame_tombol.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))  # Mengisi sisa ruang jendela

        tombol_layout = [  # Mendefinisikan susunan baris dan kolom tombol kalkulator
            ["7", "8", "9", "/"],  # Baris ke-0
            ["4", "5", "6", "*"],  # Baris ke-1
            ["1", "2", "3", "-"],  # Baris ke-2
            ["C", "0", "=", "+"],  # Baris ke-3
        ]

        for r, baris in enumerate(tombol_layout):  # Melakukan literasi tiap baris beserta indeks barisnya (r)
            frame_tombol.rowconfigure(r, weight=1)  # Memberi bobot tinggi baris agar tombol proporsional
            for c, teks in enumerate(baris):  # Melakukan iterasi tiap tombol beserta indeks kolomnya (c)
                frame_tombol.columnconfigure(c, weight=1)  # Memberi bobot lebar kolom agar tombol proporsional
                btn = tk.Button(  # Membuat tombol untuk karakter pada posisi (r, c)
                    frame_tombol,  # Menempatkan tombol di dalam frame_tombol
                    text=teks,  # Menampilkan label karakter pada tombol
                    font=("Segoe UI", 14, "bold"),  # Mengatur font tombol
                    command=lambda t=teks: self._klik_tombol(t),  # Menjalankan _klik_tombol dengan nilai t saat diklik
                )
                btn.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)  # Menempatkan tombol memenuhi sel grid

    def _klik_tombol(self, karakter: str) -> None:  # Method yang dipanggil setiap kali tombol diklik
        if karakter == "C": 
            self.ekspresi = ""  # Mengosongkan ekspresi yang tersimpan
            self.var_layar.set("0")  # Mengembalikan tampilan layar menjadi "0"
        elif karakter == "=": 
            self._hitung()  # Memanggil method _hitung() untuk memproses hasil
        else: 
            self.ekspresi += karakter  # Menambahkan karakter tombol ke akhir string ekspresi
            self.var_layar.set(self.ekspresi)  # Memperbarui tampilan layar dengan ekspresi terbaru

    def _hitung(self) -> None:  # Method untuk menghitung hasil dari ekspresi matematika
        try:  # Memulai blok try untuk menangkap potensi error saat perhitungan
            hasil = eval(self.ekspresi)  # Mengevaluasi string ekspresi matematika menjadi nilai hasil
            self.var_layar.set(str(hasil))  # Menampilkan hasil perhitungan ke layar dalam bentuk string
            self.ekspresi = str(hasil)  # Menyimpan hasil ke self.ekspresi agar bisa dihitung lanjutan
        except ZeroDivisionError:  # Menangkap error jika terjadi pembagian dengan nol
            messagebox.showerror("Error", "Tidak bisa membagi dengan nol!")  # Menampilkan pop-up error pembagian nol
            self.ekspresi = ""  # Mereset ekspresi menjadi kosong
            self.var_layar.set("0")  # Mereset layar kembali ke "0"
        except Exception:  # Menangkap error umum (misal sintaks/ekspresi tidak valid)
            messagebox.showerror("Error", "Format perhitungan tidak valid!")  # Menampilkan pop-up error format
            self.ekspresi = ""  # Mereset ekspresi menjadi kosong
            self.var_layar.set("0")  # Mereset layar kembali ke "0"


if __name__ == "__main__":  # Menjalankan kode di bawah hanya jika file ini dieksekusi langsung
    root = tk.Tk()  # Membuat objek jendela utama Tkinter
    app = KalkulatorGUI(root)  # Menginstansiasi aplikasi kalkulator dengan jendela root
    root.mainloop()  # Menjalankan event loop GUI agar jendela tetap terbuka dan responsif

    