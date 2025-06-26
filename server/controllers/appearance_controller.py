from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from server.models.appearance import Appearance
from server.app import db

appearance_bp = Blueprint('appearances', __name__, url_prefix='/appearances')

@appearance_bp.route('', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    appearance = Appearance(
        rating=data.get('rating'),
        guest_id=data.get('guest_id'),
        episode_id=data.get('episode_id')
    )
    db.session.add(appearance)
    db.session.commit()
    return jsonify({'message': 'Appearance created', 'id': appearance.id}), 201
