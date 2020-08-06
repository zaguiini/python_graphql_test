import sys
import click
from flask import Flask
from flask_graphql import GraphQLView

from schema.schema import schema

@click.command(context_settings=dict(ignore_unknown_options=True))
@click.option("--port", "-p", default=3000, help="Desired port")
def main(port):
    app = Flask(__name__)

    app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
    app.run(host='0.0.0.0', port=port)


if __name__ == "__main__":
    main()
