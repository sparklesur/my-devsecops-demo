from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from DevSecOps demo!"

# 模拟一个不安全的 eval（Semgrep 会检测到！）
user_input = "1+1"
# result = eval(user_input)  # ← 如果取消注释，Semgrep 会报警！

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
