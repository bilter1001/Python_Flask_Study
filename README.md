# Python_Flask_Study
学习Python后端开发的Flask项目，包含RESTful API示例和视频内容分析工具。

## 项目结构
- `app.py`: Flask应用主文件，包含基本的API路由示例
- `main.py`: 项目入口文件示例
- `video_analysis.py`: 视频内容分析工具，使用阿里云DashScope服务通过OpenAI兼容接口分析视频内容
- `pyproject.toml`: 项目配置文件，包含依赖管理

## 功能介绍

### Flask API示例
- 基础路由示例
- 带参数的路由
- 返回JSON数据的API接口

### 视频内容分析工具
`video_analysis.py` 文件提供了使用阿里云DashScope服务分析视频内容的功能：
- 支持通过URL分析视频内容
- 可以自定义提问内容
- 流式输出分析结果

## 安装指南

1. 确保已安装Python 3.12或更高版本
2. 克隆项目代码
3. 安装依赖：
   
   ```bash
   pip install -r requirements.txt
   ```

## 使用指南

### 运行Flask应用

```bash
python app.py
```

应用将在 http://localhost:5000 启动，可以通过浏览器访问以下API端点：
- http://localhost:5000/ - 基础问候
- http://localhost:5000/user/[用户名] - 带参数的路由示例
- http://localhost:5000/product/[类别]/[价格] - 多参数路由示例
- http://localhost:5000/api/data - JSON数据API示例

### 使用视频分析工具

1. 首先设置环境变量，配置阿里云DashScope API密钥：
   
   ```bash
   # Windows系统
   set DASHSCOPE_API_KEY=your_api_key_here
   
   # Linux/Mac系统
   export DASHSCOPE_API_KEY=your_api_key_here
   ```

2. 运行视频分析脚本：
   
   ```bash
   python video_analysis.py
   ```

   默认会分析示例视频，如果需要分析其他视频，可以修改脚本中的`sample_video_url`变量。

## 注意事项
- 使用视频分析功能时需要有效的阿里云DashScope API密钥
- 示例视频URL可能会失效，请根据实际情况替换为有效的视频URL
