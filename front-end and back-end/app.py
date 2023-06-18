from flask import Flask, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL数据库配置
app.config['MYSQL_HOST'] = '23.95.140.241'
app.config['MYSQL_USER'] = 'mysql_username'
app.config['MYSQL_PASSWORD'] = 'mysql_password'
app.config['MYSQL_DB'] = 'game_db'

# 初始化MySQL
mysql = MySQL(app)

# 用户注册
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # 检查用户名是否已存在
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        existing_user = cur.fetchone()
        if existing_user:
            # 用户名已存在，返回错误消息给用户
            return render_template('register.html', error='Username already exists')
        else:
            # 在数据库中插入新用户信息
            cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            mysql.connection.commit()
            cur.close()
            # 注册成功，跳转到登录页面
            return redirect('/login')
    else:
        return render_template('register.html')

# 用户登录
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cur.fetchone()
        cur.close()
        if user:
            # 登录成功，进行后续操作
            return render_template('game.html', user=user)
        else:
            # 登录失败，返回错误消息给用户
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

# 游戏界面和物品加载
@app.route('/game')
def game():
    user_id = request.args.get('user_id')
    # 从数据库中获取用户的物品列表
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM items WHERE user_id = %s", (user_id,))
    items = cur.fetchall()
    cur.close()
    return render_template('game.html', items=items)

# NLP安慰功能
@app.route('/comfort', methods=['POST'])
def comfort():
    message = request.form['message']
    # 在此处使用NLP模型对message进行处理和安慰生成
    comforting_message = generate_comforting_message(message)
    return comforting_message

if __name__ == '__main__':
    app.run(host='23.95.140.241', port=500)
