# Lab: PostgreSQL
# Pet Hotel
## Create a database called pet_hotel that has the following tables and structure

![1](https://user-images.githubusercontent.com/67734870/124121667-da1c7f80-da7d-11eb-9f64-3265bc2ba2da.png)

## Field Restrictions
    • owner_name – must have a maximum length of 15
    • owner_age – must be a number between 1 and 110
    • dog_name – must have a maximum length of 15
    • dog_age – must be between 1 and 25
    • cat_name – must have a maximum length of 15
    • cat_age – must be between 1 and 25
    • hotel_name – must have a maximum length of 25
    • hotel_stars – must be between 1 and 5
## Features
    • When deleting a cat or dog, their records from the rooms should also be deleted
    • When deleting an owner, the corresponding pets should also be deleted
    • When deleting a hotel, the corresponding rooms should also be deleted
##     1. Insert
## Let us insert some data into the tables
### Pet Owners

owner_id | name | owner_age
---------| -----| ---------
1 |'Peter' | 26
2 | 'George' | 32
3 | 'Amy' | 67

### Dogs

dog_id  | owner_id  | dog_name  | dog_age
--------| --------- | --------- | -------
1  | 1 | 'Fluffy'  | 2
2  | 3 | 'Bully' | 3
3  | 1 | 'Rousey' | 5

### Cats

cat_id  | owner_id  | cat_name  | cat_age
--------| --------- | ----------| -------
1  | 2 | 'Tommy'  | 1
2  | 3 | 'Jessy'  | 7
3  | 2 | 'Bubbles'  | 3

### Hotels

hotel_id  | hotel_name  | hotel_stars
----------| ------------| -----------
1 | 'Grand Pets Hotel' | 5
2 | 'Pets Heaven' | 2

### Dog Rooms

room_id | dog_id  | hotel_id  | register_date  | unregister_date
--------| --------| ----------| ---------------| ---------------
1  | 1 | 1 | '2020-06-08' | '2020-06-10'
2  | 2 | 2 | '2020-06-10' | '2020-06-15'
3  | 3 | 2 | '2020-06-20' | '2020-06-23'

### Cat Rooms

room_id  | cat_id  | hotel_id  | register_date  | unregister_date
---------| --------| ----------| -------------- | ---------------
1  | 1 | 1 | '2020-06-08' | '2020-06-10'
2 | 2 | 2 | '2020-06-10' | '2020-06-15'
3  | 3 | 2 | '2020-06-20' | '2020-06-23'

##    2. Select
Select all the information from the dog_room table

![1](https://user-images.githubusercontent.com/67734870/124122930-51064800-da7f-11eb-8898-494e4cb607fd.png)

##    3. Where
Select only the ids of the cats that are in rooms from the hotel with id=2

![1](https://user-images.githubusercontent.com/67734870/124123000-6a0ef900-da7f-11eb-8b60-fd606ff058b0.png)

##    4. Sort
Sort all the pet owners by age in descending

![1](https://user-images.githubusercontent.com/67734870/124123077-827f1380-da7f-11eb-91aa-16bda1d39353.png)

##    5. Count
Get the count of all cats that are of age 3 or older

![1](https://user-images.githubusercontent.com/67734870/124123131-94f94d00-da7f-11eb-872f-10a700609254.png)

##    6. Delete
Delete all cats and dogs, that are of age 2 or less

![1](https://user-images.githubusercontent.com/67734870/124123180-a80c1d00-da7f-11eb-9e34-57f743ae7b38.png)

![1](https://user-images.githubusercontent.com/67734870/124123217-b5c1a280-da7f-11eb-8429-d747485bc992.png)

![1](https://user-images.githubusercontent.com/67734870/124123257-c2de9180-da7f-11eb-8157-6fecf21d0f05.png)

![1](https://user-images.githubusercontent.com/67734870/124123294-d2f67100-da7f-11eb-88bd-b903729f4343.png)



