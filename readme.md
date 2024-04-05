# Blog Post Web App

This is a Advanced blog post web application built with Flask and SQLAlchemy with user authentication and authorization

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6+
- Flask
- SQLAlchemy
- Flask-Login

### Installing

1. Clone the repository
    ```
    git clone https://github.com/yourusername/blogpost-webapp.git
    ```
2. Install the dependencies
    ```
    pip install -r requirements.txt
    ```
3. Run the application
    ```
    python app.py
    ```

## Usage

The application has routes defined for creating and viewing blog posts. 

- `@views.route('/login', methods=['GET', 'POST'])`
    - This route is used for user login. It checks the entered password with the hashed password in the database. If the password is correct, the user is logged in and redirected to the home page.

- `@views.route('/logout')`
    - This route is used for user logout. It logs out the current user and redirects to the home page.

- `@views.route('/home')`
    - This route is used to display the home page. It fetches all the blog posts from the database and renders them on the home page.

- `@views.route("/create-post", methods=['GET', 'POST'])`
    - This route is used for creating a new post. If the method is POST, it checks if the text is not empty and then creates a new post.

- `@views.route("/delete-post/<id>")`
    - This route is used for deleting a post. It checks if the post exists and if the current user is the author of the post before deleting it.

- `@views.route("/edit-post/<id>", methods=['GET', 'POST'])`
    - This route is used for editing a post. It checks if the post exists and if the current user is the author of the post before allowing the post to be edited.

Please note that the routes for creating, editing, and deleting blog posts require login. If a user who is not logged in tries to access these routes, they will be redirected to the login page with a flash message.

## Built With

- Flask - The web framework used
- SQLAlchemy - SQL Toolkit and Object-Relational Mapping (ORM) system for Python

## Authors

- Your Name

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
