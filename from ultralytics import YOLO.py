from ultralytics import YOLO

# Trainiertes Modell laden
model = YOLO("C:\\Users\\reinstudent1\\Desktop\\ultralytics\\yolo11n.pt")

# Klassen anzeigen
print(model.names)