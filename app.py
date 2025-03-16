from flask import Flask
from scripts.routes.customer.routes import blueprint as customer_blueprint
from scripts.routes.items.routes import blueprint as items_blueprint
from scripts.routes.reviews.routes import blueprint as reviews_blueprint
from scripts.routes.about.routes import blueprint as about_blueprint
from scripts.routes.policies.routes import blueprint as policies_blueprint

app = Flask(__name__)
app.register_blueprint(customer_blueprint)
app.register_blueprint(items_blueprint)
app.register_blueprint(reviews_blueprint)
app.register_blueprint(about_blueprint)
app.register_blueprint(policies_blueprint)

if __name__ == '__main__':
    PORT = 8001
    app.run(port=PORT, debug=True, host='0.0.0.0', use_reloader=True)
