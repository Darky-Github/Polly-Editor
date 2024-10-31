import tkinter as tk
from tkinter import filedialog, messagebox

class PollyEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Polly Editor")  # Set the title
        
        # Initial theme
        self.is_dark_mode = False
        
        # Create text area with undo functionality
        self.text_area = tk.Text(self.master, bg='white', fg='black', undo=True)
        self.text_area.pack(expand=True, fill='both')

        # Create menu
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)

        # File menu
        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save As", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.quit)

        # Edit menu
        self.edit_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.undo)
        self.edit_menu.add_command(label="Redo", command=self.redo)

        # View menu
        self.view_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="View", menu=self.view_menu)
        self.view_menu.add_command(label="Toggle Dark/Light Mode", command=self.toggle_theme)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt"),
                                                           ("Python files", "*.py"),
                                                           ("C files", "*.c"),
                                                           ("C++ files", "*.cpp"),
                                                           ("C# files", "*.cs"),
                                                           ("HTML files", "*.html"),
                                                           ("JavaScript files", "*.js"),
                                                           ("PHP files", "*.php"),
                                                           ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, file.read())
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {e}")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                   filetypes=[("Text files", "*.txt"),
                                                              ("Python files", "*.py"),
                                                              ("C files", "*.c"),
                                                              ("C++ files", "*.cpp"),
                                                              ("C# files", "*.cs"),
                                                              ("HTML files", "*.html"),
                                                              ("JavaScript files", "*.js"),
                                                              ("PHP files", "*.php"),
                                                              ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(self.text_area.get(1.0, tk.END).strip())
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")

    def undo(self):
        self.text_area.edit_undo()  # Undo the last action

    def redo(self):
        self.text_area.edit_redo()  # Redo the last undone action

    def toggle_theme(self):
        if self.is_dark_mode:
            self.text_area.config(bg='white', fg='black')
            self.master.config(bg='white')
            self.is_dark_mode = False
        else:
            self.text_area.config(bg='black', fg='white')
            self.master.config(bg='black')
            self.is_dark_mode = True

if __name__ == "__main__":
    root = tk.Tk()
    editor = PollyEditor(root)
    root.mainloop()
