# Red Flag Challenge

## Michael Bahr

I developed the flask app using VSCode.  To run from VSCode, use `python -m flask run`.

I was not able to find a good scraper package in time.
I used dummy code to load images files from the file system.

## API Examples

### Search

GET http://127.0.0.1:5000/search/bee
200
946 ms
GET /search/bee HTTP/1.1
User-Agent: PostmanRuntime/7.26.8
Accept: */*
Postman-Token: ff577bbe-d64c-47f2-9e81-03a31e66b128
Host: 127.0.0.1:5000
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 65
Server: Werkzeug/2.0.2 Python/3.9.7
Date: Mon, 06 Dec 2021 03:42:25 GMT
{"classifications":["bucket","hook","bucket","bucket","bucket"]}

### Upload

POST http://localhost:5000/upload
200
315 ms
POST /upload HTTP/1.1
User-Agent: PostmanRuntime/7.26.8
Accept: */*
Postman-Token: db798ea3-af89-4a91-911e-ce52194580cb
Host: localhost:5000
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Type: multipart/form-data; boundary=--------------------------219062233821068812297853
Content-Length: 145051
----------------------------219062233821068812297853
Content-Disposition: form-data; name="file"; filename="WBHFromWestRWB.png"

<WBHFromWestRWB.png>
----------------------------219062233821068812297853--

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 26
Server: Werkzeug/2.0.2 Python/3.9.7
Date: Mon, 06 Dec 2021 03:57:24 GMT
{"classification":"pole"}