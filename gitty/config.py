

class Config:

  @staticmethod
  def get(repo, config_key):
    splitted_keys = config_key.split('.')

    splitted_keys_in_byte = [key.encode() for key in splitted_keys]
    
    if splitted_keys.__len__() > 2:
      section = tuple(splitted_keys_in_byte[:-1])
      arg = splitted_keys_in_byte[-1]
    else:
      section = splitted_keys_in_byte[0]
      arg = splitted_keys_in_byte[1]

    config = repo.get_config()

    try:
      value = config.get(section, arg)
    except KeyError:
      value = None 
      
    return value.decode() if value else value
