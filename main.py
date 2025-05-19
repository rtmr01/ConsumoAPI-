import googleapiclient.discovery
import csv

api_key = ""  # coloque aqui sua CHAVE API

# Inicializar o cliente da API YouTube
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

# Obter itens da playlist
response = youtube.playlistItems().list(
    part="snippet", 
    playlistId="PLfoNZDHitwjUv0pjTwlV1vzaE0r7UDVDR", 
    maxResults=24
).execute()

# Coletar IDs e títulos dos vídeos
video_data = {
    video["snippet"]["resourceId"]["videoId"]: video["snippet"]["title"] 
    for video in response["items"]
}

# Obter estatísticas e detalhes dos vídeos
video_ids = list(video_data.keys())
stats_response = youtube.videos().list(
    part="snippet,statistics,contentDetails", 
    id=",".join(video_ids)
).execute()

# Criar e escrever no arquivo CSV
with open('Estatísticas.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Cabeçalhos
    writer.writerow([
        "Título", "ID do vídeo", "Views", "Likes", "Comentários", 
        "Duração", "Data de publicação", "Descrição", "Palavras-chave"
    ])

    for item in stats_response["items"]:
        video_id = item["id"]
        stats = item.get("statistics", {})
        snippet = item["snippet"]
        content_details = item["contentDetails"]

        title = video_data[video_id]
        views = stats.get('viewCount', 'N/A')
        likes = stats.get('likeCount', 'N/A')
        comments = stats.get('commentCount', 'N/A')
        duration = content_details.get('duration', 'N/A')
        published_at = snippet.get('publishedAt', 'N/A')
        description = snippet.get('description', 'N/A')
        tags = ", ".join(snippet.get('tags', []))  # Combinar tags em uma string separada por vírgulas

        writer.writerow([
            title, video_id, views, likes, comments, 
            duration, published_at, description, tags
        ])

print("Dados salvos no arquivo 'Estatísticas.csv'.")
