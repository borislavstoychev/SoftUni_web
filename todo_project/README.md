# Lab: Models and MTV Pattern
In this exercise we are going to create a very simple To-do App. At the end, it will look something like this
![1](https://user-images.githubusercontent.com/67734870/121031848-660af680-c7b3-11eb-9ada-d2174b71200d.png)
 ##   1. The Basics
Let us start by creating a new Django Project
![1](https://user-images.githubusercontent.com/67734870/121032032-8fc41d80-c7b3-11eb-99d5-24323e9bf439.png)
Then, we are going to create our app
![1](https://user-images.githubusercontent.com/67734870/121032208-bb470800-c7b3-11eb-9299-c5ec34e57c92.png)
Next, we need to import our app in the settings.py file in the project
![1](https://user-images.githubusercontent.com/67734870/121032275-cdc14180-c7b3-11eb-9041-6af9fc267997.png)
 ##   2. Setting up the App
Now, let us create an index view in our app
![1](https://user-images.githubusercontent.com/67734870/121032365-e0d41180-c7b3-11eb-9d3c-46c500855953.png)
Before we create the HTML file, let us create the urls.py file in the app
![1](https://user-images.githubusercontent.com/67734870/121032422-ee899700-c7b3-11eb-832f-1b778d7e2577.png)


Now, since we do not yet have the index.html file, let us create it in the templates folder. You can copy the following HTML
```
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Todo App</title>
</head>
<style>
    h1 {
        margin: 5px;
        text-align: center;
        padding: 5px;
    }

    h2 {
        text-align: center;
        text-decoration: underline;
    }

    div.done {
        color: green;
        font-weight: bold;
    }

    div.open {
        color: red;
        font-weight: bold;
    }

    div.todo {
        display: block;
        background: white;
        border: 2px solid white;
        border-radius: 10px;
        margin: 5px;
        text-align: center;
    }

    div.todo p {
        font-size: 20px;
        font-weight: bold;
        text-decoration: underline;
    }

    div.todo div.description {
        padding: 10px;
    }

    div.container {
        background: greenyellow;
        display: flex;
        flex-direction: column;
        margin: 0 auto;
        padding: 10px;
    }
</style>
<body>
    <h1>My Todo List</h1>
</body>
</html>
```

### Note: It is a bad practice to write the style in the HTML file. Here we use it, because we have not yet learned about static files
Let us include in the project the urls from the app
![1](https://user-images.githubusercontent.com/67734870/121032899-62c43a80-c7b4-11eb-8e7f-c1b3a2a8a2e7.png)
    3. Configuring the Database
Before we test our project, let us configure the database. First, we go to the settings.py file and write the following
![1](https://user-images.githubusercontent.com/67734870/121032974-74a5dd80-c7b4-11eb-8d33-725d31f89f9a.png)
Now, let us connect to PostgreSQL
![1](https://user-images.githubusercontent.com/67734870/121033086-8b4c3480-c7b4-11eb-8135-d60ca8413483.png)
and create a new database with name "dbtodo"
![1](https://user-images.githubusercontent.com/67734870/121033149-999a5080-c7b4-11eb-9076-2ded2e815b52.png)
Now we are ready to test our project for the first time. Start the project and open it in the browser
![1](https://user-images.githubusercontent.com/67734870/121033213-a8810300-c7b4-11eb-963e-ebac9075f91b.png)





##    4. Creating the Todo Model
Now, it is time to create our model. Go to the models.py file and create a class called Todo
![1](https://user-images.githubusercontent.com/67734870/121033350-c8b0c200-c7b4-11eb-9e23-23084f2440a1.png)
The next step is to register the model in the admin.py file in the app
![1](https://user-images.githubusercontent.com/67734870/121033413-d9613800-c7b4-11eb-845f-1b2f631f760f.png)
Finally, let us make the migrations
![1](https://user-images.githubusercontent.com/67734870/121033524-f269e900-c7b4-11eb-99b0-57cb6f4800e5.png)
##    5. Adding Context to the View
Now, let us go back to the views.py file and edit the index, so it passes a context to the template
![1](https://user-images.githubusercontent.com/67734870/121033613-03b2f580-c7b5-11eb-9b0a-6398fee3cc4b.png)
    6. Implement Template Logic
Before testing our project again, let us loop through all our todos in the index.html file
![1](https://user-images.githubusercontent.com/67734870/121033678-10cfe480-c7b5-11eb-9fe5-6093cc4d22d0.png)
Now let us test the project again
![1](https://user-images.githubusercontent.com/67734870/121033742-1e856a00-c7b5-11eb-92a6-3fcd8b269a7f.png)
Since our database is empty, we do not render any todos, just the h2 tag with the "No TODOS" text in it.
 ##   7. Practicing Some CRUD Operations
### Since we yet do not know how to use html forms to create objects in the database, we have two options:
    • Use the Django Admin to manually create some objects (try doing it)
    • Use the shell to create some objects using the Django Database API (what we are going to do)


Open the terminal and type the following: python manage.py shell
Now you should see something like this
![1](https://user-images.githubusercontent.com/67734870/121033914-42e14680-c7b5-11eb-8976-61fadb5aff5f.png)
Now let us create a new Todo
![1](https://user-images.githubusercontent.com/67734870/121033974-52608f80-c7b5-11eb-9b91-f5bf5580b753.png)
Refresh the page in the browser to see the new Todo
![1](https://user-images.githubusercontent.com/67734870/121034037-60161500-c7b5-11eb-81e3-c4b1863d4595.png)
Next, let us try and edit the Todo
![1](https://user-images.githubusercontent.com/67734870/121034151-758b3f00-c7b5-11eb-900f-d015d22bf0cd.png)
You can now see the changes in the browser.
### With that we are done with our Todo App. Try adding some more features in the app to practice what you have learned 😊