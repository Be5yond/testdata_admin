import json
from sanic.response import json as json_response
from sanic import Blueprint

from utils import assist

bp_tool = Blueprint('tool', url_prefix='/tool')

def amis_response(data=''):
    return json_response({
        "status": 0,
        "msg": "ok",
        "data": data
        })

@bp_tool.route('/schema', methods=['POST'])
async def schema(request):
    data = json.loads(request.json['json'])
    scm = assist.transform(data)
    ret = json.dumps(scm, indent=4)
    return amis_response({'schema': ret})