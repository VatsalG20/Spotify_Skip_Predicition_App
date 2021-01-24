mkdir -p ~/.streamlit/
echo "[general]
email = \"vatsal.gandhi12@com\"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
