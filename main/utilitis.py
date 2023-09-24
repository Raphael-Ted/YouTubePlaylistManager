from googleapiclient.discovery import build
import re

# def print_dict(dic):
#     for i in dic.keys():
#         print(i + ': ' + str(dic[i]))


def get_videos_id_from_playlist(pl_id, ):
    youtube = build("youtube", 'v3', developerKey=youtube_api_key)
    nextPageToken = None
    video_ids = []
    while True:
        pl_request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=pl_id,
            maxResults=50,
            pageToken=nextPageToken,
        )
        pl_response = pl_request.execute()

        # print_dict(pl_response)

        for item in pl_response["items"]:
            # print(item)
            video_ids.append(item["contentDetails"]["videoId"])

        nextPageToken = pl_response.get('nextPageToken')
        if not nextPageToken:
            break
    youtube.close()
    return video_ids


def get_pl_Id_from_url(url):
    if not is_youtube_playlist(url):
        return "not a playlist"

    pattern = r'(?:playlist\?list=|watch\?v=[\w-]+&list=)([\w-]+)'
    match = re.search(pattern, url)

    if match:
        playlist_id = match.group(1)  # Extract the matched group
        return playlist_id
    else:
        return "Unable to extract playlist ID"


def is_youtube_playlist(url):
    """
    So, in summary, the regex pattern checks for YouTube playlist URLs that start with either http:// or https://,
    followed by an optional "www." subdomain, then "youtube.com/", and finally either "playlist?list=" or
    "watch?v=VIDEO_ID&list=" followed by the playlist identifier.
     :param url: url to check
     :return: true if there is a playlist id in it
    """
    # Define a regex pattern for YouTube playlist URLs
    pattern = r'^https?://(?:www\.)?youtube\.com/(?:playlist\?list=|watch\?v=[\w-]+&list=)[\w-]+'
    match = re.match(pattern, url)

    return bool(match)
