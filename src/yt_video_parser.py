import googleapiclient.discovery
import isodate


def get_playlist_videos(api_key, playlist_id):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

    playlist_items = []
    next_page_token = None

    while True:
        request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()

        playlist_items.extend(response['items'])

        next_page_token = response.get('nextPageToken')
        if next_page_token is None:
            break

    return [item['contentDetails']['videoId'] for item in playlist_items]


def get_video_count_durations(api_key, video_ids):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

    total_duration = isodate.parse_duration("PT0S")
    total_count = 0

    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part="contentDetails",
            id=','.join(video_ids[i:i+50])
        )
        response = request.execute()

        for item in response['items']:
            duration = isodate.parse_duration(item['contentDetails']['duration'])
            total_duration += duration
            total_count += 1

    return total_count, total_duration
