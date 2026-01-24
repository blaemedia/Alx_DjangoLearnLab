## Permissions and Groups Setup

This application uses Django's permission and group system to control access
to Book-related actions.

### Custom Permissions
Defined in the Book model:
- can_view
- can_create
- can_edit
- can_delete

### Groups
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: all permissions

### Enforcement
Permissions are enforced in views using Django's
@permission_required decorator with raise_exception=True.

Unauthorized users receive a 403 Forbidden response.


## Security Measures Implemented

### Settings
- DEBUG set to False for production
- XSS, clickjacking, and MIME sniffing protections enabled
- Secure cookies enforced via HTTPS

### CSRF Protection
- All forms include {% csrf_token %}
- Django CSRF middleware enabled by default

### SQL Injection Protection
- Django ORM used for all database queries
- No raw SQL queries used

### Content Security Policy
- CSP headers configured using django-csp
- Only same-origin resources allowed

### Testing
- Verified CSRF protection by submitting forms without tokens
- Tested input fields against XSS and SQL injection attempts