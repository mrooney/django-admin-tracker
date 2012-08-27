RUNSERVER_PORT = 17224
SERVICES = {
    "runserver":
        {
            "port": RUNSERVER_PORT,
            "start": ["python", "manage.py", "runserver", "0.0.0.0:%i" % RUNSERVER_PORT],
            "daemonizes": False,
        },
}
"""
    "nginx":
        {
            "port": 27190,
            "start": ["nginx", "-c", "{project_dir}/nginx.conf"],
            "restart": ["kill", "-s", "SIGHUP", "{pid}"],
            "templates": ["nginx.conf.template"],
        },
    "gunicorn":
        {
            "port": 18650,
            "start": ["gunicorn", "-D", "-c", "settings_gunicorn.py", "tasktrack.wsgi:application"],
            "restart": ["kill", "-s", "SIGHUP", "{pid}"],
        },
"""

