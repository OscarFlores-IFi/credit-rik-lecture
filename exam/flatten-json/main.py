import utils
from models import load



filename = 'ex-5.json'
tmp = load(filename)
flatten = utils.flatten_dict(tmp)




