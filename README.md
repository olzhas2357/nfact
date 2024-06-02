## Shop all the things 
#### Overview
This project was developed to create a basic e-commerce platform with user authentication and a shopping cart system. The primary goal was to provide a simple and intuitive interface for users to browse and purchase products.
***
#### Technologies Used
* __Django__: The web framework used for developing the application.
* __SQLite3__: The database used for storing application data.
* __Bootstrap__: For responsive and modern UI design.
* __Django-Allauth__: For handling user authentication, registration, and social account management
***
#### Unique Approaches and Methodologies
##### Authentication
The authentication system leverages Django's built-in user authentication combined with Django-Allauth for enhanced features like email verification and social account authentication.
```
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
```
***
#### Compromises and Known Issues
##### Compromises
* __Database Choice__: SQLite3 was chosen for simplicity and ease of setup. For a production environment, a more robust database such as PostgreSQL or MySQL would be recommended.
* __Session-Based Cart__: The current implementation of the shopping cart is session-based. This means that if a user logs out or switches devices, their cart will not persist.

##### Known Issues
* __Cart System__: The shopping cart functionality needs further improvement to handle edge cases, such as simultaneous updates by multiple users.

***
    Clone the repository https://github.com/olzhas2357/nfact.git
    
    Home page http://127.0.0.1:8000/shop/home
