from application import Application
import requests
import pytest

GET_CATEGORIES_V2 = "/api/v2/Category/MasterList/"
GET_THEMES_V2 = "/api/v2/theme/list/"
GET_MOMENTS_V2 = "/api/v2/moment/list/"
GET_STORIES_V2 = "/api/v2/Story/MasterList/"

GET_CATEGORIES_V1 = "/api/Category/MasterList/"
GET_THEMES_V1 = "/api/theme/list/"
GET_MOMENTS_V1 = "/api/moment/list/"
GET_STORIES_V1 = "/api/Story/MasterList/"


@pytest.yield_fixture()
def app():
    app = Application()
    yield app
    # app.destroy()


def test_compare_board_qa_with_app_data_prod(app):
    # app = application.Application()

    users = app.get_users()
    for numb in range(len(users)-3):
    #for numb in range(1):
        app.logger.info("User number {0}".format(numb))
        user = users[numb]
        companyID = user[0]
        communityID = user[1]
        user_login = user[2][1:-1]
        user_pswd = user[3][1:-1]
        login_string = "{0}/{1} under company {2} and community {3}".format(user_login, user_pswd, companyID, communityID)

        #Login to QA
        qa_login_header = app.curr_session.authenticate(app.get_qa_server_url(), user_login, user_pswd)
        assert(qa_login_header is not None, "Authentication to Stage failed as {0}".format(login_string))
        app.logger.info("Authenticated to Stage as {0}".format(login_string))

        # #Login to Prod
        # prod_login_header = app.curr_session.authenticate(app.get_prod_server_url(), user_login, user_pswd)
        # assert(prod_login_header is not None, "Authentication to Prod failed as {0}".format(login_string))
        # app.logger.info("Authenticated to Prod as {0}".format(login_string))


        # #Categories
        # api_request_v2 = "{0}{1}/{2}".format(GET_CATEGORIES_V2, companyID, communityID)
        # api_request_v1 = "{0}{1}".format(GET_CATEGORIES_V1, companyID)
        # app.logger.info("Comparing Categories got by request: {0} for v.2 and request: {1} for v.1".format(
        #                                                                                 api_request_v2, api_request_v1))
        # qa_categories_response = requests.get("{0}{1}".format(app.get_qa_server_url(), api_request_v2),
        #                 headers = qa_login_header).json()
        # prod_categories_response = requests.post("{0}{1}".format(app.get_prod_server_url(), api_request_v1),
        #                 headers = qa_login_header).json()
        #
        # sorting_key = "CmsCategoryId"
        # assert(app.compare_responses(sorted(qa_categories_response, key=lambda k: k[sorting_key]),
        #                          sorted(prod_categories_response, key=lambda k: k[sorting_key]), sorting_key))
        #
        # app.logger.info("Categories are equal")
        #
        #
        # #Stories
        # api_request_v2 = "{0}{1}/{2}".format(GET_STORIES_V2, companyID, communityID)
        # api_request_v1 = "{0}{1}".format(GET_STORIES_V1, companyID)
        # app.logger.info("Comparing Stories got by request: {0} for v.2 and request: {1} for v.1".format(
        #                                                                                 api_request_v2, api_request_v1))
        # qa_categories_response = requests.get("{0}{1}".format(app.get_qa_server_url(), api_request_v2),
        #                 headers = qa_login_header).json()
        # prod_categories_response = requests.post("{0}{1}".format(app.get_prod_server_url(), api_request_v1),
        #                 headers = qa_login_header).json()
        #
        # sorting_key = "CmsStoryId"
        # assert(app.compare_responses(sorted(qa_categories_response, key=lambda k: k[sorting_key]),
        #                         sorted(prod_categories_response, key=lambda k: k[sorting_key]), sorting_key))
        #
        # app.logger.info("Stories are equal")


        #Moments
        api_request_v2 = "{0}{1}/{2}".format(GET_MOMENTS_V2, companyID, communityID)
        api_request_v1 = "{0}{1}".format(GET_MOMENTS_V1, companyID)
        app.logger.info("Comparing Moments got by request: {0} for v.2 and request: {1} for v.1".format(
                                                                                        api_request_v2, api_request_v1))
        qa_categories_response = requests.get("{0}{1}".format(app.get_qa_server_url(), api_request_v2),
                        headers = qa_login_header).json()
        prod_categories_response = requests.post("{0}{1}".format(app.get_prod_server_url(), api_request_v1),
                        headers = qa_login_header).json()

        sorting_key = "CmsMomentId"
        assert(app.compare_responses(sorted(qa_categories_response, key=lambda k: k[sorting_key]),
                                sorted(prod_categories_response, key=lambda k: k[sorting_key]), sorting_key))

        app.logger.info("Moments are equal")


        # #Theme
        # api_request_v2 = "{0}{1}".format(GET_THEMES_V2, companyID)
        # api_request_v1 = "{0}{1}".format(GET_THEMES_V1, companyID)
        # app.logger.info("Comparing Themes got by request: {0} for v.2 and request: {1} for v.1".format(
        #                                                                                 api_request_v2, api_request_v1))
        # qa_categories_response = requests.get("{0}{1}".format(app.get_qa_server_url(), api_request_v2),
        #                 headers = qa_login_header).json()
        # prod_categories_response = requests.post("{0}{1}".format(app.get_prod_server_url(), api_request_v1),
        #                 headers = qa_login_header).json()
        #
        # sorting_key = "CmsThemeId"
        # assert(app.compare_responses(sorted(qa_categories_response, key=lambda k: k[sorting_key]),
        #                          sorted(prod_categories_response, key=lambda k: k[sorting_key]), sorting_key))
        #
        # app.logger.info("Themes are equal")