from ..Entity.Models import Category
from flask import request, jsonify
from pony.orm import *
class Category:
    def __init__(self):
        self.category = Category()

    def insert(self):
        if not request.json:
            return jsonify('there is no data', 404)
        self.category.name = request.json['name']
        commit()

    def update(self):
        if not request.json:
            return jsonify('there is no data', 404)
        ctgry = self.category.get(id=request.json['id'])
        if not ctgry :
            return jsonify('category does not exist', 404)
        self.category.name = request.json['name']
        commit()
        return self.category.name

    def getAll(self):
        ctgry= self.category.getAll()
        if len(ctgry) == 0:
            return jsonify('there is no categories yet')
        return ctgry

    def getById(self):
        if not request.json:
            return jsonify('there is no data', 404)
        ctrgry = self.category.get(id=request.json['id'])
        if not ctrgry:
            return jsonify('category does not exist', 404)
        return ctrgry

    def deleteById(self):
        if not request.json:
            return jsonify('there is no data', 404)
        ctgry = self.category.getById(id=request.json['id'])
        if not ctgry:
            return jsonify('category does not exist', 404)
        self.category.deleteById(request.json['id'])
        return jsonify('category deleted', 200)




