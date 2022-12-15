# neoself
The repository for Tequila &amp; Lime's Final Momentum project
# Deployment
https://neoself-be-service.onrender.com

# Endpoints
|Url|Description|Request|
|---|-----------|-------|
|user/| User can view there own profile info | GET |
|user/self/| User is able to edit their profile info and delete profile if they so choose | GET, PUT, DELETE |
|questionnaire/| this shows all questionnaires a user has filled out as well as letting them to create more| GET, POST |
|questionnaire/int:pk/| This shows an individual questionnaire filled out | GET |
|reflection/| see all reflections for a particular user | GET, POST |
|reflection/int:pk/ | see the details for an individual reflection | GET, PUT |
|record/user/| be able to see all the users own records | GET, POST |
|record/friends/| see all friends most recent records that are public | GET |
|record/int:pk| be able to look at an individual record | GET, PUT|
|weeklogs/| able to see all the records for a particular week for a particular habit | GET |
|results/| see all results for a user | GET |
|results/int:pk/| see details on one result for user | GET |
|friends/| able to see friends profiles | GET, POST|
|friends/int:pk/| to see a specific friend | GET, DELETE, PUT |
|friends/search/| search for your friends | GET, POST |