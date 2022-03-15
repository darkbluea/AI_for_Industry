mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml

pip install --upgrade tensorflow-hub
wget https://storage.googleapis.com/drive-bulk-export-anonymous/20220315T164205Z/4133399871716478688/97d5845b-b2d0-47b5-9432-f1f6f2ffb103/1/a3507ce0-1499-4348-a1c8-29a2d7ddffe8
unzip a3507ce0-1499-4348-a1c8-29a2d7ddffe8
