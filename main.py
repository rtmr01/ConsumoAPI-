import googleapiclient.discovery
import csv

api_key = "AIzaSyDFYO5NXhuAMVgiXjUgDdCZjhpafRJebx8"  # MINHA CHAVE API

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)  # qual yt vamos usar

response = youtube.playlistItems().list(part="snippet", playlistId="PLfoNZDHitwjUv0pjTwlV1vzaE0r7UDVDR", maxResults=24).execute()  # 24 para contar o GP Abu Dhabi (08/12) que ainda nao rolou


video_data = {video["snippet"]["resourceId"]["videoId"]: video["snippet"]["title"] for video in response["items"]}

video_ids = list(video_data.keys())
stats_response = youtube.videos().list(part="snippet,statistics,contentDetails", id=",".join(video_ids)).execute()


with open('video_stats.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Título", "ID do vídeo", "Views", "Likes", "Comentários", "Duração", "Data de publicação"])

   
    for item in stats_response["items"]:
        video_id = item["id"]
        stats = item["statistics"]
        snippet = item["snippet"]
        content_details = item["contentDetails"]
        
        title = video_data[video_id]
        views = stats.get('viewCount', 'N/A')
        likes = stats.get('likeCount', 'N/A')
        comments = stats.get('commentCount', 'N/A')
        duration = content_details.get('duration', 'N/A')
        published_at = snippet.get('publishedAt', 'N/A')
        
        
        writer.writerow([title, video_id, views, likes, comments, duration, published_at])

print("Dados salvos no arquivo 'video_stats.csv'.")
