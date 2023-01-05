# neoself
The repository for Tequila &amp; Lime's Final Momentum project
# Deployment
https://neoself-be-service.onrender.com

# Endpoints
|Url|Description|Request|documentation|
|---|-----------|-------|---|
|user/| User can view there own profile info | GET | x |
|user/self/| User is able to edit their profile info and delete profile if they so choose | GET, PUT, DELETE | x |
|user/int:pk| See profile info for individual user | GET | |
|user/search/| Search users by username/first name/last name | GET | x |
|questionnaire/| this shows all questionnaires a user has filled out as well as letting them to create more| GET, POST | x |
|questionnaire/int:pk/| This shows an individual questionnaire filled out | GET, PATCH | x | 
|reflection/| see all reflections for a particular user | GET, POST | x |
|questionnaire/<int:id>/reflection/| get all the reflections for a questionnaire | GET, POST | X |
|reflection/int:pk/ | see the details for an individual reflection | GET | x |
|record/user/| be able to see all the users own records | GET | x |
|record/all/| get all records for everyone | GET | X |
|habit/<int:questionnaire_id>/records/| gets the records for a particular questionnaire | GET | X |
|record/friends/| see all friends most recent records that are public | GET | X |
|record/today/user/| users records for today | GET ||
|record/user/<int:user_id>/| get records for users that are public | GET | X |
|record/weeklog/<int:wk_id>/| get records in weeklog | GET |  |
|record/int:pk/| be able to look at an individual record | GET, PUT| x |
|reaction/| able to see reaction to every record by every user (not really useful now) | GET, POST | x |
|reaction/record/int:record_id/| see reactions for a record | GET, POST |  |
|reaction/int:pk/| able to see individual reaction to a record from particular user | GET, PUT, DELETE| x |
|weeklogs/| able to see all the records for a particular habit for a particular user | GET | x |
|weeklogs/int:id/| able to see a specific weeklog detail | GET | x |
|weeklogs/habit/int:id/| see the week logs for a particular questionnaire | GET |  |
|results/| see all results for a user | GET | x |
|results/all/| see all records | GET | x |
|results/habit/int:id/| able to see the results for a particular habit | GET |  |
|results/int:pk/| see details on one result for user | GET | x |
|friends/| able to see friends profiles | GET, POST| x |
|friends/all/| able to view all friend relationships | GET | x |
|friends/int:pk/| to see a specific friend | GET, DELETE, PUT | x |
|friends/search/| search for your friends | GET, POST | x |
|auth/users/me/avatar/| add avatar to user | PATCH | |
|auth/users/|register a new user | POST | x|
|auth/token/login/| login established user & create auth token | POST | x |
|auth/token/logout/| logout established user & destroy auth token | POST | x |

# Documentation

## User Authentication

### Register a new user:

#### request:
Username and password are required fields. Email is optional.
Token should not be entered or enabled.

POST  <BASE_URL>/auth/users/

```json
{
  "username": "baby_yoda",
  "password": "grogu"
}
```

#### response:
201 Created

```json
{
  "email": "",
  "username": "baby_yoda",
  "id": 6
}
```

### Log In:

#### request:
Username and password are required fields.

POST  <BASE_URL>/auth/token/login/

```json
{
  "username": "testusername",
  "password": "testpassword"
}
```

### response:
```json
{
  "auth_token": "c312049c7f034a3d1b52eabc2040b46e094ff34c"
}
```

### Log out

#### request:

Authentication Required.
Must be logged in.

POST  <BASE_URL>/auth/token/login/


#### response:
```json
"No body returned for response"
```

## User Endpoints

### User is able to view own profile 

#### request:
Username and password are required fields.

GET  <BASE_URL>/user/

```json

```

### response:
```json
[
	{
		"id": 1,
		"username": "Chosenone",
		"full_name": "",
		"bio": "",
		"created_at": "2022-12-10T00:52:07.002479Z",
		"avatar": null
	}
]
```

### User to edit own profile 

#### request:
Username and password are required fields.

GET, PUT, DELETE  <BASE_URL>/user/self/

for PUT
```json
{
	"username": "Chosenone",
	"full_name": "Bruce Lee",
	"bio": "I am an edit",
	"avatar": null
}
```

### response:
```json
[
	{
		"id": 1,
		"username": "Chosenone",
		"full_name": "Bruce Lee",
		"bio": "I am an edit",
		"created_at": "2022-12-10T00:52:07.002479Z",
		"avatar": null
	}
]
```
### To search user profiles

#### request:
Username and password are required fields.

GET  <BASE_URL>/user/search/?q=<search term>

```json

```

### response:
```json
[
	{
		"id": 1,
		"username": "Chosenone",
		"full_name": "",
		"bio": "",
		"created_at": "2022-12-10T00:52:07.002479Z",
		"avatar": null
	}
]
```

## Questionnaire endpoints

### To create and Get user's questionnaire

#### request:
Username and password are required fields.

GET, POST  <BASE_URL>/questionnaire/

for POST only
```json
{
    "start_habit": true,
	"habit_name": "This field is required.",
    "date": "2022-12-01",
    "duration": 30,
	"sunday": true,
	"monday": true,
	"tuesday": true,
	"wednesday": true,
	"thursday": true,
	"friday": true,
	"saturday": true,
	"metric_label": "This field is required.",
    "metric_baseline": 0,
	"goal_label": "This field is required.",
    "goal_metric": 0,
    "opt_in": false,
	"cue_question_1": "This field is required.",
	"cue_question_2": "This field is required.",
	"cue_question_3": "This field is required.",
	"craving_question_1": "This field is required.",
	"response_question_1": "This field is required.",
	"response_question_2": "This field is required.",
	"signature": "This field is required."
}
```

### response:
```json
[
	{
		"id": 159,
		"user": 1,
		"start_habit": true,
		"habit_name": "Sing",
		"date": "2022-12-01",
		"duration": 30,
		"sunday": true,
		"monday": true,
		"tuesday": true,
		"wednesday": true,
		"thursday": true,
		"friday": true,
		"saturday": true,
		"metric_label": "min",
		"metric_baseline": 0,
		"goal_label": "min",
		"goal_metric": 0,
		"opt_in": false,
		"cue_question_1": "text",
		"cue_question_2": "text",
		"cue_question_3": "text",
		"craving_question_1": "text",
		"response_question_1": "text",
		"response_question_2": "text",
		"signature": "Bruce Lee"
	}
]
```

### To Get details of a particular questionnaire

#### request:
Username and password are required fields.

GET <BASE_URL>/questionnaire/int:pk

```json
```

### response:
```json
[
	{
		"id": 159,
		"user": 1,
		"start_habit": true,
		"habit_name": "Sing",
		"date": "2022-12-01",
		"duration": 30,
		"metric_label": "min",
		"metric_baseline": 0,
		"goal_label": "min",
		"goal_metric": 0,
		"opt_in": false,
		"cue_question_1": "text",
		"cue_question_2": "text",
		"cue_question_3": "text",
		"craving_question_1": "text",
		"response_question_1": "text",
		"response_question_2": "text",
		"signature": "Bruce Lee"
	}
]
```

## Reflection endpoints

### To get and create reflections

#### request:
Username and password are required fields.

GET, POST <BASE_URL>/reflection/

for POST only
```json
[
	{
		"id": 191,
		"questionnaire": 159,
		"cue_question_1": "IsAuthenticatedOrReadOnly",
		"cue_question_2": "IsAuthenticatedOrReadOnly",
		"cue_question_3": "IsAuthenticatedOrReadOnly",
		"craving_question_1": "IsAuthenticatedOrReadOnly",
		"response_question_1": "IsAuthenticatedOrReadOnly",
		"response_question_2": "IsAuthenticatedOrReadOnly",
		"date": "2022-12-01",
		"metric_baseline": 0,
		"goal_metric": 0
	}
]
```

### response:
```json
[
	{
		"id": 191,
		"questionnaire": 159,
		"cue_question_1": "IsAuthenticatedOrReadOnly",
		"cue_question_2": "IsAuthenticatedOrReadOnly",
		"cue_question_3": "IsAuthenticatedOrReadOnly",
		"craving_question_1": "IsAuthenticatedOrReadOnly",
		"response_question_1": "IsAuthenticatedOrReadOnly",
		"response_question_2": "IsAuthenticatedOrReadOnly",
		"date": "2022-12-01",
		"metric_baseline": 0,
		"goal_metric": 0
	}
]
```

### To get all the reflections made for a habit

#### request:
Username and password are required fields.

GET <BASE_URL>/questionnaire/int:id/reflection

id is the id of the questionnaire
```json
```

### response:
```json
[
	{
		"id": 197,
		"questionnaire": 164,
		"cue_question_1": "Things happening",
		"cue_question_2": "adsadasdsad",
		"cue_question_3": "adsadasdsad",
		"craving_question_1": "adsadasdsad",
		"response_question_1": "adsadasdsad",
		"response_question_2": "adsadasdsad",
		"date": "2022-12-11",
		"metric_baseline": 14,
		"goal_metric": 20
	},
	{
		"id": 196,
		"questionnaire": 164,
		"cue_question_1": "adsadasdsad",
		"cue_question_2": "adsadasdsad",
		"cue_question_3": "adsadasdsad",
		"craving_question_1": "saddsasadsda",
		"response_question_1": "adsadasdsad",
		"response_question_2": "adsadasdsad",
		"date": "2022-12-01",
		"metric_baseline": 0,
		"goal_metric": 0
	}
]
```

### To get individual reflection

#### request:
Username and password are required fields.

GET <BASE_URL>/reflection/int:pk

```json
```

### response:
```json
[
	{
		"id": 191,
		"questionnaire": 159,
		"cue_question_1": "IsAuthenticatedOrReadOnly",
		"cue_question_2": "IsAuthenticatedOrReadOnly",
		"cue_question_3": "IsAuthenticatedOrReadOnly",
		"craving_question_1": "IsAuthenticatedOrReadOnly",
		"response_question_1": "IsAuthenticatedOrReadOnly",
		"response_question_2": "IsAuthenticatedOrReadOnly",
		"date": "2022-12-01",
		"metric_baseline": 0,
		"goal_metric": 0
	}
]
```

## Record endpoints

### To get all of individual records and update records

#### request:
Username and password are required fields.

GET, POST <BASE_URL>/record/user/

```json

```

### response:
```json
[
	{
		"id": 1818,
		"week_reflection": 191,
		"daily_record": 0,
		"cue_dh": false,
		"craving_dh": false,
		"response_dh": false,
		"comment_dh": "False",
		"date": "2022-12-18",
		"public": true,
		"filled_in": false,
		"likes_num": 0
	}
]
```

### To get all records created that are filled_in and made today or before

#### request:
Username and password are required fields.

GET <BASE_URL>/record/all/

```json

```

### response:
```json
[
	{
		"id": 1818,
		"week_reflection": 191,
		"daily_record": 0,
		"cue_dh": false,
		"craving_dh": false,
		"response_dh": false,
		"comment_dh": "False",
		"date": "2022-12-18",
		"public": true,
		"filled_in": false,
		"likes_num": 0
	}
]
```
### To get all records for a user that is public and filled in

#### request:
Username and password are required fields.

GET <BASE_URL>/record/user/int:pk

```json

```

### response:
```json
[
	{
		"id": 1817,
		"user": null,
		"week_reflection": 191,
		"daily_record": 0,
		"cue_dh": false,
		"craving_dh": false,
		"response_dh": false,
		"comment_dh": "False",
		"date": "2022-12-11",
		"public": true,
		"filled_in": true,
		"likes_num": 0
	}
]
```

### To get all friends records that are filled_in

#### request:
Username and password are required fields.

GET <BASE_URL>/record/all/

```json

```

### response:
```json
[
	{
		"id": 1818,
		"week_reflection": 191,
		"daily_record": 0,
		"cue_dh": false,
		"craving_dh": false,
		"response_dh": false,
		"comment_dh": "False",
		"date": "2022-12-18",
		"public": true,
		"filled_in": false,
		"likes_num": 0
	}
]
```

### To get all records for a habit

#### request:
Username and password are required fields.

GET <BASE_URL>/habit/<int:questionnaire_id>/records/

the id is the Id of the questionnaire that was initially filled out by user
```json

```

### response:
```json
{
	"id": 1818,
	"week_reflection": 191,
	"daily_record": 30,
	"cue_dh": false,
	"craving_dh": true,
	"response_dh": false,
	"comment_dh": "False",
	"date": "2022-12-18",
	"public": true,
	"filled_in": false,
	"likes_num": 0
},
{
	"id": 1819,
	"week_reflection": 191,
	"daily_record": 30,
	"cue_dh": false,
	"craving_dh": true,
	"response_dh": false,
	"comment_dh": "False",
	"date": "2022-12-18",
	"public": true,
	"filled_in": false,
	"likes_num": 0
}
```
### To get detail of individual record

#### request:
Username and password are required fields.

GET, PUT <BASE_URL>/record/int:pk/

for PUT can update one or all
```json
{
	"daily_record": 30,
	"cue_dh": false,
	"craving_dh": true,
	"response_dh": false,
	"comment_dh": "False",
	"date": "2022-12-18",
	"public": true,
	"filled_in": false
}
```

### response:
```json
{
	"id": 1818,
	"week_reflection": 191,
	"daily_record": 30,
	"cue_dh": false,
	"craving_dh": true,
	"response_dh": false,
	"comment_dh": "False",
	"date": "2022-12-18",
	"public": true,
	"filled_in": false,
	"likes_num": 0
}
```

## Reactions endpoints (record responses)

### To get all reactions made 

#### request:
Username and password are required fields.

GET, POST <BASE_URL>/reaction/

for POST only
```json
{
    "gif_url": "",
    "record": 1816 ,
    "commentor": 3
}
```

### response:
```json
[
	{
		"id": 7,
		"gif_url": "sick",
		"record": 1816,
		"commentor": 3
	},
	{
		"id": 8,
		"gif_url": "sick",
		"record": 1816,
		"commentor": 2
	}
]
```

### To get individual reaction

#### request:
Username and password are required fields.

GET, PUT, DELETE <BASE_URL>/reaction/int:pk/

for PUT 
```json
{
    "gif_url": "sick",
}
```

### response:
```json
{
	"id": 7,
	"gif_url": "sick",
	"record": 1816,
	"commentor": 3
}
```

## Weeklogs endpoints

### To get users week logs for a habit

#### request:
Username and password are required fields.

GET <BASE_URL>/weeklogs/

```json
```

note records attribute will show records detail
### response:
```json
[
	{
		"id": 113,
		"date": "2022-12-14",
		"day": 14,
		"questionnaire": 159,
		"records": [
			1817
		]
	},
	{
		"id": 112,
		"date": "2022-12-07",
		"day": 7,
		"questionnaire": 159,
		"records": [
			1816
		]
	}
]
```

### To detail on particular detail

#### request:
Username and password are required fields.

GET <BASE_URL>/weeklogs/int:pk/

```json
```

note records attribute "records" will show records detail and not just id
### response:
```json
{
	"id": 113,
	"date": "2022-12-14",
	"day": 14,
	"questionnaire": 159,
	"records": [
		1817
	]
}
```

## Results endpoints

### See all results for a user in habit

#### request:
Username and password are required fields.

GET <BASE_URL>/results/

```json
```

note habit log will show record info and not just id
### response:
```json
[
	{
		"id": 14,
		"questionnaire": 159,
		"habit_log": [
			1817,
			1816,
			1818,
			1819
		],
		"success": false
	}
]
```

## Results endpoints

### Detail for results of habit

#### request:
Username and password are required fields.

GET <BASE_URL>/results/int:pk/

```json
```

note habit log will show record info and not just id
### response:
```json
{
	"id": 14,
	"questionnaire": 159,
	"habit_log": [
		1817,
		1816,
		1818,
		1819
	],
	"success": false
}
```
### Get all results for everyone

#### request:
Username and password are required fields.

GET <BASE_URL>/results/all/

```json
```

note habit log will show record info and not just id
### response:
```json
{
	"id": 14,
	"questionnaire": 159,
	"habit_log": [
		1817,
		1816,
		1818,
		1819
	],
	"success": false
}
```

## Friends endpoints 


### View all of users friends

#### request:
Username and password are required fields.

GET,POST <BASE_URL>/friends/

for POST only
```json

{
	"friend": "user1",
}

```

### response:
```json
{
	"id": 1,
	"friend": "user1",
	"created_at": "2022-12-12T20:30:21.029470Z"
}
```


### View all friend relationships

#### request:
Username and password are required fields.

GET <BASE_URL>/friends/all/

for POST only
```json
```

### response:
```json
{
	"id": 1,
	"friend": "user1",
	"created_at": "2022-12-12T20:30:21.029470Z"
}
```


### View individual friend detail


#### request:
Username and password are required fields.

GET,DELETE, PUT <BASE_URL>/friends/int:pk/

```json
```

### response:
```json
{
	"id": 1,
	"friend": "user1",
	"created_at": "2022-12-12T20:30:21.029470Z"
}
```


### Add an avatar to a User:

#### request:
A selected image/jpeg input is required.

PATCH  <BASE_URL>/auth/users/me/avatar/

```binary file
{
  "Selected File": "~Desktop/flounder.jpeg"
}
```

#### response:
200 OK

```
{
	"id": 5,
	"username": "flounder24",
	"full_name": "",
	"bio": "",
	"created_at": "2022-12-14T15:04:18.496336Z",
	"avatar": "http://127.0.0.1:8000/media/user_avatars/flounder_2TBjzYv.jpeg"

### To search friends

DOESN'T EXIST RIGHT NOW

#### request:
Username and password are required fields.

GET <BASE_URL>/friends/search/

```json
```

### response:
```json
{
	"id": 1,
	"friend": "user1",
	"created_at": "2022-12-12T20:30:21.029470Z"
}
```