class Spacemission(object):

    """
    In this class one initiates a counter for every country
    to make sure the political constraint are held
    """
      
    def __init__(self, sm_id):
        self.sm_id = sm_id
        self.count = 0

    def counter(self):
        self.count += 1
        return
