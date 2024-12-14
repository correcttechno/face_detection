from flask import Flask, render_template,Response
import cv2

# Flask uygulamasını başlatıyoruz
app = Flask(__name__)

# Genel bir rota tanımı
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/view')
def view():
    return render_template('view.html')

@app.route('/video_feed')
def video_feed():
    # Kameradan gelen veriyi döndürüyoruz
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


camera = cv2.VideoCapture(0)
def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Görüntüyü JPEG formatına dönüştürüyoruz
            frame=cv2.flip(frame, 1)
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Uygulamayı çalıştırma
if __name__ == '__main__':
    app.run(debug=True)
