import tkinter as tk
from tkinter import filedialog, messagebox

class SimpleEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Простой редактор")
        self.geometry("800x600")

        self.current_file = None

        # Меню
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Новый", command=self.new_file, accelerator="Ctrl+N")
        filemenu.add_command(label="Открыть...", command=self.open_file, accelerator="Ctrl+O")
        filemenu.add_command(label="Сохранить", command=self.save_file, accelerator="Ctrl+S")
        filemenu.add_command(label="Сохранить как...", command=self.save_file_as)
        filemenu.add_separator()
        filemenu.add_command(label="Выход", command=self.quit)
        menubar.add_cascade(label="Файл", menu=filemenu)
        self.config(menu=menubar)

        # Текстовое поле с вертикальной прокруткой
        self.text = tk.Text(self, wrap="word", undo=True)
        self.vscroll = tk.Scrollbar(self, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vscroll.set)
        self.vscroll.pack(side="right", fill="y")
        self.text.pack(fill="both", expand=True)

    def new_file(self):
        if self._confirm_discard_changes():
            self.text.delete("1.0", tk.END)
            self.current_file = None
            self.title("Простой редактор")

    def open_file(self):
        if not self._confirm_discard_changes():
            return
        path = filedialog.askopenfilename(
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
        )
        if path:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                self.text.delete("1.0", tk.END)
                self.text.insert("1.0", content)
                self.current_file = path
                self.title(f"Простой редактор — {path}")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось открыть файл:\n{e}")

    def save_file(self):
        if self.current_file:
            try:
                with open(self.current_file, "w", encoding="utf-8") as f:
                    f.write(self.text.get("1.0", tk.END))
                messagebox.showinfo("Сохранено", "Файл сохранён.")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить файл:\n{e}")
        else:
            self.save_file_as()

    def save_file_as(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
        )
        if path:
            try:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(self.text.get("1.0", tk.END))
                self.current_file = path
                self.title(f"Простой редактор — {path}")
                messagebox.showinfo("Сохранено", "Файл сохранён.")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить файл:\n{e}")

    def _confirm_discard_changes(self):
        content = self.text.get("1.0", tk.END).strip()
        if content:
            return messagebox.askyesno("Подтвердите", "Сохранить текущие изменения перед продолжением?") is False
        return True

if __name__ == "__main__":
    app = SimpleEditor()
    app.mainloop()
