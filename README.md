This is a Flask restful API for checking inventories of a store.<br />
<br />
The app has following endpoints:<br />
<br />
POST /register - for registering a user.<br />
POST /auth - for authentication.<br />
GET /items - gets all items in the database.<br />
GET /stores - gets all stores in the database.<br />
GET /item/<name> - fetch details of only item <name>.<br />
GET /store/<name> - fetch details of <name> store.<br />
POST /item/<name> - post details of item <name>.<br />
POST /store/<name> - post details of store <name>.<br />
DEL /item/<name> - deletes item <name>.<br />
DEL /store/<name> - deletes item <store>.<br />
PUT /item/<name> - updates item <name>.<br />



