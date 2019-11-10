## Fan-Fictor Web Application

#### Description:

​	Fan-Fictor is a web application using python and the django web framework. I made it using the textbook Python Crash Course: A Hands-on, Project-based Introduction to Programming. It's a simple website where users can log in and write fan fiction on whatever subject they like. They can write a new story for Lord of The Rings to whatever they want. It started off as just a test site to see what I can do with the framework but I kept adding features. 

​	Users can create public or private stories, each story have their own chapters. Users can register an account. Users can post comments and authors can remove comments. I see about adding more features, but I think I may just move on.

#### Demo

![site demo](C:\Users\Jonathan\Desktop\fan_fictor\site demo.gif)

#### Installation 

- In the command prompt 

```cmd
cd Desktop
python get-pip.py
pip install virtual env
cd fan_fictor
virtualenv env 
```

Once this is done, activate the virtualenv. 

```cmd
on Windows, virtualenv creates a batch file
\env\Scripts\activate.bat
to activate virtualenv on Windows, activate script in Scripts folder.
\path\to\env\Scripts\activate
Example:
C:\Users\'Username'\venv\Scripts\activate.bat
OR
C:\Users\'Username'\venv\Scripts\activate
```

Once you're in the virtual environment.  Run this command in the terminal.

```cmd
C:\Users\'Username'\venv\Scripts\activate.bat
OR
C:\Users\'Username'\venv\Scripts\activate
```

Then run the server.

```cmd
python manage.py runserver
```

