import subprocess
import os

def generate_clips(videos):
    clips = []
    for video in videos:
        video_id = video['video_id']
        # Aquí se debe descargar el video primero (puedes usar pytube o youtube-dl)
        # Para ejemplo, asumimos video ya descargado: "{video_id}.mp4"

        input_file = f"videos/{video_id}.mp4"
        output_file = f"clips/{video_id}_clip.mp4"

        # Corta 30 segundos del minuto 1 (puedes cambiar según lógica)
        command = [
            "ffmpeg",
            "-ss", "00:01:00",
            "-i", input_file,
            "-t", "00:00:30",
            "-c", "copy",
            output_file
        ]
        subprocess.run(command, check=True)

        clips.append({"clip_path": output_file, "title": video['title']})
    return clips
