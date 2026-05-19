# 🛍️ Online clothing store (Django + HTMX + Alpine.js)

## 🌟 Project Features
- **Modern stack**: Django + HTMX + Alpine.js
- **Payment system**: Stripe
- **Database**: PostgreSQL
- **Customized user model**
- **Protected Settings** (CSRF, HTTPS, Security Headers)

## 🚀 Project launch

### 1. Local launch

1. Install dependencies:
```bash
python -m pip install -r requirements.txt
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

3. Configure environment variables:
```
SECRET_KEY='example'

POSTGRES_DB=enfdb
POSTGRES_USER=enfdb
POSTGRES_PASSWORD=enfdb
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

STRIPE_SECRET_KEY='example'
STRIPE_WEBHOOK_SECRET='example'
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Start the server:
```bash
python manage.py runserver
```

## 🔒 Security Settings
The project is pre-configured with:
- CSRF protection
- Secure cookies
- Security Headers

## 🌍 Site access
- Locally: [http://localhost:8000](http://localhost:8000)

## ⚙️ Important settings from settings.py
```python
# Safety
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        # ... other parameters
    }
}

# Payment system
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
```
