"""autogenerated by genpy from beginner_tutorials/Message.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Message(genpy.Message):
  _md5sum = "50078cda89e3386814e896902e59c5d5"
  _type = "beginner_tutorials/Message"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32 year
int32 month
string day
int8 hour
int8 minut
int8 sec
"""
  __slots__ = ['year','month','day','hour','minut','sec']
  _slot_types = ['int32','int32','string','int8','int8','int8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       year,month,day,hour,minut,sec

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Message, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.year is None:
        self.year = 0
      if self.month is None:
        self.month = 0
      if self.day is None:
        self.day = ''
      if self.hour is None:
        self.hour = 0
      if self.minut is None:
        self.minut = 0
      if self.sec is None:
        self.sec = 0
    else:
      self.year = 0
      self.month = 0
      self.day = ''
      self.hour = 0
      self.minut = 0
      self.sec = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_2i.pack(_x.year, _x.month))
      _x = self.day
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3b.pack(_x.hour, _x.minut, _x.sec))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 8
      (_x.year, _x.month,) = _struct_2i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.day = str[start:end].decode('utf-8')
      else:
        self.day = str[start:end]
      _x = self
      start = end
      end += 3
      (_x.hour, _x.minut, _x.sec,) = _struct_3b.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_2i.pack(_x.year, _x.month))
      _x = self.day
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3b.pack(_x.hour, _x.minut, _x.sec))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 8
      (_x.year, _x.month,) = _struct_2i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.day = str[start:end].decode('utf-8')
      else:
        self.day = str[start:end]
      _x = self
      start = end
      end += 3
      (_x.hour, _x.minut, _x.sec,) = _struct_3b.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3b = struct.Struct("<3b")
_struct_2i = struct.Struct("<2i")
