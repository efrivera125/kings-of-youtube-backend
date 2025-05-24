import whisper

model = whisper.load_model("base")

def generate_subtitles(clips):
    for clip in clips:
        result = model.transcribe(clip['clip_path'])
        srt_path = clip['clip_path'].replace(".mp4", ".srt")
        with open(srt_path, "w", encoding="utf-8") as f:
            f.write(result["text"])
        clip['subtitle_path'] = srt_path
