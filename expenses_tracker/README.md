# Exam Preparation – Expenses Tracker
Expenses Tracker is an application that allows you to create your own profile (name and budget), create, edit, delete expenses and track your budget. You are also able to edit your profile data and delete your profile.
 ##    1. Skeleton
You are provided with all the html pages, all the images and the CSS for the project.
##     2. Database
You will need 2 models:
###     • Profile
        ◦ first_name - Character field with max length of 15 characters
        ◦ last_name - Character field with max length of 15 characters
        ◦ budget – Integer field
###    • Expense
        ◦ title - Character field with max length of 50 characters
        ◦ image_url - URL field
        ◦ description - Text field
        ◦ price - Float field
##    3. Routes
    • http://localhost:8000/ - home page
    • http://localhost:8000/create - create expense page
    • http://localhost:8000/edit/:id - edit expense page
    • http://localhost:8000/delete/:id - delete expense page
    • http://localhost:8000/profile - profile page
    • http://localhost:8000/profile/edit - profile edit page
    • http://localhost:8000/profile/delete - delete profile page
##    4. Pages
### Home Page
If there is no profile created yet:

![1](https://user-images.githubusercontent.com/67734870/123007324-b1cbbb80-d3c1-11eb-9c2c-5016b4a435de.png)

### If a profile has been created and there are no expenses:

![1](https://user-images.githubusercontent.com/67734870/123007388-ca3bd600-d3c1-11eb-9f59-be5330625384.png)

### There is a profile and expenses:

![1](https://user-images.githubusercontent.com/67734870/123007438-de7fd300-d3c1-11eb-82bb-206d1c6feadd.png)

### Create Expense Page

![1](https://user-images.githubusercontent.com/67734870/123007486-f2c3d000-d3c1-11eb-96cf-9b0a4a96341e.png)

### Edit Expense Page
On the page the form must be filled with the data of the expense we want to edit

![1](https://user-images.githubusercontent.com/67734870/123007569-12f38f00-d3c2-11eb-8693-025dca9454fc.png)

### Delete Expense Page
On the page the form must be filled with the data of the expense and the fields should be disabled
#### Hint: check here how to disable fields

![1](https://user-images.githubusercontent.com/67734870/123007615-2272d800-d3c2-11eb-9279-0711997c8d18.png)

### Profile Page
The budget displayed on the profile page should be after subtracting the expenses

![1](https://user-images.githubusercontent.com/67734870/123007668-361e3e80-d3c2-11eb-9ad1-8281223d2732.png)

### Edit Profile Page
On the page the form must be filled with the data of the profile

![1](https://user-images.githubusercontent.com/67734870/123007709-49310e80-d3c2-11eb-8754-6d4ede7fb0cb.png)

### Delete Profile Page
Deleting a profile should delete not only the profile info, but also all expenses

![1](https://user-images.githubusercontent.com/67734870/123007778-636aec80-d3c2-11eb-9e94-b5749c4eb2ce.png)
