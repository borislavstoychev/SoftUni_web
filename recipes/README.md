# Python Web Basics Exam – Recipes
Recipes is an application where you can add, edit and delete your own recipes. You can also open a details page of each recipe to see the time needed for the recipe, the ingredients and the full description.
##    1. Skeleton
You are provided with all the html pages, all the images and the CSS for the project.
##    2. Database
You will need 1 model:
###    • Recipe
        ◦ title - Character field with max length of 30 characters
        ◦ image_url - URL field
        ◦ description - Text field
        ◦ ingredients - Character field with max length of 250 characters
        ◦ time - Integer field
##    3. Routes
    • '/' - home page
    • '/create' - create recipe page
    • '/edit/:id' - edit recipe page
    • '/delete/:id' - delete recipe page
    • '/details/:id' - recipe details page
##    4. Pages
Home Page – 30p
### If there are no recipes created yet:

![1](https://user-images.githubusercontent.com/67734870/123087208-f3458080-d42c-11eb-9187-eca079764a95.png)

### If there are recipes:

![1](https://user-images.githubusercontent.com/67734870/123087282-09534100-d42d-11eb-82c0-bd1a7f4be051.png)

### Create Recipe Page – 20p
The ingredients should be separated by ", ". After the button is clicked, create the recipe and redirect to home.

![1](https://user-images.githubusercontent.com/67734870/123087364-1ff99800-d42d-11eb-86c7-73a63b5494a2.png)

### Edit Recipe Page – 15p
The form must be filled with the data of the recipe we want to edit. When the button is clicked, edit the recipe and redirect to home.

![1](https://user-images.githubusercontent.com/67734870/123087429-33a4fe80-d42d-11eb-82d2-1cb4c1b53404.png)

### Delete Recipe Page – 15p
The form must be filled with the data of the recipe and the fields should be disabled. When the button is clicked, delete the recipe and redirect to home.

![1](https://user-images.githubusercontent.com/67734870/123087489-491a2880-d42d-11eb-8910-169b006b2e73.png)

### Recipe Details Page – 20p
Fill the needed data. The ingredients should be separate "li" items.

![1](https://user-images.githubusercontent.com/67734870/123087558-5d5e2580-d42d-11eb-953d-719a24622860.png)

