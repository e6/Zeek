import Queue

CONFIG = 'CONFIG'
INFO = 'INFO'
URL = 'URL'


class Packet:
    def __init__(self, type, payload):
        self.type = type
        self.payload = payload

    def setPayload(self, payload):
        self.payload = payload


class ConfigurationPayload():
    STATIC_CRAWLING = 'STATIC'
    DYNAMIC_CRAWLING = 'DYNAMIC'

    def __init__(self, crawlingType):
        self.crawlingType = crawlingType
        self.domainRestricted = False
        self.requestLimit = 0
        self.crawlDelay = 0


class InfoPayload():
    CLIENT_ACK = 0
    SERVER_ACK = 1

    def __init__(self, info):
        self.info = info


class URLPayload():
    VISITED = 'VISITED'
    SKIPPED = 'SKIPPED'
    TOVISIT = 'TOVISIT'
    SCRAPPED_URL = 'SCRAPPED'

    def __init__(self, urlList, type, data=None):
        #self.url = url TODO : add url param (to know where the data is coming from)
        self.urlList = []
        self.type = type
        self.data = data

        for url in urlList:
            self.urlList.append(url)


def deQueue(queueArray):
    packetArray = []
    for queue in queueArray:
        try:
            packet = queue.get(block=False)
            packetArray.append(packet)
        except Queue.Empty:
            pass
    return packetArray