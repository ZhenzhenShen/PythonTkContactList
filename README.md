C# and Python Comparison
I have to admit that because I started with Java, I am now more familiar with the syntax of java. It
takes me some time to understand C# and Python. But C# Maui is really friendly and powerful
with GUI. For C#, I started with console, and then jumped to the Maui. The list of solution explorers got
me confused at the beginning. It took me some time to understand the meaning of different
items. “MauiProgram.cs” is entry point, “App.xaml” and “App.xaml.cs” build framework, “AppShell.xaml” define the navigation structure. These items are built in as a part of project
template.  UI and code-behind
Python mix the UI design and code-behind in one file. C# :“xaml” is for the UI design, and corresponding “xaml.cs” is to set the functions. The benefit
is that C# separate UI and functions, which makes the code-behind more concise and easy to
read. “MessagingCenter” facilitates communication between “OpenContactPage” and “main page”
to distinguish between “AddContact” or “UpdateContact”. This mechanism is a simple message
contract that allows easier communication, just subscribing and sending messages with a
identifier of “message name”.  In C#, when I used “_” in the class name, there was some errors occurring. While python
allows “_”. It is good practice to follow naming conventions when writing code.  Data Query
“Language integrated query” is another feature of C#. LINQ queries are similar like SQL
queries, it is easy to read and write. Python’s list comprehensions are a concise way to create lists, allowing you to define
filtering conditions with an easy expression.  GUI data dynamically updating
In C#, “CollectionView” is a successor to older “ListView”, binding in “CollectionView” is used
to connect its items dynamically. “CollectionView” in xaml is connected with
“ObservableCollection<T>” in cs. “ObservableCollection<T>” is a collection used for data binding, and we don’t need to write extra code to deal with data update.“<Button Text="Delete"
Grid.Column="5" Clicked="OnDeleteClicked" CommandParameter="{Binding .}"/>”
“Binding. ” is used to bind the current contact. When I add or remove contacts, the GUI will
automatically and real-timely refreshed to reflect changes.
In python, when I add or remove contacts, I have a method of “show_all” at the end of each
method, or the GUI will not update.
In python, indentation at the beginning of lines is crucial for the structure of code. On the one
hand, it is convenient and handy. On the other hand, if I am not careful enough, I could make
mistakes.
In C#, when I add or edit contact, another “OpenContactWindow” will pop out, “async” is used
to avoid blocking main thread block. So the program does not need to wait on main thread to
improve UI responsive. The most distinguished difference between Maui C# and Python is that C# makes awesome
GUI. Python GUI is bit of original, native and primary using tkinter. Python is good for data
analysis, smaller application. C# is complex and build big applications, the built in tools and
controls make it much easier for complex functions
