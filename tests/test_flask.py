from app import app

class TestFlask:

    #Home path status code Pass
    def test_home_path_status_code_pass(self):
        res = app.test_client().get("/")
        assert res.status_code == 200
    
    #Home path status code Fail
    def test_home_path_status_code_fail(self):
        res = app.test_client().get("/nothome")
        assert res.status_code == 404
    
    #Post route sending data Pass
    def test_post_route_data_send_pass(self):
        res = app.test_client().post("/processing", data={"username":"Test", "textInput":"kayak"})
        # Check that the request was to the processing page.
        assert res.request.path == "/processing"
    
    #Post route sending data Fail
    def test_post_route_data_send_fail(self):
        res = app.test_client().post("/processin", data={"username":"Test", "textInput":"kayak"})
        # Check that the request was to the processing page.
        assert res.status_code == 404
