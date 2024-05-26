import os
from dotenv import load_dotenv
from yt_video_parser import get_video_count_durations
from yt_video_parser import get_playlist_videos


load_dotenv()


def main():
    api_key = os.getenv("YOUTUBE_API_KEY")
    if not api_key:
        raise ValueError("Please set the YOUTUBE_API_KEY environment variable")

    playlist_url = input("Enter YouTube playlist URL: ")
    if "list=" not in playlist_url:
        raise ValueError("Invalid YouTube playlist URL")

    playlist_id = playlist_url.split("list=")[1].split("&")[0]

    video_ids = get_playlist_videos(api_key, playlist_id)
    total_count, total_duration = get_video_count_durations(api_key, video_ids)

    print(f"Total duration of the playlist is: {total_duration}")
    print(f"Total count of the playlist videos: {total_count}")


if __name__ == "__main__":
    main()
