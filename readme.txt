The Application uses Flask framework to provide Bank Names with Details.
It takes a GET request with argument 'branch_name' to search through the database and return the results.
Database should be available locally for the Application to work.
The App uses sqlalchemy using which a direct sql statement is provided.
The results are returned in json with function 'jsonified()' in app.py if argument is provided else the results are empty.
Single route is used to perform the retrieval (the home route i.e "/")

Usage:
1. Make sure all the dependencies are installed
2. Import data locally.
3. Rename database name in the url with the name with which the database was made locally. (flask in this case)
4. Run app.py with 'flask run' in cmd line
5. Add an argument manually to the url provided eg: http://127.0.0.1:5000/?branch_name="FORT"

Time Taken: 5 hours
