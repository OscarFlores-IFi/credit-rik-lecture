import utils
from models import load



filename = 'ex-5.json'
tmp = load(filename)

utils.flatten_dict(tmp)




