This is a Flask restful API for checking inventories of a store.

The app has following endpoints:

POST /register - for registering a user.
POST /auth - for authentication.
GET /items - gets all items in the database.
GET /stores - gets all stores in the database.
GET /item/<name> - fetch details of only item <name>
GET /store/<name> - fetch details of <name> store.
POST /item/<name> - post details of item <name>.
POST /store/<name> - post details of store <name>.
DEL /item/<name> - deletes item <name>.
DEL /store/<name> - deletes item <store>.
PUT /item/<name> - updates item <name>.



