# Package requirement
apt install python3-pip

# Python rest with hug
# https://www.hug.rest/website/quickstart
# if pip is set to Python3 pip
pip install hug -U

# Python neural network 
pip install gensim
pip install gunicorn
pip install waitress

# Download neural bin file : 
# https://embeddings.net/embeddings/frWac_no_postag_no_phrase_700_skip_cut50.bin

# Run 
waitress-serve --listen=*:8000 api:__hug_wsgi__
