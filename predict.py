import pickle
import pandas as pd


class PredictaMind:

    def __init__(
        self,
        sleep_quality,
        academic_performance,
        study_load,
        extracurricular_activity
    ):

        self.sleep_quality = sleep_quality
        self.academic_performance = academic_performance
        self.study_load = study_load
        self.extracurricular_activity = extracurricular_activity

    # =========================
    # PREDIKSI STRES (ML)
    # =========================

    def prediksi_stres(self):

        with open("models/model.pkl", "rb") as file:
            model = pickle.load(file)

        with open("models/encoder.pkl", "rb") as file:
            encoder = pickle.load(file)

        data = pd.DataFrame(
            [[
                self.sleep_quality,
                self.academic_performance,
                self.study_load,
                self.extracurricular_activity
            ]],
            columns=[
                "sleep_quality",
                "academic_performance",
                "study_load",
                "extracurricular_activity"
            ]
        )

        hasil = model.predict(data)

        return encoder.inverse_transform(hasil)[0]

    # =========================
    # PRODUKTIVITAS (RULE-BASED)
    # =========================

    def prediksi_produktivitas(self):

        score = (
            self.sleep_quality
            + self.academic_performance
            + self.extracurricular_activity
            - self.study_load
        )

        if score >= 15:
            return "High"

        elif score >= 10:
            return "Moderate"

        else:
            return "Low"

    # =========================
    # READINESS SCORE
    # =========================

    def hitung_readiness(self):

        readiness = (
            (self.sleep_quality * 4)
            + (self.academic_performance * 3)
            + (self.extracurricular_activity * 2)
            - (self.study_load * 2)
        )

        readiness = max(0, min(readiness, 100))

        return readiness

    # =========================
    # REKOMENDASI WAKTU PRODUKTIF
    # =========================

    def productivity_forecast(self):

        produktivitas = self.prediksi_produktivitas()

        if produktivitas == "High":
            return "08.00 - 12.00"

        elif produktivitas == "Moderate":
            return "13.00 - 16.00"

        else:
            return "17.00 - 20.00"