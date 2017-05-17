# import pytest
#
# from application import Application
#
# fixture = None
#
# @pytest.fixture(scope="session")
# def app():
#     """Create fixture"""
#     global fixture
#     fixture = Application()
#     return fixture
#
#
# @pytest.fixture(scope="session", autouse=True)
# def close(request):
#     """Destroy fixture"""
#     def fin():
#         fixture.destroy()
#     request.addfinalizer(fin)
#     return fixture