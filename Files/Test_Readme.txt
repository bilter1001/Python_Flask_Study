mediaprocess — 启动、测试与部署说明
=================================

简介
----
本项目是一个基于 FastAPI 的微服务（包名：mediaprocess），在 mediaprocess.app 模块中暴露 FastAPI 对象 app，并提供 /v1/tags 等接口用于图像打标签（Clinx 集成）。

快速准备（推荐）
----------------
1. 创建并激活虚拟环境（推荐在项目根目录）：

- Windows (PowerShell)
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1

- Linux / macOS
  python3 -m venv .venv
  source .venv/bin/activate

2. 安装依赖（若有 requirements.txt，请优先使用）：
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

若没有 requirements.txt，至少安装：
python -m pip install fastapi uvicorn pydantic

在开发环境启动（本机）
---------------------
推荐使用项目虚拟环境的 python 来启动 uvicorn，确保使用的是项目依赖的解释器：

# 在项目根目录下（Windows PowerShell 示例）
. .venv\Scripts\Activate.ps1
# 使用项目 Python 启动 uvicorn，指定模块路径 mediaprocess.app:app
.venv\Scripts\python -m uvicorn mediaprocess.app:app --host 127.0.0.1 --port 8000 --reload

说明：
- 使用 127.0.0.1 绑定可以避免外部访问；若需要外部访问改为 --host 0.0.0.0。
- --reload 用于开发热重载；生产环境请移除并使用更稳健的部署方式（systemd 或容器化）。

测试
----
运行单元测试（推荐使用虚拟环境）：
.venv\Scripts\python -m pytest -q

注意：不要在测试文件的运行块里直接 import pytest（某些静态检查工具如 pyright 可能无法解析 pytest 导入）。如果需要在 __main__ 中支持“python tests/test_app.py”直接运行测试，请通过 subprocess 调用 python -m pytest 来避免静态分析器报错，例如：

if __name__ == "__main__":
    import sys, subprocess
    sys.exit(subprocess.call([sys.executable, "-m", "pytest", "-q", __file__]))

API 文档
-------
启动服务后，FastAPI 自动生成文档：
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- OpenAPI JSON: http://127.0.0.1:8000/openapi.json

示例：请求 /v1/tags
- 请求方法：POST
- Content-Type: application/json
- Body 示例（注意 Windows 路径中的反斜杠需要转义或使用正斜杠）：
  {"source": "D:/path/to/test-image.jpg"}
  或
  {"source": "D:\\\\path\\\\to\\\\test-image.jpg"}

生产部署（systemd 示例）
-----------------------
示例 systemd 单元（请替换路径、用户与组）：

[Unit]
Description=mediaprocess FastAPI service
After=network.target

[Service]
User=youruser
Group=yourgroup
WorkingDirectory=/path/to/renyun_media_process
Environment="PATH=/path/to/renyun_media_process/.venv/bin"
ExecStart=/path/to/renyun_media_process/.venv/bin/python -m uvicorn mediaprocess.app:app --host 0.0.0.0 --port 8000
Restart=on-failure

然后：
sudo systemctl daemon-reload
sudo systemctl enable mediaprocess
sudo systemctl start mediaprocess
sudo journalctl -u mediaprocess -f

Docker 化（可选）
----------------
可基于 python:3.x-slim 构建镜像，复制代码、安装依赖并用 uvicorn 启动。若需要我可以生成一个推荐的 Dockerfile。

常见问题与提示
----------------
- 若访问根路径 "/" 返回 404，请使用 /docs 或确认是否要在 mediaprocess.app 中添加根路由（GET /）进行重定向或返回健康检查信息。  
- 启动时出现端口被占用或多个 Python/uvicorn 进程：优先用项目 .venv 的 python 启动服务，并在必要时结束错误的进程（taskkill /PID <pid> /F 或使用系统进程管理工具）。  
- 在通过 HTTP 客户端（curl 或 Swagger UI）发送包含 Windows 路径的 JSON 时，请正确转义反斜杠或使用正斜杠以避免 "JSON decode error"。

后续
----
需要我为你：
- 在 mediaprocess.app 中添加一个根路由（/）返回健康检查或重定向到 /docs；
- 生成 Dockerfile、systemd 更详细的安全配置，或创建 start.ps1/start.sh 启动脚本？
请回复你想要的项。