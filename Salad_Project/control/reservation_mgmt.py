from model.mongodb import conn_mongodb
from datetime import datetime
from bson.objectid import ObjectId

class Reservation():
    def __init__(self, id, salad_cd, name, company_cd, team_nm, emp_num, inpt_dt, receive_yn, receive_dt, cancel_dt):
        self.id = id
        self.salad_cd
        self.name = name
        self.company_cd = company_cd
        self.team_nm = team_nm
        self.emp_num = emp_num
        self.inpt_dt = inpt_dt
        self.receive_yn = receive_yn
        self.receive_dt = receive_dt
        self.cancel_dt = cancel_dt

    @staticmethod
    def makeReservation(salad_cd, name, company_cd, team_nm, emp_num):
        mongo_db = conn_mongodb()
        mongo_db.insert_one({
            'salad_cd': salad_cd,
            'name': name,
            'company_cd': company_cd,
            'team_nm': team_nm,
            'emp_num': emp_num,
            'inpt_dt': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })

    @staticmethod
    def getall():
        mongo_db = conn_mongodb()
        results = mongo_db.find()
        return results
    
    @staticmethod
    def findByName(name):
        mongo_db = conn_mongodb()
        results = mongo_db.find({"name":name})
        return results

    @staticmethod
    def findByEmpNum(emp_num):
        mongo_db = conn_mongodb()
        results = mongo_db.find({"emp_num":emp_num})
        return results
    
    @staticmethod
    def received(reservation_id):
        mongo_db = conn_mongodb()
        mongo_db.update({"_id":ObjectId(reservation_id)}, {"$set":{
            "receive_yn":1,
            "receive_dt":datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }})
    
    @staticmethod
    def cancel(reservation_id):
        mongo_db = conn_mongodb()
        mongo_db.update({"_id":ObjectId(reservation_id)}, {"$set":{
            "cancel_dt":datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }})