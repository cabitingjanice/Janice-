import tkinter as tk

class ContactsManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contacts")
        self.root.configure(bg="skyblue")

        self.contacts = []

        self.name_label = tk.Label(root, text="Name:", bg="pink", fg="black")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(root, bg="white", fg="black")
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.phone_label = tk.Label(root, text="Phone:", bg="pink", fg="black")
        self.phone_label.grid(row=1, column=0, padx=10, pady=10)
        self.phone_entry = tk.Entry(root, bg="white", fg="black")
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact, bg="pink", fg="black")
        self.add_button.grid(row=2, columnspan=2, padx=10, pady=10)

        self.contact_listbox = tk.Listbox(root, width=40, bg="white", fg="black")
        self.contact_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.remove_button = tk.Button(root, text="Remove Contact", command=self.remove_contact, bg="pink", fg="black")
        self.remove_button.grid(row=4, columnspan=2, padx=10, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            contact = f"{name}: {phone}"
            self.contacts.append(contact)
            self.contact_listbox.insert(tk.END, contact)
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)

    def remove_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            self.contact_listbox.delete(selected_index)
            del self.contacts[selected_index[0]]

root = tk.Tk()
app = ContactsManager(root)
root.mainloop()