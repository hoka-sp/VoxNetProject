import random
from datetime import datetime
from pathlib import Path
from voicevox_core import VoicevoxCore


class CreateWavBytes:
    def __init__(self):
        self.core = VoicevoxCore(
            open_jtalk_dict_dir=Path(
                "VoiceVoxEngine/open_jtalk_dic_utf_8-1.11"
            )
        )

    def create_wav_file(self, text, speaker_id, output_path):
        if not self.core.is_model_loaded(speaker_id):
            self.core.load_model(speaker_id)

        wave_bytes = self.core.tts(text, speaker_id)

        now = datetime.now()
        formatted_date = now.strftime('%Y%m%d_%H%M%S')
        milliseconds = now.strftime('%f')[:3]
        random_number = f"{random.randint(0, 999):03}"
        file_name = f"{formatted_date}_{milliseconds}_{random_number}"

        with open(f"{output_path}/{file_name}.wav", "wb") as f:
            f.write(wave_bytes)

        return file_name
