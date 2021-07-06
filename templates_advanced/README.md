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
