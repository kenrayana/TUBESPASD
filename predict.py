class PredictaMind:

    # Constructor
    def __init__(self, jam_tidur, aktivitas, mood):

        self.jam_tidur = jam_tidur
        self.aktivitas = aktivitas
        self.mood = mood

    # =========================
    # PREDIKSI STRES
    # =========================
    def prediksi_stres(self):

        score = 0

        if self.jam_tidur < 5:
            score += 40

        if self.mood < 5:
            score += 40

        if self.aktivitas > 7:
            score += 20

        return score

    # =========================
    # KATEGORI STRES
    # =========================
    def kategori_stres(self):

        score = self.prediksi_stres()

        if score >= 70:
            return "Tinggi"

        elif score >= 40:
            return "Sedang"

        else:
            return "Rendah"

    # =========================
    # PREDIKSI PRODUKTIVITAS
    # =========================
    def prediksi_produktivitas(self):

        if self.jam_tidur >= 7 and self.mood >= 7:
            return "Tinggi"

        elif self.jam_tidur < 5 or self.mood < 5:
            return "Rendah"

        else:
            return "Sedang"

    # =========================
    # DAILY READINESS SCORE
    # =========================
    def hitung_readiness(self):

        score = (
            self.jam_tidur * 10 +
            self.mood * 5 +
            self.aktivitas * 3
        )

        if score > 100:
            score = 100

        return score

    # =========================
    # PRODUCTIVITY FORECAST
    # =========================
    def productivity_forecast(self):

        if self.mood >= 8:
            return "11 AM - 3 PM"

        elif self.mood >= 6:
            return "9 AM - 12 PM"

        else:
            return "Disarankan istirahat lebih dulu"