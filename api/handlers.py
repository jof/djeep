
from django.core import exceptions
from piston import handler
from piston.utils import rc

from rolemapper import models

#class BaseHandler(handler.BaseHandler):

#  def update(self, request, *args, **kwargs):
#    if not self.has_model():
#      return rc.NOT_IMPLEMENTED

#    pkfield = self.model._meta.pk.name

#    if pkfield not in kwargs:
#      # No pk was specified
#      return rc.BAD_REQUEST

#    try:
#      inst = self.queryset(request).get(pk=kwargs.get(pkfield))
#    except exceptions.ObjectDoesNotExist:
#      return rc.NOT_FOUND
#    except exceptions.MultipleObjectsReturned:
#      return rc.BAD_REQUEST

#    attrs = self.flatten_dict(request.data)
#    for k,v in attrs.iteritems():
#      setattr(inst, k, v)

#    inst.save()
#    return rc.ALL_OK

class HardwareInfoHandler(handler.BaseHandler):
  allowed_methods = ('GET', 'PUT')
  model = models.HardwareInfo

  #def read(self, request, hardware_id=None):
  #  base = models.HardwareInfo.objects

  #  if hardware_id:
  #    return base.get(pk=hardware_id)
  #  else:
  #    return base.all()
