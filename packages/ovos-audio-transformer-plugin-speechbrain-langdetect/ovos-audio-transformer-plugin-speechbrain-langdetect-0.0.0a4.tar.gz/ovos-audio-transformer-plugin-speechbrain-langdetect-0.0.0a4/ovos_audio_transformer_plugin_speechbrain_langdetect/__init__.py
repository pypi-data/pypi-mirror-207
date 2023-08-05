import numpy as np
import torch

from ovos_bus_client.session import SessionManager
from ovos_plugin_manager.templates.transformers import AudioTransformer
from ovos_utils.log import LOG
from ovos_utils.xdg_utils import xdg_data_home
from speechbrain.pretrained import EncoderClassifier


class SpeechBrainLangClassifier(AudioTransformer):
    def __init__(self, config=None):
        config = config or {}
        super().__init__("ovos-audio-transformer-plugin-speechbrain-langdetect", 10, config)
        model = self.config.get("model") or "speechbrain/lang-id-commonlanguage_ecapa"
        if self.config.get("use_cuda"):
            self.engine = EncoderClassifier.from_hparams(source=model, savedir=f"{xdg_data_home()}/speechbrain",
                                                         run_opts={"device": "cuda"})
        else:
            self.engine = EncoderClassifier.from_hparams(source=model, savedir=f"{xdg_data_home()}/speechbrain")

    @staticmethod
    def audiochunk2array(audio_data):
        # Convert buffer to float32 using NumPy
        audio_as_np_int16 = np.frombuffer(audio_data, dtype=np.int16)
        audio_as_np_float32 = audio_as_np_int16.astype(np.float32)

        # Normalise float32 array so that values are between -1.0 and +1.0
        max_int16 = 2 ** 15
        data = audio_as_np_float32 / max_int16
        return torch.from_numpy(data).float()

    def signal2probs(self, signal):
        probs, _, _, _ = self.engine.classify_batch(signal)
        probs = torch.softmax(probs[0], dim=0)
        labels = self.engine.hparams.label_encoder.decode_ndim(range(len(probs)))
        results = {}
        for prob, label in sorted(zip(probs, labels), reverse=True):
            results[label.split(":")[0]] = prob.item()
        return results

    # plugin api
    def transform(self, audio_data):
        signal = self.audiochunk2array(audio_data)

        # list of lang codes for this request from bus message/config
        s = SessionManager.get()
        valid = [l.split("-")[0] for l in s.valid_languages]

        probs = self.signal2probs(signal)
        probs = [(k, v) for k, v in probs.items() if k in valid]
        lang, prob = max(probs, key=lambda k: k[1])
        LOG.info(f"Detected speech language '{lang}' with probability {prob}")
        return audio_data, {"stt_lang": lang.split(":")[0], "lang_probability": prob}


if __name__ == "__main__":
    from speech_recognition import Recognizer, AudioFile

    jfk = "/home/miro/PycharmProjects/ovos-stt-plugin-fasterwhisper/jfk.wav"
    with AudioFile(jfk) as source:
        audio = Recognizer().record(source)

    s = SpeechBrainLangClassifier()
    s.transform(audio.get_wav_data())
    # {'stt_lang': 'en', 'lang_probability': 0.8076384663581848}
