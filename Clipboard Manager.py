# clipboard_manager.py
import tkinter as tk
from tkinter import messagebox, simpledialog
import pyperclip
import json, os

# pasta e arquivo pra salvar clipes
file_path = "clips.json"
if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        clips = json.load(f)
else:
    clips = []

def save_clips():
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(clips, f, indent=4)

def add_clip():
    text = pyperclip.paste().strip()
    if text:
        clips.append(text)
        save_clips()
        listbox.insert(tk.END, text)
        messagebox.showinfo("Clipboard Manager", "Texto salvo")
    else:
        messagebox.showwarning("Clipboard Manager", "Não tem texto copiado")

def delete_clip():
    sel = listbox.curselection()
    if sel:
        idx = sel[0]
        clips.pop(idx)
        listbox.delete(idx)
        save_clips()
    else:
        messagebox.showwarning("Clipboard Manager", "Selecione um item")

def copy_clip():
    sel = listbox.curselection()
    if sel:
        idx = sel[0]
        pyperclip.copy(clips[idx])
        messagebox.showinfo("Clipboard Manager", "Texto copiado pro clipboard")

root = tk.Tk()
root.title("Clipboard Manager")

listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(padx=10, pady=10)

for c in clips:
    listbox.insert(tk.END, c)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Button(frame, text="Adicionar do Clipboard", command=add_clip).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Copiar Selecionado", command=copy_clip).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Deletar Selecionado", command=delete_clip).grid(row=0, column=2, padx=5)

root.mainloop()
