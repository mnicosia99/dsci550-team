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

    def __str__(self):
        return "Label: " +  self.label + " Type: " +  str(self.type) + " Date: " +  self.date + " Count: " + str(self.count)  
    
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Mention):
            return self.label == other.label and self.type == other.type and self.date == other.date
        return False
        
    def __hash__(self):
        return hash(self.label + self.date + str(self.type))
    
    def as_csv(self):
        return self.country + "," + self.date + "," + self.label + "," + str(self.latitude) + "," + str(self.longitude) + "," + str(self.count) + "," + self.type
