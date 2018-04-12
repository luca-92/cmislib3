from src.cmislib.browser.binding import BrowserBinding
from src.cmislib.model import CmisClient


class CmisDAO(object):
    def __init__(self,url,username,password):
        self.url = url
        self.username = username
        self.password = password
        self.client = CmisClient(self.url, self.username, self.password, binding=BrowserBinding())

    def getDocumentStream(self,document_id):
        raise Exception("method not-implemented")

    def update_file(self, cmisFile):
        raise Exception("method not-implemented")

class CmisAlfresco(CmisDAO):

    def __init__(self, url, username, password):
        super(CmisAlfresco, self).__init__(url,username,password)

    def getDocumentStream(self,document_id):
        repo = self.client.defaultRepository
        document = repo.getObject(document_id)
        properties = document.getProperties()
        print(properties['cmis:name'])
        doc_update = {'cmis:name': "bla1.eml"}
        document.updateProperties(doc_update)
        repo = self.client.defaultRepository
        document = repo.getObject(document_id)
        properties = document.getProperties()
        print(properties['cmis:name'])
        return document.getContentStream()


if __name__ == '__main__':
    REPOSITORY_URLAL = 'https://docs.dstech.info/alfresco/api/-default-/cmis/versions/1.1/browser'
    USERNAMEAL = 'l.marchetti@ilivetech.it'
    PASSWORDAL = 'buthujodac'

    docDao = CmisAlfresco(REPOSITORY_URLAL, USERNAMEAL, PASSWORDAL)
    docDao.getDocumentStream("workspace://SpacesStore/1c457c61-8b9a-49e4-9edd-ef4801ef76f5")