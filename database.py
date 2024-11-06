
import os
from supabase import create_client, Client
from keys.py import *

class ImagineAllTheData():
    # Init class & suprabase database
    def ImagineAllTheData(self):

        # Always keep credentials in keys.py
        url: str = SUPABASE_URL
        key: str = SUPABASE_URL
        supabase: Client = create_client(url, key)

    # push news-article under /country/publisher/articleName to avoid name collition
    def pushArticle(country: str, publisher: str, articleName: str):
        pass
    # pull news-article under /country/publisher/articleName
    def pullArticle(country: str, publisher: str, articleName: str):
        pass

    # Check first if document exist; create document first before doing the compute to avoid double compute of an article
    def checkIfComputeExists(country: str, publisher: str, articleName: str):
        pass
    # push compute
    def pushCompute(country: str, publisher: str, articleName: str):
        if self.checkIfComputeExists(country, publisher, articleName):
            # TODO
            raise Exception("Not implemented")

        pass
    
    def pullCompute(country: str, publisher: str, articleName: str):
        pass