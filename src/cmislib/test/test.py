from cmislib.model import CmisClient


class CmisDAO(object):
    def __init__(self,url,username,password):
        self.url = url
        self.username = username
        self.password = password
        self.client = CmisClient(self.url, self.username, self.password)

    def getDocumentStream(self,document_id):
        raise Exception("method not-implemented")

    def update_file(self, cmisFile):
        raise Exception("method not-implemented")

class CmisAlfresco(CmisDAO):

    def __init__(self, url, username, password):
        super(CmisAlfresco, self).__init__(url,username,password)

    def getDocumentStream(self,document_id):
        repo = self.client.defaultRepository
        document = repo.getObject("idd_"+document_id)
        properties = document.getProperties()
        doc_update = {}
        document.updateProperties(doc_update)
        repo = self.client.defaultRepository
        document = repo.getObject("idd_"+document_id)
        properties = document.getProperties()
        document.getContentStream()
# -------------------------------------------------------------
        document = repo.getObject("idf_" + "")
        properties = document.getProperties()
        doc_update = {}
        document.updateProperties(doc_update)
        repo = self.client.defaultRepository
        document = repo.getObject("idf_" + "")
        properties = document.getProperties()
        return ""


if __name__ == '__main__':
    REPOSITORY_URLAL = ''
    USERNAMEAL = ''
    PASSWORDAL = ''

    docDao = CmisAlfresco(REPOSITORY_URLAL, USERNAMEAL, PASSWORDAL)
    docDao.getDocumentStream()