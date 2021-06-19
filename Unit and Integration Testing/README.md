# Lab: Unit and Integration Testing
##    1. Create Unit and Integration Testing on Project
You will be provided with a project called "Lost and Found". You need to create tests to cover all the functionalities of the app. The following points describe how the project works
### Home Page
On the home page you should see all the posts from the database and a button with "Create" should appear on the top. URL: "http://localhost:8000"

![1](https://user-images.githubusercontent.com/67734870/122651706-38bf3080-d143-11eb-85f9-53663f3f66ec.png)

### Create
On the create page, the following form should be displayed. URL: "http://localhost:8000/create"

![1](https://user-images.githubusercontent.com/67734870/122651714-5391a500-d143-11eb-8005-6890007ff835.png)

### Edit
On the edit page, the following form should be displayed. URL: "http://localhost:8000/edit/{id}"

![1](https://user-images.githubusercontent.com/67734870/122651741-8dfb4200-d143-11eb-80ff-d702cb501bd8.png)

### Delete
When clicking the delete button, the post should be deleted, and the index page should be refreshed
### Found and Not Found
When an item has not yet been found, a button with content "Found it!" should appear in the post. If the item has been found, the button should not be there.
Also, the labels "Not Found" and "Found" should be displayed based on whether the item has been found.
For more clarification, see the picture

![1](https://user-images.githubusercontent.com/67734870/122651766-b420e200-d143-11eb-802f-478de06cae33.png)

## Testing
### Create tests for
    • All the models
    • All the forms
    • All the views