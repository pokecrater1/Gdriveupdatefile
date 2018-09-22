from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from apiclient.http import MediaFileUpload
from pathlib import Path
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/drive'

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))

    # Call the Drive v3 API
    results = service.files().list(
        pageSize=10, fields="nextPageToken, files(id, name, mimeType)").execute()
		
    items = results.get('files', [])
	
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print('name:{0}\t id: {1} \t mimeType: {2}'.format(item['name'], item['id'], item['mimeType']))
	
    print()
    print('File(s) uploaded:')
    name = 'FILENAMEHERE'
    
	
    media = MediaFileUpload(name, mimetype='MIMETYPEHERE', resumable=True)
	
	#dictionary for file's metadata
    metadata = {
		'title': 'FILENAMEHERE'
    }
	
    updatefile = service.files().update(body=metadata, fileId = 'GOOGLEDRIVEFILEIDHERE',
		media_body=media).execute()
	
    if updatefile:
    	print('Uploaded "%s"' %(name))

if __name__ == '__main__':
    main()