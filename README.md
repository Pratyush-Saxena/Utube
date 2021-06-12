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
<!--If everything works fine then go to url  ```localhost:8080/API/``` you must see below page in your browser 
-->

### Docker Installation (Prefer)
1. Clone the repo : ```git clone https://github.com/Pratyush-Saxena/Utube ``` 
2. Move into the cloned repository : ```cd Utube ```
3. Run ``` docker compose build && docker compose up ```

## Accessing the API
<b>API URL : ```  localhost:8080/API/videos  ```</b>




