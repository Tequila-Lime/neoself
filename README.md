# neoself
The repository for Tequila &amp; Lime's Final Momentum project


# Endpoints
|Url|Description|Request|
|---|-----------|-------|
|user/| User can view there own profile info | GET |
|user/self/| User is able to edit their profile info and delete profile if they so choose | GET, PUT, DELETE |
|questionnaire/| this shows all questionnaires a user has filled out as well as letting them to create more| GET, POST |
|questionnaire/int:pk/| This shows an individual questionnaire filled out | GET |
|reflection/| see all reflections for a particular user | GET, POST |
|reflection/int:pk/ | see the details for an individual reflection | GET, PUT |