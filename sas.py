import json
from datetime import datetime

class HabitManager:
    def __init__(self):
        self.habits = {}
        self.load_data()

    def load_data(self):
        """Memuat data kebiasaan dari file JSON (jika ada)"""
        try:
            with open('habits.json', 'r') as file:
                self.habits = json.load(file)
        except FileNotFoundError:
            self.habits = {}

    def save_data(self):
        """Menyimpan data kebiasaan ke file JSON"""
        with open('habits.json', 'w') as file:
            json.dump(self.habits, file, indent=4)

    def add_habit(self, habit_name):
        """Menambahkan kebiasaan baru"""
        if not habit_name.strip():
            print("Nama kebiasaan tidak boleh kosong.")
            return
        if habit_name not in self.habits:
            self.habits[habit_name] = []
            self.save_data()
            print(f"Kebiasaan '{habit_name}' berhasil ditambahkan.")
        else:
            print(f"Kebiasaan '{habit_name}' sudah ada.")

    def mark_done(self, habit_name):
        """Menandai kebiasaan sebagai selesai untuk hari ini"""
        today = datetime.today().strftime('%Y-%m-%d')
        if habit_name in self.habits:
            if today not in self.habits[habit_name]:
                self.habits[habit_name].append(today)
                self.save_data()
                print(f"Kebiasaan '{habit_name}' selesai pada {today}.")
            else:
                print(f"Kebiasaan '{habit_name}' sudah ditandai selesai hari ini.")
        else:
            print(f"Kebiasaan '{habit_name}' tidak ditemukan.")

    def show_stats(self):
        """Menampilkan statistik kebiasaan"""
        if not self.habits:
            print("Tidak ada kebiasaan yang tercatat.")
            return
        for habit, dates in self.habits.items():
            print(f"Kebiasaan '{habit}' selesai {len(dates)} kali.")
            print(f"  Tanggal selesai: {', '.join(dates) if dates else 'Belum selesai.'}")

    def remove_habit(self, habit_name):
        """Menghapus kebiasaan dari daftar"""
        if habit_name in self.habits:
            del self.habits[habit_name]
            self.save_data()
            print(f"Kebiasaan '{habit_name}' telah dihapus.")
        else:
            print(f"Kebiasaan '{habit_name}' tidak ditemukan.")

def main():
    tracker = HabitManager()
    
    while True:
        print("\n--- Habit Tracker ---")
        print("1. Tambah kebiasaan")
        print("2. Tandai kebiasaan selesai")
        print("3. Tampilkan statistik kebiasaan")
        print("4. Hapus kebiasaan")
        print("5. Keluar")
        
        choice = input("Pilih opsi (1/2/3/4/5): ")

        if choice == '1':
            habit_name = input("Masukkan nama kebiasaan: ")
            tracker.add_habit(habit_name)
        elif choice == '2':
            habit_name = input("Masukkan nama kebiasaan yang sudah selesai: ")
            tracker.mark_done(habit_name)
        elif choice == '3':
            tracker.show_stats()
        elif choice == '4':
            habit_name = input("Masukkan nama kebiasaan yang ingin dihapus: ")
            tracker.remove_habit(habit_name)
        elif choice == '5':
            tracker.save_data()
            print("Data kebiasaan disimpan. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == '__main__':
    main()