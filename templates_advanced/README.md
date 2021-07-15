# Lab: Templates Advanced
# Pythons Wiki

![1](https://user-images.githubusercontent.com/67734870/124132128-291be200-da89-11eb-9dfd-5abf15ca21c5.png)

## You are provided with a working project. Refactor all the templates, so you use template inheritance
### Tips
    • Create a separate folder called common. In the folder create two separate files for the header and the footer (header.html and footer.html)
    • Create a file called base.html in which the header and the footer templates are included and create a block called content
    • Refactor the create and index files to extend the base file
    • Separate the html for the python details in a separate html file
    • In the index.html in the for loop use the created template for the python details
## Example Structure

![1](https://user-images.githubusercontent.com/67734870/124132211-40f36600-da89-11eb-817c-ff390c260177.png)

## base.html

![1](https://user-images.githubusercontent.com/67734870/124132266-4fda1880-da89-11eb-8432-b904519bf919.png)

## create.html

![1](https://user-images.githubusercontent.com/67734870/124132542-9891d180-da89-11eb-87eb-b856a93e8df8.png)

## index.html

![1](https://user-images.githubusercontent.com/67734870/124132351-65e7d900-da89-11eb-9662-ad8de647b21b.png)

## python_detail.html

![1](https://user-images.githubusercontent.com/67734870/124132630-b2cbaf80-da89-11eb-8f5c-b38a36857175.png)


# Lab: Media Files
## Pythons Wiki (with Image Upload)
Refactor the project from the previous lecture, so instead of link to an image of a python, it works with file upload. 
### Steps
    • Create a folder called 'media' and a folder 'images' in it
    • Add the needed configuration for the media files to work
    • Add enctype="multipart/form-data" to your form
    • Change the image field in the Python model to ImageField()
    • Add appropriate styling to the field using bootstrap (as shown below)
```
<div class="custom-file">
    <label class="custom-file-label" for="image">Choose Image File</label>
    {{ form.image }}
</div>
<input type="submit" value="Create" class="btn btn-primary mt-3">
```
```
class PythonCreateForm(forms.ModelForm):
    class Meta:
        model = Python
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'image': forms.FileInput(attrs={'class': 'custom-file-input'})
        }
        fields = '__all__'
```
    • Update the 'python_detail.html' file, so the image displays properly
```
<div class="card m-3" style="width: 18rem;">
    <img class="card-img-top" src="{{ python.image.url }}" alt="Card image cap">
    <div class="card-body">
        <h5 class="card-title">{{ python.name }}</h5>
        <p class="card-text">{{ python.description }}</p>
    </div>
</div>
```
### At the end, the form should look something like this:

![1](https://user-images.githubusercontent.com/67734870/124674169-e90e9200-dec2-11eb-9ab2-65cca338306d.png)

### And the home page should look like this:

![1](https://user-images.githubusercontent.com/67734870/124674239-06436080-dec3-11eb-9857-e63cfd627bec.png)


# Lab: Authentication
## Pythons Wiki (with Authentication)
Extend the pythons wiki project, so it has very simple authentication. 
##    1. Create User group
Create a group called 'User' with the following permissions

![1](https://user-images.githubusercontent.com/67734870/125804554-fc41ec15-27e4-4c73-8cac-d359f6e25c5a.png)

##    2. Create User
Since we don't know how to create register forms yet, create your own user that is in the 'User' group using the django admin

![1](https://user-images.githubusercontent.com/67734870/125804665-5d2d8e74-9a1a-4776-ba28-6d4d7046ada9.png)

##    3. Add Login and Logout
In the nav bar, implement some logic in the template, so when a user is not logged in (user is Anonymous), a Login link is displayed. Otherwise display 'Welcome {username}' and a Logout link
## Not Logged In

![1](https://user-images.githubusercontent.com/67734870/125804799-b32f7cc7-54fe-4b1e-b0c4-8bcbe2478be2.png)

## Logged In

![1](https://user-images.githubusercontent.com/67734870/125804915-112f23ec-f04f-42a0-94b5-26cdbf8bcd7c.png)

##    4. Login and Logout View
Implement the login view, so the user you created logs in (use his credentials)

![1](https://user-images.githubusercontent.com/67734870/125805020-3b9d4ecf-7f50-493a-a1e6-e659875068ce.png)

Implement the logout logic, so the currently logged user logs out and redirect to the home page

![1](https://user-images.githubusercontent.com/67734870/125805102-170a9881-a5e3-495a-9a64-299116d39289.png)

##    5. Group Restrictions
Implement your own decorator function that allows only users from the group 'User' or superusers to access the create python page. If the user does not belong to those groups, create your own 401 page like in the example below
Not Logged In

![1](https://user-images.githubusercontent.com/67734870/125805248-78a0d846-aeac-4fe8-bc73-dddfbe0a07fa.png)

Logged In

![1](https://user-images.githubusercontent.com/67734870/125805353-0ab443d8-dd32-45e2-a29b-e1f1787a6953.png)