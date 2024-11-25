# Leave Management System  

A comprehensive Leave Management System designed to streamline faculty leave applications and approvals within an academic institution. Built using Django and MySQL, this system includes user authentication, leave application workflows, and reporting features to ensure efficient leave management.

## Features  

1. **User Registration and Authentication**  
   - Faculty registration with details like Employee ID, Username, Email, Department, Faculty Type, Phone Number, and Password.  
   - Authentication system to secure access and categorize faculty by role.  

2. **Leave Application Module**  
   - Faculty can apply for leaves through an intuitive interface.  
   - Includes fields for leave type, duration, and justification.  

3. **Leave History Page**  
   - Allows users to view their leave history with statuses like approved, rejected, or pending.  

4. **Requests Management**  
   - Higher-level faculty can review, accept, or reject leave requests from lower-level employees.  

5. **Leave Report Generator**  
   - Generates reports summarizing leaves taken, categorized by faculty type or department.  

## Technologies Used  

- **Backend**: Django Framework  
- **Frontend**: HTML, CSS, JavaScript  
- **Database**: MySQL  
- **Authentication**: Django's built-in user authentication system  

## Prerequisites  

- Python 3.x  
- Django 4.x  
- MySQL Server  
- Virtual Environment (optional)  

## Installation and Setup  

1. **Clone the Repository**  
   ```bash  
   git clone https://github.com/vvr10223/University-Leave-Hub.git  
   cd University-Leave-Hub/LeaveManagementSystem  
   ```  

2. **Create a Virtual Environment** (optional but recommended)  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate  
   ```  

3. **Install Dependencies**  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. **Set Up the Database**  
   - Create a MySQL database named `leave_management`.  
   - Update `settings.py` with your database credentials:  
     ```python  
     DATABASES = {  
         'default': {  
             'ENGINE': 'django.db.backends.mysql',  
             'NAME': 'leave_management',  
             'USER': 'your_username',  
             'PASSWORD': 'your_password',  
             'HOST': 'localhost',  
             'PORT': '3306',  
         }  
     }  
     ```  

5. **Run Migrations**  
   ```bash  
   python manage.py makemigrations  
   python manage.py migrate  
   ```  

6. **Create a Superuser**  
   ```bash  
   python manage.py createsuperuser  
   ```  

7. **Run the Development Server**  
   ```bash  
   python manage.py runserver  
   ```  

8. **Access the Application**  
   Open `http://127.0.0.1:8000` in your browser.  


## Contributing  

Contributions are welcome! Feel free to fork the repository and submit pull requests.  

## License  

This project is licensed under the [MIT License](LICENSE).  

---

Let me know if you'd like to tweak or add anything!
