from flask_socketio import SocketIO, emit
from ..app_factory import create_app
from app.models import db, Item

socketio = SocketIO()

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('create_item')
def handle_create_item(data):
    item = Item(name=data['name'], value=data['value'])
    db.commit()  # Commit changes to the database
    emit('item_created', {'id': item.id, 'name': item.name, 'value': item.value}, broadcast=True)

@socketio.on('update_item')
def handle_update_item(data):
    item = Item.get(id=data['id'])
    if item:
        item.name = data['name']
        item.value = data['value']
        db.commit()  # Commit changes to the database
        emit('item_updated', {'id': item.id, 'name': item.name, 'value': item.value}, broadcast=True)

def init_socketio(app):
    socketio.init_app(app)
