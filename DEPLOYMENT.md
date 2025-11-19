# 🚀 Deployment Guide - Factor Momentum Visualizer

Complete guide for deploying the Factor Momentum Visualizer to various platforms.

---

## 📋 Table of Contents

1. [Streamlit Cloud (Recommended)](#streamlit-cloud)
2. [Heroku](#heroku)
3. [HuggingFace Spaces](#huggingface-spaces)
4. [Docker](#docker)
5. [AWS EC2](#aws-ec2)

---

## 🌥️ Streamlit Cloud (Recommended)

**Easiest and fastest deployment option - FREE tier available!**

### Prerequisites
- GitHub account
- Your code pushed to a GitHub repository

### Steps

1. **Prepare Your Repository**
   ```bash
   # Make sure all files are committed
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Go to Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"

3. **Connect Your Repository**
   - Authorize Streamlit to access your GitHub
   - Select your repository
   - Select branch: `main`
   - Main file path: `app.py`

4. **Configure Settings**
   - App URL: Choose a custom subdomain (optional)
   - Python version: 3.8+

5. **Deploy!**
   - Click "Deploy"
   - Wait 2-3 minutes for build
   - Your app is live! 🎉

### Configuration (Optional)

Create `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

[server]
maxUploadSize = 200
enableCORS = false
```

---

## 🔴 Heroku

Deploy to Heroku for more control and custom domain support.

### Prerequisites
- Heroku account (free tier available)
- Heroku CLI installed

### Steps

1. **Install Heroku CLI**
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku

   # Windows
   # Download from: https://devcenter.heroku.com/articles/heroku-cli

   # Verify installation
   heroku --version
   ```

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku App**
   ```bash
   cd factor_momentum_visualizer
   heroku create your-app-name
   ```

4. **Create Procfile**
   ```bash
   echo "web: streamlit run app.py --server.port \$PORT --server.enableCORS false" > Procfile
   ```

5. **Create setup.sh**
   ```bash
   cat > setup.sh << 'EOF'
   mkdir -p ~/.streamlit/

   echo "\
   [server]\n\
   headless = true\n\
   port = $PORT\n\
   enableCORS = false\n\
   \n\
   " > ~/.streamlit/config.toml
   EOF
   ```

6. **Deploy**
   ```bash
   git add Procfile setup.sh
   git commit -m "Add Heroku deployment files"
   git push heroku main
   ```

7. **Open Your App**
   ```bash
   heroku open
   ```

### Heroku Configuration

Set environment variables:
```bash
heroku config:set STREAMLIT_SERVER_HEADLESS=true
heroku config:set STREAMLIT_SERVER_PORT=\$PORT
```

---

## 🤗 HuggingFace Spaces

Deploy as a Hugging Face Space for free hosting with ML community integration.

### Steps

1. **Create Space**
   - Go to [huggingface.co/spaces](https://huggingface.co/spaces)
   - Click "Create new Space"
   - Choose name and license
   - Select SDK: **Streamlit**

2. **Clone Space Repository**
   ```bash
   git clone https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
   cd YOUR_SPACE_NAME
   ```

3. **Copy Your Files**
   ```bash
   cp -r ../factor_momentum_visualizer/* .
   ```

4. **Create README.md for Space**
   ```markdown
   ---
   title: Factor Momentum Visualizer
   emoji: 📊
   colorFrom: blue
   colorTo: green
   sdk: streamlit
   sdk_version: 1.29.0
   app_file: app.py
   pinned: false
   ---

   # Factor Momentum Visualizer
   
   A production-grade quant research tool for factor analysis.
   ```

5. **Push to HuggingFace**
   ```bash
   git add .
   git commit -m "Deploy Factor Momentum Visualizer"
   git push
   ```

6. **Access Your Space**
   - Your app will be available at: `https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME`

---

## 🐳 Docker

Deploy with Docker for maximum portability.

### Prerequisites
- Docker installed

### Steps

1. **Create Dockerfile**
   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   RUN apt-get update && apt-get install -y \
       build-essential \
       curl \
       software-properties-common \
       && rm -rf /var/lib/apt/lists/*

   COPY requirements.txt .
   RUN pip3 install -r requirements.txt

   COPY . .

   EXPOSE 8501

   HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

   ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Build Image**
   ```bash
   docker build -t factor-momentum-visualizer .
   ```

3. **Run Container**
   ```bash
   docker run -p 8501:8501 factor-momentum-visualizer
   ```

4. **Access App**
   - Open browser: `http://localhost:8501`

### Docker Compose (Optional)

Create `docker-compose.yml`:
```yaml
version: '3.8'

services:
  streamlit:
    build: .
    ports:
      - "8501:8501"
    volumes:
      - ./data:/app/data
    restart: unless-stopped
```

Run with:
```bash
docker-compose up -d
```

---

## ☁️ AWS EC2

Deploy on AWS for production-grade hosting.

### Prerequisites
- AWS account
- EC2 instance (t2.micro eligible for free tier)

### Steps

1. **Launch EC2 Instance**
   - AMI: Ubuntu 22.04 LTS
   - Instance type: t2.small (minimum)
   - Security group: Allow HTTP (80), HTTPS (443), Custom TCP (8501)

2. **Connect to Instance**
   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-ip
   ```

3. **Install Dependencies**
   ```bash
   sudo apt update
   sudo apt install -y python3-pip python3-venv nginx
   ```

4. **Clone Repository**
   ```bash
   git clone YOUR_REPO_URL
   cd factor_momentum_visualizer
   ```

5. **Setup Python Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

6. **Run with Systemd**
   
   Create `/etc/systemd/system/factor-viz.service`:
   ```ini
   [Unit]
   Description=Factor Momentum Visualizer
   After=network.target

   [Service]
   User=ubuntu
   WorkingDirectory=/home/ubuntu/factor_momentum_visualizer
   ExecStart=/home/ubuntu/factor_momentum_visualizer/venv/bin/streamlit run app.py --server.port 8501
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

   Enable and start:
   ```bash
   sudo systemctl enable factor-viz
   sudo systemctl start factor-viz
   ```

7. **Configure Nginx (Optional)**
   
   Create `/etc/nginx/sites-available/factor-viz`:
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://localhost:8501;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection "upgrade";
           proxy_set_header Host $host;
           proxy_cache_bypass $http_upgrade;
       }
   }
   ```

   Enable:
   ```bash
   sudo ln -s /etc/nginx/sites-available/factor-viz /etc/nginx/sites-enabled/
   sudo systemctl restart nginx
   ```

---

## 🔒 Security Best Practices

### Environment Variables

Never commit sensitive data. Use environment variables:

Create `.streamlit/secrets.toml`:
```toml
# API keys (if needed)
api_key = "your-api-key"

# Database credentials (if needed)
[database]
host = "localhost"
port = 5432
username = "user"
password = "password"
```

Add to `.gitignore`:
```
.streamlit/secrets.toml
```

Access in code:
```python
import streamlit as st
api_key = st.secrets["api_key"]
```

---

## 📊 Monitoring

### Streamlit Cloud
- Built-in monitoring dashboard
- View logs in real-time
- Check resource usage

### Custom Deployment
Use these tools:
- **Logs**: `journalctl -u factor-viz -f`
- **Monitoring**: Prometheus + Grafana
- **Uptime**: UptimeRobot or Pingdom

---

## 🐛 Troubleshooting

### Common Issues

**Port already in use**
```bash
# Find process
lsof -i :8501
# Kill process
kill -9 PID
```

**Memory issues**
- Increase instance size
- Optimize data loading
- Use data caching

**yfinance connection errors**
- Check internet connectivity
- Verify firewall settings
- Use VPN if restricted

---

## 🎯 Performance Optimization

### Caching
Add to your code:
```python
@st.cache_data
def fetch_data(tickers, start, end):
    # Your data fetching code
    pass
```

### Load Balancing (Advanced)
For high traffic, use:
- AWS Elastic Load Balancer
- Nginx load balancing
- Multiple instances

---

## 📝 Checklist Before Deployment

- [ ] All dependencies in requirements.txt
- [ ] Secrets not committed to git
- [ ] README.md is complete
- [ ] .gitignore configured
- [ ] Code tested locally
- [ ] Error handling implemented
- [ ] Loading states added
- [ ] Documentation complete

---

## 🎉 You're Ready!

Choose the deployment method that best fits your needs:
- **Learning/Personal**: Streamlit Cloud
- **Production/Custom**: AWS EC2 or Heroku
- **ML Community**: HuggingFace Spaces
- **Portability**: Docker

Good luck with your deployment! 🚀
