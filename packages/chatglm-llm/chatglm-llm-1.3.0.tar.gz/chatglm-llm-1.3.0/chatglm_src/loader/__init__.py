from langchain.document_loaders.word_document import UnstructuredWordDocumentLoader
from langchain.document_loaders import DirectoryLoader, TextLoader

def scan_docx(root):

    ds = DirectoryLoader(root, glob="**/*.docx", loader_cls=UnstructuredWordDocumentLoader)
    return ds.load()