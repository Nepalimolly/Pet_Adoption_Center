from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Spot = Pet(name='Spot', species='dog', age='6')
Hoppy = Pet(name='Hoppy', species='bunny', age='2')
Buddy = Pet(name='Buddy', species='dog', age='8')
Feline = Pet(name='Feline', species='cat', age='3')

db.session.add_all([Spot, Hoppy, Buddy, Feline])
db.session.commit()