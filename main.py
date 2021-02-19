from sanic import Sanic
from app.data_admin import bp_data
from app.tool import bp_tool
from model import db

app = Sanic(__name__)
app.blueprint(bp_data)
app.blueprint(bp_tool)
app.static('/', './static')

@app.middleware('request')
async def handle_request(request):
    if db.is_closed():
        db.connect()

@app.middleware('response')
async def handle_response(request, response):
    if not db.is_closed():
        db.close()

app.run(host='0.0.0.0', port=8000, debug=True)