from sanic.response import json
from sanic.views import HTTPMethodView
from sanic import Blueprint

from model import TestData

bp_data = Blueprint('database_admin', url_prefix='/testdata')

def amis_response(data=''):
    return json({
        "status": 0,
        "msg": "ok",
        "data": data
        })


class TestDataListView(HTTPMethodView):
    def get(self, request):
        args = dict(request.query_args)
        page = int(args.get('page', 1))
        size = int(args.get('perPage', 10))
        select = TestData.select()
        if args.get('module'):
            select = select.where(TestData.module == args['module'])
        if args.get('epic'):
            select = select.where(TestData.epic == args['epic'])
        ret = select.paginate(page, size)
        data = {
            'items': [d.to_dict() for d in ret],
            'total': select.count()
        }
        return amis_response(data)

    async def post(self, request):
        TestData.create(**request.json)
        return amis_response()


class TestDataView(HTTPMethodView):
    def get(self, request, id):
        return amis_response(id)

    def put(self, request, id):
        query = TestData.update(**request.json).where(TestData.id==id)
        code = query.execute()
        return amis_response()

    def delete(self, request):
        pass



bp_data.add_route(TestDataListView.as_view(), '/')
bp_data.add_route(TestDataView.as_view(), '/<id>')


@bp_data.route('/modules', methods=['GET'])
async def modules(request):
    ret = TestData.select(TestData.module).group_by(TestData.module)
    data = [d.module for d in ret]
    return amis_response(data)