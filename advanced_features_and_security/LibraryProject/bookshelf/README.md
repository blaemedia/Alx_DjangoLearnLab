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
