import pymssql
import logging
import os

QA_SERVER_URL = "http://cms-st.oneday.com"
PROD_SERVER_URL = "http://cms.oneday.com"


class Application:
    def __init__(self):
        logging.basicConfig(filename = "{0}/{1}.log".format(os.getcwd(), "Logfile"), level=logging.INFO,
                            format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger("Logger")

        # Create DB connection
        #QA
        self.qa_db_connection = pymssql.connect(server="qa.cpiqjs9uzigz.us-west-2.rds.amazonaws.com",
                                                user="sa", password="ODProd!2", database="oneday")
        self.qa_db_cursor = self.qa_db_connection.cursor()
        self.logger.info("Connected to QA DB")

        #Prod
        self.prod_db_connection = pymssql.connect(server="onedayprod.cpiqjs9uzigz.us-west-2.rds.amazonaws.com",
                                                user="OneDayuser", password="ODProd!2", database="oneday")
        self.prod_db_cursor = self.prod_db_connection.cursor()
        self.logger.info("Connected to Production DB")


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
        self.logger.info("User get from file:")
        with open("{0}\{1}".format(os.getcwd(), "expdata.csv")) as user_file:
            users = user_file.read().split()
            user_list = []
            for user in users:
                self.logger.info("{0}".format(user))
                user_list.append(user.split(';'))
            user_list[0][0] = user_list[0][0][-2:]

        return user_list

    def compare_responses(self, qa_server_response, prod_server_response):
        if len(qa_server_response) != len(prod_server_response):
            self.logger.info("qa server response length is {0} and doesn't equal production serve response length {1}".format(
                             len(qa_server_response), len(prod_server_response)))
            self.logger.info(qa_server_response)
            self.logger.info(prod_server_response)
            return False

        for numb in range(len(qa_server_response)):
            for key in qa_server_response[numb].keys():
                if qa_server_response[numb][key] != prod_server_response[numb][key]:
                    self.logger.info("responses by key {0} are not equal, qa server response {1}, prod server response {2}".format(
                                 key, qa_server_response[numb][key], prod_server_response[numb][key]))
                    return False

        return True


