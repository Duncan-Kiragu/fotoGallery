 PICTURESQUE {fotoGallery}

## Developed by [Duncan Kiragu](https://github.com/Duncan-Kiragu)

## DESCRIPTION
This is a web application built using django framework that allows users to view images; the images are filtered using title,categories and tagged location. The app has an admin panel that allows adding of images and editing the details

## USER STORIES
A user is able to :

* View different photos that interest me.
* Click on a single photo to expand it and also view the details of the   photo. The photo details must appear on a modal within the same route as the main page.
* Search for different categories of photos. (ie. Travel, Food)
* Copy a link to the photo to share with my friends.
* View photos based on the location they were taken.

The web application is accessible to users of both desktop and mobile formats: reponsivity for different screens is therefore enabled

The application is thoroughly tested and has implemented various error handlers to prevent the application from crashing.

The link to the images posted on the application can be gotten by clicking the **COPY IMAGE LINK** in the modal displayed on clicking an image.

## PROJECT SPECIFICATIONS
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | **On demand** | Access Admin dashboard |
| Display all images | **Home page** | Clickable links to open any images in a modal |
| Display single images on click | **On  click** | All details should be viewed|
| To add an image  | **Through Admin dashboard** | Add image and add categories and tag location of Image|
| To edit image  | **Through Admin dashboard** | Redirected to the  image form details and editing happens|
| To delete an image  | **Through Admin dashboard ** | click on image object and confirm by delete button|
| To search  | **Enter text in search bar** | Users can search by category|
| To filter by Location  | **Click drop-down on navbar** | Users can view images by Location|

## SETUP / INSTALLATION

### PREREQUISITES
* Python 3.8
* Virtualenv
* Good code editor
* Bash / Terminal
* Programming knowledge (any level)
* Internet connection

### ACQUIRING PROJECT
> CLONING
> DOWNLOAD ZIP

#### CLONING PROJECT
* Open terminal and type:

    $ git clone https://github.com/Duncan-Kiragu/fotoGallery
        $ cd fotoGallery