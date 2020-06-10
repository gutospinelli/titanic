
#imports to donwload data frm kaggle
import os
from dotenv import load_dotenv, find_dotenv
from requests import session
import logging

#payload for post
payload = {
    'action' : 'login',
    'username' : os.environ.get("KAGGLE_USERNAME"),
    'password' : os.environ.get("KAGGLE_PASSWORD")
}

#cria método generico para extrair dados do kaggle em um arquivo
def extract_data(url, file_path):
    with session() as c:
        #post request
        c.post('https://www.kaggle.com/account/login', data=payload)
        #open file to write (w = write string to file wb= write bytes to file) 
        with open(file_path,'wb') as handle:
            response = c.get(url, stream=True)
            for block in response.iter_content(1024):
                handle.write(block)

#cria main
def main(project_dir):
    #get logger
    logger = logging.getLogger(__name__)
    logger.info('START: getting raw data')
    
    #csv urls
    train_url = 'https://storage.googleapis.com/kagglesdsdata/competitions/3136/26502/train.csv?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1592010496&Signature=lwBG%2BE7uES4XaeSMHsGEHFP8m7vBa19fb5LYoWLBuhVVgvA3V6SWmMYm8HGwL8Jw1BCsXK5yh2fSBkdQiLInR6yBz5141hbKGedvzgCYh03prZ0cnnV4HJihXKx8oMJNy1ES9uyg1TAac8UQeykdZvOaElB9hUa%2Bt7y38iGdVEU4NmgJz4HAs36gfSbcV5VqCI8cakspNvIOgwIXu8xnoyKRKdKyoWSWe5AXOlAQJmt9%2BckoCHQWD0E9Q3gluPUh6Ilu3TR9aEDnv2no3kjQ8W%2Fm2AL5DDQtdQ95%2ByACfYe%2FBTHmfvei2GrRdwzej91AgL29bovhIe6x69ejDiO5vA%3D%3D&response-content-disposition=attachment%3B+filename%3Dtrain.csv'
    test_url = 'https://storage.googleapis.com/kagglesdsdata/competitions/3136/26502/test.csv?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1592011259&Signature=lCzZsd%2Bjf3eKFXjSZjP17LVgkT7QzfeBWnl9iGbZJvSQV1NpFOyAUzfMKe%2FvVigtT%2F%2FDsqsXnUddg6rVzD6NMHRNF1vmWQDjqKQMiL%2BE9SmAZpxDJLPR9O4D6HCyFfo2Iv5bJtVNCKFEQTYvzoJafOhkMJWHTpdU5z6tIu0ZcFvPcYq1zY7OfFRQk83CwkLTCw2GuzTVf7qINATQL4qQ7kXxZsusSV%2FtxrRsA4YZ3BSxauLZPMHjFRAG9Bzo9XZZDAmQqKBGje%2F7Ho8PnSCywH0F2Uh8Cjq8dVKtttlhAbF9qqs3wW0IqQtOXvTzywLR58UrZ3cn%2BZWNbMnmvhDoEQ%3D%3D&response-content-disposition=attachment%3B+filename%3Dtest.csv'

    #file paths
    raw_data_path = os.path.join(os.path.pardir, 'data', 'raw')
    train_data_path = os.path.join(raw_data_path, 'train.csv')
    test_data_path = os.path.join(raw_data_path, 'test.csv')

    #extract the data
    extract_data(train_url, train_data_path)
    extract_data(test_url, test_data_path)
    logger.info('END: downloaded raw test and training data')
    
if __name__ == '__main__':
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
    
    #setup logger
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    
    #acha o arquivo .ENV com a senha do kaggle na estrutura do projeto
    dotenv_path = find_dotenv()
    #carrega o arquivo
    load_dotenv(dotenv_path)
    
    #call main
    main(project_dir)
    
    
    
    
