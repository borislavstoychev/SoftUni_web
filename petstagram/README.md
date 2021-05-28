# Workshop: Petstagram
Throughout the whole module we are going to be creating a complete Django project called "Petstagram". The project will cover the following functionalities: registration/login, user profile (with profile picture that can be changed); a user will be able to view all photos of pets, open details, comment and like a photo, edit and delete their own pet photos. 
##    1. Final Project
Home Page
![petstagram1](https://user-images.githubusercontent.com/67734870/120034619-fb64f880-c005-11eb-9af2-3afa1d133a1d.png)
Register

![petstagram1](https://user-images.githubusercontent.com/67734870/120034754-31a27800-c006-11eb-98e6-905867be6b02.png)

Login
![petstagram1](https://user-images.githubusercontent.com/67734870/120034830-4e3eb000-c006-11eb-8a48-7811b8a1f831.png)
Create
![petstagram1](https://user-images.githubusercontent.com/67734870/120034904-6adae800-c006-11eb-8bb3-d8a5a60bd7c5.png)
All Pet Photos
![petstagram1](https://user-images.githubusercontent.com/67734870/120034985-8940e380-c006-11eb-9d2c-d137c287ed04.png)
Pet Details (not own)
![petstagram1](https://user-images.githubusercontent.com/67734870/120035058-a70e4880-c006-11eb-9f0a-b0693f93c773.png)
Pet Details (own)
![petstagram1](https://user-images.githubusercontent.com/67734870/120035196-dd4bc800-c006-11eb-82f5-2189379e6bea.png)
Pet Edit
![petstagram1](https://user-images.githubusercontent.com/67734870/120035258-f3598880-c006-11eb-9a29-e033e06cd835.png)
Pet Delete
![petstagram1](https://user-images.githubusercontent.com/67734870/120035311-0d936680-c007-11eb-9db7-35ad81f8dc1b.png)
Profile
![petstagram1](https://user-images.githubusercontent.com/67734870/120035351-213ecd00-c007-11eb-998f-1c2186b0b9a9.png)
##    2. Part I – The Landing Page
Setup
Let us start by creating the project
![petstagram1](https://user-images.githubusercontent.com/67734870/120035422-43384f80-c007-11eb-8e67-8d99e397ab9a.png)
Now, let us create the first app which will be called 'common' which will contain all the common parts of our project, including the language page
![petstagram1](https://user-images.githubusercontent.com/67734870/120035489-5e0ac400-c007-11eb-97b8-226feecc28df.png)
The next step will be to create the templates folder

![petstagram1](https://user-images.githubusercontent.com/67734870/120035552-7a0e6580-c007-11eb-887b-f90cfea1ea5c.png)
### Configurations
Now, we need to do some configurations. We will start with configuring our templates path
![petstagram1](https://user-images.githubusercontent.com/67734870/120035639-98746100-c007-11eb-80f7-f1b9a7ed6727.png)
![petstagram1](https://user-images.githubusercontent.com/67734870/120035746-bb067a00-c007-11eb-94cd-75ce37fbd100.png)
Then, we need to add the app we just created in the INSTALLED_APPS
![petstagram1](https://user-images.githubusercontent.com/67734870/120035852-ebe6af00-c007-11eb-8d2d-c511bbbb1581.png)
### Migrations and Starting the Project
![petstagram1](https://user-images.githubusercontent.com/67734870/120035969-146ea900-c008-11eb-95c6-a32c8058ed41.png)
![petstagram1](https://user-images.githubusercontent.com/67734870/120036025-2cdec380-c008-11eb-841f-401a74a26d5a.png)
![petstagram1](https://user-images.githubusercontent.com/67734870/120036087-45e77480-c008-11eb-9f2e-7c5e123f6eea.png)
### Creating the Landing Page
Let us first create the html file of the landing page and write the html in it

![petstagram1](https://user-images.githubusercontent.com/67734870/120036178-66173380-c008-11eb-8130-764f7f0aa59e.png)

Copy the content of the given html file and paste it in your html file
Now, we can create the view

![petstagram1](https://user-images.githubusercontent.com/67734870/120036233-79c29a00-c008-11eb-911a-f96517305b00.png)

Now, create the urls.py file and write the following code

![petstagram1](https://user-images.githubusercontent.com/67734870/120036275-9068f100-c008-11eb-9a58-68b682fb115d.png)

Finally, we need to include the urls from the app in our project

![petstagram1](https://user-images.githubusercontent.com/67734870/120036317-a4acee00-c008-11eb-961c-5a9e793c256e.png)

Now we can start the project

![petstagram1](https://user-images.githubusercontent.com/67734870/120036376-b9898180-c008-11eb-83fe-42186d5e434e.png)