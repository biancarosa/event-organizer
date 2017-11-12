"""connector helps us connect mongodb"""
import mongoengine

def connect():
    mongoengine.connect('organizer', username='bia', password='supersecurepwd')