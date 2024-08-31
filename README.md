# Bank API

The Bank API is a Django-based project that provides an API for querying bank and branch details.


## Installation

### Prerequisites
- Python 3.8 or higher
- MySQL (or another supported database)
- Virtualenv (optional, but recommended)


### Setup

1. Clone the Repository
```
git clone https://github.com/Abhishek-Jilowa/Bank_API
cd bankapi
```
2. Create and Activate a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Apply Migrations
```
python manage.py migrate
```
5. Run the Development Server
```
python manage.py runserver
```

## API Endpoints

### REST API

- List Banks: http://127.0.0.1:8000/banks/
- Branch Details: GET http://127.0.0.1:8000/api/branches/ifsc/


### Contact
For any questions or feedback, please contact jilowa.1@iitj.ac.in.
