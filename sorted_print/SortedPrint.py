import collections
import json

class OrderedResponse(object):
  def __init__(self, config=None):
    self.config = config

  def get_ordered_response(self, response, config=None):
    if not config:
      config = self.config
    try:
      result = collections.OrderedDict()
      for val in range(1, len(config)+1):
          x = str(val)
          if config[x]['type'] == 'obj':
            result[config[x]['key']] = self.get_ordered_response(response[config[x]['key']], config[x]['value'])
          elif config[x]['type'] == 'list':
            append_list = list()
            for item in response[config[x]['key']]:
              append_list.append(self.get_ordered_response(item, config[x]['value']))
            result[config[x]['key']] = append_list
          else:
            result[config[x]['key']] = response[config[x]['key']]

      return result
    except Exception, e:
      print ("Error ordering content, check the config is set correctly")

  def ordered_print(self, response, config=None):
    print(json.dumps(self.get_ordered_response(response, config), indent=4))