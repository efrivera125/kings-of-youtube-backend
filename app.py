from fastapi import FastAPI, BackgroundTasks
from yt_scraper import fetch_viral_videos
from clip_generator import generate_clips
from subtitle_generator import generate_subtitles
from uploader import upload_to_youtube

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Kings of YouTube backend activo."}

@app.post("/run-workflow/")
def run_workflow(background_tasks: BackgroundTasks):
    background_tasks.add_task(full_workflow)
    return {"message": "Proceso automatizado iniciado."}

def full_workflow():
    # 1. Obtener videos virales
    videos = fetch_viral_videos()

    # 2. Crear clips
    clips = generate_clips(videos)

    # 3. Generar subtítulos
    generate_subtitles(clips)

    # 4. Subir clips a YouTube
    for clip in clips:
        upload_to_youtube(clip)
