import tkinter as tk
from tkinter import ttk, filedialog
#
#
class SourceSelector:
    def __init__(self, initialdir):
        self.source = None
        self.kind = None
        self.initialdir = initialdir
        self.root = tk.Tk()
        self.root.title("Choose a star list")
        self.url_var = tk.StringVar()
        ttk.Label(self.root, text="URL:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(self.root, textvariable=self.url_var, width=50).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.root, text="Select File", command=self.on_file).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(self.root, text="Use URL", command=self.on_url).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(self.root, text="Cancel", command=self.on_cancel).grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        self.root.protocol("WM_DELETE_WINDOW", self.on_cancel)
    #
    #
    def on_file(self):
        path = filedialog.askopenfilename(parent=self.root, title="Select Data", initialdir=self.initialdir, filetypes=[("All Files", "*.*")])
        if path:
            self.source = path
            self.kind = "file"
            self.root.destroy()
    #
    #
    def on_url(self):
        url = self.url_var.get().strip()
        if url:
            self.source = url
            self.kind = "url"
            self.root.destroy()
    #
    #
    def on_cancel(self):
        self.root.destroy()
    #
    #
    def run(self):
        self.root.mainloop()
        return self.source, self.kind
#
#
def data_selector(initialdir):
    return SourceSelector(initialdir).run()
#
#