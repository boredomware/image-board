from flask import Flask, request, render_template, g
from werkzeug.utils import secure_filename
import sqlite3, datetime, os, random

DATABASE = 'chan.db'
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

