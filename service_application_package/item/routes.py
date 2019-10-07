from flask import render_template, request, Blueprint

item = Blueprint('item', __name__)


@item.route('/addItem/<new_item>', methods=['POST']) #adding new item to list
def addItem(new_item):
	bucketList = mongo.db.bucketList
	item_new = {'name' : new_item}
	if bucketList.find({'name' : new_item}).count() > 0:
		return "Item Already Exists!"
	else:
		bucketList.insert(item_new)
		return "Added Item successfully"

@item.route('/deleteItem/<item_name>', methods=['GET']) #function to delete one item on list
def deleteItem(item_name):
	bucketList = mongo.db.bucketList
	bucketList.remove({'name': item_name})
	return "Item deleted successfully!"