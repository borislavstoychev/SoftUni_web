# Python Web Basics Exam – Notes

*Notes is an application where we create our own profiles and manage our notes. We can open a details page of each note to see the full content.*
##    1. Skeleton
You are provided with all the html pages, all the images and the CSS for the project.
##    2. Database
You will need 2 models:
###    • Profile
        ◦ first_name - Character field with max length of 20 characters
        ◦ last_name - Character field with max length of 20 characters
        ◦ age - Integer field
        ◦ image_url - URL field
###    • Note
        ◦ title - Character field with max length of 30 characters
        ◦ image_url - URL field
        ◦ content - Text field

##    3. Routes
    • http://localhost:8000/ - home page
    • http://localhost:8000/add - add note page
    • http://localhost:8000/edit/:id - edit note page
    • http://localhost:8000/delete/:id - delete note page
    • http://localhost:8000/details/:id - note details page
    • http://localhost:8000/profile - profile page

##    4. Pages
### Home Page – 20p
#### If there is no profile created yet:

![1](https://user-images.githubusercontent.com/67734870/123549754-029d3480-d773-11eb-9f14-4088e7726d16.png)

#### If a profile has been created and there are no notes:

![1](https://user-images.githubusercontent.com/67734870/123549779-1d6fa900-d773-11eb-8e97-f95289da61c6.png)

#### There is a profile and notes:

![1](https://user-images.githubusercontent.com/67734870/123549794-34ae9680-d773-11eb-8c29-4d4040c5ce21.png)

### Add Note Page – 15p
After the button "Publish" is clicked, add the note and redirect to home:

![1](https://user-images.githubusercontent.com/67734870/123549815-4d1eb100-d773-11eb-97d1-a22012ed4f7c.png)

###  Edit Note Page – 15p
The form must be filled with the data of the note we want to edit. When the button "Edit" is clicked, edit the note and redirect to home.

![1](https://user-images.githubusercontent.com/67734870/123549841-63c50800-d773-11eb-8483-b2f30d833c4a.png)

### Delete Note Page – 15p
The form must be filled with the data of the note and the fields should be disabled. When the button "Delete" is clicked, delete the note and redirect to home.

![1](https://user-images.githubusercontent.com/67734870/123549875-7ccdb900-d773-11eb-9123-9dbebeaf4252.png)

### Note Details Page – 20p
Fill the needed data: title, image, and content. Also, the view should have two buttons at the bottom – "Edit" and "Delete".

![1](https://user-images.githubusercontent.com/67734870/123549892-97079700-d773-11eb-8486-3e0cf1ce2798.png)

### Profile Page - 15
The number of notes you have at the current moment should be displayed on the profile page. When the button "Delete" is clicked, delete the profile and all notes, then redirect to home page with no profile:

![1](https://user-images.githubusercontent.com/67734870/123549917-af77b180-d773-11eb-83cb-5d39d86e30b2.png)

