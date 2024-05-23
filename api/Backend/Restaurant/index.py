from ..Entity.Models import Region as RegionModel
from pony.orm import *
from flask import *


class Region:
    def __init__(self):
        self.region = RegionModel()

    def create_region(self):
        req_data = request.get_json()
        if not req_data:
            return jsonify({'error': 'Request is empty'})
        try:
            self.region.name = req_data['name']
            insert = commit()
            if insert:
                return jsonify({'success': 'Region created'})
            else:
                return jsonify({'error': 'Something went wrong, please try again'})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def get_all_region(self):
        try:
            data = self.region.select()
            if not data:
                return jsonify({'error': 'Region not found'})
            return jsonify({'region': data})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def get_region_by_id(self):
        reg_id = request.args.get('id')
        try:
            reg = self.region.get(id=reg_id)
            if not reg:
                return jsonify({'error': 'Region not found'})
            return jsonify({'region': reg})
        except Exception as e:
            return jsonify({'error': str(e)}), 500


    def delete_region_by_id(self):
        reg_id = request.args.get('id')
        try:
            reg = self.region.get(id=reg_id)
            if not reg:
                return jsonify({'error': 'Region not found'})
            self.region.delete(id=reg_id)
            return jsonify({'success': 'Region deleted'})
        except Exception as e:
            return jsonify({'error': str(e)}), 500


    def delete_all_region(self):
        try:
            dt=self.region.delete()
            if not dt:
                return jsonify({'error': 'Region Table is Empty'})
            return jsonify({'success': 'Region Table deleted'})
        except Exception as e:
            return jsonify({'error': str(e)}), 500


