# Lab: Model Forms
##    1. Create a new Project
Create a new project and an application.
##    2. Create a Book Model
### Each book should have the following fields:
    • title – CharField with max-length of 20
    • pages – IntegerField with default value of 0
    • description – CharField with max length of 100 and empty string as a default value
    • author – CharField with max length of 20 
##    3. Create a Model Form
### Add the following styling to the form:
    • title – TextInput with class form-control
    • pages – NumberInput with class form-control
    • author – TextInput with class form-control
    • description – Textarea with class form-control
##    4. Create the Views
Create an edit and create view (use the provided templates)
The edit view should render the following form with the current data of the book

![1](https://user-images.githubusercontent.com/67734870/121511170-08fc8400-c9f1-11eb-9f4a-c0a62a023e48.png)

The create view should render the create form

![1](https://user-images.githubusercontent.com/67734870/121511272-216c9e80-c9f1-11eb-868b-419e9252eb0e.png)

    5. Validate the Form
Validate the pages count of the form, they cannot be less than or equal to zero