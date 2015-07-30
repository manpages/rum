from sqlalchemy import Column, Integer, Boolean, String, ForeignKey

class Agreement(Base):
  __tablename__ = 'agreements'
  id            = Column (Integer,      primary_key=True)
  number        = Column (String(255),  nullable=False)
  def __repr__(self):
    return "<Agreement(number='%s')>" % (self.number)

class Device(Base):
  __tablename__ = 'devices'
  id            = Column (Integer,      primary_key=True)
  name          = Column (String(255),  nullable=False)
  def __repr__(self):
    return "<Device(name='%s')>" % (self.name)

class Session(Base):
  __tablename__ = 'sessions'
  id            = Column (Integer,      primary_key=True)
  agreement_id  = Column (Integer,      ForeignKey('agreements.id'))
  device_id     = Column (Integer,      ForeignKey('devices.id'))
  token         = Column (String(255),  nullable=False)
  def __repr__(self):
    return "<Session(device_id='%s', agreement_id='%s', token='%s')>" % ( self.device_id
                                                                        , self.agreement_id
                                                                        , self.token)

class Call(Base):
  __tablename__ = 'calls'
  id            = Column (Integer,      primary_key=True)
  agreement_id  = Column (Integer,      ForeignKey('agreements.id'))
  active        = Column (Boolean,      default=True)
  latitude      = Column (String(255),  nullable=False)
  longitude     = Column (String(255),  nullable=False)
  message       = Column (String(1000), nullable=True)
  def __repr__(self):
    return "<Call(agreement_id='%s', active='%s', latitude='%s', longitude='%s', message='%s'> % ( self.agreement_id
                                                                                                 , self.active
                                                                                                 , self.latitude
                                                                                                 , self.longitude
                                                                                                 , self.message )
