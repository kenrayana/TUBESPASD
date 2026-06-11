from predict import PredictaMind

user = PredictaMind(
    sleep_quality=8,
    academic_performance=8,
    study_load=3,
    extracurricular_activity=6
)

print("Stress Level :", user.prediksi_stres())
print("Productivity :", user.prediksi_produktivitas())
print("Readiness    :", user.hitung_readiness())
print("Forecast     :", user.productivity_forecast())