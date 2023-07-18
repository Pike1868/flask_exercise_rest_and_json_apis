# Flask Cupcakes Exercise

This Flask Cupcakes Exercise is a great way to practice working with Flask, SQLAlchemy, and JavaScript to build a simple, yet fully-functional web application.

## Setup

1. Begin by setting up your virtual environment:

    ```
    python3 -m venv venv
    ```

2. Activate the virtual environment:

    ```
    source venv/bin/activate
    ```

3. Install the necessary dependencies using the requirements file:

    ```
    pip install -r requirements.txt
    ```

4. Initialize git:

    ```
    git init
    ```

5. Make an initial commit for completing Part 0:

    ```
    git add .
    git commit -m "Part 0: Setup"
    ```
###### Note: It's a good practice to commit your changes regularly. After each part of the exercise, consider making a commit. This will not only help you to track your progress but also allow you to roll back your code to a previous state if necessary. 

## Part 1: Models and SQLAlchemy

Create the main app file (`app.py`) and set up the `Cupcake` model in `models.py`. 

1. Create a PostgreSQL database for your app:

    ```
    createdb cupcakes
    ```

2. Run `seed.py` to seed the database:

    ```
    python3 seed.py
    ```

3. Define the routes for listing, getting, and creating cupcakes in `app.py`. This will practice returning JSON data, simulating an API.

## Part 2: Adding PATCH and DELETE Routes

Extend the functionality of the app by adding routes to update and delete cupcakes.

1. Define the PATCH and DELETE routes in `app.py`. 

## Part 3: Testing

1. Write tests for the PATCH and DELETE routes. 
2. Run the tests to ensure that all routes are working as expected.

## Part 4: Creating the Homepage

Finally, we'll add a static HTML page as the homepage.

1. Define a GET route at `/` in `app.py`. This should return an HTML page that includes an empty list for displaying cupcakes and a form for adding new cupcakes.

2. Write JavaScript using axios and jQuery to:
    - Query the API to get all cupcakes and add them to the page.
    - Handle form submission to let the API know about a new cupcake and update the list on the page to show it.

## Running the Application

After following the steps above, you can run the application using Flask's built-in server:

```
flask run
```
