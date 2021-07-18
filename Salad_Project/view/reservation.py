
from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for
from model.mongodb import conn_mongodb
from control.reservation_mgmt import Reservation

bp_salad = Blueprint('salad', __name__)

@bp_salad.route('/list',methods=['GET'])
def getAllList():
    results = Reservation.getall()
    return render_template('reservation_list.html', data=results)