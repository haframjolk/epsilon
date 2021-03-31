#!/usr/bin/env python3

from waitress import serve
import app

serve(app=app.app, listen="127.0.0.1:8080")
