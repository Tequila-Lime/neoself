# neoself
The repository for Tequila &amp; Lime's Final Momentum project
# Deployment
https://neoself-be-service.onrender.com

# Endpoints
|Url|Description|Request|documentation|
|---|-----------|-------|---|
|user/| User can view there own profile info | GET | x |
|user/self/| User is able to edit their profile info and delete profile if they so choose | GET, PUT, DELETE | x |
|user/search/| Search users by username/first name/last name | GET | x |
|questionnaire/| this shows all questionnaires a user has filled out as well as letting them to create more| GET, POST | x |
|questionnaire/int:pk/| This shows an individual questionnaire filled out | GET | x | 
|reflection/| see all reflections for a particular user | GET, POST | |
|reflection/int:pk/ | see the details for an individual reflection | GET, PUT | |
|record/user/| be able to see all the users own records | GET, POST | |
|record/friends/| see all friends most recent records that are public | GET | |
|record/int:pk/| be able to look at an individual record | GET, PUT| |
|reaction/| able to see reaction to every record by every user | GET, CREATE | |
|reaction/int:pk/| able to see individual reaction to a record from particular user | GET, PUT, DELETE| |
|weeklogs/| able to see all the records for a particular week for a particular habit | GET | |
|results/| see all results for a user | GET | |
|results/int:pk/| see details on one result for user | GET | |
|friends/| able to see friends profiles | GET, POST| |
|friends/int:pk/| to see a specific friend | GET, DELETE, PUT | |
|friends/search/| search for your friends | GET, POST | |
|auth/users/me/avatar/| add avatar to user | PATCH | |
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

for POST only
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
