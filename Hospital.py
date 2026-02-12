import logging
logging.basicConfig(
    filename="patient.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Hospital:
    consultation_fee=500
    def __init__(self,patient_name,age,disease,ph_no,room_charge_per_day):
        self.patient_name=patient_name
        self.age=age
        self.disease=disease
        self.ph_no=ph_no
        self.days_admitted=0
        self.room_charge_per_day=room_charge_per_day
        self.is_admitted=False

    def admit(self,days):
        if days>0:
            self.days_admitted=days 
            self.is_admitted=True
            logging.info("%s admitted for %d days", self.patient_name, self.days_admitted)

    def discharge(self):
        if self.is_admitted:
            self.is_admitted=False
            logging.info("%s discharged successfully",self.patient_name)
        else:
            logging.info("Patient is not admitted.")    

    def cal_bill(self):
        if self.days_admitted > 0:
            self.total = (self.room_charge_per_day * self.days_admitted) + Hospital.consultation_fee  
            logging.info("total bill is %d",self.total)
    @classmethod
    def update_consultation_fee(cls,new_fee):
        cls.consultation_fee=new_fee
        logging.info("consultation fee updated to %d",new_fee)

p1 = Hospital("Jhon", 22, "Fever", 123456789,2000)    
p1.admit(3)
p1.cal_bill()
p1.discharge() 
Hospital.update_consultation_fee(800)
p1.cal_bill()                 
