import application
import session
import requests

GET_CATEGORIES = "/api/Category/MasterList/"
GET_STORIES = "/api/theme/list/"
GET_MOMENTS = "/api/moment/list/"
GET_THEMES = "/api/Story/MasterList/"

def test_compare_board_qa_with_app_data_prod():
    app = application.Application()

    users = app.get_users()
    # for user in users:
    for numb in range(1):
        user = users[numb]
        companyID = user[0]
        communityID = user[1]
        user_login = user[2][1:-1]
        user_pswd = user[3][1:-1]
        print("{0} {1} {2} {3}".format(companyID, communityID, user_login, user_pswd))


        #Login to QA
        qa_login_header = session.Session.authenticate(app.get_qa_server_url(), user_login, user_pswd)
        assert(qa_login_header is not None)
        app.logger.info("Authenticated to QA as {0}/{1} under compeny {2} and community {3}".format(user_login,
                                                                          user_pswd, companyID, communityID))

        #Login to Prod
        prod_login_header = session.Session.authenticate(app.get_prod_server_url(), user_login, user_pswd)
        assert(prod_login_header is not None)
        app.logger.info("Authenticated to Prod as {0}/{1} under compeny {2} and community {3}".format(user_login,
                                                                       user_pswd, companyID, communityID))


        #Categories
        app.logger.info("Comparing Categories")
        qa_categories_response = requests.get("{0}{1}/{2}/{3}".format(app.get_qa_server_url(), GET_CATEGORIES, companyID, communityID),
                        headers = qa_login_header).json()
        prod_categories_response = requests.post("{0}{1}/{2}".format(app.get_prod_server_url(), GET_CATEGORIES, companyID),
                        headers = prod_login_header).json()


        assert(app.compare_responses(sorted(qa_categories_response, key=lambda k: k["Name"]),
                                 sorted(prod_categories_response, key=lambda k: k["Name"]))) #Can also be sorted by CMSCategoryId

        # assert(app.compare_responses(qa_categories_response, prod_categories_response)) #Can also be sorted by CMSCategoryId
        app.logger.info("Categories are equal")


        #Stories
        app.logger.info("Comparing Stories")
        # qa_categories_response = requests.get("{0}{1}/{2}/{3}".format(app.get_qa_server_url(), GET_CATEGORIES, companyID, communityID),
        #                 headers = qa_login_header).json()
        # prod_categories_response = requests.post("{0}{1}/{2}".format(app.get_prod_server_url(), GET_CATEGORIES, companyID),
        #                 headers = prod_login_header).json()
        #
        #
        # assert(app.compare_responses(sorted(qa_categories_response, key=lambda k: k["Name"]),
        #                         sorted(prod_categories_response, key=lambda k: k["Name"]))) #Can also be sorted by CMSCategoryId
        #
        # assert(app.compare_responses(qa_categories_response, prod_categories_response)) #Can also be sorted by CMSCategoryId
        app.logger.info("Stories are equal")


        #Moments
        app.logger.info("Comparing Moments")
        # qa_categories_response = requests.get("{0}{1}/{2}/{3}".format(app.get_qa_server_url(), GET_CATEGORIES, companyID, communityID),
        #                 headers = qa_login_header).json()
        # prod_categories_response = requests.post("{0}{1}/{2}".format(app.get_prod_server_url(), GET_CATEGORIES, companyID),
        #                 headers = prod_login_header).json()
        #
        #
        # assert(app.compare_responses(sorted(qa_categories_response, key=lambda k: k["Name"]),
        #                         sorted(prod_categories_response, key=lambda k: k["Name"]))) #Can also be sorted by CMSCategoryId
        #
        # assert(app.compare_responses(qa_categories_response, prod_categories_response)) #Can also be sorted by CMSCategoryId
        app.logger.info("Moments are equal")


        #Theme
        app.logger.info("Comparing Themes")
        # qa_categories_response = requests.get("{0}{1}/{2}/{3}".format(app.get_qa_server_url(), GET_CATEGORIES, companyID, communityID),
        #                 headers = qa_login_header).json()
        # prod_categories_response = requests.post("{0}{1}/{2}".format(app.get_prod_server_url(), GET_CATEGORIES, companyID),
        #                 headers = prod_login_header).json()
        #
        #
        # assert(app.compare_responses(sorted(qa_categories_response, key=lambda k: k["Name"]),
        #                         sorted(prod_categories_response, key=lambda k: k["Name"]))) #Can also be sorted by CMSCategoryId
        #
        # assert(app.compare_responses(qa_categories_response, prod_categories_response)) #Can also be sorted by CMSCategoryId
        app.logger.info("Themes are equal")