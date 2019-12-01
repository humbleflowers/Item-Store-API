from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('store_id',
        type=int,
        required=True,
        help="Every item has store_id"
    )
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message':'item {} not found'.format(name)}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message":"The item {} already exists.".format(name)}, 400
          #if contenttype and body  is not json, this statement fails
        data = Item.parser.parse_args()
        #force converts the request to json
        item = ItemModel(name, **data)
        try:
            item.save_to_db()
        except:
            return {'message': 'Error occured while inserting item {}'.format(name)}, 500 # internal server error
        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'item {} deleted'.format(name)}


    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']
        item.save_to_db()
        return item.json()

class ItemList(Resource):
    def get(self):

        #return {'items':[item.json() for item in ItemModel.query.all()}
        return {'items':list(map(lambda x:x.json(), ItemModel.query.all()))}
