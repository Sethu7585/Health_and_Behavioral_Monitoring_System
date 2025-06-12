from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')


@app.route('/signup')
def account_create():
    return render_template('signup.html')
@app.route('/resetpwd')
def reset_password():
    return render_template('resetpwd.html')
@app.route('/dashboard')
def dashboard_main():
    return render_template('dashboard.html')
@app.route('/home')
def home_content():
    return render_template('home.html')
@app.route('/professional-about-us-page')
def about_us():
    return render_template('professional-about-us-page.html')
@app.route('/firebase-profile-update')
def profile_update():
    return render_template('firebase-profile-update.html')
@app.route('/notifications')
def about_us1():
    return render_template('notifications.html')

@app.route('/reports')
def report_1():
    return render_template('reports.html')

@app.route('/live-monitoring')
def live_monitoring():
    return render_template('live-monitoring.html')

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

@app.route('/change-password')
def change_password():
    return render_template('change-password.html')
@app.route('/feedback')
def get_feedback():
    return render_template('feedback.html')

@app.route('/sensor-management')
def sensor_management():
    return render_template('sensor-management.html')

@app.route('/user-management')
def user_management():
    return render_template('user-management.html')
@app.route('/appointments')
def appointments_doctor():
    return render_template('appointments.html')
@app.route('/chat')
def ai_chat():
    return render_template('chat.html')
@app.route('/education')
def health_education():
    return render_template('education.html')
if __name__ == '__main__':
    app.run(host='localhost', port=5000, ssl_context=('localhost.pem', 'localhost-key.pem'), debug=True)
