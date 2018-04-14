

def serialize_people_as_json(people):
    return {
        'name': people.name,
        'homeworld': 'http://localhost:8000/planets/{}/'.format(people.homeworld.id),
        'height': people.height,
        'mass': people.mass,
        'hair_color': people.hair_color,
        'created': people.created.isoformat(),
    }
