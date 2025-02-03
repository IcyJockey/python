from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Flask-Login requires a user_loader callback
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Here you should validate the user credentials and create a User instance
        user = User(username='testuser')
        login_user(user)
        return redirect(url_for('protected'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/protected')
@login_required
def protected():
    return f'Welcome, {current_user.username}!'

class User(UserMixin):
    pass

if __name__ == '__main__':
# Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    app.run(debug=True)
    