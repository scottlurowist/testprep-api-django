
# API Payloads Documentation

## Table of Contents
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
  

- [API Payloads - authentication](#api-payloads---authentication)
  - [POST /api/v1/auth/sign-up - request and response](#post-apiv1authsign-up---request-and-response)
  - [POST /api/v1/auth/sign-in - request and response](#post-apiv1authsign-in---request-and-response)
  - [PATCH /api/v1/auth/change-password - header and request](#patch-apiv1authchange-password---header-and-request)
  - [DELETE /api/v1/auth/change-password - header and request](#delete-apiv1authchange-password---header-and-request)
  - [POST /api/v1/token/ - request and response](#post-apiv1token---request-and-response)
  - [POST /api/v1/token/refresh/ - request and response](#post-apiv1tokenrefresh---request-and-response)
- [API Payloads - tests](#api-payloads---tests)
  - [GET /api/v1/tests/ - response](#get-apiv1tests---response)
  - [GET /api/v1/tests/1 - response](#get-apiv1tests1---response)
  - [PATCH /api/v1/tests/1 - request](#patch-apiv1tests1---request)
- [API Payloads - categories](#api-payloads---categories)
  - [POST /api/v1/categories - response](#post-apiv1categories---response)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
  
<br/><br/>

## API Payloads - authentication

<table>
<tr>
  <th colspan="4">Request</th>
  <th colspan="2">Response</th>
</tr>
<tr>
  <th>Verb</th>
  <th>URI</th>
  <th>body</th>
  <th>Headers</th>
  <th>Status</th>
  <th>body</th>
</tr>
<tr>
  <td>POST</td>
  <td>`/api/v1/auth/sign-up/</td>
  <td><strong>credentials</strong></td>
  <td>empty</td>
  <td>201, Created</td>
  <td><strong>user</strong></td>
</tr>
<tr>
  <td colspan="4"></td>
  <td>400 Bad Request</td>
  <td><em>empty</em></td>
</tr>
<tr>
  <td>POST</td>
  <td>`/api/v1/auth/sign-in/`</td>
  <td><strong>credentials</strong></td>
  <td>empty</td>
  <td>200 OK</td>
  <td><strong>user w/token</strong></td>
</tr>
<tr>
  <td colspan="4"></td>
  <td>401 Unauthorized</td>
  <td><em>empty</em></td>
</tr>
<tr>
  <td>DELETE</td>
  <td>`/api/v1/sign-out/`</td>
  <td>empty</td>
  <td><strong>token</strong></td>
  <td>201 Created</td>
  <td>empty</td>
</tr>
<tr>
  <td colspan="4"></td>
  <td>401 Unauthorized</td>
  <td><em>empty</em></td>
</tr>
<tr>
  <td>PATCH</td>
  <td>`/api/v1/auth/change-password/`</td>
  <td><strong>passwords</strong></td>
  <td><strong>token</strong></td>
  <td>204 No Content</td>
  <td><strong>user w/token</strong></td>
</tr>
<tr>
  <td colspan="4"></td>
  <td>400 Bad Request</td>
  <td><em>empty</em></td>
</tr>
<tr>
  <td>DELETE</td>
  <td>`/api/v1/auth/sign-out/`</td>
  <td><strong>passwords</strong></td>
  <td><strong>token</strong></td>
  <td>204 No Content</td>
  <td><strong>user w/token</strong></td>
</tr>
<tr>
  <td colspan="4"></td>
  <td>400 Bad Request</td>
  <td><em>empty</em></td>
</tr>
  <td>POST</td>
  <td>`api/v1/token/'</td>
  <td><strong>credentials</strong></td>
  <td><strong>token</strong></td>
  <td>200 OK</td>
  <td><strong>tokens</strong></td>
</tr>
<tr>
  <td colspan="4"></td>
  <td>401 Unauthorized</td>
  <td><em>status message</em></td>
</tr>
</table>

<br /><br />

### POST /api/v1/auth/sign-up - request and response
```
{
  {
    "email": "someone@foo.com",
    "password": "somepassword",
    "password_confirmation": "an example password"
  }
}
```
```
{
    {
        "id": "5fd7a3c0d3d64f3c681f19f2",
        "email": "x@x.com",
        "createdAt": "2020-12-14T17:41:20.829Z",
        "updatedAt": "2020-12-14T17:41:20.829Z"
    }
}
```

<br />

### POST /api/v1/auth/sign-in - request and response
```
{
  {
    "email": "an@example.email",
    "password": "somepassword",
  }
}
```
```
{
    {
        "id": "5fd7a3c0d3d64f3c681f19f2",
        "email": "x@x.com",
        "createdAt": "2020-12-14T17:41:20.829Z",
        "updatedAt": "2020-12-14T17:48:14.980Z",
        "token": "561151009eec876f7a1d5914cbbfafbe"
    }
}
```
<br />

### PATCH /api/v1/auth/change-password - header and request

```
authorization: 'Bearer 561151009eec876f7a1d5914cbbfafbe'
```

```
{
  {
    "email": "an@example.email",
    "old-password": "somepassword",
    "new-password": "newpassword"
  }
}
```

<br />

### DELETE /api/v1/auth/change-password - header and request

```
authorization: 'Bearer 561151009eec876f7a1d5914cbbfafbe'
```

```
{
}
```
<br />

### POST /api/v1/token/ - request and response
```
{
    "username": "some_existing_username",
    "password": "user_password"
}
```

```
{
  "access":"eyJhbGciOiJIUzI1NiI ... aYSfd1S-AuT7lU",
  "refresh":"eyJhbGciOiJIUzI1Ni ... kapko6HFRt7Rh4"
}
```

<br />

### POST /api/v1/token/refresh/ - request and response
```
{
  "refresh":"eyJhbGciOiJIUzI1Ni ... kapko6HFRt7Rh4"
}
```

```
{
  "access":"eyJhbGciOiJIUzI1NiI ... aYSfd1S-AuT7lU",
}
```

<br /><br /><br /><br /><br />

## API Payloads - tests

All requests must use the 'Authorizaton' header using a current JWT access token.
```
authorization: 'Bearer 561151009eec876f7a1d5914cbbfafbe'
```

<br />

<table>
  <tr>
    <th colspan="3">Request</th>
    <th colspan="2">Response</th>
  </tr>
  <tr>
    <th>Verb</th>
    <th>URI</th>
    <th>body</th>
    <th>Status</th>
    <th>body</th>
  </tr>
  <tr>
    <td>GET</td>
    <td>`/api/v1/tests/`</td>
    <td>n/a</td>
    <td>200, OK</td>
    <td><strong>all published tests found</strong></td>
  </tr>
  <tr>
    <td colspan="3"></td>
    <td>200, OK</td>
    <td><em>empty tests</em></td>
  </tr>
  <tr>
    <td colspan="3"></td>
    <td>401 Unauthorized</td>
    <td><em>empty</em></td>
  </tr>
  <tr>
    <td>GET</td>
    <td>`/api/v1/tests/:id` </td>
    <td>'n/a'</td>
    <td>200, OK</td>
    <td><strong>retrieves the test by test id</strong></td>
  </tr>
  <tr>
    <td colspan="3">
    </td>
    <td>400 Bad Request</td>
    <td><strong>errors</strong></td>
  </tr>
  <tr>
    <td colspan="3"></td>
    <td>401 Unauthorized</td>
    <td><em>empty</em></td>
  </tr>
  <tr>
    <td colspan="3"></td>
    <td>404 Not found</td>
    <td><em>empty</em></td>
  </tr>
  <tr>
  <tr>
    <td>POST</td>
    <td>`/api/v1/tests/` </td>
    <td></td>
    <td>201, Created</td>
    <td><strong>Creates a test that can be empty.</strong></td>
  </tr>
  <tr>
    <td colspan="3">
    </td>
    <td>400 Bad Request</td>
    <td><strong>errors</strong></td>
  </tr>
  <tr>
    <td colspan="3"></td>
    <td>401 Unauthorized</td>
    <td><em>empty</em></td>
  </tr>
  <tr>
    <td>PATCH</td>
    <td>`/api/v1/tests/:id` </td>
    <td></td>
    <td>200, OK</td>
    <td><strong>Test is updated.</strong></td>
  </tr>
  <tr>
    <td colspan="3">
    </td>
    <td>400 Bad Request</td>
    <td><strong>errors</strong></td>
  </tr>
  <tr>
    <td colspan="3"></td>
    <td>401 Unauthorized</td>
    <td><em>empty</em></td>
  </tr>
  <tr>
    <td colspan="3"></td>
    <td>404 Not found</td>
    <td><em>empty</em></td>
  </tr>
  <tr>
    <td>DELETE</td>
    <td>`/api/v1/tests/:id` </td>
    <td></td>
    <td>200, OK</td>
    <td><strong>Test is deleted.</strong></td>
  </tr>
  <tr>
    <td colspan="3">
    </td>
    <td>204, No Content</td>
    <td><strong>errors</strong></td>
  </tr>
  <tr>
    <td colspan="3"></td>
    <td>401 Unauthorized</td>
    <td><em>empty</em></td>
  </tr>
  <tr>
    <td colspan="3"></td>
    <td>404 Not found</td>
    <td><em>empty</em></td>
  </tr>  
</table>

<br /><br />

### GET /api/v1/tests/ - response
```
Only one question and answer shown for brevity.

{
  [
    {
      "id": 1,
      "name": "some test",
      "description": "some test description",
      "is_published": True,
      "categories": ['Python', 'Django']
      "owner": "Scott Lurowist",
      "questions": [
        {
          "id": 1,
          "text": "What is a decorator?",
          "type": "selectBest",
          "createdAt": "2020-12-14T17:41:20.829Z",
          "updatedAt": "2020-12-14T17:48:14.980Z",
          "test_id": 1,
          "choices": [
            {
              "id": 1,
              "text": "Someone who decorates cakes",
              "is_correct": True,
              "createdAt": "2020-12-14T17:41:20.829Z",
              "updatedAt": "2020-12-14T17:48:14.980Z",
              "question_id": 1,  
            }
          ]
        }
      ]
      "createdAt": "2020-12-14T17:41:20.829Z",
      "updatedAt": "2020-12-14T17:48:14.980Z"
    }    
  ]
}
```

<br /><br />

### GET /api/v1/tests/1 - response
```
{
  {
    "id": 1,
    "name": "some test",
    "description": "some test description",
    "is_published": True,
    "categories": ['Python', 'Django']
    "owner": "Scott Lurowist",
    "questions": [
      {
        "id": 1,
        "text": "What is a decorator?",
        "type": "selectBest",
        "createdAt": "2020-12-14T17:41:20.829Z",
        "updatedAt": "2020-12-14T17:48:14.980Z",
        "test_id": 1,
        "choices": [
          {
            "id": 1,
            "text": "Someone who decorates cakes",
            "is_correct": True,
            "createdAt": "2020-12-14T17:41:20.829Z",
            "updatedAt": "2020-12-14T17:48:14.980Z",
            "question_id": 1,  
          }
        ]
      }
    ]
    "createdAt": "2020-12-14T17:41:20.829Z",
    "updatedAt": "2020-12-14T17:48:14.980Z"
  }    
}
```

<br /><br />

### PATCH /api/v1/tests/1 - request
```
{
  {
    "id": 1,
    "name": "some test",
    "description": "some test description",
    "is_published": True,
    "categories": ['Python', 'Django']
    "owner": "Scott Lurowist",
    "questions": [
      {
        "id": 1,
        "text": "What is a decorator?",
        "type": "selectBest",
        "createdAt": "2020-12-14T17:41:20.829Z",
        "updatedAt": "2020-12-14T17:48:14.980Z",
        "test_id": 1,
        "choices": [
          {
            "id": 1,
            "text": "Someone who decorates cakes",
            "is_correct": True,
            "createdAt": "2020-12-14T17:41:20.829Z",
            "updatedAt": "2020-12-14T17:48:14.980Z",
            "question_id": 1,  
          }
        ]
      }
    ]
    "createdAt": "2020-12-14T17:41:20.829Z",
    "updatedAt": "2020-12-14T17:48:14.980Z"
  }    
}
```


<br /><br /><br /><br /><br />

## API Payloads - categories

All requests must use the 'Authorizaton' header using a current JWT access token.

```
authorization: 'Bearer 561151009eec876f7a1d5914cbbfafbe'
```

<br />

<table>
  <tr>
    <th colspan="3">Request</th>
    <th colspan="2">Response</th>
  </tr>
  <tr>
    <th>Verb</th>
    <th>URI</th>
    <th>body</th>
    <th>Status</th>
    <th>body</th>
  </tr>
  <tr>
    <td>GET</td>
    <td>`/api/v1/tests/`</td>
    <td>n/a</td>
    <td>200, OK</td>
    <td><strong>all published tests found</strong></td>
  </tr>
  <tr>
    <td colspan="3"></td>
    <td>200, OK</td>
    <td><em>empty tests</em></td>
  </tr>
  <tr>
    <td colspan="3"></td>
    <td>401 Unauthorized</td>
    <td><em>empty</em></td>
  </tr>
</table>

<br /><br />

### POST /api/v1/categories - response
```
{
  {
    "id": 1,
    "name": "Python Trivia",
    "tests": ["Pythons Basics", "Advanced Python"]
    "createdAt": "2020-12-14T17:41:20.829Z",
    "updatedAt": "2020-12-14T17:48:14.980Z",
  }
}
```