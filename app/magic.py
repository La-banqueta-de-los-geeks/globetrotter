class Magic:
  def __init__(self, username, password):
    self.username = username
    self.password = password

  def start(self):
    print(self.username)
    print(self.password)

class StartMagic(Magic):
  def gg(self):
    return self.password

while True:
  s = StartMagic(1,2)
  s.start()
  print(s.password)
  