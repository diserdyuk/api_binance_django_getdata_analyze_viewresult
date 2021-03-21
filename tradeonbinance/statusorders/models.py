from django.db import models


class StatusOrder(models.Model):
    LONGPOSITION = 'LP'
    SHORTPOSITION = 'SP'
    WAITINGCONDITION = 'WC'
    SIDE_POSITION = [
        (LONGPOSITION, 'Long position'),
        (SHORTPOSITION, 'Short position'),
        (WAITINGCONDITION, 'Waiting condition'),
    ]
    
    NOTPOSITION = 'NP'
    OPENEDLONGPOSITION = 'OLP'
    OPENEDSHORTPOSITION = 'OSP'
    CLOSEDLONGPOSITION = 'CLP'
    CLOSEDSHORTPOSITION = 'CLP'
    NOTCLOSEDPOSITION = 'NCP'
    STATUS_POSITION = [
        (NOTPOSITION, 'Not position'),
        (OPENEDLONGPOSITION, 'Opened long position'),
        (OPENEDSHORTPOSITION, 'Opened short position'),
        (CLOSEDLONGPOSITION, 'Closed long position'),
        (CLOSEDSHORTPOSITION, 'Closed short position'),
        (NOTCLOSEDPOSITION, 'Not closed position'),
    ]

    ticker = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=19, decimal_places=10)
    side = models.CharField(max_length=255, choices=SIDE_POSITION, default=WAITINGCONDITION)
    size = models.IntegerField()
    time = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=STATUS_POSITION, default=NOTPOSITION)
    
    def __str__(self):
        return (self.ticker)


class Config(models.Model):

    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    
 



