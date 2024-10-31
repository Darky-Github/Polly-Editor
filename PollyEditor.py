import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, simpledialog

class SimpleTextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")
        self.root.geometry("800x600")

        # Create a text area
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, undo=True)
        self.text_area.pack(expand=True, fill='both')

        # Create a menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Create file menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_editor)

        # Create edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Undo", command=self.undo)
        self.edit_menu.add_command(label="Redo", command=self.redo)
        self.edit_menu.add_command(label="Find", command=self.find_text)

        self.file_path = None  # Track file path for saving

    def new_file(self):
        if self.text_area.edit_modified():
            if messagebox.askyesno("Warning", "You have unsaved changes. Do you want to continue?"):
                self.text_area.delete(1.0, tk.END)
        else:
            self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*"), 
                                                           ("Text Files", "*.txt"), 
                                                           ("Python Files", "*.py"), 
                                                           ("HTML Files", "*.html"), 
                                                           ("CSS Files", "*.css"), 
                                                           ("JavaScript Files", "*.js"), 
                                                           ("C++ Files", "*.cpp"), 
                                                           ("C# Files", "*.cs"), 
                                                           ("Java Files", "*.java"), 
                                                           ("Markdown Files", "*.md")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
                self.file_path = file_path

    def save_file(self):
        if self.file_path:
            with open(self.file_path, 'w') as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), 
                                                           ("Text Files", "*.txt"), 
                                                           ("Python Files", "*.py"), 
                                                           ("HTML Files", "*.html"), 
                                                           ("CSS Files", "*.css"), 
                                                           ("JavaScript Files", "*.js"), 
                                                           ("C++ Files", "*.cpp"), 
                                                           ("C# Files", "*.cs"), 
                                                           ("Java Files", "*.java"), 
                                                           ("Markdown Files", "*.md")])
        if file_path:
            self.file_path = file_path
            with open(file_path, 'w') as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)

    def exit_editor(self):
        if self.text_area.edit_modified():
            if messagebox.askyesno("Warning", "You have unsaved changes. Do you want to exit?"):
                self.root.quit()
        else:
            self.root.quit()

    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    def undo(self):
        self.text_area.edit_undo()

    def redo(self):
        if self.text_area.edit_modified():
            self.text_area.edit_redo()  # Only redo if there's something to redo

    def find_text(self):
        find_word = simpledialog.askstring("Find", "Enter the word to find:")
        if find_word:
            content = self.text_area.get(1.0, tk.END)
            occurrences = content.count(find_word)
            messagebox.showinfo("Find", f"'{find_word}' found {occurrences} times.")

if __name__ == "__main__":
    root = tk.Tk()
    editor = SimpleTextEditor(root)
    root.mainloop()

