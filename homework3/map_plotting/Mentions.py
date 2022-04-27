import string
from datetime import datetime
from enum import Enum

class MentionType(Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"

class Mention:
    date: datetime
    type: string
    country: string
    label: string
    latitude: float
    longitude: float
    count: int

    # override for displaying the object in a readable representation
    def __str__(self):
        return "Label: " +  self.label + " Type: " +  str(self.type) + " Date: " +  self.date + " Count: " + str(self.count)  
    
    # override for use in a dict where the Mention object is the key
    def __eq__(self, other):
        if isinstance(other, Mention):
            return self.label == other.label and self.type == other.type and self.date == other.date
        return False
        
    # override for use in a dict where the Mention object is the key
    def __hash__(self):
        return hash(self.label + self.date + str(self.type))

    # return a string csv representation of the object
    def as_csv(self):
        return self.country + "," + self.date + "," + self.label + "," + str(self.latitude) + "," + str(self.longitude) + "," + str(self.count) + "," + self.type
