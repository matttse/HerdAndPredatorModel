from flask import render_template, request, Blueprint, jsonify

catalog = Blueprint('catalog', __name__)


@catalog.route('/viewCatalog', methods=['GET']) #viewing all contents of catalog
def getCatalog():
	Catalog = mongo.db.Catalog
	items = []
	item = Catalog.find()
	for j in item:
		j.pop('_id')
		items.append(j)
	return jsonify(items)	