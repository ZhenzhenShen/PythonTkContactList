#!/usr/bin/python3
import tkinter as tk
import json
import tkinter.messagebox as messagebox
from contact import Contact

def load_contacts():
    try:
        with open('contact.json', 'r') as file:
            contact_dicts = json.load(file)
            return [Contact(**cd) for cd in contact_dicts]
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_contacts():
    with open('contact.json', 'w') as file:
        contacts_to_save = [c.__dict__ for c in contacts]
        json.dump(contacts_to_save, file)

app = tk.Tk()
app.title("Contact Manager") 

contacts = load_contacts()

def clear_contact_display():
    for widget in app.grid_slaves():
        if int(widget.grid_info()["row"])>1:
           widget.grid_forget()

def show_all():
    clear_contact_display()
    tk.Label(app,text="Name").grid(row=1,column=0)
    tk.Label(app,text="Company").grid(row=1,column=1)
    tk.Label(app,text="Phone").grid(row=1,column=2)
    tk.Label(app,text="Email").grid(row=1,column=3)
    for i, contact in enumerate(contacts, start=2):
        tk.Label(app, text=contact.name).grid(row=i, column=0)
        tk.Label(app, text=contact.company).grid(row=i, column=1)
        tk.Label(app, text=contact.phone).grid(row=i, column=2)
        tk.Label(app, text=contact.email).grid(row=i, column=3)
        tk.Button(app, text="Edit", command=lambda c=contact: open_contact_window(c)).grid(row=i, column=4)
        tk.Button(app, text="Delete", command=lambda c=contact: delete_contact(c)).grid(row=i, column=5) 

def add_contact(name, company, phone, email):
    contacts.append(Contact(name, company, phone, email))
    save_contacts()
    show_all()

    
def search_contact(contacts, name):
    # 找到所有匹配的联系人
    search_results = [c for c in contacts if c.name == name]

    # 如果找到了匹配的联系人，更新显示，否则显示提示信息
    if search_results:
        update_contact_display(search_results)
    else:
        tk.messagebox.showinfo("Search Result", "Contact not found")

def delete_contact(contact):
        contacts.remove(contact)
        save_contacts()
        show_all()  # 更新界面显示

def edit_contact(contact, name,company,phone,email):
        contact.name = name
        contact.company = company
        contact.phone = phone
        contact.email = email
        save_contacts()    
        show_all()

def save_contact(contact,name,company,phone,email):
    if contact:
        edit_contact(contact,name,company,phone,email)
    else:
        add_contact(name,company,phone,email)    

contacts = load_contacts()
show_all()

def open_contact_window(contact=None):

    window = tk.Toplevel(app)
    window.title("Edit Contact" if contact else "Add Contact")

    # 输入字段的标签
    tk.Label(window, text="Name").grid(row=0, column=0)
    name_entry = tk.Entry(window)
    name_entry.insert(0, contact.name if contact else "")
    name_entry.grid(row=0, column=1)

    tk.Label(window, text="Company").grid(row=1, column=0)
    company_entry = tk.Entry(window)
    company_entry.insert(0, contact.company if contact else "")
    company_entry.grid(row=1, column=1)

    tk.Label(window, text="Phone").grid(row=2, column=0)
    phone_entry = tk.Entry(window)
    phone_entry.insert(0, contact.phone if contact else "")
    phone_entry.grid(row=2, column=1)

    tk.Label(window, text="Email").grid(row=3, column=0)
    email_entry = tk.Entry(window)
    email_entry.insert(0, contact.email if contact else "")
    email_entry.grid(row=3, column=1)

    # 保存按钮
    save_button = tk.Button(window, text="Save", command=lambda: save_contact(contact, 
                                                                             name_entry.get(), 
                                                                             company_entry.get(), 
                                                                             phone_entry.get(), 
                                                                             email_entry.get()))
    save_button.grid(row=4, column=1)

def update_contact_display(contacts_to_display):
    # 首先，清除当前的联系人显示
    clear_contact_display()

    # 然后，根据 contacts_to_display 显示联系人
    for i, contact in enumerate(contacts_to_display, start=2):
        tk.Label(app, text=contact.name).grid(row=i, column=0)
        tk.Label(app, text=contact.company).grid(row=i, column=1)
        tk.Label(app, text=contact.phone).grid(row=i, column=2)
        tk.Label(app, text=contact.email).grid(row=i, column=3)
        tk.Button(app, text="Edit", command=lambda c=contact: edit_contact(contacts, c.name, c.company, c.phone, c.email)).grid(row=i, column=4)
        tk.Button(app, text="Delete", command=lambda c=contact: delete_contact(contacts, c)).grid(row=i, column=5)
    if not contacts_to_display:
           tk.messagebox.showinfo("Search Result", "Contact not found")

search_entry = tk.Entry(app)
search_entry.grid(row=0, column=0, sticky="w")
search_button = tk.Button(app, text="Search", command=lambda: search_contact(contacts,search_entry.get()))
search_button.grid(row=0,column=1,sticky="w")
add_button = tk.Button(app, text="Add", command=open_contact_window)
add_button.grid(row=0, column=2, sticky="e")
showAll_button = tk.Button(app, text="Show All Contacts", command=show_all)
showAll_button.grid(row=0, column=3, sticky="e")

app.mainloop()
