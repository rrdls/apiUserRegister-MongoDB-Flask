

userSchema = {
    "name": {"type": "string", 'empty': False},
    "email": {"type": "string",  'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'},
    "pwd": {"type": "string"},
    "date": {"type": "date"}
}
