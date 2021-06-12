# Utube
This is a django backend Application consisting of customized API of youtube,This backend system fetches data from Youtube [API](https://developers.google.com/youtube/v3/getting-started) and then
store it to the database after every 10sec.The API is designed using Django-REST and is scalable,optimised, and allows many features like listing in paginated format , search feature, filtering.
The best part of this API is that you can search the video having particular tag in its tags list.


## Installation

### Local Installation
1. Clone the repo : ```git clone https://github.com/Pratyush-Saxena/Utube ``` 
2. Move into the cloned repository : ```cd Utube ```
3. Install requirements ``` pip3 install -r requirements.txt ```
4. Export the host variable ```export HOST=0.0.0.0:8080 ```
5. Run ```python3 loader.py ```


### Docker Installation (Prefer)
1. Clone the repo : ```git clone https://github.com/Pratyush-Saxena/Utube ``` 
2. Move into the cloned repository : ```cd Utube ```
3. Run ``` docker compose build && docker compose up ```


If everything works fine then go to url  ```localhost:8080/API/``` and you must see below page in your browser

![Screenshot (33)](https://user-images.githubusercontent.com/52444607/121772341-7a276d00-cb92-11eb-8c56-36ec63dc4ffe.png)


## Accessing the API
<li> API URL : <b>  localhost:8080/API/videos </b> </li>

<li>To acces the api you have to add <b>X-Api-Key: <API_KEY></b> in the header of your request, </li>
  
```
 curl --location --request GET 'localhost:8080/API/videos' \ --header 'X-Api-Key: <API-key>'
```
<li>Use <b> 2ISSpYKB.QHVpcRXKkWqmayrvIpskX2559IaaGs2A </b>as api-key for testing.</li>

## Features
 ### 1. Search and Filter
  You can search youtube video by any keyword by adding search query in your request , it will search the text in title and description , and then shows the result.
  ex.
  ```
  curl --location --request GET 'http://localhost:8080/API/videos/?search=INDIA' \ --header 'X-Api-Key:<API-KEY>'
  ```
 ### 2. Pagination and Limit
  This API provides pagination too , it provides the link to next page and previous page in response of request, also you can access random page using offset and page query parameter. Also you can limit the response by addning limit query parameter. ex.
  ```
  curl --location --request GET 'http://localhost:8080/API/videos/?limit=10&offset=10&search=INDIA' \ --header 'X-Api-Key:<API-KEY>'
  ```



