# BewiseTest

## Deployment
```bash
$ git clone 
```
```bash 
$ cd BewiseTest
```
### Manually
```bash 
$ python -m venv venv
```
```bash 
$ source venv/bin/activate
```
```bash 
$ pip install -r requirements.txt
```
Run MySQL server on any port, you can do this by yourself or use docker-compose file:
```bash
$ docker-compoes run -p {any_port}:3306 db
```
If you are not using port 3306, change variable MYSQL_PORT value in .env file to the port you are using.

After that, you can start app by command:
```bash
$ uvicorn main:app --host 127.0.0.1 --port 8000
```
### Via docker
```bash
$ docker-compose up --build
```

After setup app will be available on port 8000 at localhost.
## Usage
### Request sample
**url** - http://127.0.0.1:8000/questions/

**method** - post

**body**:
```json
{
    "questions_num": 3
}
```
questions_num - number of new questions to download
### Response sample
Response returns the last uploaded question before your request.
```json
{
    "question": "In a bizarre twist of fate, George W. Bush almost choked on one of these on January 13, 2002",
    "answer": "pretzel",
    "created_at": "2014-02-11"
}
```


