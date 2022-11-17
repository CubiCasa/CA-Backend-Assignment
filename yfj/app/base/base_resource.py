from flask_restful import reqparse, Resource, abort


class BaseResource(Resource):
    parser = reqparse.RequestParser()

    def map_func(self, item):
        return item.to_dict(rules=('-password',))

    def get_paginated_list(self, klass, page, limit, init_query=None):
        if init_query:
            total = init_query.filter_by(deleted_at=None).count()
            results = init_query.paginate(int(page), int(limit))
        else:
            total = klass.query.filter_by(deleted_at=None).count()
            results = klass.query.paginate(int(page), int(limit))

        return dict(items=list(map(self.map_func, results.items)), page=page, total=total)

    def __init__(self):
        super(BaseResource, self).__init__()
