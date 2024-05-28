from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Секретный ключ для работы flash-сообщений

# Список пользователей для проверки (используем простой словарь для примера)
users = {
    "doctor": {
        "password": "password123",
        "first_name": "John",
        "last_name": "Doe",
        "email": "doctor@example.com",
        "passport": "1234567890"
    }
}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        identifier = request.form.get('identifier')
        password = request.form.get('password')
        
        user = None
        for username, user_data in users.items():
            if username == identifier or user_data['email'] == identifier:
                user = user_data
                break
        
        if user and user['password'] == password:
            return redirect(url_for('dashboard'))
        else:
            flash("Неправильное имя пользователя, почта или пароль", "danger")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        passport = request.form.get('passport')
        
        # Проверка совпадения паролей
        if password != confirm_password:
            flash("Пароли не совпадают", "danger")
        elif username in users:
            flash("Пользователь уже существует!", "danger")
        else:
            users[username] = {
                "password": password,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "passport": passport
            }
            flash("Регистрация прошла успешно! Теперь вы можете войти.", "success")
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/patients')
def patients():
    return render_template('patients.html')

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

@app.route('/messages')
def messages():
    return render_template('messages.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
    app.run(debug=True)
