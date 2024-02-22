class ATM:
    def __init__(self, saldo_awal):
        self.saldo = saldo_awal

    def cek_saldo(self):
        return self.saldo

    def tarik_dana(self, jumlah):
        if jumlah > self.saldo:
            return "Saldo tidak mencukupi"
        else:
            self.saldo -= jumlah
            return f"Anda telah menarik {jumlah}. Saldo Anda sekarang {self.saldo}"

    def setor_dana(self, jumlah):
        self.saldo += jumlah
        return f"Anda telah menyetor {jumlah}. Saldo Anda sekarang {self.saldo}"

def main():
    atm = ATM(0)  

    while True:
        print("\nSelamat datang di ATM Rayo")
        print("1. Cek Saldo")
        print("2. Tarik Dana")
        print("3. Setor Dana")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            print("Saldo Anda saat ini:", atm.cek_saldo())
        elif pilihan == "2":
            jumlah = int(input("Masukkan jumlah yang ingin Anda tarik: "))
            print(atm.tarik_dana(jumlah))
        elif pilihan == "3":
            jumlah = int(input("Masukkan jumlah yang ingin Anda setor: "))
            print(atm.setor_dana(jumlah))
        elif pilihan == "4":
            print("Terima kasih telah menggunakan layanan ATM Rayo.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
