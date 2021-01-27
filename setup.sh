mkdir -p ~/.streamlit/
echo "[general]
email = \"vatsal.gandhi12@com\"
" > ~/.streamlit/credentials.toml
echo "\
[server] \n\
headless = true \n\
port = $PORT \n\
enableCORS = false \n\
\n\
" > ~/.streamlit/config.toml
