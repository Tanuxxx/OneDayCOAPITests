import pymssql
import logging
import os
from session import Session

QA_SERVER_URL = "http://cms-st.oneday.com"
PROD_SERVER_URL = "http://cms-st.oneday.com"


class Application:
    def __init__(self):
        self.curr_session = Session()
        logging.basicConfig(filename = "{0}/{1}.log".format(os.getcwd(), "Logfile"), level=logging.INFO,
                            format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger("Logger")

        # # Create DB connection
        # #QA
        # self.qa_db_connection = pymssql.connect(server="qa.cpiqjs9uzigz.us-west-2.rds.amazonaws.com",
        #                                         user="sa", password="ODProd!2", database="oneday")
        # self.qa_db_cursor = self.qa_db_connection.cursor()
        # self.logger.info("Connected to QA DB")
        #
        # #Prod
        # self.prod_db_connection = pymssql.connect(server="onedayprod.cpiqjs9uzigz.us-west-2.rds.amazonaws.com",
        #                                         user="OneDayuser", password="ODProd!2", database="oneday")
        # self.prod_db_cursor = self.prod_db_connection.cursor()
        # self.logger.info("Connected to Production DB")


    def destroy(self):
        #Close connection to the DB
        self.qa_db_cursor.close()
        self.qa_db_connection.close()

        self.prod_db_cursor.close()
        self.prod_db_connection.close()

    def get_qa_server_url(self):
        return QA_SERVER_URL

    def get_prod_server_url(self):
        return PROD_SERVER_URL

    def get_users(self):
        self.logger.info("Get users from file:")
        with open("{0}\{1}".format(os.getcwd(), "expdata.csv")) as user_file:
            users = user_file.read().split()
            user_list = []
            for user in users:
                self.logger.info("{0}".format(user))
                user_list.append(user.split(';'))
            user_list[0][0] = user_list[0][0][-2:]

        return user_list

    def compare_responses(self, qa_server_response, prod_server_response, key_value):
        if len(qa_server_response) != len(prod_server_response):
            self.logger.info("Stage api v.2 server response length = {0} and doesn't equal stage api v.1 server "
                             "response length = {1}".format(
                             len(qa_server_response), len(prod_server_response)))
            self.logger.info("Stage server response: {0}".format(qa_server_response))
            self.logger.info("Prod server response: {0}".format(prod_server_response))
            return False

        for numb in range(len(qa_server_response)):
            for key in qa_server_response[numb].keys():
                if type(qa_server_response[numb][key]) is list:
                    if len(qa_server_response[numb][key]) != len(prod_server_response[numb][key]):
                        self.logger.info(
                            "Responses with {0} = {1} by field {2} are not equal: stage api v.2 server response length "
                            "= {3}, stage api v.1 server response length = {4}".format(key_value,
                                                                                qa_server_response[numb][key_value],
                                                                                key, len(qa_server_response[numb][key]),
                                                                                len(prod_server_response[numb][key])))
                        return False
                    qa_serv_response_curr = sorted(qa_server_response[numb][key])
                    prod_serv_response_curr = sorted(prod_server_response[numb][key])
                else:
                    qa_serv_response_curr = qa_server_response[numb][key]
                    prod_serv_response_curr = prod_server_response[numb][key]
                if qa_serv_response_curr != prod_serv_response_curr:
                    self.logger.info("Responses with {0} = {1} by field {2} are not equal: stage api v.2 server "
                                     "response is {3}, stage api v.1 server response is {4}".format(key_value,
                                                                        qa_server_response[numb][key_value],key,
                                                                        qa_serv_response_curr, prod_serv_response_curr))
                    return False
            self.logger.info("Responses with {0} = {1} are equal".format(key_value, qa_server_response[numb][key_value]))
        return True


