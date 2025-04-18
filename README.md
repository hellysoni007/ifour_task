# ifour_pms
## Setup Instructions
Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### Install requirement
pip install -r requirements.txt

### Prepare DB
python manage.py makemigrations
python manage.py migrate

### Create superuser
python manage.py createsuperuser

### Run server
python manage.py runserver

### Notes
- To test the functionality for admin create an admin user from admin panel
- Register and login routes are provided to enter the routes that the user can access
- Currently used sqlite db, but can change to postgres from settings.py 