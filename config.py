from dotenv import dotenv_values

config = dotenv_values('.env')
password = config['PASSWORD']

