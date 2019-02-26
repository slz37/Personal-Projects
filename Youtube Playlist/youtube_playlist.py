import os, sys
import youtube_dl

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from oauth2client import client, GOOGLE_TOKEN_URI

#Credential Information
CLIENT_SECRETS_FILE = 'client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
VIDEO_BASE_URL = 'https://www.youtube.com/watch?v='


#######
####### Begin Edit

#Account Information
'''
See for setting up Youtube API credentials:
https://help.aolonnetwork.com/hc/en-us/articles/218079623-How-to-Create-Your-YouTube-API-Credentials
'''
CLIENT_ID = 'REPLACE WITH CLIENT ID'
CLIENT_SECRET = 'REPLACE WITH CLIENT SECRET'
REFRESH_TOKEN = 'REPLACE WITH REFRESH TOKEN'

#Download Information
DOWNLOAD = False
PLAYLIST_ID = 'REPLACE WITH ID OF PLAYLIST TO DOWNLOAD FROM'
MP3_QUALITY = '320' #kbps
CODEC = 'mp3'

#Transfer Information
TRANSFER = False
FROM_PLAYLIST_ID = 'REPLACE WITH ID OF PLAYLIST TO MOVE FROM'
TO_PLAYLIST_ID = 'REPLACE WITH ID OF PLAYLIST TO MOVE TO'

#Delete Information
DELETE = False
DELETE_PLAYLIST_ID = 'REPLACE WITH ID OF PLAYLIST TO DELETE ALL VIDEOS FROM'

####### End Edit
#######

def get_authenticated_service():
    #Get your credentials and authorize a resource for interacting with
    #Youtube API. This should work even if access token has expired
    
    credentials = client.OAuth2Credentials(access_token = None,
                                           client_id = CLIENT_ID,
                                           client_secret = CLIENT_SECRET,
                                           refresh_token = REFRESH_TOKEN,
                                           token_expiry = None,
                                           token_uri = GOOGLE_TOKEN_URI,
                                           user_agent = None,
                                           revoke_uri= None)    
    service = build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

    return service

def get_playlist_videos(service, playlist_id = PLAYLIST_ID):
    #Grabs information about all videos in playlist indicated
    #by PLAYLIST_ID and passes them to be downloaded
    
    #Get list of videos from first page of playlist
    video_list = service.playlistItems().list(part = 'snippet',
                                              playlistId = playlist_id,
                                              maxResults = 50
                                              ).execute()
    items = video_list['items']
    
    #Run until we reach the last page of the playlist
    next_page_token = video_list.get('nextPageToken')
    while 'nextPageToken' in video_list:
        #Get list of videos from next page in playlist
        page_list = service.playlistItems().list(part = 'snippet',
                                                 playlistId = playlist_id,
                                                 maxResults = 50,
                                                 pageToken = next_page_token
                                                 ).execute()
        items = items + page_list['items']
        
        #If last page, we're done
        if 'nextPageToken' not in page_list:
            break
        else:
            next_page_token = page_list.get('nextPageToken')

    return items

def get_video_ids(items):
    #Creates an array with the first column being
    #the name and the second being the video id
    
    #Make new array with title and id
    videos = []
    for item in items:
        #Grab useful information from list
        title = item['snippet']['title']
        ids = item['snippet']['resourceId']['videoId']

        videos.append([title, ids])

    return videos

def get_video_long_ids(items):
    #Creates an array with the first column being
    #the name and the second being the long video id
    #This is necessary for deleting videos from a playlist
    
    #Make new array with title and long id
    videos = []
    for item in items:
        #Grab useful information from list
        title = item['snippet']['title']
        ids = item['id']

        videos.append([title, ids])

    return videos

def format_name(name):
    #Formats file name for checking if exists
    #Doesn't catch everything
    name = name.replace(':', ' -')
    name = name.replace('"', '\'')
    name = name.replace('|', '_')
    name = name.replace('//', '_')
    name = name.replace('/', '_')
    return name

def download_videos(service):
    #Downloads the list of videos contained within
    #PLAYLIST_ID
    
    #Video list
    items = get_playlist_videos(service)
    video_list = get_video_ids(items)
    
    #Options for downloading
    yd_opts = {'format': 'bestaudio/best',
               'outtmpl': '/downloads/%(title)s.%(ext)s',
               'postprocessors': [{'key': 'FFmpegExtractAudio',
                                   'preferredcodec': CODEC,
                                   'preferredquality': MP3_QUALITY,
                                   }],
               }

    downloaded = [file.rsplit('.', 1)[0] for file in os.listdir('downloads/')]

    #Download each video as mp3
    for video in video_list:
        name = format_name(video[0])
        
        #Check if already downloaded, else download
        if name in downloaded:
            print('File with name exists, skipping {}'.format(video[0]))
            continue
        else:
            with youtube_dl.YoutubeDL(yd_opts) as yd:
                url = VIDEO_BASE_URL + video[1]
                yd.download([url])

    return

def move_to_playlist(service):
    #Moves all videos in the FROM_PLAYLIST_ID
    #to TO_PLAYLIST_ID
    
    #Get list of videos from playlist
    items = get_playlist_videos(service, FROM_PLAYLIST_ID)
    video_list = get_video_ids(items)

    #List of videos already in playlist
    items = get_playlist_videos(service, TO_PLAYLIST_ID)
    transfer_playlist_videos = get_video_ids(items)
    transfer_playlist_videos = [video[1] for video in transfer_playlist_videos]

    #Add videos to transfer playlist
    for video in video_list:
        video_name = video[0]
        video_id = video[1]
        
        #Skip if already in playlist or private
        if video_name == 'Private video':
            print('Skipping private video.')
            continue
        elif video_id in transfer_playlist_videos:
            print('Video already in playlist, skipping {}'.format(video[0]))
            continue
        else:
            print('Adding {} to playlist...'.format(video[0]))
            updated_playlist = service.playlistItems().insert(part = 'snippet',
                                                              body = {
                                                                  'snippet': {
                                                                      'playlistId': TO_PLAYLIST_ID,
                                                                      'resourceId': {
                                                                          'kind': 'youtube#video',
                                                                          'videoId': video_id
                                                                          }
                                                                      }
                                                                  }
                                                              ).execute()
    return

def delete_from_playlist(service):
    #Deletes all videos contained within
    #DELETE_PLAYLIST_ID

    #Get list of videos from playlist
    items = get_playlist_videos(service, DELETE_PLAYLIST_ID)
    video_list = get_video_long_ids(items)

    #Add videos to transfer playlist
    for video in video_list:
        video_name = video[0]
        video_id = video[1]
        
        print('Deleting {} from playlist...'.format(video[0]))
        updated_playlist = service.playlistItems().delete(id = video_id).execute()
    
    return

service = get_authenticated_service()
if DOWNLOAD:
    print('Downloading...')
    download_videos(service)
if TRANSFER:
    print('Transfering...')
    move_to_playlist(service)
if DELETE:
    print('Deleting...')
    delete_from_playlist(service)
