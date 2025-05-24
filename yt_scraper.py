from googleapiclient.discovery import build

API_KEY = "TU_YOUTUBE_API_KEY"  # Pon aquí tu clave de YouTube API

youtube = build('youtube', 'v3', developerKey=API_KEY)

def fetch_viral_videos(max_results=10):
    # Busca videos virales relacionados con streamers y youtubers populares
    query = "streamers youtubers virales"

    request = youtube.search().list(
        part="snippet",
        q=query,
        maxResults=max_results,
        order="viewCount",
        type="video",
        videoDuration="medium"
    )
    response = request.execute()

    videos = []
    for item in response['items']:
        video = {
            "video_id": item['id']['videoId'],
            "title": item['snippet']['title'],
            "channel": item['snippet']['channelTitle']
        }
        videos.append(video)
    return videos
