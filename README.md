# Prerequisites

1- Have Flask installed in your dev env `pip install flask`
2- Install pytest as the unit testing module `pip install pytest`
2- run `export FLASK_APP=simple-yet-powerful-app.py` to configure flask env.

# Running the application
By simply running `flask run` the application will be accessible via localhost on default port 5000.

Access the following paths in order to get the appropiate response:
- /simplemath (Multiples two numbers)
- /statictext (Displays static text)
- /input/X (Returns the X value that it is included innto the URL)
- /json (Return a JSON response)

## Testing the Application
By running `pytest simple-yet-powerful-app.py` all the test will be executed and the propper output will be delivered.