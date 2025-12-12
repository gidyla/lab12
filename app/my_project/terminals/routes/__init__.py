# my_project/routes.py
from my_project.terminals.routes.alert_routes import alert_bp
from my_project.terminals.routes.battery_status_router import battery_status_bp
from my_project.terminals.routes.incident_report_routes import incident_report_bp
from my_project.terminals.routes.maintenance_routes import maintenance_bp
from my_project.terminals.routes.robot_routes import robot_bp
from my_project.terminals.routes.robot_control_routes import robot_control_bp
from my_project.terminals.routes.robot_zone_routes import robot_zone_bp
from my_project.terminals.routes.sensor_routes import sensor_bp
from my_project.terminals.routes.user_routes import user_bp
from my_project.terminals.routes.zone_routes import zone_bp

def register_routes(app):
    app.register_blueprint(alert_bp, url_prefix='/api')
    app.register_blueprint(battery_status_bp, url_prefix='/api')
    app.register_blueprint(incident_report_bp, url_prefix='/api')
    app.register_blueprint(maintenance_bp, url_prefix='/api')
    app.register_blueprint(robot_bp, url_prefix='/api')
    app.register_blueprint(robot_control_bp, url_prefix='/api')
    app.register_blueprint(robot_zone_bp, url_prefix='/api')
    app.register_blueprint(sensor_bp, url_prefix='/api')
    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(zone_bp, url_prefix='/api')
