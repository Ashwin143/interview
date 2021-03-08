# In Form Builder, the user can create their own customized forms like Google Forms or Type Forms. For simplicity, the form builder has to contain Short Answer and Long Answer, Radio and Multi-select. Now we have to create a form for capturing the guest details for an event, the form has to contain following fields like 

# Name - Short text

# Mobile Number - Short text only numbers

# E-Mail

# Gender (Radio - M,F,Any)

# Subject. (MultiSelect)

# The guests can access the form and fill the details.



# You have to create a data model for the Database
# To store multiple forms with their basic conditions like min-length, max length and validation for Mobile number and E-Mail id.

# To store the captured data in the database.


# Our portal should have the following pages: 

#/forms/ (post, get, delete methods) - create, delete and list forms

/form/{id} - view forms to update the fields

/{form-id} - get a specific form to fill 

# /enquiries/ - View all the filled details

# /enquiry/{id} - To view the filled details


We will use flask for building the backend. You can read more about flask here https://flask.palletsprojects.com/en/1.1.x/.



Useful links:

https://flask.palletsprojects.com/en/1.1.x/quickstart/

https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/

https://pydantic-docs.helpmanual.io/

https://jinja.palletsprojects.com/en/2.11.x/


Rules:

=====

Feel free to ask questions. Be it about functionality or technical we are happy to help you.

You can use any open source library

You should use sqlite database

You should define the basic tables (Forms, User, User_query, User_query_history) required. Define 5-8 minimal fields required in these tables.

You should use sqlalchemy for ORM

Define the relationship between the tables using SQLAlchemyORM

You can ask for a time extension, provided you show the progress and we are satisfied with your progress.

The code should be hosted in a GitHub private repository. Also when you do this, note down how much time it took overall.


Kindly confirm the receipt of the task and your acceptance for completing the task.
