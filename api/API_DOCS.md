## API DOCUMENTATION

### Register url: /api/register method: POST content_type: x-www-form-urlencoded
#### Data expected
* first_name
* last_name
* user_name
* user_email
* user_password
* birth_date
* gender
* location

### Login url: /api/login method: POST content_type: x-www-form-urlencoded
#### Data expected
* user_email
* user_password

Returns
* application_id
* access_token

### New Post url: /api/new/post method: POST content_type: application/json
* post_data
* access_token
* application_id
