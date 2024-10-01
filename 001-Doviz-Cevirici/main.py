import tkinter as tk
from tkinter import ttk, messagebox
import requests

root = tk.Tk()
root.title("Döviz Çevirici")
root.geometry("400x300")

currency_dict = {
    "Türk Lirası": "TRY",
    "ABD Doları": "USD",
    "Avustralya Doları": "AUD",
    "Kanada Doları": "CAD",
    "İsviçre Frangı": "CHF",
    "Danimarka Kronu": "DKK",
    "Euro": "EUR",
    "İngiliz Sterlini": "GBP",
    "Japon Yeni": "JPY",
    "Norveç Kronu": "NOK",
    "Rus Rublesi": "RUB",
    "Suudi Arabistan Riyali": "SAR",
    "İsveç Kronu": "SEK"
}


tk.Label(root, text="Kaynak Para Birimi:").pack(pady=5)
source_currency = ttk.Combobox(root, values=list(currency_dict.keys()))
source_currency.pack(pady=5)

tk.Label(root, text="Hedef Para Birimi:").pack(pady=5)
target_currency = ttk.Combobox(root, values=list(currency_dict.keys()))
target_currency.pack(pady=5)

tk.Label(root, text="Miktar:").pack(pady=5)
amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)


def print_selected_value():
    source = source_currency.get()
    target = target_currency.get()
    amount = amount_entry.get()

    if not source or not target or not amount:
        messagebox.showwarning("Eksik Bilgi", "Lütfen tüm alanları doldurun.")
        return

    source_short = currency_dict.get(source)
    target_short = currency_dict.get(target)

    url = "https://api.collectapi.com/economy/exchange"

    headers = {
        'content-type': "application/json",
        'authorization': "Burasıı"  # <- Buraya kendi tokeninizi yazınız.
    }

    params = {
        "int": amount,
        "to": target_short,
        "base": source_short
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        calculatedstr_value = data['result']['data'][0]['calculatedstr']
        messagebox.showinfo("Hesaplama Sonucu", f"{amount} {source_short} = {calculatedstr_value} {target_short}")
    else:
        messagebox.showerror("Hata", "API isteği başarısız oldu.")

tk.Button(root, text="Hesapla", command=print_selected_value).pack(pady=10)
root.mainloop()
