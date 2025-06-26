from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.models.guest import Guest
from server.app import db

episode_bp = Blueprint('episodes', __name__, url_prefix='/episodes')

@episode_bp.route('', methods=['GET'])
def list_episodes():
    episodes = Episode.query.all()
    return jsonify([{'id': e.id, 'number': e.number} for e in episodes])

@episode_bp.route('/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    appearances = [
        {
            'id': a.id,
            'rating': a.rating,
            'guest': {
                'id': a.guest.id,
                'name': a.guest.name,
                'occupation': a.guest.occupation
            }
        }
        for a in episode.appearances
    ]
    return jsonify({
        'id': episode.id,
        'number': episode.number,
        'appearances': appearances
    })

@episode_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({'message': 'Episode deleted'})
