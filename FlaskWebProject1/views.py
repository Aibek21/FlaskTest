
"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import jsonify
from flask import make_response
from flask import abort
from flask import request
from flask import url_for
from FlaskWebProject1 import app
# from models.azuretablestorage import get_gens
# from azure.storage.table import TableService, Entity
# from azure.storage.queue import QueueService




# @app.errorhandler(404)
# def not_found(error):
#     return make_response(jsonify({'error': 'Not found'}), 404)


# @app.route('/todo/api/v1.0/generators', methods=['GET'])
# def get_generators():
#     table_service = TableService(account_name='kuralbayevday1', account_key='8onfJI8YYDJ9pB+SLOcFycntsRnL+iJm6y7R0mhTk8mSKZs9bXBo1v19bdwYOW4ts09440t6Gct2H2JtvjosRQ==')
#     generators = table_service.query_entities('generatorslist')
#     # print type(tasks)
#     # generators = get_gens()
#     return jsonify({'generators': map(make_public_generator, generators)})
#     # return "ok"



# @app.route('/todo/api/v1.0/results/<string:generator_id>', methods=['GET'])
# def get_results(generator_id):
#     table_service = TableService(account_name='kuralbayevday1', account_key='8onfJI8YYDJ9pB+SLOcFycntsRnL+iJm6y7R0mhTk8mSKZs9bXBo1v19bdwYOW4ts09440t6Gct2H2JtvjosRQ==')
#     result = table_service.query_entities('resulttable', filter="PartitionKey eq '%s'" % generator_id)
    
#     # result = filter(lambda t: t['id'] == generator_id, generators)
#     # if len(result) == 0:
#     #     abort(404)
#     return jsonify({'result': map(make_public_generator, result)})



# @app.route('/todo/api/v1.0/add_task', methods=['POST'])
# def create_task():
#     if not request.json or not 'generator' in request.json:
#         abort(400)


#     # queue_service = QueueService(account_name='kuralbayevday1', account_key='8onfJI8YYDJ9pB+SLOcFycntsRnL+iJm6y7R0mhTk8mSKZs9bXBo1v19bdwYOW4ts09440t6Gct2H2JtvjosRQ==')
#     # queue_service.put_message('generatorqueue', request.json['generator'])

#     return "ok", 201



# def make_public_generator(generator):
#     new_generator = {}
#     for field in generator:
#             new_generator[field] = generator[field]
#     return new_generator

