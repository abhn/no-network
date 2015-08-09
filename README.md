## PUBLIC API 

### Object information fetch
* [GET /users](#getusers)
* [GET /posts](#getposts)
* [GET /comments](#getcomments)
* [GET /stars](#getstars)
* [GET /recommends](#getrecommends)

### Modifying calls
* [POST /register](#postregister)
* [POST /login](#postlogin)

* [POST /new/post](#postnewpost)
* [POST /new/comment](#postnewcomment)
* [POST /new/star](#postnewstar)
* [POST /new/recommend](#postnewrecommend)

* [POST /edit/user](#postedituser)
* [POST /edit/post](#posteditpost)
* [POST /edit/comment](#posteditcomment)

* [POST /delete/user](#postdeleteuser)
* [POST /delete/post](#postdeletepost)
* [POST /delete/comment](#postdeletecomment)
* [POST /delete/star](#postdeletestar)
* [POST /delete/recommend](#postdeleterecommend)

#### <a name="getusers"></a> GET /users 
Example request
```
GET /users/userId/accessToken
```
Example response
```json
{

    "username": "abhi",
    "first_name": "Abhishek",
    "last_name": "Nagekar",
    "gender": "M",
    "location": "IN",
    "email": "abhishek@nagekar.com"

}
```

#### <a name="getposts"></a> GET /posts 
Example request
```
GET /posts/postId/accessToken
```
Example response
```json
{

    "source": 1,
    "updated": "2015/08/09 08:28:22",
    "data": "I am edited",
    "created": "2015/07/25 18:27:35"

}
```

*this list is constantly being updated..*
